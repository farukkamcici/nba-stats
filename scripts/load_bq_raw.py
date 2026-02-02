"""Load raw NDJSON files from GCS into BigQuery staging tables."""

from google.cloud import bigquery, storage
from calendar import monthrange
import os
import logging
import argparse

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)
logger = logging.getLogger(__name__)

PROJECT_ID = os.environ.get("GCP_PROJECT_ID", "nba-stats-485819")
BUCKET_NAME = os.environ.get("GCS_BUCKET_NAME", "nba-stats-9070")
LOCATION = os.environ.get("GCP_LOCATION", "europe-west3")
DATASET = "nba_raw_stg"

JOB_CONFIG = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("payload", "JSON", "REQUIRED"),
        bigquery.SchemaField("source_date", "DATE", "REQUIRED"),
        bigquery.SchemaField("run_id", "STRING", "REQUIRED"),
        bigquery.SchemaField("ingested_at", "TIMESTAMP", "REQUIRED"),
        bigquery.SchemaField("gcs_uri", "STRING", "REQUIRED"),
    ],
    source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
    write_disposition=bigquery.WriteDisposition.WRITE_APPEND,
    ignore_unknown_values=True,
)

bq_client = bigquery.Client(project=PROJECT_ID, location=LOCATION)
storage_client = storage.Client()
bucket = storage_client.bucket(BUCKET_NAME)


def build_gcs_prefix(table_name: str, date_prefix: str) -> str:
    """Build a GCS prefix for a table and date prefix."""
    if table_name == "raw_scoreboard_json":
        # Matches: dt=2026-01-29/run_id=xxx/scoreboard.jsonl
        path = f"raw_ndjson/nba/scoreboard/dt={date_prefix}"
    elif table_name == "raw_boxscore_json":
        # Matches: dt=2026-01-29/game_id=xxx/run_id=xxx/boxscore.jsonl
        path = f"raw_ndjson/nba/boxscore/dt={date_prefix}"
    else:
        raise ValueError(f"Unknown table name: {table_name}")
    return path


import re


def parse_blob_path(blob_name: str, table_name: str) -> tuple[str, str]:
    """Extract grouping key and run_id from a blob path.

    For scoreboard: group by dt
    For boxscore: group by dt + game_id

    Returns:
        (group_key, run_id)
    """
    # Extract dt=YYYY-MM-DD
    dt_match = re.search(r"dt=(\d{4}-\d{2}-\d{2})", blob_name)
    if not dt_match:
        raise ValueError(f"Cannot parse dt from: {blob_name}")
    dt = dt_match.group(1)

    # Extract run_id=YYYYMMDD_HHMMSS
    run_match = re.search(r"run_id=(\d{8}_\d{6})", blob_name)
    if not run_match:
        raise ValueError(f"Cannot parse run_id from: {blob_name}")
    run_id = run_match.group(1)

    if table_name == "raw_boxscore_json":
        # Also extract game_id for boxscore
        game_match = re.search(r"game_id=(\d+)", blob_name)
        if not game_match:
            raise ValueError(f"Cannot parse game_id from: {blob_name}")
        group_key = f"{dt}|{game_match.group(1)}"
    else:
        group_key = dt

    return group_key, run_id


def list_gcs_uris(table_name: str, date_prefix: str) -> list[str]:
    """List NDJSON file URIs for a table and date prefix.

    Only returns the latest run_id for each group:
    - scoreboard: latest run per date
    - boxscore: latest run per date + game_id
    """
    prefix = build_gcs_prefix(table_name, date_prefix)

    # Collect all files grouped by key
    groups: dict[str, list[tuple[str, str]]] = {}  # key -> [(run_id, uri), ...]

    for blob in bucket.list_blobs(prefix=prefix):
        if not blob.name.endswith(".jsonl"):
            continue
        uri = f"gs://{BUCKET_NAME}/{blob.name}"
        try:
            group_key, run_id = parse_blob_path(blob.name, table_name)
            if group_key not in groups:
                groups[group_key] = []
            groups[group_key].append((run_id, uri))
        except ValueError as e:
            logger.warning("Skipping blob: %s", e)

    # Select latest run_id for each group
    uris: list[str] = []
    for group_key, runs in groups.items():
        # run_id format YYYYMMDD_HHMMSS sorts lexicographically
        latest_run_id, latest_uri = max(runs, key=lambda x: x[0])
        uris.append(latest_uri)
        if len(runs) > 1:
            logger.debug("Group %s: selected run_id=%s from %d runs", group_key, latest_run_id, len(runs))

    return uris


