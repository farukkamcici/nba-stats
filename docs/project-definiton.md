# Project Definition Document (PDD)
## NBA Data Platform — GCP (Self-Managed) + BigQuery + Airflow + dbt + Kafka + PySpark

### 1) Purpose
Build a production-pattern data platform for NBA game data that supports:
- **Historical backfill** (one-time or repeatable)
- **Daily incremental loads** (reliable scheduled runs)
- **Optional near-real-time streaming** (game-time events)

The project is designed to demonstrate real-world Data Engineering capabilities:
- **Idempotency** (safe reruns)
- **Backfill / replay**
- **Data quality gates** (tests + freshness/volume checks)
- **Operational robustness** (retries, logging, auditability)
- **Tooling that is portable** (Airflow/Kafka/Spark/dbt), while using **BigQuery** as the warehouse.

---

### 2) Scope

#### Phase 1 — MVP (Batch ELT, reliable daily pipeline)
**Data sources**
- Scoreboard (daily game list)
- Boxscore (team + player game stats)

**Deliverables**
- Raw data stored in GCS (Bronze)
- Staging + Core + Marts in BigQuery
- dbt models + tests
- Airflow DAG for daily runs + backfills
- Data quality checks (dbt tests + freshness/volume checks)
- Run audit table + basic runbook docs

#### Phase 2 — Streaming (Kafka)
- Poll live game endpoints (scoreboard and/or play-by-play) and publish events to Kafka
- Kafka consumer appends to GCS “event log” (append-only)
- Scheduled batch jobs load to BigQuery and update marts (hourly/daily)

#### Phase 3 — PySpark (heavy processing / replay acceleration)
- PySpark jobs for:
  - large backfills / reprocessing
  - event-level heavy transformations (e.g., derived metrics, aggregation, enrichment)
- Output written to BigQuery (directly) or to GCS curated zone then loaded to BigQuery

---

### 3) Out of Scope (Non-goals)
- Ingesting “every endpoint” available (scope will remain intentionally narrow)
- Building a fully-featured consumer product UI (optional later)
- Millisecond real-time streaming semantics (polling-based streaming is sufficient)
- Kubernetes-first deployment (can be explored later; not required)

---

### 4) Target Audience / Use Cases
**Audience**
- Technical reviewers (DE/Analytics Engineering) evaluating production readiness
- Personal use for NBA analytics and experimentation

**Core use cases**
- “Today’s games” summary and final results
- Team-level and player-level trends over last N games
- Season-to-date summaries by team/player
- (Optional) live game event stream and near-real-time summaries

---

### 5) Technology Stack

#### GCP (Managed services)
- **BigQuery**: data warehouse (staging/core/marts; SQL execution for dbt)
- **Cloud Storage (GCS)**: raw/bronze storage (append-only logs, replay source)
- **Cloud IAM**: Service Accounts + least privilege

#### Self-managed runtime (Compute Engine VM + Docker Compose)
- **Airflow**: orchestration (scheduler, webserver, workers)
- **Postgres**: Airflow metadata database
- **dbt (dbt-bigquery)**: transformations, tests, documentation
- **Kafka**: streaming backbone (Phase 2)
- **PySpark**: distributed processing (Phase 3)

---

### 6) System Architecture (High Level)
**Where things run**
- **Compute Engine VM** runs: Airflow, dbt CLI, ingestion code, Kafka (optional), Spark (optional)
- **GCS** stores raw data (Bronze) and streaming event logs (append-only)
- **BigQuery** stores staging/core/marts and runs transformation SQL

**Key principle**
- **Raw data is immutable and always retained** (enables replay/backfill and debugging)
- BigQuery contains curated tables for analytics and downstream consumption

---

### 7) Data to Store (What exactly we keep)

#### 7.1 Bronze (Raw, in GCS)
- `scoreboard` raw JSON per date/run
- `boxscore` raw JSON per game/date/run
- (Phase 2) `events` raw JSONL append-only per game/date/run

#### 7.2 BigQuery Datasets (Logical Layers)
- `nba_raw_stg`  — staging tables loaded from raw files
- `nba_core`     — cleaned/standardized “silver” layer
- `nba_marts`    — analytics-ready “gold” layer
- `nba_audit`    — run logs, quality results, pipeline metrics

