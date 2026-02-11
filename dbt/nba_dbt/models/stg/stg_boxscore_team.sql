WITH src AS (
    SELECT
        JSON_VALUE(payload, '$.boxScoreTraditional.gameId') AS game_id,
        JSON_QUERY(payload, '$.boxScoreTraditional.homeTeam') AS home_team,
        JSON_QUERY(payload, '$.boxScoreTraditional.awayTeam') AS away_team
    FROM {{source('nba_raw_stg', 'raw_boxscore_json')}}
    WHERE source_date BETWEEN DATE('{{ var("start_date", "2026-01-29") }}') AND DATE('{{ var("end_date", "2026-01-29") }}')
),

home_teams AS (
    SELECT
        game_id,
        JSON_VALUE(home_team, '$.teamId') AS team_id,
        JSON_VALUE(home_team, '$.teamCity') AS team_city,
        JSON_VALUE(home_team, '$.teamName') AS team_name,
        JSON_VALUE(home_team, '$.teamTricode') AS team_tricode,
        JSON_VALUE(home_team, '$.statistics.minutes') AS minutes,
        SAFE_CAST(JSON_VALUE(home_team, '$.statistics.fieldGoalsMade') AS INT64) AS fgm,
        SAFE_CAST(JSON_VALUE(home_team, '$.statistics.fieldGoalsAttempted') AS INT64) AS fga,
        SAFE_CAST(JSON_VALUE(home_team, '$.statistics.fieldGoalsPercentage') AS FLOAT64) AS fg_pct,
        SAFE_CAST(JSON_VALUE(home_team, '$.statistics.threePointersMade') AS INT64) AS fg3m,
        SAFE_CAST(JSON_VALUE(home_team, '$.statistics.threePointersAttempted') AS INT64) AS fg3a,
        SAFE_CAST(JSON_VALUE(home_team, '$.statistics.threePointersPercentage') AS FLOAT64) AS fg3_pct,
        SAFE_CAST(JSON_VALUE(home_team, '$.statistics.freeThrowsMade') AS INT64) AS ftm,
        SAFE_CAST(JSON_VALUE(home_team, '$.statistics.freeThrowsAttempted') AS INT64) AS fta,
        SAFE_CAST(JSON_VALUE(home_team, '$.statistics.freeThrowsPercentage') AS FLOAT64) AS ft_pct,
        SAFE_CAST(JSON_VALUE(home_team, '$.statistics.reboundsOffensive') AS INT64) AS oreb,
        SAFE_CAST(JSON_VALUE(home_team, '$.statistics.reboundsDefensive') AS INT64) AS dreb,
        SAFE_CAST(JSON_VALUE(home_team, '$.statistics.reboundsTotal') AS INT64) AS reb,
        SAFE_CAST(JSON_VALUE(home_team, '$.statistics.assists') AS INT64) AS ast,
        SAFE_CAST(JSON_VALUE(home_team, '$.statistics.steals') AS INT64) AS stl,
        SAFE_CAST(JSON_VALUE(home_team, '$.statistics.blocks') AS INT64) AS blk,
        SAFE_CAST(JSON_VALUE(home_team, '$.statistics.turnovers') AS INT64) AS tov,
        SAFE_CAST(JSON_VALUE(home_team, '$.statistics.foulsPersonal') AS INT64) AS pf,
        SAFE_CAST(JSON_VALUE(home_team, '$.statistics.points') AS INT64) AS pts,
        SAFE_CAST(JSON_VALUE(home_team, '$.statistics.plusMinusPoints') AS FLOAT64) AS plus_minus
    FROM src
),

away_teams AS (
    SELECT
        game_id,
        JSON_VALUE(away_team, '$.teamId') AS team_id,
        JSON_VALUE(away_team, '$.teamCity') AS team_city,
        JSON_VALUE(away_team, '$.teamName') AS team_name,
        JSON_VALUE(away_team, '$.teamTricode') AS team_tricode,
        JSON_VALUE(away_team, '$.statistics.minutes') AS minutes,
        SAFE_CAST(JSON_VALUE(away_team, '$.statistics.fieldGoalsMade') AS INT64) AS fgm,
        SAFE_CAST(JSON_VALUE(away_team, '$.statistics.fieldGoalsAttempted') AS INT64) AS fga,
        SAFE_CAST(JSON_VALUE(away_team, '$.statistics.fieldGoalsPercentage') AS FLOAT64) AS fg_pct,
        SAFE_CAST(JSON_VALUE(away_team, '$.statistics.threePointersMade') AS INT64) AS fg3m,
        SAFE_CAST(JSON_VALUE(away_team, '$.statistics.threePointersAttempted') AS INT64) AS fg3a,
        SAFE_CAST(JSON_VALUE(away_team, '$.statistics.threePointersPercentage') AS FLOAT64) AS fg3_pct,
        SAFE_CAST(JSON_VALUE(away_team, '$.statistics.freeThrowsMade') AS INT64) AS ftm,
        SAFE_CAST(JSON_VALUE(away_team, '$.statistics.freeThrowsAttempted') AS INT64) AS fta,
        SAFE_CAST(JSON_VALUE(away_team, '$.statistics.freeThrowsPercentage') AS FLOAT64) AS ft_pct,
        SAFE_CAST(JSON_VALUE(away_team, '$.statistics.reboundsOffensive') AS INT64) AS oreb,
        SAFE_CAST(JSON_VALUE(away_team, '$.statistics.reboundsDefensive') AS INT64) AS dreb,
        SAFE_CAST(JSON_VALUE(away_team, '$.statistics.reboundsTotal') AS INT64) AS reb,
        SAFE_CAST(JSON_VALUE(away_team, '$.statistics.assists') AS INT64) AS ast,
        SAFE_CAST(JSON_VALUE(away_team, '$.statistics.steals') AS INT64) AS stl,
        SAFE_CAST(JSON_VALUE(away_team, '$.statistics.blocks') AS INT64) AS blk,
        SAFE_CAST(JSON_VALUE(away_team, '$.statistics.turnovers') AS INT64) AS tov,
        SAFE_CAST(JSON_VALUE(away_team, '$.statistics.foulsPersonal') AS INT64) AS pf,
        SAFE_CAST(JSON_VALUE(away_team, '$.statistics.points') AS INT64) AS pts,
        SAFE_CAST(JSON_VALUE(away_team, '$.statistics.plusMinusPoints') AS FLOAT64) AS plus_minus
    FROM src
),

teams AS (
    SELECT * FROM home_teams
    UNION ALL
    SELECT * FROM away_teams
)

SELECT
    game_id,
    team_id,
    team_city,
    team_name,
    team_tricode,
    minutes,
    fgm,
    fga,
    fg_pct,
    fg3m,
    fg3a,
    fg3_pct,
    ftm,
    fta,
    ft_pct,
    oreb,
    dreb,
    reb,
    ast,
    stl,
    blk,
    tov,
    pf,
    pts,
    plus_minus
FROM teams


