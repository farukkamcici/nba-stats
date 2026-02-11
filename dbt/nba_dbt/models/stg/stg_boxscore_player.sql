WITH src AS (
    SELECT
        JSON_VALUE(payload, '$.boxScoreTraditional.gameId') AS game_id,
        JSON_QUERY(payload, '$.boxScoreTraditional.homeTeam') AS home_team,
        JSON_QUERY(payload, '$.boxScoreTraditional.awayTeam') AS away_team
    FROM {{source('nba_raw_stg', 'raw_boxscore_json')}}
    WHERE source_date BETWEEN DATE('{{ var("start_date", "2026-01-29") }}') AND DATE('{{ var("end_date", "2026-01-29") }}')
),

home_players AS(
    SELECT
        game_id,
        JSON_VALUE(home_team, '$.teamId') AS team_id,
        player
    FROM src,
    UNNEST(JSON_QUERY_ARRAY(home_team, '$.players')) AS player
),

away_players AS(
    SELECT
        game_id,
        JSON_VALUE(away_team, '$.teamId') AS team_id,
        player
    FROM src,
    UNNEST(JSON_QUERY_ARRAY(away_team, '$.players')) AS player
),

players AS(
    SELECT
        *
    FROM home_players
    UNION ALL
    SELECT
        *
    FROM away_players
)

SELECT
    game_id,
    team_id,
    JSON_VALUE(player, '$.personId') AS player_id,
    JSON_VALUE(player, '$.firstName') AS first_name,
    JSON_VALUE(player, '$.familyName') AS family_name,
    JSON_VALUE(player, '$.nameI') AS name_i,
    JSON_VALUE(player, '$.playerSlug') AS player_slug,
    JSON_VALUE(player, '$.position') AS position,
    JSON_VALUE(player, '$.statistics.minutes') AS minutes,
    SAFE_CAST(JSON_VALUE(player, '$.statistics.fieldGoalsMade') AS INT64) AS fgm,
    SAFE_CAST(JSON_VALUE(player, '$.statistics.fieldGoalsAttempted') AS INT64) AS fga,
    SAFE_CAST(JSON_VALUE(player, '$.statistics.fieldGoalsPercentage') AS FLOAT64) AS fg_pct,
    SAFE_CAST(JSON_VALUE(player, '$.statistics.threePointersMade') AS INT64) AS fg3m,
    SAFE_CAST(JSON_VALUE(player, '$.statistics.threePointersAttempted') AS INT64) AS fg3a,
    SAFE_CAST(JSON_VALUE(player, '$.statistics.threePointersPercentage') AS FLOAT64) AS fg3_pct,
    SAFE_CAST(JSON_VALUE(player, '$.statistics.freeThrowsMade') AS INT64) AS ftm,
    SAFE_CAST(JSON_VALUE(player, '$.statistics.freeThrowsAttempted') AS INT64) AS fta,
    SAFE_CAST(JSON_VALUE(player, '$.statistics.freeThrowsPercentage') AS FLOAT64) AS ft_pct,
    SAFE_CAST(JSON_VALUE(player, '$.statistics.reboundsOffensive') AS INT64) AS oreb,
    SAFE_CAST(JSON_VALUE(player, '$.statistics.reboundsDefensive') AS INT64) AS dreb,
    SAFE_CAST(JSON_VALUE(player, '$.statistics.reboundsTotal') AS INT64) AS reb,
    SAFE_CAST(JSON_VALUE(player, '$.statistics.assists') AS INT64) AS ast,
    SAFE_CAST(JSON_VALUE(player, '$.statistics.steals') AS INT64) AS stl,
    SAFE_CAST(JSON_VALUE(player, '$.statistics.blocks') AS INT64) AS blk,
    SAFE_CAST(JSON_VALUE(player, '$.statistics.turnovers') AS INT64) AS tov,
    SAFE_CAST(JSON_VALUE(player, '$.statistics.foulsPersonal') AS INT64) AS pf,
    SAFE_CAST(JSON_VALUE(player, '$.statistics.points') AS INT64) AS pts,
    SAFE_CAST(JSON_VALUE(player, '$.statistics.plusMinusPoints') AS FLOAT64) AS plus_minus
FROM players