#### 7.3 Core Tables (Minimum)
Dimensions
- `dim_team(team_id, team_name, tricode, ...)`
- `dim_player(player_id, player_name, ...)`
- `dim_date(date, season, week, ...)` (optional but recommended)

Facts (MVP)
- `fact_game(game_id, game_date, home_team_id, away_team_id, status, home_score, away_score, ...)`
- `fact_team_game(game_id, team_id, pts, reb, ast, fgm, fga, fg3m, fg3a, ftm, fta, tov, stl, blk, ...)`
- `fact_player_game(game_id, player_id, team_id, min, pts, reb, ast, fgm, fga, fg3m, fg3a, ftm, fta, tov, ...)`

(Phase 2/3) Event Fact
- `fact_pbp_event(game_id, event_num, period, clock, msg_type, score, margin, description, player_ids..., ...)`

Audit / Ops
- `pipeline_runs(run_id, logical_date, env, status, started_at, finished_at, error_summary, ...)`
- `pipeline_metrics(run_id, logical_date, entity, rows_loaded, freshness_ok, volume_ok, ...)`

---

### 8) Workflows (End-to-end Flows)

#### 8.1 Historical Backfill (Repeatable)
1. Airflow triggers a backfill run for a date range.
2. Ingestion pulls Scoreboard per date → extracts `game_id`s.
3. Ingestion pulls Boxscore for each `game_id`.
4. Raw is written to GCS in a deterministic partitioned path.
5. Files are loaded into BigQuery staging (`nba_raw_stg`).
6. dbt builds core + marts (incremental where applicable).
7. dbt tests + freshness/volume checks run.
8. Audit tables are updated (success/failure + metrics).

#### 8.2 Daily Incremental (Scheduled)
1. Airflow scheduled run starts (daily; optionally more frequent on game days).
2. Pull today’s scoreboard → list of `game_id`s.
3. Pull boxscore for each game → write raw to GCS.
4. Load only today’s files into BigQuery staging.
5. Run dbt incremental models (core + marts).
6. Run dbt tests and basic freshness/volume checks.
7. Write audit results.

#### 8.3 Streaming (Phase 2, Optional)
1. Producer polls live game data and publishes events to Kafka.
2. Consumer reads from Kafka and appends to GCS raw event logs (JSONL).
3. A scheduled job loads new events to BigQuery and updates event-based marts.

#### 8.4 PySpark Processing (Phase 3, Optional)
- Spark jobs read GCS raw/event logs, compute heavy aggregations, and write results to BigQuery (or curated GCS then load).

---

### 9) Orchestration Standard (Airflow)

#### 9.1 DAG Strategy
MVP uses **one DAG** to avoid operational fragmentation:
- DAG: `nba_daily_pipeline`

Tasks (MVP)
1. `fetch_scoreboard`
2. `extract_game_ids`
3. `fetch_boxscores` (mapped per `game_id`)
4. `write_raw_to_gcs`
5. `load_to_bq_staging`
6. `dbt_run`
7. `dbt_test`
8. `freshness_volume_checks`
9. `write_audit`

Backfill uses the same DAG with different `logical_date` and date ranges.

#### 9.2 Idempotency Rules
- Re-running a DAG for the same logical date must not produce duplicates or inconsistent results.
- Staging loads are partitioned and/or merged deterministically.
- Fact tables use stable keys:
  - `fact_game`: `game_id` unique
  - `fact_team_game`: `(game_id, team_id)` unique
  - `fact_player_game`: `(game_id, player_id)` unique

---

### 10) Data Quality (MVP Baseline)

#### 10.1 dbt Tests (Minimum)
- **not_null**: `game_id`, `team_id`, `player_id`, `game_date`
- **unique**:
  - `fact_game.game_id`
  - `fact_team_game(game_id, team_id)`
  - `fact_player_game(game_id, player_id)`
- **relationships**:
  - `fact_*` → `dim_team`
  - `fact_*` → `dim_player`

