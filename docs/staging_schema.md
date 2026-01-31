# Staging Schema in BigQuery

## Tables:
   - `stg_scoreboard_games`
   - `stg_boxscore_team`
   - `stg_boxscore_player`

### `stg_scoreboard_games`
    - game_date
    - game_id
    - game_status
    - game_status_text
    - game_time_utc
    - series_game_number
    - game_label
    - game_sub_label
    - series_text
    - series_conference
    - home_team_id
    - home_team_name
    - home_team_city
    - home_team_tricode
    - home_wins
    - home_losses
    - home_seed
    - home_score
    - away_team_id
    - away_team_name
    - away_team_city
    - away_team_tricode
    - away_wins
    - away_losses
    - away_seed
    - away_score

### `stg_boxscore_team`
    - game_id
    - team_id
    - team_city
    - team_name
    - team_tricode
    - minutes
    - fgm
    - fga
    - fg_pct
    - fg3m
    - fg3a
    - fg3_pct
    - ftm
    - fta
    - ft_pct
    - oreb
    - dreb
    - reb
    - ast
    - stl
    - blk
    - tov
    - pf
    - pts
    - plus_minus

### `stg_boxscore_player`
    - game_id
    - team_id
    - player_id
    - first_name
    - family_name
    - name_i
    - player_slug
    - position
    - minutes
    - fgm
    - fga
    - fg_pct
    - fg3m
    - fg3a
    - fg3_pct
    - ftm
    - fta
    - ft_pct
    - oreb
    - dreb
    - reb
    - ast
    - stl
    - blk
    - tov
    - pf
    - pts
    - plus_minus
    




