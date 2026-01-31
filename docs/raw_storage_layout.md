# Raw Storage Layout + Ingestion Plan (MVP)

This document defines how we store raw NBA data in GCS and the MVP ingestion plan.

## 1) Raw GCS Path Conventions

Bucket: `nba-stats-9070`

### Scoreboard (daily index)
One file per date per run.

```
gs://nba-stats-9070/raw/nba/scoreboard/dt=YYYY-MM-DD/run_id=YYYYMMDD_HHMMSS/scoreboard.json
```

### Boxscore (per game)
One file per game per run.

```
gs://nba-stats-9070/raw/nba/boxscore/dt=YYYY-MM-DD/game_id=GAME_ID/run_id=YYYYMMDD_HHMMSS/boxscore.json
```

## 2) Ingestion Plan (MVP)

Endpoints (consumer only):
- Scoreboard (daily game list)
- BoxScore (per `game_id`)

Plan:
1) Call Scoreboard for a specific date.
2) Extract `game_id` list from the response.
3) For each `game_id`, call BoxScore.
4) Write raw JSON to GCS using the paths above.
5) Pace requests with ~1.0s delay; retry failures (3 attempts, exponential backoff).

## 3) Idempotency Rules
- Raw data is immutable in GCS.
- Each run has a unique `run_id` (format: `YYYYMMDD_HHMMSS`).
- Re-running a date writes a new run; **do not delete old raw files**.
- Downstream loads (BQ staging/core/marts) select the **latest run** for that date.

## 4) Notes
- Raw storage is for replay/debugging; keep it append-only.
- Scoreboard is the daily “index” of games.
- Boxscore is the detailed per-game stats.
