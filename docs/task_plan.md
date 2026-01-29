# Task Plan (Mentor-First, MVP Focus)

This plan shows the broader path while keeping work in short, learn-by-doing tasks.

## Phase 0 — Foundations (GCP + Local Dev)
Goal: minimal cloud setup to store raw data and run dbt later.

Tasks
- Create GCP project and enable APIs (BigQuery, GCS, IAM).
- Create one GCS bucket for raw data.
- Create BigQuery datasets: `nba_raw_stg`, `nba_core`, `nba_marts`, `nba_audit`.
- Create a service account with least-privilege access.
- Record configs in `.env.example` (do not commit secrets).

Deliverables
- Project + bucket + datasets exist.
- A short `docs/ops_setup.md` describing how to reproduce setup.

Learning focus
- GCP basics (project, APIs, service accounts, IAM).

## Phase 1 — Ingestion (Scoreboard + Boxscore)
Goal: get raw NBA data into GCS in a replayable layout.

Tasks
- Define GCS raw path convention (date, run_id, game_id).
- Build a minimal ingestion script for scoreboard (single date).
- Add boxscore ingestion by game_id list from scoreboard.
- Persist raw JSON to GCS; keep it immutable.

Deliverables
- Raw files appear in GCS for a chosen date.
- A simple run log (local JSON or BQ table later).

Learning focus
- Idempotency, retries, API rate limits, and schema drift handling.

## Phase 2 — Warehouse Staging (BigQuery)
Goal: load raw files into BigQuery staging tables.

Tasks
- Define staging table schemas for scoreboard and boxscore.
- Create load jobs (GCS -> BigQuery staging).
- Ensure partitioning by `game_date` (or `dt`).

Deliverables
- `nba_raw_stg` contains scoreboard and boxscore tables.

Learning focus
- BigQuery load jobs, partitioning, and cost-aware design.

## Phase 3 — Transformations (dbt Core + Marts)
Goal: transform staging into clean core and analytics marts.

Tasks
- Create dbt project skeleton and connect to BigQuery.
- Build core dimensions: `dim_team`, `dim_player`, `dim_date`.
- Build facts: `fact_game`, `fact_team_game`, `fact_player_game`.
- Add dbt tests (not_null, unique, relationships).

Deliverables
- `nba_core` and `nba_marts` populated by dbt.
- dbt test results documented.

Learning focus
- Incremental models and data quality gates.

## Phase 4 — Orchestration (Airflow)
Goal: schedule and backfill the pipeline reliably.

Tasks
- Stand up Airflow via Docker Compose (local first).
- Implement a single DAG with tasks: fetch, load, dbt run/test, audit.
- Add backfill capability for a date range.

Deliverables
- Daily DAG runs end-to-end.
- Backfill works for a small date window.

Learning focus
- Task dependencies, retries, and idempotency in orchestration.

## Phase 5 — Observability + Audit
Goal: track runs and detect data issues early.

Tasks
- Create `pipeline_runs` and `pipeline_metrics` tables.
- Log status, row counts, freshness, and anomalies.
- Add basic alerts (can start with logs only).

Deliverables
- Queryable audit trail for each run.

Learning focus
- Operational monitoring in data pipelines.

## Phase 6 — Optional Enhancements
Phase 6A (Streaming)
- Kafka producer polls live endpoints.
- Consumer appends JSONL to GCS event log.
- Batch loads update marts.

Phase 6B (PySpark)
- Spark jobs for heavy backfills and transformations.

Learning focus
- Streaming patterns, event logs, and replay.

## Suggested Short-Task Cadence
- Each task should be 30–90 minutes.
- Each task includes: goal, inputs, outputs, and a quick validation step.

## Current Next Step (Recommendation)
Start with Phase 0 (Foundations) so we can run the pipeline end-to-end later.
