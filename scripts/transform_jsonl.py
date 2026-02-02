"""Transform raw JSON files in GCS to NDJSON format with metadata enrichment."""

from google.cloud import storage
from datetime import datetime, timezone
import argparse
import json
import logging
import os

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)
logger = logging.getLogger(__name__)

BUCKET_NAME = os.environ.get("GCS_BUCKET_NAME", "nba-stats-9070")
client = storage.Client()
bucket = client.bucket(BUCKET_NAME)


def parse_gcs_path(path: str) -> dict[str, str]:
    """Extract metadata (source_date, run_id, game_id) from a GCS path.

    Args:
        path: GCS object path with Hive-style partitions (e.g., dt=2026-01-30/run_id=xxx).

    Returns:
        Dictionary with source_date, run_id, and optionally game_id.

    Raises:
        ValueError: If required keys (dt, run_id) are missing.
    """
    parts = path.strip("/").split("/")

    def get_value(key: str) -> str:
        part = next((p for p in parts if p.startswith(f"{key}=")), None)
        if not part:
            raise ValueError(f"Missing {key} in path: {path}")
        return part.split("=", 1)[1]

    meta = {
        "source_date": get_value("dt"),
        "run_id": get_value("run_id"),
    }
    # game_id is optional (only present for boxscore)
    game = next((p for p in parts if p.startswith("game_id=")), None)
    if game:
        meta["game_id"] = game.split("=", 1)[1]

    return meta

def build_output_path(input_path: str) -> str:
    """Convert a raw/ JSON path to a raw_ndjson/ JSONL path.

    Args:
        input_path: GCS path starting with 'raw/' and ending with '.json'.

    Returns:
        Corresponding path under 'raw_ndjson/' with '.jsonl' extension.

    Raises:
        ValueError: If path doesn't start with 'raw/' or end with '.json'.
    """
    if not input_path.startswith("raw/"):
        raise ValueError(f"Unexpected input path: {input_path}")
    output_path = input_path.replace("raw/", "raw_ndjson/", 1)
    if not output_path.endswith(".json"):
        raise ValueError(f"Unexpected file extension: {input_path}")
    return output_path[:-5] + ".jsonl"



def transform_jsonl(input_path: str, output_path: str, metadata: dict[str, str] | None = None) -> None:
    """Download a raw JSON blob, wrap it with metadata, and upload as NDJSON.

    Args:
        input_path: GCS path to the source JSON file.
        output_path: GCS path for the output JSONL file.
        metadata: Additional fields to include in the output record.
    """
    blob = bucket.blob(input_path)
    payload = json.loads(blob.download_as_string())
    data = {
        "payload": payload,
        **(metadata or {}),
        "ingested_at": datetime.now(timezone.utc).isoformat(),
        "gcs_uri": f"gs://{BUCKET_NAME}/{blob.name}",
    }

    output_blob = bucket.blob(output_path)
    output_blob.upload_from_string(json.dumps(data) + "\n", content_type="application/x-ndjson")
    logger.info("Wrote JSONL: %s", output_path)

def process_prefix(prefix: str) -> dict[str, int]:
    """Process all JSON files under a GCS prefix, converting to NDJSON.

    Args:
        prefix: GCS prefix to scan (e.g., 'raw/nba/scoreboard/dt=2026-01-').

    Returns:
        Dictionary with counts: scanned, processed, skipped, errors.
    """
    scanned = 0
    processed = 0
    skipped = 0
    errors = 0
    blobs = bucket.list_blobs(prefix=prefix)

    for blob in blobs:
        if not blob.name.endswith(".json"):
            continue
        scanned += 1
        try:
            meta = parse_gcs_path(blob.name)
            output_path = build_output_path(blob.name)

            if bucket.blob(output_path).exists(client=client):
                skipped += 1
                logger.info("Skip existing: %s", output_path)
                continue

            transform_jsonl(blob.name, output_path, meta)
            processed += 1
        except Exception as exc:
            errors += 1
            logger.exception("Failed on %s: %s", blob.name, exc)

    logger.info(
        "Prefix summary: %s | scanned=%d processed=%d skipped=%d errors=%d",
        prefix,
        scanned,
        processed,
        skipped,
        errors,
    )
    return {"scanned": scanned, "processed": processed, "skipped": skipped, "errors": errors}

def process_date_prefix(date_prefix: str) -> dict[str, int]:
    """Process scoreboard and boxscore files for a given date prefix.

    Args:
        date_prefix: Date prefix like '2026-01-' (month) or '2026-01-15' (day).

    Returns:
        Dictionary with totals: scanned, processed, skipped, errors.
    """
    totals = {"scanned": 0, "processed": 0, "skipped": 0, "errors": 0}

    for entity in ("scoreboard", "boxscore"):
        result = process_prefix(f"raw/nba/{entity}/dt={date_prefix}")
        for key in totals:
            totals[key] += result[key]

    return totals


def main() -> None:
    """CLI entry point: parse args and run transformation."""
    parser = argparse.ArgumentParser(description="Transform raw JSON in GCS to NDJSON.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--month", type=str, help="YYYY-MM (transform entire month)")
    group.add_argument("--date", type=str, help="YYYY-MM-DD (transform single day)")
    args = parser.parse_args()

    if args.month:
        date_prefix = f"{args.month}-"
        logger.info("Starting transform for month: %s", args.month)
    else:
        date_prefix = args.date
        logger.info("Starting transform for date: %s", args.date)

    totals = process_date_prefix(date_prefix)

    logger.info(
        "Transform complete | scanned=%d processed=%d skipped=%d errors=%d",
        totals["scanned"],
        totals["processed"],
        totals["skipped"],
        totals["errors"],
    )


if __name__ == "__main__":
    main()
