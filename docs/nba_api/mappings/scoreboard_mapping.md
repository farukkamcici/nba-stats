# Scoreboard Mapping (Full Fields)

Source: `nba_api.live.nba.endpoints.ScoreBoard`

## Full example response (all fields shown, values shortened)
```json
{
  "meta": {
    "version": 1,
    "request": "http://nba.cloud/league/00/YYYY/MM/DD/scoreboard?Format=json",
    "time": "YYYY-MM-DDTHH:MM:SS.SSSZ"
  },
  "scoreboard": {
    "gameDate": "YYYY-MM-DD",
    "leagueId": "00",
    "leagueName": "National Basketball Association",
    "games": [
      {
        "gameId": "0022500001",
        "gameCode": "YYYYMMDD/ABCCDE",
        "gameStatus": 3,
        "gameStatusText": "Final",
        "period": 4,
        "gameClock": "",
        "gameTimeUTC": "YYYY-MM-DDTHH:MM:SSZ",
        "gameEt": "YYYY-MM-DDTHH:MM:SSZ",
        "regulationPeriods": 4,
        "seriesGameNumber": "",
        "gameLabel": "",
        "gameSubLabel": "",
        "seriesText": "",
        "ifNecessary": false,
        "seriesConference": "",
        "poRoundDesc": "",
        "gameSubtype": "",
        "isNeutral": false,
        "gameLeaders": {
          "homeLeaders": {
            "personId": 0,
            "name": "",
            "playerSlug": "",
            "jerseyNum": "",
            "position": "",
            "teamTricode": "",
            "points": 0,
            "rebounds": 0,
            "assists": 0
          },
          "awayLeaders": {
            "personId": 0,
            "name": "",
            "playerSlug": "",
            "jerseyNum": "",
            "position": "",
            "teamTricode": "",
            "points": 0,
            "rebounds": 0,
            "assists": 0
          }
        },
        "teamLeaders": {
          "homeLeaders": {
            "personId": 0,
            "name": "",
            "playerSlug": "",
            "jerseyNum": "",
            "position": "",
            "teamTricode": "",
            "points": 0.0,
            "rebounds": 0.0,
            "assists": 0.0
          },
          "awayLeaders": {
            "personId": 0,
            "name": "",
            "playerSlug": "",
            "jerseyNum": "",
            "position": "",
            "teamTricode": "",
            "points": 0.0,
            "rebounds": 0.0,
            "assists": 0.0
          },
          "seasonLeadersFlag": 0
        },
        "broadcasters": {
          "nationalBroadcasters": [],
          "nationalRadioBroadcasters": [],
          "nationalOttBroadcasters": [],
          "homeTvBroadcasters": [],
          "homeRadioBroadcasters": [],
          "homeOttBroadcasters": [],
          "awayTvBroadcasters": [],
          "awayRadioBroadcasters": [],
          "awayOttBroadcasters": []
        },
        "homeTeam": {
          "teamId": 0,
          "teamName": "",
          "teamCity": "",
          "teamTricode": "",
          "teamSlug": "",
          "wins": 0,
          "losses": 0,
          "score": 0,
          "seed": 0,
          "inBonus": null,
          "timeoutsRemaining": 0,
          "periods": [
            { "period": 1, "periodType": "REGULAR", "score": 0 }
          ]
        },
        "awayTeam": {
          "teamId": 0,
          "teamName": "",
          "teamCity": "",
          "teamTricode": "",
          "teamSlug": "",
          "wins": 0,
          "losses": 0,
          "score": 0,
          "seed": 0,
          "inBonus": null,
          "timeoutsRemaining": 0,
          "periods": [
            { "period": 1, "periodType": "REGULAR", "score": 0 }
          ]
        }
      }
    ]
  }
}
```

## Parsing guide (key dicts and how to reach them)

- `meta` [dict] → `meta`
- `scoreboard` [dict] → `scoreboard`
- `games` [list of dict] → `scoreboard.games`
- `gameLeaders` [dict] → `scoreboard.games[*].gameLeaders`
- `teamLeaders` [dict] → `scoreboard.games[*].teamLeaders`
- `broadcasters` [dict] → `scoreboard.games[*].broadcasters`
- `homeTeam` [dict] → `scoreboard.games[*].homeTeam`
- `awayTeam` [dict] → `scoreboard.games[*].awayTeam`
