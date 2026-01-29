# NBA Data Platform (Learning Project)

This is a mentor‑first, learning‑focused data engineering project. The goal is to build a production‑style NBA data platform while learning real tools and workflows by doing.

## Why this project
- Learn end‑to‑end data platform design (ingestion → warehouse → marts → orchestration).
- Build portfolio‑quality artifacts for data engineering roles.

## High‑level architecture (MVP)
NBA endpoints (via `nba_api`) → Ingestion (Python) → GCS Raw → BigQuery Staging → dbt Core + Marts → Consumers

See `docs/architecture.md` for the full overview.

## Third‑party NBA API docs (required)
We are consumers of `nba_api`. Use these docs when building ingestion:
- `docs/nba_api/integration_manual.md`
- `docs/nba_api/api_reference.md`

## Project roadmap
The current plan is documented in:
- `docs/task_plan.md`

## Current status
Documentation only; implementation starts with Phase 0 (foundations).

