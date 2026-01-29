# Architecture Overview (MVP)

This document explains the high-level architecture for the NBA data platform.

## Goals
- Learn production-style data engineering concepts by building a real pipeline.
- Prioritize batch MVP first, then add streaming and Spark later.

## High-Level Flow

NBA endpoints (via nba_api)
    -> Ingestion scripts (Python)
    -> GCS Raw (Bronze, immutable JSON)
    -> BigQuery Staging (raw tables)
    -> dbt Core + Marts (clean analytics tables)
    -> Consumers (queries, dashboards, experiments)

Airflow orchestrates the steps above on a schedule and for backfills.
Audit tables record every run (status, counts, freshness).

## Components (MVP)
- nba_api (Python package): data source client for NBA endpoints.
- Ingestion (Python): fetch scoreboard + boxscore, write raw files to GCS.
- GCS (raw storage): immutable files for replay and debugging.
- BigQuery (warehouse): staging, core, marts, audit datasets.
- dbt: transforms, tests, and documentation for core/marts.
- Airflow: schedules daily runs and backfills.

## Data Layers
- Bronze (GCS raw): scoreboard.json, boxscore.json (per date/game/run).
- Staging (BigQuery): raw tables loaded from GCS.
- Core (BigQuery): cleaned, standardized facts and dimensions.
- Marts (BigQuery): analytics-ready aggregates and summaries.
- Audit (BigQuery): pipeline_runs, pipeline_metrics.

## Orchestration (Single DAG MVP)
Task flow (example):
1) fetch_scoreboard
2) extract_game_ids
3) fetch_boxscores (mapped per game)
4) write_raw_to_gcs
5) load_to_bq_staging
6) dbt_run
7) dbt_test
8) freshness_volume_checks
9) write_audit

## Idempotency Rules
- Raw data is immutable in GCS; every run has a run_id.
- BigQuery loads are partitioned by date and merged by stable keys.
- Re-running a logical date should not create duplicates.

## Local First, GCP Later
- Local dev uses Docker Compose for Airflow (and later Kafka/Spark).
- Cloud deploy uses GCP Compute Engine to run the same stack 24/7.

## Future Phases (Optional)
- Streaming (Kafka): live events -> GCS event log -> BQ updates.
- PySpark: heavy backfills and large transformations.

## Open Questions
- Exact GCS bucket naming and partitioning conventions.
- Final table schemas for staging/core/marts.
- Scheduling frequency and SLA expectations.