#### 10.2 Freshness Checks
- Scoreboard for a given date must arrive within an expected window (configurable).
- Latest successful run timestamp must be within the SLA window.

#### 10.3 Volume Checks
- Count of games for a date should be within reasonable bounds (0 allowed on off-days).
- Player rows per game should be within expected ranges (flag anomalies).

Failures:
- If tests/checks fail, the pipeline run is marked failed and recorded in audit tables.

---

### 11) Storage, Partitioning, and Cost Control (BigQuery)
- Partition fact tables by `game_date` (or `dt`).
- Cluster by common filter keys (e.g., `game_id`, `team_id`) when helpful.
- Keep staging tables ephemeral where possible.
- Use selective loads (only new/changed partitions) to avoid expensive scans.

---

### 12) Security & IAM
- Use **Service Accounts** for runtime identity.
- Preferred: attach Service Account to VM (avoid key files).
- Permissions are least-privilege:
  - GCS: read/write specific bucket/prefix
  - BigQuery: run jobs, read/write specific datasets
- Secrets (if any) stored via environment variables/secret management; never committed to Git.

---

### 13) Conventions & Standards

#### 13.1 Naming
- BigQuery datasets: `nba_raw_stg`, `nba_core`, `nba_marts`, `nba_audit`
- Tables: `snake_case`, semantic prefixes:
  - `dim_*`, `fact_*`, `mart_*`, `stg_*`

#### 13.2 GCS Layout
Recommended layout (partitioned and replay-friendly):
- `gs://<bucket>/raw/nba/scoreboard/dt=YYYY-MM-DD/run_id=<id>/scoreboard.json`
- `gs://<bucket>/raw/nba/boxscore/dt=YYYY-MM-DD/game_id=<id>/run_id=<id>/boxscore.json`
- (Phase 2) `gs://<bucket>/raw/nba/events/dt=YYYY-MM-DD/game_id=<id>/run_id=<id>/events.jsonl`

#### 13.3 Environments
- Separate `dev` and `prod` via:
  - dataset prefix/suffix (`nba_dev_*`, `nba_prod_*`) OR
  - separate GCS prefixes (`.../dev/...`, `.../prod/...`)
- Config-driven toggles (ENV, bucket, dataset, schedule frequency)

---

### 14) Deployment & Development Approach

#### Development (Local)
- Code is written locally in a Git repository.
- Local Docker Compose for fast iteration:
  - Airflow + Postgres (and optionally Kafka/Spark)
- Local runs can still target GCP services (BigQuery/GCS) for realistic testing.

#### Runtime (GCP)
- A Compute Engine VM runs the same Docker Compose stack for 24/7 scheduling.
- Deploy by pulling the repo (or building a Docker image) and restarting services.
- Logs and audit tables provide traceability.

---

### 15) Project Completion Criteria (“Definition of Done”)

MVP is considered complete when:
1. The stack starts with one command (Docker Compose) on a VM.
2. Backfill can run for a configured date range without manual intervention.
3. Daily scheduled runs succeed and update BigQuery marts.
4. dbt tests run automatically and gate publishing.
5. Freshness/volume checks run and write results to audit tables.
6. Rerunning a day is safe (idempotent) and reproducible.
7. Basic documentation exists:
   - Architecture overview
   - How to run backfill
   - How to troubleshoot failures (runbook)
   - Data model summary (core + marts)

Optional completion additions:
- Kafka streaming path implemented with replayable event logs
- PySpark jobs implemented for heavy backfill/reprocessing
- Minimal BI dashboard (Metabase/Superset/Looker Studio) pointing to marts

---

### 16) Appendix — Suggested Repository Structure (Guideline)
- `airflow/`
  - `dags/`
  - `plugins/` (optional)
- `ingestion/`
  - `fetch_scoreboard.py`
  - `fetch_boxscore.py`
- `dbt/`
  - `models/`
  - `tests/`
- `spark/` (Phase 3)
- `kafka/` (Phase 2)
  - `producer/`
  - `consumer/`
- `infra/`
  - `docker-compose.yml`
  - `.env.example`
- `docs/`
  - `architecture.md`
  - `runbook.md`
  - `data_model.md`
  - `operations.md`
