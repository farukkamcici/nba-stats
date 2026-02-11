WITH src AS (
    SELECT
        source_date AS game_date,
        payload
    FROM {{source('nba_raw_stg', 'raw_scoreboard_json')}}
    WHERE source_date BETWEEN DATE('{{ var("start_date", "2026-01-29") }}') AND DATE('{{ var("end_date", "2026-01-29") }}')
),

games AS (
    SELECT
        game_date,
        game
    FROM src,
    UNNEST(JSON_QUERY_ARRAY(payload, '$.scoreboard.games')) AS game
)

SELECT
    game_date,
    JSON_VALUE(game, '$.gameId') AS game_id,
    SAFE_CAST(JSON_VALUE(game, '$.gameStatus') as INT64) AS game_status,
    JSON_VALUE(game, '$.gameStatusText') AS game_status_text,
    JSON_VALUE(game, '$.gameTimeUTC') AS game_time_utc,
    SAFE_CAST(JSON_VALUE(game, '$.seriesGameNumber') as INT64) AS series_game_number,
    JSON_VALUE(game, '$.gameLabel') AS game_label,
    JSON_VALUE(game, '$.gameSubLabel') AS game_sub_label,
    JSON_VALUE(game, '$.seriesText') AS series_text,
    JSON_VALUE(game, '$.seriesConference') AS series_conference,
    JSON_VALUE(game, '$.homeTeam.teamId') AS home_team_id,
    JSON_VALUE(game, '$.homeTeam.teamName') AS home_team_name,
    JSON_VALUE(game, '$.homeTeam.teamCity') AS home_team_city,
    JSON_VALUE(game, '$.homeTeam.teamTricode') AS home_team_tricode,
    SAFE_CAST(JSON_VALUE(game, '$.homeTeam.wins') as INT64) AS home_wins,
    SAFE_CAST(JSON_VALUE(game, '$.homeTeam.losses') as INT64) AS home_losses,
    SAFE_CAST(JSON_VALUE(game, '$.homeTeam.seed') as INT64) AS home_seed,
    SAFE_CAST(JSON_VALUE(game, '$.homeTeam.score') as INT64) AS home_score,
    JSON_VALUE(game, '$.awayTeam.teamId') AS away_team_id,
    JSON_VALUE(game, '$.awayTeam.teamName') AS away_team_name,
    JSON_VALUE(game, '$.awayTeam.teamCity') AS away_team_city,
    JSON_VALUE(game, '$.awayTeam.teamTricode') AS away_team_tricode,
    SAFE_CAST(JSON_VALUE(game, '$.awayTeam.wins') as INT64) AS away_wins,
    SAFE_CAST(JSON_VALUE(game, '$.awayTeam.losses') as INT64) AS away_losses,
    SAFE_CAST(JSON_VALUE(game, '$.awayTeam.seed') as INT64) AS away_seed,
    SAFE_CAST(JSON_VALUE(game, '$.awayTeam.score') as INT64) AS away_score
FROM games