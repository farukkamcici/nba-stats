# NBA API Integration Manual (for This Project)

This document focused on **how we should use the third‑party `nba_api` service inside this project**.

## 1) What `nba_api` is (and is not)
- It is a **Python client** that calls upstream NBA.com endpoints.
- It is **not** a web server; we are **consumers** of upstream data.

Upstream API families:
- **NBA Stats** (`stats.nba.com`) — tabular datasets (headers + rows)
- **NBA Live Data** (`cdn.nba.com`) — JSON payloads (scoreboard, boxscore, play‑by‑play)

## 2) How we use it in this project
We only consume a small subset of endpoints to build our data platform:
- **MVP**: scoreboard + boxscore
- **Later**: play‑by‑play (optional streaming)

All raw responses are written **immutably** to GCS before any transformations.

## 3) Recommended usage patterns (reliability first)
The upstream endpoints can throttle or change without warning. Use defensive patterns:

### 3.1 Use a shared HTTP session with retries
- Configure a shared `requests.Session()` with retry + backoff.
- Limit retries to idempotent GET requests only.

### 3.2 Add request pacing
- Avoid parallel storms.
- Add a small sleep between calls (0.2–1.0s).

### 3.3 Cache raw responses
- Cache by request URL or by (endpoint + params).
- Store raw JSON in GCS with a deterministic path.

### 3.4 Handle schema drift
- Use `dict.get()` for JSON keys.
- Check DataFrame columns before selecting.
- Persist raw JSON for debugging.

## 4) Response shapes (important)

### Stats endpoints
- Return **datasets** (headers + rows).
- In the client, each dataset is an `Endpoint.DataSet`.
- Useful methods:
  - `data_set.get_dict()` → `{headers, data}`
  - `data_set.get_data_frame()` → pandas DataFrame (if installed)

### Live endpoints
- Return JSON dictionaries.
- Useful methods:
  - `endpoint.get_dict()` → dict
  - `endpoint.get_json()` → string

## 5) Minimal examples (for local testing)

### Add as a dependency

```bash
pip install nba_api
```

### Stats example
```python
from nba_api.stats.endpoints import CommonPlayerInfo

player = CommonPlayerInfo(player_id=2544)
df = player.common_player_info.get_data_frame()
print(df.head())
```

### Live example
```python
from nba_api.live.nba.endpoints import ScoreBoard, BoxScore

sb = ScoreBoard()
games = sb.games.get_dict() or []
if games:
    game_id = games[0]["gameId"]
    box = BoxScore(game_id=game_id)
    print(box.get_dict().keys())
```

## 6) Where to find endpoint details
Use this reference doc when you need exact parameters or datasets:
- `api_reference.md` — full endpoint list + datasets/columns (also includes base URLs)

## 7) Operational constraints we must respect
- **403 risk**: NBA Stats endpoints can block non‑browser requests.
- **Rate limiting**: avoid high‑volume bursts; throttle requests.
- **Schema drift**: columns and keys can change without notice.
```

## 9) Summary (how we should behave)
- Treat the NBA API as unstable: **defensive coding + caching**.
- Write **raw JSON** to GCS first, then transform.
- Keep ingestion idempotent and replayable.