def delete_existing_data(table_name: str, start_date: str, end_date: str) -> int:
    """Delete existing rows for a date range before loading new data.

    Args:
        table_name: Target table name.
        start_date: Start date (YYYY-MM-DD).
        end_date: End date (YYYY-MM-DD).

    Returns:
        Number of rows deleted.
    """
    table_ref = f"{PROJECT_ID}.{DATASET}.{table_name}"
    query = f"""
        DELETE FROM `{table_ref}`
        WHERE source_date BETWEEN @start_date AND @end_date
    """
    job_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter("start_date", "DATE", start_date),
            bigquery.ScalarQueryParameter("end_date", "DATE", end_date),
        ]
    )
    query_job = bq_client.query(query, job_config=job_config)
    query_job.result()  # Wait for completion

    deleted_rows = query_job.num_dml_affected_rows or 0
    if deleted_rows > 0:
        logger.info("Deleted %d existing rows from %s", deleted_rows, table_ref)
    return deleted_rows


def load_uri_to_bq(table_name: str, gcs_uris: list[str]) -> int:
    """Load JSONL files from a list of GCS URIs into a BigQuery table.

    Args:
        table_name: Target table name (e.g., 'raw_scoreboard_json').
        gcs_uris: List of GCS URIs to load.

    Returns:
        Number of rows loaded.

    Raises:
        Exception: If the load job fails.
    """
    table_ref = f"{PROJECT_ID}.{DATASET}.{table_name}"
    # load_table_from_uri accepts a list of URIs
    load_job = bq_client.load_table_from_uri(gcs_uris, table_ref, job_config=JOB_CONFIG)
    load_job.result()  # Wait for job to complete

    logger.info(
        "Loaded %d rows into %s from %d files",
        load_job.output_rows,
        table_ref,
        len(gcs_uris),
    )
    return load_job.output_rows



def main() -> None:
    """CLI entry point: parse args and load NDJSON from GCS to BigQuery."""
    parser = argparse.ArgumentParser(description="Load raw JSONL from GCS to BigQuery.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--month", type=str, help="YYYY-MM (load entire month)")
    group.add_argument("--date", type=str, help="YYYY-MM-DD (load single day)")
    args = parser.parse_args()

    if args.month:
        year, month = map(int, args.month.split("-"))
        last_day = monthrange(year, month)[1]
        start_date = f"{args.month}-01"
        end_date = f"{args.month}-{last_day:02d}"
        date_prefix = f"{args.month}-"
        logger.info("Starting BQ load for month: %s (%s to %s)", args.month, start_date, end_date)
    else:
        start_date = args.date
        end_date = args.date
        date_prefix = args.date
        logger.info("Starting BQ load for date: %s", args.date)

    total_deleted = 0
    total_rows = 0

    for table_name in ("raw_scoreboard_json", "raw_boxscore_json"):
        # Delete existing data for idempotency
        deleted = delete_existing_data(table_name, start_date, end_date)
        total_deleted += deleted

        # Load new data
        gcs_uris = list_gcs_uris(table_name, date_prefix)
        if not gcs_uris:
            logger.warning("No files found for %s with prefix %s", table_name, date_prefix)
            continue
        logger.info("Loading %d files into %s", len(gcs_uris), table_name)
        rows = load_uri_to_bq(table_name, gcs_uris)
        total_rows += rows

    logger.info("Load complete | deleted=%d loaded=%d", total_deleted, total_rows)


if __name__ == "__main__":
    main()
