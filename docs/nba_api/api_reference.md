# nba_api — Aggregated API Reference

Single-file reference for endpoints and response shapes used by this client library.

Generated from this repo on `2026-01-29`.

## Servers (Base URLs)
- Stats: `https://stats.nba.com/stats`
- Live: `https://cdn.nba.com/static/json/liveData`

## Response Shapes (Quick Reference)
### Stats endpoints
Stats responses are usually *tabular result sets* with `headers` + `rowSet`.

### Live endpoints
Live endpoints return JSON dictionaries (e.g., `scoreboard`, `game`, `meta`).

## Index

- Stats endpoints: **138**
- Live endpoints: **4**

### Stats endpoints

| Python class | HTTP path | Required args | Data sets |
|---|---|---|---|
| [`AllTimeLeadersGrids`](#alltimeleadersgrids) | `/alltimeleadersgrids` |  | ASTLeaders, BLKLeaders, DREBLeaders, FG3ALeaders, FG3MLeaders, FG3_PCTLeaders, FGALeaders, FGMLeaders, FG_PCTLeaders, FTALeaders, FTMLeaders, FT_PCTLeaders, GPLeaders, OREBLeaders, PFLeaders, PTSLeaders, REBLeaders, STLLeaders, TOVLeaders |
| [`AssistLeaders`](#assistleaders) | `/assistleaders` |  | AssistLeaders |
| [`AssistTracker`](#assisttracker) | `/assisttracker` |  | AssistTracker |
| [`BoxScoreAdvancedV2`](#boxscoreadvancedv2) | `/boxscoreadvancedv2` | `game_id` | PlayerStats, TeamStats |
| [`BoxScoreAdvancedV3`](#boxscoreadvancedv3) | `/boxscoreadvancedv3` | `game_id` | PlayerStats, TeamStats |
| [`BoxScoreDefensiveV2`](#boxscoredefensivev2) | `/boxscoredefensivev2` | `game_id` | PlayerStats, TeamStats |
| [`BoxScoreFourFactorsV2`](#boxscorefourfactorsv2) | `/boxscorefourfactorsv2` | `game_id` | sqlPlayersFourFactors, sqlTeamsFourFactors |
| [`BoxScoreFourFactorsV3`](#boxscorefourfactorsv3) | `/boxscorefourfactorsv3` | `game_id` | PlayerStats, TeamStats |
| [`BoxScoreHustleV2`](#boxscorehustlev2) | `/boxscorehustlev2` | `game_id` | PlayerStats, TeamStats |
| [`BoxScoreMatchupsV3`](#boxscorematchupsv3) | `/boxscorematchupsv3` | `game_id` | PlayerStats |
| [`BoxScoreMiscV2`](#boxscoremiscv2) | `/boxscoremiscv2` | `game_id` | sqlPlayersMisc, sqlTeamsMisc |
| [`BoxScoreMiscV3`](#boxscoremiscv3) | `/boxscoremiscv3` | `game_id` | PlayerStats, TeamStats |
| [`BoxScorePlayerTrackV3`](#boxscoreplayertrackv3) | `/boxscoreplayertrackv3` | `game_id` | PlayerStats, TeamStats |
| [`BoxScoreScoringV2`](#boxscorescoringv2) | `/boxscorescoringv2` | `game_id` | sqlPlayersScoring, sqlTeamsScoring |
| [`BoxScoreScoringV3`](#boxscorescoringv3) | `/boxscorescoringv3` | `game_id` | PlayerStats, TeamStats |
| [`BoxScoreSummaryV2`](#boxscoresummaryv2) | `/boxscoresummaryv2` | `game_id` | AvailableVideo, GameInfo, GameSummary, InactivePlayers, LastMeeting, LineScore, Officials, OtherStats, SeasonSeries |
| [`BoxScoreSummaryV3`](#boxscoresummaryv3) | `/boxscoresummaryv3` | `game_id` | GameSummary, GameInfo, ArenaInfo, Officials, LineScore, InactivePlayers, LastFiveMeetings, OtherStats, AvailableVideo |
| [`BoxScoreTraditionalV2`](#boxscoretraditionalv2) | `/boxscoretraditionalv2` | `game_id` | PlayerStats, TeamStarterBenchStats, TeamStats |
| [`BoxScoreTraditionalV3`](#boxscoretraditionalv3) | `/boxscoretraditionalv3` | `game_id` | PlayerStats, TeamStarterBenchStats, TeamStats |
| [`BoxScoreUsageV2`](#boxscoreusagev2) | `/boxscoreusagev2` | `game_id` | sqlPlayersUsage, sqlTeamsUsage |
| [`BoxScoreUsageV3`](#boxscoreusagev3) | `/boxscoreusagev3` | `game_id` | PlayerStats, TeamStats |
| [`CommonAllPlayers`](#commonallplayers) | `/commonallplayers` |  | CommonAllPlayers |
| [`CommonPlayerInfo`](#commonplayerinfo) | `/commonplayerinfo` | `player_id` | AvailableSeasons, CommonPlayerInfo, PlayerHeadlineStats |
| [`CommonPlayoffSeries`](#commonplayoffseries) | `/commonplayoffseries` |  | PlayoffSeries |
| [`CommonTeamRoster`](#commonteamroster) | `/commonteamroster` | `team_id` | Coaches, CommonTeamRoster |
| [`CommonTeamYears`](#commonteamyears) | `/commonteamyears` |  | TeamYears |
| [`CumeStatsPlayer`](#cumestatsplayer) | `/cumestatsplayer` | `player_id`, `game_ids` | GameByGameStats, TotalPlayerStats |
| [`CumeStatsPlayerGames`](#cumestatsplayergames) | `/cumestatsplayergames` | `player_id` | CumeStatsPlayerGames |
| [`CumeStatsTeam`](#cumestatsteam) | `/cumestatsteam` | `team_id`, `game_ids` | GameByGameStats, TotalTeamStats |
| [`CumeStatsTeamGames`](#cumestatsteamgames) | `/cumestatsteamgames` | `team_id` | CumeStatsTeamGames |
| [`DefenseHub`](#defensehub) | `/defensehub` |  | DefenseHubStat1, DefenseHubStat10, DefenseHubStat2, DefenseHubStat3, DefenseHubStat4, DefenseHubStat5, DefenseHubStat6, DefenseHubStat7, DefenseHubStat8, DefenseHubStat9 |
| [`DraftBoard`](#draftboard) | `/draftboard` |  | DraftBoard |
| [`DraftCombineDrillResults`](#draftcombinedrillresults) | `/draftcombinedrillresults` |  | Results |
| [`DraftCombineNonStationaryShooting`](#draftcombinenonstationaryshooting) | `/draftcombinenonstationaryshooting` |  | Results |
| [`DraftCombinePlayerAnthro`](#draftcombineplayeranthro) | `/draftcombineplayeranthro` |  | Results |
| [`DraftCombineSpotShooting`](#draftcombinespotshooting) | `/draftcombinespotshooting` |  | Results |
| [`DraftCombineStats`](#draftcombinestats) | `/draftcombinestats` |  | DraftCombineStats |
| [`DraftHistory`](#drafthistory) | `/drafthistory` |  | DraftHistory |
| [`DunkScoreLeaders`](#dunkscoreleaders) | `/dunkscoreleaders` |  | Dunks |
| [`FantasyWidget`](#fantasywidget) | `/fantasywidget` |  | FantasyWidgetResult |
| [`FranchiseHistory`](#franchisehistory) | `/franchisehistory` |  | DefunctTeams, FranchiseHistory |
| [`FranchiseLeaders`](#franchiseleaders) | `/franchiseleaders` | `team_id` | FranchiseLeaders |
| [`FranchisePlayers`](#franchiseplayers) | `/franchiseplayers` | `team_id` | FranchisePlayers |
| [`GameRotation`](#gamerotation) | `/gamerotation` | `game_id` | AwayTeam, HomeTeam |
| [`GLAlumBoxScoreSimilarityScore`](#glalumboxscoresimilarityscore) | `/glalumboxscoresimilarityscore` | `person2_id`, `person1_id` | GLeagueAlumBoxScoreSimilarityScores |
| [`HomePageLeaders`](#homepageleaders) | `/homepageleaders` |  | HomePageLeaders, LeagueAverage, LeagueMax |
| [`HomePageV2`](#homepagev2) | `/homepagev2` |  | HomePageStat1, HomePageStat2, HomePageStat3, HomePageStat4, HomePageStat5, HomePageStat6, HomePageStat7, HomePageStat8 |
| [`HustleStatsBoxScore`](#hustlestatsboxscore) | `/hustlestatsboxscore` | `game_id` | HustleStatsAvailable, PlayerStats, TeamStats |
| [`InfographicFanDuelPlayer`](#infographicfanduelplayer) | `/infographicfanduelplayer` | `game_id` | FanDuelPlayer |
| [`ISTStandings`](#iststandings) | `/iststandings` |  | Standings |
| [`LeadersTiles`](#leaderstiles) | `/leaderstiles` |  | AllTimeSeasonHigh, LastSeasonHigh, LeadersTiles, LowSeasonHigh |
| [`LeagueDashLineups`](#leaguedashlineups) | `/leaguedashlineups` |  | Lineups |
| [`LeagueDashOppPtShot`](#leaguedashoppptshot) | `/leaguedashoppptshot` |  | LeagueDashPTShots |
| [`LeagueDashPlayerBioStats`](#leaguedashplayerbiostats) | `/leaguedashplayerbiostats` |  | LeagueDashPlayerBioStats |
| [`LeagueDashPlayerClutch`](#leaguedashplayerclutch) | `/leaguedashplayerclutch` |  | LeagueDashPlayerClutch |
| [`LeagueDashPlayerPtShot`](#leaguedashplayerptshot) | `/leaguedashplayerptshot` |  | LeagueDashPTShots |
| [`LeagueDashPlayerShotLocations`](#leaguedashplayershotlocations) | `/leaguedashplayershotlocations` |  | ShotLocations |
| [`LeagueDashPlayerStats`](#leaguedashplayerstats) | `/leaguedashplayerstats` |  | LeagueDashPlayerStats |
| [`LeagueDashPtDefend`](#leaguedashptdefend) | `/leaguedashptdefend` |  | LeagueDashPTDefend |
| [`LeagueDashPtStats`](#leaguedashptstats) | `/leaguedashptstats` |  | LeagueDashPtStats |
| [`LeagueDashPtTeamDefend`](#leaguedashptteamdefend) | `/leaguedashptteamdefend` |  | LeagueDashPtTeamDefend |
| [`LeagueDashTeamClutch`](#leaguedashteamclutch) | `/leaguedashteamclutch` |  | LeagueDashTeamClutch |
| [`LeagueDashTeamPtShot`](#leaguedashteamptshot) | `/leaguedashteamptshot` |  | LeagueDashPTShots |
| [`LeagueDashTeamShotLocations`](#leaguedashteamshotlocations) | `/leaguedashteamshotlocations` |  | ShotLocations |
| [`LeagueDashTeamStats`](#leaguedashteamstats) | `/leaguedashteamstats` |  | LeagueDashTeamStats |
| [`LeagueGameFinder`](#leaguegamefinder) | `/leaguegamefinder` |  | LeagueGameFinderResults |
| [`LeagueGameLog`](#leaguegamelog) | `/leaguegamelog` |  | LeagueGameLog |
| [`LeagueHustleStatsPlayer`](#leaguehustlestatsplayer) | `/leaguehustlestatsplayer` |  | HustleStatsPlayer |
| [`LeagueHustleStatsTeam`](#leaguehustlestatsteam) | `/leaguehustlestatsteam` |  | HustleStatsTeam |
| [`LeagueLeaders`](#leagueleaders) | `/leagueleaders` |  | LeagueLeaders |
| [`LeagueLineupViz`](#leaguelineupviz) | `/leaguelineupviz` | `minutes_min` | LeagueLineupViz |
| [`LeaguePlayerOnDetails`](#leagueplayerondetails) | `/leagueplayerondetails` | `team_id` | PlayersOnCourtLeaguePlayerDetails |
| [`LeagueSeasonMatchups`](#leagueseasonmatchups) | `/leagueseasonmatchups` |  | SeasonMatchups |
| [`LeagueStandings`](#leaguestandings) | `/leaguestandings` |  | Standings |
| [`LeagueStandingsV3`](#leaguestandingsv3) | `/leaguestandingsv3` |  | Standings |
| [`MatchupsRollup`](#matchupsrollup) | `/matchupsrollup` |  | MatchupsRollup |
| [`PlayByPlay`](#playbyplay) | `/playbyplay` | `game_id` | AvailableVideo, PlayByPlay |
| [`PlayByPlayV2`](#playbyplayv2) | `/playbyplayv2` | `game_id` | AvailableVideo, PlayByPlay |
| [`PlayByPlayV3`](#playbyplayv3) | `/playbyplayv3` | `game_id` | AvailableVideo, PlayByPlay |
| [`PlayerAwards`](#playerawards) | `/playerawards` | `player_id` | PlayerAwards |
| [`PlayerCareerByCollege`](#playercareerbycollege) | `/playercareerbycollege` | `college` | PlayerCareerByCollege |
| [`PlayerCareerByCollegeRollup`](#playercareerbycollegerollup) | `/playercareerbycollegerollup` |  | East, Midwest, South, West |
| [`PlayerCareerStats`](#playercareerstats) | `/playercareerstats` | `player_id` | CareerTotalsAllStarSeason, CareerTotalsCollegeSeason, CareerTotalsPostSeason, CareerTotalsRegularSeason, SeasonRankingsPostSeason, SeasonRankingsRegularSeason, SeasonTotalsAllStarSeason, SeasonTotalsCollegeSeason, SeasonTotalsPostSeason, SeasonTotalsRegularSeason |
| [`PlayerCompare`](#playercompare) | `/playercompare` | `vs_player_id_list`, `player_id_list` | Individual, OverallCompare |
| [`PlayerDashboardByClutch`](#playerdashboardbyclutch) | `/playerdashboardbyclutch` | `player_id` | Last10Sec3Point2PlayerDashboard, Last10Sec3PointPlayerDashboard, Last1Min5PointPlayerDashboard, Last1MinPlusMinus5PointPlayerDashboard, Last30Sec3Point2PlayerDashboard, Last30Sec3PointPlayerDashboard, Last3Min5PointPlayerDashboard, Last3MinPlusMinus5PointPlayerDashboard, Last5Min5PointPlayerDashboard, Last5MinPlusMinus5PointPlayerDashboard, OverallPlayerDashboard |
| [`PlayerDashboardByGameSplits`](#playerdashboardbygamesplits) | `/playerdashboardbygamesplits` | `player_id` | ByActualMarginPlayerDashboard, ByHalfPlayerDashboard, ByPeriodPlayerDashboard, ByScoreMarginPlayerDashboard, OverallPlayerDashboard |
| [`PlayerDashboardByGeneralSplits`](#playerdashboardbygeneralsplits) | `/playerdashboardbygeneralsplits` | `player_id` | DaysRestPlayerDashboard, LocationPlayerDashboard, MonthPlayerDashboard, OverallPlayerDashboard, PrePostAllStarPlayerDashboard, StartingPosition, WinsLossesPlayerDashboard |
| [`PlayerDashboardByLastNGames`](#playerdashboardbylastngames) | `/playerdashboardbylastngames` | `player_id` | GameNumberPlayerDashboard, Last10PlayerDashboard, Last15PlayerDashboard, Last20PlayerDashboard, Last5PlayerDashboard, OverallPlayerDashboard |
| [`PlayerDashboardByShootingSplits`](#playerdashboardbyshootingsplits) | `/playerdashboardbyshootingsplits` | `player_id` | AssistedBy, AssitedShotPlayerDashboard, OverallPlayerDashboard, Shot5FTPlayerDashboard, Shot8FTPlayerDashboard, ShotAreaPlayerDashboard, ShotTypePlayerDashboard, ShotTypeSummaryPlayerDashboard |
| [`PlayerDashboardByTeamPerformance`](#playerdashboardbyteamperformance) | `/playerdashboardbyteamperformance` | `player_id` | OverallPlayerDashboard, PointsScoredPlayerDashboard, PontsAgainstPlayerDashboard, ScoreDifferentialPlayerDashboard |
| [`PlayerDashboardByYearOverYear`](#playerdashboardbyyearoveryear) | `/playerdashboardbyyearoveryear` | `player_id` | ByYearPlayerDashboard, OverallPlayerDashboard |
| [`PlayerDashPtPass`](#playerdashptpass) | `/playerdashptpass` | `team_id`, `player_id` | PassesMade, PassesReceived |
| [`PlayerDashPtReb`](#playerdashptreb) | `/playerdashptreb` | `team_id`, `player_id` | NumContestedRebounding, OverallRebounding, RebDistanceRebounding, ShotDistanceRebounding, ShotTypeRebounding |
| [`PlayerDashPtShotDefend`](#playerdashptshotdefend) | `/playerdashptshotdefend` | `team_id`, `player_id` | DefendingShots |
| [`PlayerDashPtShots`](#playerdashptshots) | `/playerdashptshots` | `team_id`, `player_id` | ClosestDefender10ftPlusShooting, ClosestDefenderShooting, DribbleShooting, GeneralShooting, Overall, ShotClockShooting, TouchTimeShooting |
| [`PlayerEstimatedMetrics`](#playerestimatedmetrics) | `/playerestimatedmetrics` |  | PlayerEstimatedMetrics |
| [`PlayerFantasyProfileBarGraph`](#playerfantasyprofilebargraph) | `/playerfantasyprofilebargraph` | `player_id` | LastFiveGamesAvg, SeasonAvg |
| [`PlayerGameLog`](#playergamelog) | `/playergamelog` | `player_id` | PlayerGameLog |
| [`PlayerGameLogs`](#playergamelogs) | `/playergamelogs` |  | PlayerGameLogs |
| [`PlayerGameStreakFinder`](#playergamestreakfinder) | `/playergamestreakfinder` |  | PlayerGameStreakFinderResults |
| [`PlayerIndex`](#playerindex) | `/playerindex` |  | PlayerIndex |
| [`PlayerNextNGames`](#playernextngames) | `/playernextngames` | `player_id` | NextNGames |
| [`PlayerProfileV2`](#playerprofilev2) | `/playerprofilev2` | `player_id` | CareerHighs, CareerTotalsAllStarSeason, CareerTotalsCollegeSeason, CareerTotalsPostSeason, CareerTotalsPreseason, CareerTotalsRegularSeason, NextGame, SeasonHighs, SeasonRankingsPostSeason, SeasonRankingsRegularSeason, SeasonTotalsAllStarSeason, SeasonTotalsCollegeSeason, SeasonTotalsPostSeason, SeasonTotalsPreseason, SeasonTotalsRegularSeason |
| [`PlayerVsPlayer`](#playervsplayer) | `/playervsplayer` | `vs_player_id`, `player_id` | OnOffCourt, Overall, PlayerInfo, ShotAreaOffCourt, ShotAreaOnCourt, ShotAreaOverall, ShotDistanceOffCourt, ShotDistanceOnCourt, ShotDistanceOverall, VsPlayerInfo |
| [`PlayoffPicture`](#playoffpicture) | `/playoffpicture` |  | EastConfPlayoffPicture, EastConfRemainingGames, EastConfStandings, WestConfPlayoffPicture, WestConfRemainingGames, WestConfStandings |
| [`ScheduleLeagueV2`](#scheduleleaguev2) | `/scheduleleaguev2` |  | SeasonGames, SeasonWeeks |
| [`ScheduleLeagueV2Int`](#scheduleleaguev2int) | `/scheduleleaguev2int` |  | SeasonGames, SeasonWeeks, BroadcasterList |
| [`ScoreboardV2`](#scoreboardv2) | `/scoreboardv2` |  | Available, EastConfStandingsByDay, GameHeader, LastMeeting, LineScore, SeriesStandings, TeamLeaders, TicketLinks, WestConfStandingsByDay, WinProbability |
| [`ScoreboardV3`](#scoreboardv3) | `/scoreboardv3` | `game_date` | ScoreboardInfo, GameHeader, LineScore, GameLeaders, TeamLeaders, Broadcasters |
| [`ShotChartDetail`](#shotchartdetail) | `/shotchartdetail` | `team_id`, `player_id` | LeagueAverages, Shot_Chart_Detail |
| [`ShotChartLeagueWide`](#shotchartleaguewide) | `/shotchartleaguewide` |  | League_Wide |
| [`ShotChartLineupDetail`](#shotchartlineupdetail) | `/shotchartlineupdetail` |  | ShotChartLineupDetail, ShotChartLineupLeagueAverage |
| [`SynergyPlayTypes`](#synergyplaytypes) | `/synergyplaytypes` |  | SynergyPlayType |
| [`TeamAndPlayersVsPlayers`](#teamandplayersvsplayers) | `/teamandplayersvsplayers` | `vs_team_id`, `vs_player_id5`, `vs_player_id4`, `vs_player_id3`, `vs_player_id2`, `vs_player_id1`, `team_id`, `player_id5`, `player_id4`, `player_id3`, `player_id2`, `player_id1` | PlayersVsPlayers, TeamPlayersVsPlayersOff, TeamPlayersVsPlayersOn, TeamVsPlayers, TeamVsPlayersOff |
| [`TeamDashboardByGeneralSplits`](#teamdashboardbygeneralsplits) | `/teamdashboardbygeneralsplits` | `team_id` | DaysRestTeamDashboard, LocationTeamDashboard, MonthTeamDashboard, OverallTeamDashboard, PrePostAllStarTeamDashboard, WinsLossesTeamDashboard |
| [`TeamDashboardByShootingSplits`](#teamdashboardbyshootingsplits) | `/teamdashboardbyshootingsplits` | `team_id` | AssistedBy, AssitedShotTeamDashboard, OverallTeamDashboard, Shot5FTTeamDashboard, Shot8FTTeamDashboard, ShotAreaTeamDashboard, ShotTypeTeamDashboard |
| [`TeamDashLineups`](#teamdashlineups) | `/teamdashlineups` | `team_id` | Lineups, Overall |
| [`TeamDashPtPass`](#teamdashptpass) | `/teamdashptpass` | `team_id` | PassesMade, PassesReceived |
| [`TeamDashPtReb`](#teamdashptreb) | `/teamdashptreb` | `team_id` | NumContestedRebounding, OverallRebounding, RebDistanceRebounding, ShotDistanceRebounding, ShotTypeRebounding |
| [`TeamDashPtShots`](#teamdashptshots) | `/teamdashptshots` | `team_id` | ClosestDefender10ftPlusShooting, ClosestDefenderShooting, DribbleShooting, GeneralShooting, ShotClockShooting, TouchTimeShooting |
| [`TeamDetails`](#teamdetails) | `/teamdetails` | `team_id` | TeamAwardsChampionships, TeamAwardsConf, TeamAwardsDiv, TeamBackground, TeamHistory, TeamHof, TeamRetired, TeamSocialSites |
| [`TeamEstimatedMetrics`](#teamestimatedmetrics) | `/teamestimatedmetrics` |  | TeamEstimatedMetrics |
| [`TeamGameLog`](#teamgamelog) | `/teamgamelog` | `team_id` | TeamGameLog |
| [`TeamGameLogs`](#teamgamelogs) | `/teamgamelogs` |  | TeamGameLogs |
| [`TeamGameStreakFinder`](#teamgamestreakfinder) | `/teamgamestreakfinder` |  | TeamGameStreakFinderParametersResults |
| [`TeamHistoricalLeaders`](#teamhistoricalleaders) | `/teamhistoricalleaders` | `team_id` | CareerLeadersByTeam |
| [`TeamInfoCommon`](#teaminfocommon) | `/teaminfocommon` | `team_id` | AvailableSeasons, TeamInfoCommon, TeamSeasonRanks |
| [`TeamPlayerDashboard`](#teamplayerdashboard) | `/teamplayerdashboard` | `team_id` | PlayersSeasonTotals, TeamOverall |
| [`TeamPlayerOnOffDetails`](#teamplayeronoffdetails) | `/teamplayeronoffdetails` | `team_id` | OverallTeamPlayerOnOffDetails, PlayersOffCourtTeamPlayerOnOffDetails, PlayersOnCourtTeamPlayerOnOffDetails |
| [`TeamPlayerOnOffSummary`](#teamplayeronoffsummary) | `/teamplayeronoffsummary` | `team_id` | OverallTeamPlayerOnOffSummary, PlayersOffCourtTeamPlayerOnOffSummary, PlayersOnCourtTeamPlayerOnOffSummary |
| [`TeamVsPlayer`](#teamvsplayer) | `/teamvsplayer` | `vs_player_id`, `team_id` | OnOffCourt, Overall, ShotAreaOffCourt, ShotAreaOnCourt, ShotAreaOverall, ShotDistanceOffCourt, ShotDistanceOnCourt, ShotDistanceOverall, vsPlayerOverall |
| [`TeamYearByYearStats`](#teamyearbyyearstats) | `/teamyearbyyearstats` | `team_id` | TeamStats |
| [`VideoDetails`](#videodetails) | `/videodetails` | `team_id`, `player_id` |  |
| [`VideoDetailsAsset`](#videodetailsasset) | `/videodetailsasset` | `team_id`, `player_id` |  |
| [`VideoEvents`](#videoevents) | `/videoevents` | `game_id` |  |
| [`VideoEventsAsset`](#videoeventsasset) | `/videoeventsasset` | `game_id` |  |
| [`VideoStatus`](#videostatus) | `/videostatus` |  | VideoStatus |
| [`WinProbabilityPBP`](#winprobabilitypbp) | `/winprobabilitypbp` | `game_id` | GameInfo, WinProbPBP |

### Live endpoints

| Python class | HTTP path | Required args |
|---|---|---|
| [`BoxScore`](#boxscore) | `/boxscore/boxscore_{game_id}.json` | `game_id` |
| [`Odds`](#odds) | `/odds/odds_todaysGames.json` |  |
| [`PlayByPlay`](#playbyplay) | `/playbyplay/playbyplay_{game_id}.json` | `game_id` |
| [`ScoreBoard`](#scoreboard) | `/scoreboard/todaysScoreboard_00.json` |  |

## Endpoint details

### AllTimeLeadersGrids

- HTTP: `GET https://stats.nba.com/stats/alltimeleadersgrids`
- Repo docs: `docs/nba_api/stats/endpoints/alltimeleadersgrids.md`
- Example output: `docs/nba_api/stats/endpoints_output/alltimeleadersgrids_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import AllTimeLeadersGrids
  endpoint = AllTimeLeadersGrids()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `LeagueID` | `league_id` | no |
  | `PerMode` | `per_mode_simple` | no |
  | `SeasonType` | `season_type` | no |
  | `TopX` | `topx` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `ASTLeaders` (4): `PLAYER_ID`, `PLAYER_NAME`, `AST`, `AST_RANK`
  - `BLKLeaders` (4): `PLAYER_ID`, `PLAYER_NAME`, `BLK`, `BLK_RANK`
  - `DREBLeaders` (4): `PLAYER_ID`, `PLAYER_NAME`, `DREB`, `DREB_RANK`
  - `FG3ALeaders` (4): `PLAYER_ID`, `PLAYER_NAME`, `FG3A`, `FG3A_RANK`
  - `FG3MLeaders` (4): `PLAYER_ID`, `PLAYER_NAME`, `FG3M`, `FG3M_RANK`
  - `FG3_PCTLeaders` (4): `PLAYER_ID`, `PLAYER_NAME`, `FG3_PCT`, `FG3_PCT_RANK`
  - `FGALeaders` (4): `PLAYER_ID`, `PLAYER_NAME`, `FGA`, `FGA_RANK`
  - `FGMLeaders` (4): `PLAYER_ID`, `PLAYER_NAME`, `FGM`, `FGM_RANK`
  - `FG_PCTLeaders` (4): `PLAYER_ID`, `PLAYER_NAME`, `FG_PCT`, `FG_PCT_RANK`
  - `FTALeaders` (4): `PLAYER_ID`, `PLAYER_NAME`, `FTA`, `FTA_RANK`
  - `FTMLeaders` (4): `PLAYER_ID`, `PLAYER_NAME`, `FTM`, `FTM_RANK`
  - `FT_PCTLeaders` (4): `PLAYER_ID`, `PLAYER_NAME`, `FT_PCT`, `FT_PCT_RANK`
  - `GPLeaders` (4): `PLAYER_ID`, `PLAYER_NAME`, `GP`, `GP_RANK`
  - `OREBLeaders` (4): `PLAYER_ID`, `PLAYER_NAME`, `OREB`, `OREB_RANK`
  - `PFLeaders` (4): `PLAYER_ID`, `PLAYER_NAME`, `PF`, `PF_RANK`
  - `PTSLeaders` (4): `PLAYER_ID`, `PLAYER_NAME`, `PTS`, `PTS_RANK`
  - `REBLeaders` (4): `PLAYER_ID`, `PLAYER_NAME`, `REB`, `REB_RANK`
  - `STLLeaders` (4): `PLAYER_ID`, `PLAYER_NAME`, `STL`, `STL_RANK`
  - `TOVLeaders` (4): `PLAYER_ID`, `PLAYER_NAME`, `TOV`, `TOV_RANK`

  </details>

### AssistLeaders

- HTTP: `GET https://stats.nba.com/stats/assistleaders`
- Repo docs: `docs/nba_api/stats/endpoints/assistleaders.md`
- Example output: `docs/nba_api/stats/endpoints_output/assistleaders_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import AssistLeaders
  endpoint = AssistLeaders()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `LeagueID` | `league_id` | no |
  | `PerMode` | `per_mode_simple` | no |
  | `PlayerOrTeam` | `player_or_team` | no |
  | `Season` | `season` | no |
  | `SeasonType` | `season_type_playoffs` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `AssistLeaders` (5): `RANK`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_NAME`, `AST`

  </details>

### AssistTracker

- HTTP: `GET https://stats.nba.com/stats/assisttracker`
- Repo docs: `docs/nba_api/stats/endpoints/assisttracker.md`
- Example output: `docs/nba_api/stats/endpoints_output/assisttracker_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import AssistTracker
  endpoint = AssistTracker()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `College` | `college_nullable` | no |
  | `Conference` | `conference_nullable` | no |
  | `Country` | `country_nullable` | no |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `Division` | `division_simple_nullable` | no |
  | `DraftPick` | `draft_pick_nullable` | no |
  | `DraftYear` | `draft_year_nullable` | no |
  | `GameScope` | `game_scope_simple_nullable` | no |
  | `Height` | `height_nullable` | no |
  | `LastNGames` | `last_n_games_nullable` | no |
  | `LeagueID` | `league_id_nullable` | no |
  | `Location` | `location_nullable` | no |
  | `Month` | `month_nullable` | no |
  | `OpponentTeamID` | `opponent_team_id_nullable` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `PORound` | `po_round_nullable` | no |
  | `PerMode` | `per_mode_simple_nullable` | no |
  | `PlayerExperience` | `player_experience_nullable` | no |
  | `PlayerPosition` | `player_position_abbreviation_nullable` | no |
  | `Season` | `season_nullable` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_all_star_nullable` | no |
  | `StarterBench` | `starter_bench_nullable` | no |
  | `TeamID` | `team_id_nullable` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |
  | `Weight` | `weight_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `AssistTracker` (1): `ASSISTS`

  </details>

### BoxScoreAdvancedV2

- HTTP: `GET https://stats.nba.com/stats/boxscoreadvancedv2`
- Repo docs: `docs/nba_api/stats/endpoints/boxscoreadvancedv2.md`
- Example output: `docs/nba_api/stats/endpoints_output/boxscoreadvancedv2_output.md`
- Required python args: `game_id`
- Python:
  ```python
  from nba_api.stats.endpoints import BoxScoreAdvancedV2
  endpoint = BoxScoreAdvancedV2(game_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `GameID` | `game_id` | yes |
  | `EndPeriod` | `end_period` | no |
  | `EndRange` | `end_range` | no |
  | `RangeType` | `range_type` | no |
  | `StartPeriod` | `start_period` | no |
  | `StartRange` | `start_range` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `PlayerStats` (31): `GAME_ID`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_CITY`, `PLAYER_ID`, `PLAYER_NAME`, `START_POSITION`, `COMMENT`, `MIN`, `E_OFF_RATING`, `OFF_RATING`, `E_DEF_RATING`, `DEF_RATING`, `E_NET_RATING`, `NET_RATING`, `AST_PCT`, `AST_TOV`, `AST_RATIO`, `OREB_PCT`, `DREB_PCT`, `REB_PCT`, `TM_TOV_PCT`, `EFG_PCT`, `TS_PCT`, `USG_PCT`, `E_USG_PCT`, `E_PACE`, `PACE`, `PACE_PER40`, `POSS`, `PIE`
  - `TeamStats` (29): `GAME_ID`, `TEAM_ID`, `TEAM_NAME`, `TEAM_ABBREVIATION`, `TEAM_CITY`, `MIN`, `E_OFF_RATING`, `OFF_RATING`, `E_DEF_RATING`, `DEF_RATING`, `E_NET_RATING`, `NET_RATING`, `AST_PCT`, `AST_TOV`, `AST_RATIO`, `OREB_PCT`, `DREB_PCT`, `REB_PCT`, `E_TM_TOV_PCT`, `TM_TOV_PCT`, `EFG_PCT`, `TS_PCT`, `USG_PCT`, `E_USG_PCT`, `E_PACE`, `PACE`, `PACE_PER40`, `POSS`, `PIE`

  </details>

### BoxScoreAdvancedV3

- HTTP: `GET https://stats.nba.com/stats/boxscoreadvancedv3`
- Repo docs: `docs/nba_api/stats/endpoints/boxscoreadvancedv3.md`
- Example output: `docs/nba_api/stats/endpoints_output/boxscoreadvancedv3_output.md`
- Required python args: `game_id`
- Python:
  ```python
  from nba_api.stats.endpoints import BoxScoreAdvancedV3
  endpoint = BoxScoreAdvancedV3(game_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `GameID` | `game_id` | yes |
  | `EndPeriod` | `end_period` | no |
  | `EndRange` | `end_range` | no |
  | `RangeType` | `range_type` | no |
  | `StartPeriod` | `start_period` | no |
  | `StartRange` | `start_range` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `PlayerStats` (37): `gameId`, `teamId`, `teamCity`, `teamName`, `teamTricode`, `teamSlug`, `personId`, `firstName`, `familyName`, `nameI`, `playerSlug`, `position`, `comment`, `jerseyNum`, `minutes`, `estimatedOffensiveRating`, `offensiveRating`, `estimatedDefensiveRating`, `defensiveRating`, `estimatedNetRating`, `netRating`, `assistPercentage`, `assistToTurnover`, `assistRatio`, `offensiveReboundPercentage`, `defensiveReboundPercentage`, `reboundPercentage`, `turnoverRatio`, `effectiveFieldGoalPercentage`, `trueShootingPercentage`, `usagePercentage`, `estimatedUsagePercentage`, `estimatedPace`, `pace`, `pacePer40`, `possessions`, `PIE`
  - `TeamStats` (30): `gameId`, `teamId`, `teamCity`, `teamName`, `teamTricode`, `teamSlug`, `minutes`, `estimatedOffensiveRating`, `offensiveRating`, `estimatedDefensiveRating`, `defensiveRating`, `estimatedNetRating`, `netRating`, `assistPercentage`, `assistToTurnover`, `assistRatio`, `offensiveReboundPercentage`, `defensiveReboundPercentage`, `reboundPercentage`, `estimatedTeamTurnoverPercentage`, `turnoverRatio`, `effectiveFieldGoalPercentage`, `trueShootingPercentage`, `usagePercentage`, `estimatedUsagePercentage`, `estimatedPace`, `pace`, `pacePer40`, `possessions`, `PIE`

  </details>

### BoxScoreDefensiveV2

- HTTP: `GET https://stats.nba.com/stats/boxscoredefensivev2`
- Repo docs: `docs/nba_api/stats/endpoints/boxscoredefensivev2.md`
- Example output: `docs/nba_api/stats/endpoints_output/boxscoredefensivev2_output.md`
- Required python args: `game_id`
- Python:
  ```python
  from nba_api.stats.endpoints import BoxScoreDefensiveV2
  endpoint = BoxScoreDefensiveV2(game_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `GameID` | `game_id` | yes |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `PlayerStats` (29): `gameId`, `teamId`, `teamCity`, `teamName`, `teamTricode`, `teamSlug`, `personId`, `firstName`, `familyName`, `nameI`, `playerSlug`, `position`, `comment`, `jerseyNum`, `matchupMinutes`, `partialPossessions`, `switchesOn`, `playerPoints`, `defensiveRebounds`, `matchupAssists`, `matchupTurnovers`, `steals`, `blocks`, `matchupFieldGoalsMade`, `matchupFieldGoalsAttempted`, `matchupFieldGoalPercentage`, `matchupThreePointersMade`, `matchupThreePointersAttempted`, `matchupThreePointerPercentage`
  - `TeamStats` (7): `gameId`, `teamId`, `teamCity`, `teamName`, `teamTricode`, `teamSlug`, `minutes`

  </details>

### BoxScoreFourFactorsV2

- HTTP: `GET https://stats.nba.com/stats/boxscorefourfactorsv2`
- Repo docs: `docs/nba_api/stats/endpoints/boxscorefourfactorsv2.md`
- Example output: `docs/nba_api/stats/endpoints_output/boxscorefourfactorsv2_output.md`
- Required python args: `game_id`
- Python:
  ```python
  from nba_api.stats.endpoints import BoxScoreFourFactorsV2
  endpoint = BoxScoreFourFactorsV2(game_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `GameID` | `game_id` | yes |
  | `EndPeriod` | `end_period` | no |
  | `EndRange` | `end_range` | no |
  | `RangeType` | `range_type` | no |
  | `StartPeriod` | `start_period` | no |
  | `StartRange` | `start_range` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `sqlPlayersFourFactors` (17): `GAME_ID`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_CITY`, `PLAYER_ID`, `PLAYER_NAME`, `START_POSITION`, `COMMENT`, `MIN`, `EFG_PCT`, `FTA_RATE`, `TM_TOV_PCT`, `OREB_PCT`, `OPP_EFG_PCT`, `OPP_FTA_RATE`, `OPP_TOV_PCT`, `OPP_OREB_PCT`
  - `sqlTeamsFourFactors` (14): `GAME_ID`, `TEAM_ID`, `TEAM_NAME`, `TEAM_ABBREVIATION`, `TEAM_CITY`, `MIN`, `EFG_PCT`, `FTA_RATE`, `TM_TOV_PCT`, `OREB_PCT`, `OPP_EFG_PCT`, `OPP_FTA_RATE`, `OPP_TOV_PCT`, `OPP_OREB_PCT`

  </details>

### BoxScoreFourFactorsV3

- HTTP: `GET https://stats.nba.com/stats/boxscorefourfactorsv3`
- Repo docs: `docs/nba_api/stats/endpoints/boxscorefourfactorsv3.md`
- Example output: `docs/nba_api/stats/endpoints_output/boxscorefourfactorsv3_output.md`
- Required python args: `game_id`
- Python:
  ```python
  from nba_api.stats.endpoints import BoxScoreFourFactorsV3
  endpoint = BoxScoreFourFactorsV3(game_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `GameID` | `game_id` | yes |
  | `EndPeriod` | `end_period` | no |
  | `EndRange` | `end_range` | no |
  | `RangeType` | `range_type` | no |
  | `StartPeriod` | `start_period` | no |
  | `StartRange` | `start_range` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `PlayerStats` (23): `gameId`, `teamId`, `teamCity`, `teamName`, `teamTricode`, `teamSlug`, `personId`, `firstName`, `familyName`, `nameI`, `playerSlug`, `position`, `comment`, `jerseyNum`, `minutes`, `effectiveFieldGoalPercentage`, `freeThrowAttemptRate`, `teamTurnoverPercentage`, `offensiveReboundPercentage`, `oppEffectiveFieldGoalPercentage`, `oppFreeThrowAttemptRate`, `oppTeamTurnoverPercentage`, `oppOffensiveReboundPercentage`
  - `TeamStats` (15): `gameId`, `teamId`, `teamCity`, `teamName`, `teamTricode`, `teamSlug`, `minutes`, `effectiveFieldGoalPercentage`, `freeThrowAttemptRate`, `teamTurnoverPercentage`, `offensiveReboundPercentage`, `oppEffectiveFieldGoalPercentage`, `oppFreeThrowAttemptRate`, `oppTeamTurnoverPercentage`, `oppOffensiveReboundPercentage`

  </details>

### BoxScoreHustleV2

- HTTP: `GET https://stats.nba.com/stats/boxscorehustlev2`
- Repo docs: `docs/nba_api/stats/endpoints/boxscorehustlev2.md`
- Example output: `docs/nba_api/stats/endpoints_output/boxscorehustlev2_output.md`
- Required python args: `game_id`
- Python:
  ```python
  from nba_api.stats.endpoints import BoxScoreHustleV2
  endpoint = BoxScoreHustleV2(game_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `GameID` | `game_id` | yes |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `PlayerStats` (31): `gameId`, `teamId`, `teamCity`, `teamName`, `teamTricode`, `teamSlug`, `personId`, `firstName`, `familyName`, `nameI`, `playerSlug`, `position`, `comment`, `jerseyNum`, `minutes`, `points`, `contestedShots`, `contestedShots2pt`, `contestedShots3pt`, `deflections`, `chargesDrawn`, `screenAssists`, `screenAssistPoints`, `looseBallsRecoveredOffensive`, `looseBallsRecoveredDefensive`, `looseBallsRecoveredTotal`, `offensiveBoxOuts`, `defensiveBoxOuts`, `boxOutPlayerTeamRebounds`, `boxOutPlayerRebounds`, `boxOuts`
  - `TeamStats` (23): `gameId`, `teamId`, `teamCity`, `teamName`, `teamTricode`, `teamSlug`, `minutes`, `points`, `contestedShots`, `contestedShots2pt`, `contestedShots3pt`, `deflections`, `chargesDrawn`, `screenAssists`, `screenAssistPoints`, `looseBallsRecoveredOffensive`, `looseBallsRecoveredDefensive`, `looseBallsRecoveredTotal`, `offensiveBoxOuts`, `defensiveBoxOuts`, `boxOutPlayerTeamRebounds`, `boxOutPlayerRebounds`, `boxOuts`

  </details>

### BoxScoreMatchupsV3

- HTTP: `GET https://stats.nba.com/stats/boxscorematchupsv3`
- Repo docs: `docs/nba_api/stats/endpoints/boxscorematchupsv3.md`
- Example output: `docs/nba_api/stats/endpoints_output/boxscorematchupsv3_output.md`
- Required python args: `game_id`
- Python:
  ```python
  from nba_api.stats.endpoints import BoxScoreMatchupsV3
  endpoint = BoxScoreMatchupsV3(game_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `GameID` | `game_id` | yes |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `PlayerStats` (46): `gameId`, `teamId`, `teamCity`, `teamName`, `teamTricode`, `teamSlug`, `personIdOff`, `firstNameOff`, `familyNameOff`, `nameIOff`, `playerSlugOff`, `jerseyNumOff`, `personIdDef`, `firstNameDef`, `familyNameDef`, `nameIDef`, `playerSlugDef`, `positionDef`, `commentDef`, `jerseyNumDef`, `matchupMinutes`, `matchupMinutesSort`, `partialPossessions`, `percentageDefenderTotalTime`, `percentageOffensiveTotalTime`, `percentageTotalTimeBothOn`, `switchesOn`, `playerPoints`, `teamPoints`, `matchupAssists`, `matchupPotentialAssists`, `matchupTurnovers`, `matchupBlocks`, `matchupFieldGoalsMade`, `matchupFieldGoalsAttempted`, `matchupFieldGoalsPercentage`, `matchupThreePointersMade`, `matchupThreePointersAttempted`, `matchupThreePointersPercentage`, `helpBlocks`, `helpFieldGoalsMade`, `helpFieldGoalsAttempted`, `helpFieldGoalsPercentage`, `matchupFreeThrowsMade`, `matchupFreeThrowsAttempted`, `shootingFouls`

  </details>

### BoxScoreMiscV2

- HTTP: `GET https://stats.nba.com/stats/boxscoremiscv2`
- Repo docs: `docs/nba_api/stats/endpoints/boxscoremiscv2.md`
- Example output: `docs/nba_api/stats/endpoints_output/boxscoremiscv2_output.md`
- Required python args: `game_id`
- Python:
  ```python
  from nba_api.stats.endpoints import BoxScoreMiscV2
  endpoint = BoxScoreMiscV2(game_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `GameID` | `game_id` | yes |
  | `EndPeriod` | `end_period` | no |
  | `EndRange` | `end_range` | no |
  | `RangeType` | `range_type` | no |
  | `StartPeriod` | `start_period` | no |
  | `StartRange` | `start_range` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `sqlPlayersMisc` (21): `GAME_ID`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_CITY`, `PLAYER_ID`, `PLAYER_NAME`, `START_POSITION`, `COMMENT`, `MIN`, `PTS_OFF_TOV`, `PTS_2ND_CHANCE`, `PTS_FB`, `PTS_PAINT`, `OPP_PTS_OFF_TOV`, `OPP_PTS_2ND_CHANCE`, `OPP_PTS_FB`, `OPP_PTS_PAINT`, `BLK`, `BLKA`, `PF`, `PFD`
  - `sqlTeamsMisc` (18): `GAME_ID`, `TEAM_ID`, `TEAM_NAME`, `TEAM_ABBREVIATION`, `TEAM_CITY`, `MIN`, `PTS_OFF_TOV`, `PTS_2ND_CHANCE`, `PTS_FB`, `PTS_PAINT`, `OPP_PTS_OFF_TOV`, `OPP_PTS_2ND_CHANCE`, `OPP_PTS_FB`, `OPP_PTS_PAINT`, `BLK`, `BLKA`, `PF`, `PFD`

  </details>

### BoxScoreMiscV3

- HTTP: `GET https://stats.nba.com/stats/boxscoremiscv3`
- Repo docs: `docs/nba_api/stats/endpoints/boxscoremiscv3.md`
- Example output: `docs/nba_api/stats/endpoints_output/boxscoremiscv3_output.md`
- Required python args: `game_id`
- Python:
  ```python
  from nba_api.stats.endpoints import BoxScoreMiscV3
  endpoint = BoxScoreMiscV3(game_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `GameID` | `game_id` | yes |
  | `EndPeriod` | `end_period` | no |
  | `EndRange` | `end_range` | no |
  | `RangeType` | `range_type` | no |
  | `StartPeriod` | `start_period` | no |
  | `StartRange` | `start_range` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `PlayerStats` (27): `gameId`, `teamId`, `teamCity`, `teamName`, `teamTricode`, `teamSlug`, `personId`, `firstName`, `familyName`, `nameI`, `playerSlug`, `position`, `comment`, `jerseyNum`, `minutes`, `pointsOffTurnovers`, `pointsSecondChance`, `pointsFastBreak`, `pointsPaint`, `oppPointsOffTurnovers`, `oppPointsSecondChance`, `oppPointsFastBreak`, `oppPointsPaint`, `blocks`, `blocksAgainst`, `foulsPersonal`, `foulsDrawn`
  - `TeamStats` (19): `gameId`, `teamId`, `teamCity`, `teamName`, `teamTricode`, `teamSlug`, `minutes`, `pointsOffTurnovers`, `pointsSecondChance`, `pointsFastBreak`, `pointsPaint`, `oppPointsOffTurnovers`, `oppPointsSecondChance`, `oppPointsFastBreak`, `oppPointsPaint`, `blocks`, `blocksAgainst`, `foulsPersonal`, `foulsDrawn`

  </details>

### BoxScorePlayerTrackV3

- HTTP: `GET https://stats.nba.com/stats/boxscoreplayertrackv3`
- Repo docs: `docs/nba_api/stats/endpoints/boxscoreplayertrackv3.md`
- Example output: `docs/nba_api/stats/endpoints_output/boxscoreplayertrackv3_output.md`
- Required python args: `game_id`
- Python:
  ```python
  from nba_api.stats.endpoints import BoxScorePlayerTrackV3
  endpoint = BoxScorePlayerTrackV3(game_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `GameID` | `game_id` | yes |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `PlayerStats` (35): `gameId`, `teamId`, `teamCity`, `teamName`, `teamTricode`, `teamSlug`, `personId`, `firstName`, `familyName`, `nameI`, `playerSlug`, `position`, `comment`, `jerseyNum`, `minutes`, `speed`, `distance`, `reboundChancesOffensive`, `reboundChancesDefensive`, `reboundChancesTotal`, `touches`, `secondaryAssists`, `freeThrowAssists`, `passes`, `assists`, `contestedFieldGoalsMade`, `contestedFieldGoalsAttempted`, `contestedFieldGoalPercentage`, `uncontestedFieldGoalsMade`, `uncontestedFieldGoalsAttempted`, `uncontestedFieldGoalsPercentage`, `fieldGoalPercentage`, `defendedAtRimFieldGoalsMade`, `defendedAtRimFieldGoalsAttempted`, `defendedAtRimFieldGoalPercentage`
  - `TeamStats` (26): `gameId`, `teamId`, `teamCity`, `teamName`, `teamTricode`, `teamSlug`, `minutes`, `distance`, `reboundChancesOffensive`, `reboundChancesDefensive`, `reboundChancesTotal`, `touches`, `secondaryAssists`, `freeThrowAssists`, `passes`, `assists`, `contestedFieldGoalsMade`, `contestedFieldGoalsAttempted`, `contestedFieldGoalPercentage`, `uncontestedFieldGoalsMade`, `uncontestedFieldGoalsAttempted`, `uncontestedFieldGoalsPercentage`, `fieldGoalPercentage`, `defendedAtRimFieldGoalsMade`, `defendedAtRimFieldGoalsAttempted`, `defendedAtRimFieldGoalPercentage`

  </details>

### BoxScoreScoringV2

- HTTP: `GET https://stats.nba.com/stats/boxscorescoringv2`
- Repo docs: `docs/nba_api/stats/endpoints/boxscorescoringv2.md`
- Example output: `docs/nba_api/stats/endpoints_output/boxscorescoringv2_output.md`
- Required python args: `game_id`
- Python:
  ```python
  from nba_api.stats.endpoints import BoxScoreScoringV2
  endpoint = BoxScoreScoringV2(game_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `GameID` | `game_id` | yes |
  | `EndPeriod` | `end_period` | no |
  | `EndRange` | `end_range` | no |
  | `RangeType` | `range_type` | no |
  | `StartPeriod` | `start_period` | no |
  | `StartRange` | `start_range` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `sqlPlayersScoring` (24): `GAME_ID`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_CITY`, `PLAYER_ID`, `PLAYER_NAME`, `START_POSITION`, `COMMENT`, `MIN`, `PCT_FGA_2PT`, `PCT_FGA_3PT`, `PCT_PTS_2PT`, `PCT_PTS_2PT_MR`, `PCT_PTS_3PT`, `PCT_PTS_FB`, `PCT_PTS_FT`, `PCT_PTS_OFF_TOV`, `PCT_PTS_PAINT`, `PCT_AST_2PM`, `PCT_UAST_2PM`, `PCT_AST_3PM`, `PCT_UAST_3PM`, `PCT_AST_FGM`, `PCT_UAST_FGM`
  - `sqlTeamsScoring` (21): `GAME_ID`, `TEAM_ID`, `TEAM_NAME`, `TEAM_ABBREVIATION`, `TEAM_CITY`, `MIN`, `PCT_FGA_2PT`, `PCT_FGA_3PT`, `PCT_PTS_2PT`, `PCT_PTS_2PT_MR`, `PCT_PTS_3PT`, `PCT_PTS_FB`, `PCT_PTS_FT`, `PCT_PTS_OFF_TOV`, `PCT_PTS_PAINT`, `PCT_AST_2PM`, `PCT_UAST_2PM`, `PCT_AST_3PM`, `PCT_UAST_3PM`, `PCT_AST_FGM`, `PCT_UAST_FGM`

  </details>

### BoxScoreScoringV3

- HTTP: `GET https://stats.nba.com/stats/boxscorescoringv3`
- Repo docs: `docs/nba_api/stats/endpoints/boxscorescoringv3.md`
- Example output: `docs/nba_api/stats/endpoints_output/boxscorescoringv3_output.md`
- Required python args: `game_id`
- Python:
  ```python
  from nba_api.stats.endpoints import BoxScoreScoringV3
  endpoint = BoxScoreScoringV3(game_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `GameID` | `game_id` | yes |
  | `EndPeriod` | `end_period` | no |
  | `EndRange` | `end_range` | no |
  | `RangeType` | `range_type` | no |
  | `StartPeriod` | `start_period` | no |
  | `StartRange` | `start_range` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `PlayerStats` (30): `gameId`, `teamId`, `teamCity`, `teamName`, `teamTricode`, `teamSlug`, `personId`, `firstName`, `familyName`, `nameI`, `playerSlug`, `position`, `comment`, `jerseyNum`, `minutes`, `percentageFieldGoalsAttempted2pt`, `percentageFieldGoalsAttempted3pt`, `percentagePoints2pt`, `percentagePointsMidrange2pt`, `percentagePoints3pt`, `percentagePointsFastBreak`, `percentagePointsFreeThrow`, `percentagePointsOffTurnovers`, `percentagePointsPaint`, `percentageAssisted2pt`, `percentageUnassisted2pt`, `percentageAssisted3pt`, `percentageUnassisted3pt`, `percentageAssistedFGM`, `percentageUnassistedFGM`
  - `TeamStats` (22): `gameId`, `teamId`, `teamCity`, `teamName`, `teamTricode`, `teamSlug`, `minutes`, `percentageFieldGoalsAttempted2pt`, `percentageFieldGoalsAttempted3pt`, `percentagePoints2pt`, `percentagePointsMidrange2pt`, `percentagePoints3pt`, `percentagePointsFastBreak`, `percentagePointsFreeThrow`, `percentagePointsOffTurnovers`, `percentagePointsPaint`, `percentageAssisted2pt`, `percentageUnassisted2pt`, `percentageAssisted3pt`, `percentageUnassisted3pt`, `percentageAssistedFGM`, `percentageUnassistedFGM`

  </details>

### BoxScoreSummaryV2

- HTTP: `GET https://stats.nba.com/stats/boxscoresummaryv2`
- Repo docs: `docs/nba_api/stats/endpoints/boxscoresummaryv2.md`
- Example output: `docs/nba_api/stats/endpoints_output/boxscoresummaryv2_output.md`
- Required python args: `game_id`
- Python:
  ```python
  from nba_api.stats.endpoints import BoxScoreSummaryV2
  endpoint = BoxScoreSummaryV2(game_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `GameID` | `game_id` | yes |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `AvailableVideo` (7): `GAME_ID`, `VIDEO_AVAILABLE_FLAG`, `PT_AVAILABLE`, `PT_XYZ_AVAILABLE`, `WH_STATUS`, `HUSTLE_STATUS`, `HISTORICAL_STATUS`
  - `GameInfo` (3): `GAME_DATE`, `ATTENDANCE`, `GAME_TIME`
  - `GameSummary` (14): `GAME_DATE_EST`, `GAME_SEQUENCE`, `GAME_ID`, `GAME_STATUS_ID`, `GAME_STATUS_TEXT`, `GAMECODE`, `HOME_TEAM_ID`, `VISITOR_TEAM_ID`, `SEASON`, `LIVE_PERIOD`, `LIVE_PC_TIME`, `NATL_TV_BROADCASTER_ABBREVIATION`, `LIVE_PERIOD_TIME_BCAST`, `WH_STATUS`
  - `InactivePlayers` (8): `PLAYER_ID`, `FIRST_NAME`, `LAST_NAME`, `JERSEY_NUM`, `TEAM_ID`, `TEAM_CITY`, `TEAM_NAME`, `TEAM_ABBREVIATION`
  - `LastMeeting` (13): `GAME_ID`, `LAST_GAME_ID`, `LAST_GAME_DATE_EST`, `LAST_GAME_HOME_TEAM_ID`, `LAST_GAME_HOME_TEAM_CITY`, `LAST_GAME_HOME_TEAM_NAME`, `LAST_GAME_HOME_TEAM_ABBREVIATION`, `LAST_GAME_HOME_TEAM_POINTS`, `LAST_GAME_VISITOR_TEAM_ID`, `LAST_GAME_VISITOR_TEAM_CITY`, `LAST_GAME_VISITOR_TEAM_NAME`, `LAST_GAME_VISITOR_TEAM_CITY1`, `LAST_GAME_VISITOR_TEAM_POINTS`
  - `LineScore` (23): `GAME_DATE_EST`, `GAME_SEQUENCE`, `GAME_ID`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_CITY_NAME`, `TEAM_NICKNAME`, `TEAM_WINS_LOSSES`, `PTS_QTR1`, `PTS_QTR2`, `PTS_QTR3`, `PTS_QTR4`, `PTS_OT1`, `PTS_OT2`, `PTS_OT3`, `PTS_OT4`, `PTS_OT5`, `PTS_OT6`, `PTS_OT7`, `PTS_OT8`, `PTS_OT9`, `PTS_OT10`, `PTS`
  - `Officials` (4): `OFFICIAL_ID`, `FIRST_NAME`, `LAST_NAME`, `JERSEY_NUM`
  - `OtherStats` (14): `LEAGUE_ID`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_CITY`, `PTS_PAINT`, `PTS_2ND_CHANCE`, `PTS_FB`, `LARGEST_LEAD`, `LEAD_CHANGES`, `TIMES_TIED`, `TEAM_TURNOVERS`, `TOTAL_TURNOVERS`, `TEAM_REBOUNDS`, `PTS_OFF_TO`
  - `SeasonSeries` (7): `GAME_ID`, `HOME_TEAM_ID`, `VISITOR_TEAM_ID`, `GAME_DATE_EST`, `HOME_TEAM_WINS`, `HOME_TEAM_LOSSES`, `SERIES_LEADER`

  </details>

### BoxScoreSummaryV3

- HTTP: `GET https://stats.nba.com/stats/boxscoresummaryv3`
- Repo docs: `docs/nba_api/stats/endpoints/boxscoresummaryv3.md`
- Required python args: `game_id`
- Python:
  ```python
  from nba_api.stats.endpoints import BoxScoreSummaryV3
  endpoint = BoxScoreSummaryV3(game_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `GameID` | `game_id` | yes |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `GameSummary` (13): `gameId`, `gameCode`, `gameStatus`, `gameStatusText`, `period`, `gameClock`, `gameTimeUTC`, `gameEt`, `awayTeamId`, `homeTeamId`, `duration`, `attendance`, `sellout`
  - `GameInfo` (4): `gameId`, `gameDate`, `attendance`, `gameDuration`
  - `ArenaInfo` (7): `gameId`, `arenaId`, `arenaName`, `arenaCity`, `arenaState`, `arenaCountry`, `arenaTimezone`
  - `Officials` (7): `gameId`, `personId`, `name`, `nameI`, `firstName`, `familyName`, `jerseyNum`
  - `LineScore` (13): `gameId`, `teamId`, `teamCity`, `teamName`, `teamTricode`, `teamSlug`, `teamWins`, `teamLosses`, `period1Score`, `period2Score`, `period3Score`, `period4Score`, `score`
  - `InactivePlayers` (6): `gameId`, `teamId`, `personId`, `firstName`, `familyName`, `jerseyNum`
  - `LastFiveMeetings` (20): `recencyOrder`, `gameId`, `gameTimeUTC`, `gameEt`, `gameStatus`, `gameStatusText`, `awayTeamId`, `awayTeamCity`, `awayTeamName`, `awayTeamTricode`, `awayTeamScore`, `awayTeamWins`, `awayTeamLosses`, `homeTeamId`, `homeTeamCity`, `homeTeamName`, `homeTeamTricode`, `homeTeamScore`, `homeTeamWins`, `homeTeamLosses`
  - `OtherStats` (26): `gameId`, `teamId`, `teamCity`, `teamName`, `teamTricode`, `points`, `reboundsTotal`, `assists`, `steals`, `blocks`, `turnovers`, `fieldGoalsPercentage`, `threePointersPercentage`, `freeThrowsPercentage`, `pointsInThePaint`, `pointsSecondChance`, `pointsFastBreak`, `biggestLead`, `leadChanges`, `timesTied`, `biggestScoringRun`, `turnoversTeam`, `turnoversTotal`, `reboundsTeam`, `pointsFromTurnovers`, `benchPoints`
  - `AvailableVideo` (7): `gameId`, `videoAvailableFlag`, `ptAvailable`, `ptXYZAvailable`, `whStatus`, `hustleStatus`, `historicalStatus`

  </details>

### BoxScoreTraditionalV2

- HTTP: `GET https://stats.nba.com/stats/boxscoretraditionalv2`
- Repo docs: `docs/nba_api/stats/endpoints/boxscoretraditionalv2.md`
- Example output: `docs/nba_api/stats/endpoints_output/boxscoretraditionalv2_output.md`
- Required python args: `game_id`
- Python:
  ```python
  from nba_api.stats.endpoints import BoxScoreTraditionalV2
  endpoint = BoxScoreTraditionalV2(game_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `GameID` | `game_id` | yes |
  | `EndPeriod` | `end_period` | no |
  | `EndRange` | `end_range` | no |
  | `RangeType` | `range_type` | no |
  | `StartPeriod` | `start_period` | no |
  | `StartRange` | `start_range` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `PlayerStats` (28): `GAME_ID`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_CITY`, `PLAYER_ID`, `PLAYER_NAME`, `START_POSITION`, `COMMENT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `STL`, `BLK`, `TO`, `PF`, `PTS`, `PLUS_MINUS`
  - `TeamStarterBenchStats` (25): `GAME_ID`, `TEAM_ID`, `TEAM_NAME`, `TEAM_ABBREVIATION`, `TEAM_CITY`, `STARTERS_BENCH`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `STL`, `BLK`, `TO`, `PF`, `PTS`
  - `TeamStats` (25): `GAME_ID`, `TEAM_ID`, `TEAM_NAME`, `TEAM_ABBREVIATION`, `TEAM_CITY`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `STL`, `BLK`, `TO`, `PF`, `PTS`, `PLUS_MINUS`

  </details>

### BoxScoreTraditionalV3

- HTTP: `GET https://stats.nba.com/stats/boxscoretraditionalv3`
- Repo docs: `docs/nba_api/stats/endpoints/boxscoretraditionalv3.md`
- Example output: `docs/nba_api/stats/endpoints_output/boxscoretraditionalv3_output.md`
- Required python args: `game_id`
- Python:
  ```python
  from nba_api.stats.endpoints import BoxScoreTraditionalV3
  endpoint = BoxScoreTraditionalV3(game_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `GameID` | `game_id` | yes |
  | `EndPeriod` | `end_period` | no |
  | `EndRange` | `end_range` | no |
  | `RangeType` | `range_type` | no |
  | `StartPeriod` | `start_period` | no |
  | `StartRange` | `start_range` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `PlayerStats` (34): `gameId`, `teamId`, `teamCity`, `teamName`, `teamTricode`, `teamSlug`, `personId`, `firstName`, `familyName`, `nameI`, `playerSlug`, `position`, `comment`, `jerseyNum`, `minutes`, `fieldGoalsMade`, `fieldGoalsAttempted`, `fieldGoalsPercentage`, `threePointersMade`, `threePointersAttempted`, `threePointersPercentage`, `freeThrowsMade`, `freeThrowsAttempted`, `freeThrowsPercentage`, `reboundsOffensive`, `reboundsDefensive`, `reboundsTotal`, `assists`, `steals`, `blocks`, `turnovers`, `foulsPersonal`, `points`, `plusMinusPoints`
  - `TeamStarterBenchStats` (26): `gameId`, `teamId`, `teamCity`, `teamName`, `teamTricode`, `teamSlug`, `minutes`, `fieldGoalsMade`, `fieldGoalsAttempted`, `fieldGoalsPercentage`, `threePointersMade`, `threePointersAttempted`, `threePointersPercentage`, `freeThrowsMade`, `freeThrowsAttempted`, `freeThrowsPercentage`, `reboundsOffensive`, `reboundsDefensive`, `reboundsTotal`, `assists`, `steals`, `blocks`, `turnovers`, `foulsPersonal`, `points`, `startersBench`
  - `TeamStats` (26): `gameId`, `teamId`, `teamCity`, `teamName`, `teamTricode`, `teamSlug`, `minutes`, `fieldGoalsMade`, `fieldGoalsAttempted`, `fieldGoalsPercentage`, `threePointersMade`, `threePointersAttempted`, `threePointersPercentage`, `freeThrowsMade`, `freeThrowsAttempted`, `freeThrowsPercentage`, `reboundsOffensive`, `reboundsDefensive`, `reboundsTotal`, `assists`, `steals`, `blocks`, `turnovers`, `foulsPersonal`, `points`, `plusMinusPoints`

  </details>

### BoxScoreUsageV2

- HTTP: `GET https://stats.nba.com/stats/boxscoreusagev2`
- Repo docs: `docs/nba_api/stats/endpoints/boxscoreusagev2.md`
- Example output: `docs/nba_api/stats/endpoints_output/boxscoreusagev2_output.md`
- Required python args: `game_id`
- Python:
  ```python
  from nba_api.stats.endpoints import BoxScoreUsageV2
  endpoint = BoxScoreUsageV2(game_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `GameID` | `game_id` | yes |
  | `EndPeriod` | `end_period` | no |
  | `EndRange` | `end_range` | no |
  | `RangeType` | `range_type` | no |
  | `StartPeriod` | `start_period` | no |
  | `StartRange` | `start_range` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `sqlPlayersUsage` (27): `GAME_ID`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_CITY`, `PLAYER_ID`, `PLAYER_NAME`, `START_POSITION`, `COMMENT`, `MIN`, `USG_PCT`, `PCT_FGM`, `PCT_FGA`, `PCT_FG3M`, `PCT_FG3A`, `PCT_FTM`, `PCT_FTA`, `PCT_OREB`, `PCT_DREB`, `PCT_REB`, `PCT_AST`, `PCT_TOV`, `PCT_STL`, `PCT_BLK`, `PCT_BLKA`, `PCT_PF`, `PCT_PFD`, `PCT_PTS`
  - `sqlTeamsUsage` (24): `GAME_ID`, `TEAM_ID`, `TEAM_NAME`, `TEAM_ABBREVIATION`, `TEAM_CITY`, `MIN`, `USG_PCT`, `PCT_FGM`, `PCT_FGA`, `PCT_FG3M`, `PCT_FG3A`, `PCT_FTM`, `PCT_FTA`, `PCT_OREB`, `PCT_DREB`, `PCT_REB`, `PCT_AST`, `PCT_TOV`, `PCT_STL`, `PCT_BLK`, `PCT_BLKA`, `PCT_PF`, `PCT_PFD`, `PCT_PTS`

  </details>

### BoxScoreUsageV3

- HTTP: `GET https://stats.nba.com/stats/boxscoreusagev3`
- Repo docs: `docs/nba_api/stats/endpoints/boxscoreusagev3.md`
- Example output: `docs/nba_api/stats/endpoints_output/boxscoreusagev3_output.md`
- Required python args: `game_id`
- Python:
  ```python
  from nba_api.stats.endpoints import BoxScoreUsageV3
  endpoint = BoxScoreUsageV3(game_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `GameID` | `game_id` | yes |
  | `EndPeriod` | `end_period` | no |
  | `EndRange` | `end_range` | no |
  | `RangeType` | `range_type` | no |
  | `StartPeriod` | `start_period` | no |
  | `StartRange` | `start_range` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `PlayerStats` (33): `gameId`, `teamId`, `teamCity`, `teamName`, `teamTricode`, `teamSlug`, `personId`, `firstName`, `familyName`, `nameI`, `playerSlug`, `position`, `comment`, `jerseyNum`, `minutes`, `usagePercentage`, `percentageFieldGoalsMade`, `percentageFieldGoalsAttempted`, `percentageThreePointersMade`, `percentageThreePointersAttempted`, `percentageFreeThrowsMade`, `percentageFreeThrowsAttempted`, `percentageReboundsOffensive`, `percentageReboundsDefensive`, `percentageReboundsTotal`, `percentageAssists`, `percentageTurnovers`, `percentageSteals`, `percentageBlocks`, `percentageBlocksAllowed`, `percentagePersonalFouls`, `percentagePersonalFoulsDrawn`, `percentagePoints`
  - `TeamStats` (25): `gameId`, `teamId`, `teamCity`, `teamName`, `teamTricode`, `teamSlug`, `minutes`, `usagePercentage`, `percentageFieldGoalsMade`, `percentageFieldGoalsAttempted`, `percentageThreePointersMade`, `percentageThreePointersAttempted`, `percentageFreeThrowsMade`, `percentageFreeThrowsAttempted`, `percentageReboundsOffensive`, `percentageReboundsDefensive`, `percentageReboundsTotal`, `percentageAssists`, `percentageTurnovers`, `percentageSteals`, `percentageBlocks`, `percentageBlocksAllowed`, `percentagePersonalFouls`, `percentagePersonalFoulsDrawn`, `percentagePoints`

  </details>

### CommonAllPlayers

- HTTP: `GET https://stats.nba.com/stats/commonallplayers`
- Repo docs: `docs/nba_api/stats/endpoints/commonallplayers.md`
- Example output: `docs/nba_api/stats/endpoints_output/commonallplayers_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import CommonAllPlayers
  endpoint = CommonAllPlayers()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `IsOnlyCurrentSeason` | `is_only_current_season` | no |
  | `LeagueID` | `league_id` | no |
  | `Season` | `season` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `CommonAllPlayers` (16): `PERSON_ID`, `DISPLAY_LAST_COMMA_FIRST`, `DISPLAY_FIRST_LAST`, `ROSTERSTATUS`, `FROM_YEAR`, `TO_YEAR`, `PLAYERCODE`, `PLAYER_SLUG`, `TEAM_ID`, `TEAM_CITY`, `TEAM_NAME`, `TEAM_ABBREVIATION`, `TEAM_CODE`, `TEAM_SLUG`, `GAMES_PLAYED_FLAG`, `OTHERLEAGUE_EXPERIENCE_CH`

  </details>

### CommonPlayerInfo

- HTTP: `GET https://stats.nba.com/stats/commonplayerinfo`
- Repo docs: `docs/nba_api/stats/endpoints/commonplayerinfo.md`
- Example output: `docs/nba_api/stats/endpoints_output/commonplayerinfo_output.md`
- Required python args: `player_id`
- Python:
  ```python
  from nba_api.stats.endpoints import CommonPlayerInfo
  endpoint = CommonPlayerInfo(player_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `PlayerID` | `player_id` | yes |
  | `LeagueID` | `league_id_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `AvailableSeasons` (1): `SEASON_ID`
  - `CommonPlayerInfo` (31): `PERSON_ID`, `FIRST_NAME`, `LAST_NAME`, `DISPLAY_FIRST_LAST`, `DISPLAY_LAST_COMMA_FIRST`, `DISPLAY_FI_LAST`, `PLAYER_SLUG`, `BIRTHDATE`, `SCHOOL`, `COUNTRY`, `LAST_AFFILIATION`, `HEIGHT`, `WEIGHT`, `SEASON_EXP`, `JERSEY`, `POSITION`, `ROSTERSTATUS`, `TEAM_ID`, `TEAM_NAME`, `TEAM_ABBREVIATION`, `TEAM_CODE`, `TEAM_CITY`, `PLAYERCODE`, `FROM_YEAR`, `TO_YEAR`, `DLEAGUE_FLAG`, `NBA_FLAG`, `GAMES_PLAYED_FLAG`, `DRAFT_YEAR`, `DRAFT_ROUND`, `DRAFT_NUMBER`
  - `PlayerHeadlineStats` (7): `PLAYER_ID`, `PLAYER_NAME`, `TimeFrame`, `PTS`, `AST`, `REB`, `PIE`

  </details>

### CommonPlayoffSeries

- HTTP: `GET https://stats.nba.com/stats/commonplayoffseries`
- Repo docs: `docs/nba_api/stats/endpoints/commonplayoffseries.md`
- Example output: `docs/nba_api/stats/endpoints_output/commonplayoffseries_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import CommonPlayoffSeries
  endpoint = CommonPlayoffSeries()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `LeagueID` | `league_id` | no |
  | `Season` | `season` | no |
  | `SeriesID` | `series_id_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `PlayoffSeries` (5): `GAME_ID`, `HOME_TEAM_ID`, `VISITOR_TEAM_ID`, `SERIES_ID`, `GAME_NUM`

  </details>

### CommonTeamRoster

- HTTP: `GET https://stats.nba.com/stats/commonteamroster`
- Repo docs: `docs/nba_api/stats/endpoints/commonteamroster.md`
- Example output: `docs/nba_api/stats/endpoints_output/commonteamroster_output.md`
- Required python args: `team_id`
- Python:
  ```python
  from nba_api.stats.endpoints import CommonTeamRoster
  endpoint = CommonTeamRoster(team_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `TeamID` | `team_id` | yes |
  | `LeagueID` | `league_id_nullable` | no |
  | `Season` | `season` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `Coaches` (9): `TEAM_ID`, `SEASON`, `COACH_ID`, `FIRST_NAME`, `LAST_NAME`, `COACH_NAME`, `IS_ASSISTANT`, `COACH_TYPE`, `SORT_SEQUENCE`
  - `CommonTeamRoster` (14): `TeamID`, `SEASON`, `LeagueID`, `PLAYER`, `PLAYER_SLUG`, `NUM`, `POSITION`, `HEIGHT`, `WEIGHT`, `BIRTH_DATE`, `AGE`, `EXP`, `SCHOOL`, `PLAYER_ID`

  </details>

### CommonTeamYears

- HTTP: `GET https://stats.nba.com/stats/commonteamyears`
- Repo docs: `docs/nba_api/stats/endpoints/commonteamyears.md`
- Example output: `docs/nba_api/stats/endpoints_output/commonteamyears_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import CommonTeamYears
  endpoint = CommonTeamYears()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `LeagueID` | `league_id` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `TeamYears` (5): `LEAGUE_ID`, `TEAM_ID`, `MIN_YEAR`, `MAX_YEAR`, `ABBREVIATION`

  </details>

### CumeStatsPlayer

- HTTP: `GET https://stats.nba.com/stats/cumestatsplayer`
- Repo docs: `docs/nba_api/stats/endpoints/cumestatsplayer.md`
- Example output: `docs/nba_api/stats/endpoints_output/cumestatsplayer_output.md`
- Required python args: `player_id`, `game_ids`
- Python:
  ```python
  from nba_api.stats.endpoints import CumeStatsPlayer
  endpoint = CumeStatsPlayer(player_id='…', game_ids='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `GameIDs` | `game_ids` | yes |
  | `PlayerID` | `player_id` | yes |
  | `LeagueID` | `league_id` | no |
  | `Season` | `season` | no |
  | `SeasonType` | `season_type_all_star` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `GameByGameStats` (28): `DATE_EST`, `VISITOR_TEAM`, `HOME_TEAM`, `GP`, `GS`, `ACTUAL_MINUTES`, `ACTUAL_SECONDS`, `FG`, `FGA`, `FG_PCT`, `FG3`, `FG3A`, `FG3_PCT`, `FT`, `FTA`, `FT_PCT`, `OFF_REB`, `DEF_REB`, `TOT_REB`, `AVG_TOT_REB`, `AST`, `PF`, `DQ`, `STL`, `TURNOVERS`, `BLK`, `PTS`, `AVG_PTS`
  - `TotalPlayerStats` (48): `DISPLAY_FI_LAST`, `PERSON_ID`, `JERSEY_NUM`, `GP`, `GS`, `ACTUAL_MINUTES`, `ACTUAL_SECONDS`, `FG`, `FGA`, `FG_PCT`, `FG3`, `FG3A`, `FG3_PCT`, `FT`, `FTA`, `FT_PCT`, `OFF_REB`, `DEF_REB`, `TOT_REB`, `AST`, `PF`, `DQ`, `STL`, `TURNOVERS`, `BLK`, `PTS`, `MAX_ACTUAL_MINUTES`, `MAX_ACTUAL_SECONDS`, `MAX_REB`, `MAX_AST`, `MAX_STL`, `MAX_TURNOVERS`, `MAX_BLK`, `MAX_PTS`, `AVG_ACTUAL_MINUTES`, `AVG_ACTUAL_SECONDS`, `AVG_TOT_REB`, `AVG_AST`, `AVG_STL`, `AVG_TURNOVERS`, `AVG_BLK`, `AVG_PTS`, `PER_MIN_TOT_REB`, `PER_MIN_AST`, `PER_MIN_STL`, `PER_MIN_TURNOVERS`, `PER_MIN_BLK`, `PER_MIN_PTS`

  </details>

### CumeStatsPlayerGames

- HTTP: `GET https://stats.nba.com/stats/cumestatsplayergames`
- Repo docs: `docs/nba_api/stats/endpoints/cumestatsplayergames.md`
- Example output: `docs/nba_api/stats/endpoints_output/cumestatsplayergames_output.md`
- Required python args: `player_id`
- Python:
  ```python
  from nba_api.stats.endpoints import CumeStatsPlayerGames
  endpoint = CumeStatsPlayerGames(player_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `PlayerID` | `player_id` | yes |
  | `LeagueID` | `league_id` | no |
  | `Location` | `location_nullable` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `Season` | `season` | no |
  | `SeasonType` | `season_type_all_star` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |
  | `VsTeamID` | `vs_team_id_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `CumeStatsPlayerGames` (2): `MATCHUP`, `GAME_ID`

  </details>

### CumeStatsTeam

- HTTP: `GET https://stats.nba.com/stats/cumestatsteam`
- Repo docs: `docs/nba_api/stats/endpoints/cumestatsteam.md`
- Example output: `docs/nba_api/stats/endpoints_output/cumestatsteam_output.md`
- Required python args: `team_id`, `game_ids`
- Python:
  ```python
  from nba_api.stats.endpoints import CumeStatsTeam
  endpoint = CumeStatsTeam(team_id='…', game_ids='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `GameIDs` | `game_ids` | yes |
  | `TeamID` | `team_id` | yes |
  | `LeagueID` | `league_id` | no |
  | `Season` | `season` | no |
  | `SeasonType` | `season_type_all_star` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `GameByGameStats` (49): `JERSEY_NUM`, `PLAYER`, `PERSON_ID`, `TEAM_ID`, `GP`, `GS`, `ACTUAL_MINUTES`, `ACTUAL_SECONDS`, `FG`, `FGA`, `FG_PCT`, `FG3`, `FG3A`, `FG3_PCT`, `FT`, `FTA`, `FT_PCT`, `OFF_REB`, `DEF_REB`, `TOT_REB`, `AST`, `PF`, `DQ`, `STL`, `TURNOVERS`, `BLK`, `PTS`, `MAX_ACTUAL_MINUTES`, `MAX_ACTUAL_SECONDS`, `MAX_REB`, `MAX_AST`, `MAX_STL`, `MAX_TURNOVERS`, `MAX_BLKP`, `MAX_PTS`, `AVG_ACTUAL_MINUTES`, `AVG_ACTUAL_SECONDS`, `AVG_REB`, `AVG_AST`, `AVG_STL`, `AVG_TURNOVERS`, `AVG_BLKP`, `AVG_PTS`, `PER_MIN_REB`, `PER_MIN_AST`, `PER_MIN_STL`, `PER_MIN_TURNOVERS`, `PER_MIN_BLK`, `PER_MIN_PTS`
  - `TotalTeamStats` (36): `CITY`, `NICKNAME`, `TEAM_ID`, `W`, `L`, `W_HOME`, `L_HOME`, `W_ROAD`, `L_ROAD`, `TEAM_TURNOVERS`, `TEAM_REBOUNDS`, `GP`, `GS`, `ACTUAL_MINUTES`, `ACTUAL_SECONDS`, `FG`, `FGA`, `FG_PCT`, `FG3`, `FG3A`, `FG3_PCT`, `FT`, `FTA`, `FT_PCT`, `OFF_REB`, `DEF_REB`, `TOT_REB`, `AST`, `PF`, `STL`, `TOTAL_TURNOVERS`, `BLK`, `PTS`, `AVG_REB`, `AVG_PTS`, `DQ`

  </details>

### CumeStatsTeamGames

- HTTP: `GET https://stats.nba.com/stats/cumestatsteamgames`
- Repo docs: `docs/nba_api/stats/endpoints/cumestatsteamgames.md`
- Example output: `docs/nba_api/stats/endpoints_output/cumestatsteamgames_output.md`
- Required python args: `team_id`
- Python:
  ```python
  from nba_api.stats.endpoints import CumeStatsTeamGames
  endpoint = CumeStatsTeamGames(team_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `TeamID` | `team_id` | yes |
  | `LeagueID` | `league_id` | no |
  | `Location` | `location_nullable` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `Season` | `season` | no |
  | `SeasonID` | `season_id_nullable` | no |
  | `SeasonType` | `season_type_all_star` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |
  | `VsTeamID` | `vs_team_id_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `CumeStatsTeamGames` (2): `MATCHUP`, `GAME_ID`

  </details>

### DefenseHub

- HTTP: `GET https://stats.nba.com/stats/defensehub`
- Repo docs: `docs/nba_api/stats/endpoints/defensehub.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import DefenseHub
  endpoint = DefenseHub()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `GameScope` | `game_scope_detailed` | no |
  | `LeagueID` | `league_id` | no |
  | `PlayerOrTeam` | `player_or_team` | no |
  | `PlayerScope` | `player_scope` | no |
  | `Season` | `season` | no |
  | `SeasonType` | `season_type_playoffs` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `DefenseHubStat1` (5): `RANK`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_NAME`, `DREB`
  - `DefenseHubStat10`
  - `DefenseHubStat2` (5): `RANK`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_NAME`, `STL`
  - `DefenseHubStat3` (5): `RANK`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_NAME`, `BLK`
  - `DefenseHubStat4` (5): `RANK`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_NAME`, `TM_DEF_RATING`
  - `DefenseHubStat5` (5): `RANK`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_NAME`, `OVERALL_PM`
  - `DefenseHubStat6` (5): `RANK`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_NAME`, `THREEP_DFGPCT`
  - `DefenseHubStat7` (5): `RANK`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_NAME`, `TWOP_DFGPCT`
  - `DefenseHubStat8` (5): `RANK`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_NAME`, `FIFETEENF_DFGPCT`
  - `DefenseHubStat9` (5): `RANK`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_NAME`, `DEF_RIM_PCT`

  </details>

### DraftBoard

- HTTP: `GET https://stats.nba.com/stats/draftboard`
- Repo docs: `docs/nba_api/stats/endpoints/draftboard.md`
- Example output: `docs/nba_api/stats/endpoints_output/draftboard_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import DraftBoard
  endpoint = DraftBoard()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `College` | `college_nullable` | no |
  | `LeagueID` | `league_id` | no |
  | `OverallPick` | `overall_pick_nullable` | no |
  | `RoundNum` | `round_num_nullable` | no |
  | `RoundPick` | `round_pick_nullable` | no |
  | `Season` | `season_year` | no |
  | `TeamID` | `team_id_nullable` | no |
  | `TopX` | `topx_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `DraftBoard` (18): `PERSON_ID`, `PLAYER_NAME`, `SEASON`, `ROUND_NUMBER`, `ROUND_PICK`, `OVERALL_PICK`, `TEAM_ID`, `TEAM_CITY`, `TEAM_NAME`, `TEAM_ABBREVIATION`, `ORGANIZATION`, `ORGANIZATION_TYPE`, `HEIGHT`, `WEIGHT`, `POSITION`, `JERSEY_NUMBER`, `BIRTHDATE`, `AGE`

  </details>

### DraftCombineDrillResults

- HTTP: `GET https://stats.nba.com/stats/draftcombinedrillresults`
- Repo docs: `docs/nba_api/stats/endpoints/draftcombinedrillresults.md`
- Example output: `docs/nba_api/stats/endpoints_output/draftcombinedrillresults_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import DraftCombineDrillResults
  endpoint = DraftCombineDrillResults()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `LeagueID` | `league_id` | no |
  | `SeasonYear` | `season_year` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `Results` (12): `TEMP_PLAYER_ID`, `PLAYER_ID`, `FIRST_NAME`, `LAST_NAME`, `PLAYER_NAME`, `POSITION`, `STANDING_VERTICAL_LEAP`, `MAX_VERTICAL_LEAP`, `LANE_AGILITY_TIME`, `MODIFIED_LANE_AGILITY_TIME`, `THREE_QUARTER_SPRINT`, `BENCH_PRESS`

  </details>

### DraftCombineNonStationaryShooting

- HTTP: `GET https://stats.nba.com/stats/draftcombinenonstationaryshooting`
- Repo docs: `docs/nba_api/stats/endpoints/draftcombinenonstationaryshooting.md`
- Example output: `docs/nba_api/stats/endpoints_output/draftcombinenonstationaryshooting_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import DraftCombineNonStationaryShooting
  endpoint = DraftCombineNonStationaryShooting()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `LeagueID` | `league_id` | no |
  | `SeasonYear` | `season_year` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `Results` (30): `TEMP_PLAYER_ID`, `PLAYER_ID`, `FIRST_NAME`, `LAST_NAME`, `PLAYER_NAME`, `POSITION`, `OFF_DRIB_FIFTEEN_BREAK_LEFT_MADE`, `OFF_DRIB_FIFTEEN_BREAK_LEFT_ATTEMPT`, `OFF_DRIB_FIFTEEN_BREAK_LEFT_PCT`, `OFF_DRIB_FIFTEEN_TOP_KEY_MADE`, `OFF_DRIB_FIFTEEN_TOP_KEY_ATTEMPT`, `OFF_DRIB_FIFTEEN_TOP_KEY_PCT`, `OFF_DRIB_FIFTEEN_BREAK_RIGHT_MADE`, `OFF_DRIB_FIFTEEN_BREAK_RIGHT_ATTEMPT`, `OFF_DRIB_FIFTEEN_BREAK_RIGHT_PCT`, `OFF_DRIB_COLLEGE_BREAK_LEFT_MADE`, `OFF_DRIB_COLLEGE_BREAK_LEFT_ATTEMPT`, `OFF_DRIB_COLLEGE_BREAK_LEFT_PCT`, `OFF_DRIB_COLLEGE_TOP_KEY_MADE`, `OFF_DRIB_COLLEGE_TOP_KEY_ATTEMPT`, `OFF_DRIB_COLLEGE_TOP_KEY_PCT`, `OFF_DRIB_COLLEGE_BREAK_RIGHT_MADE`, `OFF_DRIB_COLLEGE_BREAK_RIGHT_ATTEMPT`, `OFF_DRIB_COLLEGE_BREAK_RIGHT_PCT`, `ON_MOVE_FIFTEEN_MADE`, `ON_MOVE_FIFTEEN_ATTEMPT`, `ON_MOVE_FIFTEEN_PCT`, `ON_MOVE_COLLEGE_MADE`, `ON_MOVE_COLLEGE_ATTEMPT`, `ON_MOVE_COLLEGE_PCT`

  </details>

### DraftCombinePlayerAnthro

- HTTP: `GET https://stats.nba.com/stats/draftcombineplayeranthro`
- Repo docs: `docs/nba_api/stats/endpoints/draftcombineplayeranthro.md`
- Example output: `docs/nba_api/stats/endpoints_output/draftcombineplayeranthro_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import DraftCombinePlayerAnthro
  endpoint = DraftCombinePlayerAnthro()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `LeagueID` | `league_id` | no |
  | `SeasonYear` | `season_year` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `Results` (18): `TEMP_PLAYER_ID`, `PLAYER_ID`, `FIRST_NAME`, `LAST_NAME`, `PLAYER_NAME`, `POSITION`, `HEIGHT_WO_SHOES`, `HEIGHT_WO_SHOES_FT_IN`, `HEIGHT_W_SHOES`, `HEIGHT_W_SHOES_FT_IN`, `WEIGHT`, `WINGSPAN`, `WINGSPAN_FT_IN`, `STANDING_REACH`, `STANDING_REACH_FT_IN`, `BODY_FAT_PCT`, `HAND_LENGTH`, `HAND_WIDTH`

  </details>

### DraftCombineSpotShooting

- HTTP: `GET https://stats.nba.com/stats/draftcombinespotshooting`
- Repo docs: `docs/nba_api/stats/endpoints/draftcombinespotshooting.md`
- Example output: `docs/nba_api/stats/endpoints_output/draftcombinespotshooting_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import DraftCombineSpotShooting
  endpoint = DraftCombineSpotShooting()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `LeagueID` | `league_id` | no |
  | `SeasonYear` | `season_year` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `Results` (51): `TEMP_PLAYER_ID`, `PLAYER_ID`, `FIRST_NAME`, `LAST_NAME`, `PLAYER_NAME`, `POSITION`, `FIFTEEN_CORNER_LEFT_MADE`, `FIFTEEN_CORNER_LEFT_ATTEMPT`, `FIFTEEN_CORNER_LEFT_PCT`, `FIFTEEN_BREAK_LEFT_MADE`, `FIFTEEN_BREAK_LEFT_ATTEMPT`, `FIFTEEN_BREAK_LEFT_PCT`, `FIFTEEN_TOP_KEY_MADE`, `FIFTEEN_TOP_KEY_ATTEMPT`, `FIFTEEN_TOP_KEY_PCT`, `FIFTEEN_BREAK_RIGHT_MADE`, `FIFTEEN_BREAK_RIGHT_ATTEMPT`, `FIFTEEN_BREAK_RIGHT_PCT`, `FIFTEEN_CORNER_RIGHT_MADE`, `FIFTEEN_CORNER_RIGHT_ATTEMPT`, `FIFTEEN_CORNER_RIGHT_PCT`, `COLLEGE_CORNER_LEFT_MADE`, `COLLEGE_CORNER_LEFT_ATTEMPT`, `COLLEGE_CORNER_LEFT_PCT`, `COLLEGE_BREAK_LEFT_MADE`, `COLLEGE_BREAK_LEFT_ATTEMPT`, `COLLEGE_BREAK_LEFT_PCT`, `COLLEGE_TOP_KEY_MADE`, `COLLEGE_TOP_KEY_ATTEMPT`, `COLLEGE_TOP_KEY_PCT`, `COLLEGE_BREAK_RIGHT_MADE`, `COLLEGE_BREAK_RIGHT_ATTEMPT`, `COLLEGE_BREAK_RIGHT_PCT`, `COLLEGE_CORNER_RIGHT_MADE`, `COLLEGE_CORNER_RIGHT_ATTEMPT`, `COLLEGE_CORNER_RIGHT_PCT`, `NBA_CORNER_LEFT_MADE`, `NBA_CORNER_LEFT_ATTEMPT`, `NBA_CORNER_LEFT_PCT`, `NBA_BREAK_LEFT_MADE`, `NBA_BREAK_LEFT_ATTEMPT`, `NBA_BREAK_LEFT_PCT`, `NBA_TOP_KEY_MADE`, `NBA_TOP_KEY_ATTEMPT`, `NBA_TOP_KEY_PCT`, `NBA_BREAK_RIGHT_MADE`, `NBA_BREAK_RIGHT_ATTEMPT`, `NBA_BREAK_RIGHT_PCT`, `NBA_CORNER_RIGHT_MADE`, `NBA_CORNER_RIGHT_ATTEMPT`, `NBA_CORNER_RIGHT_PCT`

  </details>

### DraftCombineStats

- HTTP: `GET https://stats.nba.com/stats/draftcombinestats`
- Repo docs: `docs/nba_api/stats/endpoints/draftcombinestats.md`
- Example output: `docs/nba_api/stats/endpoints_output/draftcombinestats_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import DraftCombineStats
  endpoint = DraftCombineStats()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `LeagueID` | `league_id` | no |
  | `SeasonYear` | `season_all_time` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `DraftCombineStats` (47): `SEASON`, `PLAYER_ID`, `FIRST_NAME`, `LAST_NAME`, `PLAYER_NAME`, `POSITION`, `HEIGHT_WO_SHOES`, `HEIGHT_WO_SHOES_FT_IN`, `HEIGHT_W_SHOES`, `HEIGHT_W_SHOES_FT_IN`, `WEIGHT`, `WINGSPAN`, `WINGSPAN_FT_IN`, `STANDING_REACH`, `STANDING_REACH_FT_IN`, `BODY_FAT_PCT`, `HAND_LENGTH`, `HAND_WIDTH`, `STANDING_VERTICAL_LEAP`, `MAX_VERTICAL_LEAP`, `LANE_AGILITY_TIME`, `MODIFIED_LANE_AGILITY_TIME`, `THREE_QUARTER_SPRINT`, `BENCH_PRESS`, `SPOT_FIFTEEN_CORNER_LEFT`, `SPOT_FIFTEEN_BREAK_LEFT`, `SPOT_FIFTEEN_TOP_KEY`, `SPOT_FIFTEEN_BREAK_RIGHT`, `SPOT_FIFTEEN_CORNER_RIGHT`, `SPOT_COLLEGE_CORNER_LEFT`, `SPOT_COLLEGE_BREAK_LEFT`, `SPOT_COLLEGE_TOP_KEY`, `SPOT_COLLEGE_BREAK_RIGHT`, `SPOT_COLLEGE_CORNER_RIGHT`, `SPOT_NBA_CORNER_LEFT`, `SPOT_NBA_BREAK_LEFT`, `SPOT_NBA_TOP_KEY`, `SPOT_NBA_BREAK_RIGHT`, `SPOT_NBA_CORNER_RIGHT`, `OFF_DRIB_FIFTEEN_BREAK_LEFT`, `OFF_DRIB_FIFTEEN_TOP_KEY`, `OFF_DRIB_FIFTEEN_BREAK_RIGHT`, `OFF_DRIB_COLLEGE_BREAK_LEFT`, `OFF_DRIB_COLLEGE_TOP_KEY`, `OFF_DRIB_COLLEGE_BREAK_RIGHT`, `ON_MOVE_FIFTEEN`, `ON_MOVE_COLLEGE`

  </details>

### DraftHistory

- HTTP: `GET https://stats.nba.com/stats/drafthistory`
- Repo docs: `docs/nba_api/stats/endpoints/drafthistory.md`
- Example output: `docs/nba_api/stats/endpoints_output/drafthistory_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import DraftHistory
  endpoint = DraftHistory()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `College` | `college_nullable` | no |
  | `LeagueID` | `league_id` | no |
  | `OverallPick` | `overall_pick_nullable` | no |
  | `RoundNum` | `round_num_nullable` | no |
  | `RoundPick` | `round_pick_nullable` | no |
  | `Season` | `season_year_nullable` | no |
  | `TeamID` | `team_id_nullable` | no |
  | `TopX` | `topx_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `DraftHistory` (13): `PERSON_ID`, `PLAYER_NAME`, `SEASON`, `ROUND_NUMBER`, `ROUND_PICK`, `OVERALL_PICK`, `DRAFT_TYPE`, `TEAM_ID`, `TEAM_CITY`, `TEAM_NAME`, `TEAM_ABBREVIATION`, `ORGANIZATION`, `ORGANIZATION_TYPE`

  </details>

### DunkScoreLeaders

- HTTP: `GET https://stats.nba.com/stats/dunkscoreleaders`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import DunkScoreLeaders
  endpoint = DunkScoreLeaders()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `GameID` | `game_id_nullable` | no |
  | `LeagueID` | `league_id_nullable` | no |
  | `PlayerID` | `player_id_nullable` | no |
  | `Season` | `season` | no |
  | `SeasonType` | `season_type_all_star` | no |
  | `TeamID` | `team_id_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `Dunks` (55): `GAME_ID`, `GAME_DATE`, `MATCHUP`, `PERIOD`, `GAME_CLOCK_TIME`, `EVENT_NUM`, `PLAYER_ID`, `PLAYER_NAME`, `FIRST_NAME`, `LAST_NAME`, `TEAM_ID`, `TEAM_NAME`, `TEAM_CITY`, `TEAM_ABBREVIATION`, `DUNK_SCORE`, `JUMP_SUBSCORE`, `POWER_SUBSCORE`, `STYLE_SUBSCORE`, `DEFENSIVE_CONTEST_SUBSCORE`, `MAX_BALL_HEIGHT`, `BALL_SPEED_THROUGH_RIM`, `PLAYER_VERTICAL`, `HANG_TIME`, `TAKEOFF_DISTANCE`, `REVERSE_DUNK`, `DUNK_360`, `THROUGH_THE_LEGS`, `ALLEY_OOP`, `TIP_IN`, `SELF_OOP`, `PLAYER_ROTATION`, `PLAYER_LATERAL_SPEED`, `BALL_DISTANCE_TRAVELED`, `BALL_REACH_BACK`, `TOTAL_BALL_ACCELERATION`, `DUNKING_HAND`, `JUMPING_FOOT`, `PASS_LENGTH`, `CATCHING_HAND`, `CATCH_DISTANCE`, `LATERAL_CATCH_DISTANCE`, `PASSER_ID`, `PASSER_NAME`, `PASSER_FIRST_NAME`, `PASSER_LAST_NAME`, `PASS_RELEASE_POINT`, `SHOOTER_ID`, `SHOOTER_NAME`, `SHOOTER_FIRST_NAME`, `SHOOTER_LAST_NAME`, `SHOT_RELEASE_POINT`, `SHOT_LENGTH`, `DEFENSIVE_CONTEST_LEVEL`, `POSSIBLE_ATTEMPTED_CHARGE`, `VIDEO_AVAILABLE`

  </details>

### FantasyWidget

- HTTP: `GET https://stats.nba.com/stats/fantasywidget`
- Repo docs: `docs/nba_api/stats/endpoints/fantasywidget.md`
- Example output: `docs/nba_api/stats/endpoints_output/fantasywidget_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import FantasyWidget
  endpoint = FantasyWidget()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `ActivePlayers` | `active_players` | no |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `LastNGames` | `last_n_games` | no |
  | `LeagueID` | `league_id` | no |
  | `Location` | `location_nullable` | no |
  | `Month` | `month_nullable` | no |
  | `OpponentTeamID` | `opponent_team_id_nullable` | no |
  | `PORound` | `po_round_nullable` | no |
  | `PlayerID` | `player_id_nullable` | no |
  | `Position` | `position_nullable` | no |
  | `Season` | `season` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_all_star` | no |
  | `TeamID` | `team_id_nullable` | no |
  | `TodaysOpponent` | `todays_opponent` | no |
  | `TodaysPlayers` | `todays_players` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `FantasyWidgetResult` (20): `PLAYER_ID`, `PLAYER_NAME`, `PLAYER_POSITION`, `TEAM_ID`, `TEAM_ABBREVIATION`, `GP`, `MIN`, `FAN_DUEL_PTS`, `NBA_FANTASY_PTS`, `PTS`, `REB`, `AST`, `BLK`, `STL`, `TOV`, `FG3M`, `FGA`, `FG_PCT`, `FTA`, `FT_PCT`

  </details>

### FranchiseHistory

- HTTP: `GET https://stats.nba.com/stats/franchisehistory`
- Repo docs: `docs/nba_api/stats/endpoints/franchisehistory.md`
- Example output: `docs/nba_api/stats/endpoints_output/franchisehistory_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import FranchiseHistory
  endpoint = FranchiseHistory()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `LeagueID` | `league_id` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `DefunctTeams` (15): `LEAGUE_ID`, `TEAM_ID`, `TEAM_CITY`, `TEAM_NAME`, `START_YEAR`, `END_YEAR`, `YEARS`, `GAMES`, `WINS`, `LOSSES`, `WIN_PCT`, `PO_APPEARANCES`, `DIV_TITLES`, `CONF_TITLES`, `LEAGUE_TITLES`
  - `FranchiseHistory` (15): `LEAGUE_ID`, `TEAM_ID`, `TEAM_CITY`, `TEAM_NAME`, `START_YEAR`, `END_YEAR`, `YEARS`, `GAMES`, `WINS`, `LOSSES`, `WIN_PCT`, `PO_APPEARANCES`, `DIV_TITLES`, `CONF_TITLES`, `LEAGUE_TITLES`

  </details>

### FranchiseLeaders

- HTTP: `GET https://stats.nba.com/stats/franchiseleaders`
- Repo docs: `docs/nba_api/stats/endpoints/franchiseleaders.md`
- Example output: `docs/nba_api/stats/endpoints_output/franchiseleaders_output.md`
- Required python args: `team_id`
- Python:
  ```python
  from nba_api.stats.endpoints import FranchiseLeaders
  endpoint = FranchiseLeaders(team_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `TeamID` | `team_id` | yes |
  | `LeagueID` | `league_id_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `FranchiseLeaders` (16): `TEAM_ID`, `PTS`, `PTS_PERSON_ID`, `PTS_PLAYER`, `AST`, `AST_PERSON_ID`, `AST_PLAYER`, `REB`, `REB_PERSON_ID`, `REB_PLAYER`, `BLK`, `BLK_PERSON_ID`, `BLK_PLAYER`, `STL`, `STL_PERSON_ID`, `STL_PLAYER`

  </details>

### FranchisePlayers

- HTTP: `GET https://stats.nba.com/stats/franchiseplayers`
- Repo docs: `docs/nba_api/stats/endpoints/franchiseplayers.md`
- Example output: `docs/nba_api/stats/endpoints_output/franchiseplayers_output.md`
- Required python args: `team_id`
- Python:
  ```python
  from nba_api.stats.endpoints import FranchisePlayers
  endpoint = FranchisePlayers(team_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `TeamID` | `team_id` | yes |
  | `LeagueID` | `league_id` | no |
  | `PerMode` | `per_mode_detailed` | no |
  | `SeasonType` | `season_type_all_star` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `FranchisePlayers` (26): `LEAGUE_ID`, `TEAM_ID`, `TEAM`, `PERSON_ID`, `PLAYER`, `SEASON_TYPE`, `ACTIVE_WITH_TEAM`, `GP`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `PF`, `STL`, `TOV`, `BLK`, `PTS`

  </details>

### GameRotation

- HTTP: `GET https://stats.nba.com/stats/gamerotation`
- Repo docs: `docs/nba_api/stats/endpoints/gamerotation.md`
- Example output: `docs/nba_api/stats/endpoints_output/gamerotation_output.md`
- Required python args: `game_id`
- Python:
  ```python
  from nba_api.stats.endpoints import GameRotation
  endpoint = GameRotation(game_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `GameID` | `game_id` | yes |
  | `LeagueID` | `league_id` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `AwayTeam` (12): `GAME_ID`, `TEAM_ID`, `TEAM_CITY`, `TEAM_NAME`, `PERSON_ID`, `PLAYER_FIRST`, `PLAYER_LAST`, `IN_TIME_REAL`, `OUT_TIME_REAL`, `PLAYER_PTS`, `PT_DIFF`, `USG_PCT`
  - `HomeTeam` (12): `GAME_ID`, `TEAM_ID`, `TEAM_CITY`, `TEAM_NAME`, `PERSON_ID`, `PLAYER_FIRST`, `PLAYER_LAST`, `IN_TIME_REAL`, `OUT_TIME_REAL`, `PLAYER_PTS`, `PT_DIFF`, `USG_PCT`

  </details>

### GLAlumBoxScoreSimilarityScore

- HTTP: `GET https://stats.nba.com/stats/glalumboxscoresimilarityscore`
- Repo docs: `docs/nba_api/stats/endpoints/glalumboxscoresimilarityscore.md`
- Example output: `docs/nba_api/stats/endpoints_output/glalumboxscoresimilarityscore_output.md`
- Required python args: `person2_id`, `person1_id`
- Python:
  ```python
  from nba_api.stats.endpoints import GLAlumBoxScoreSimilarityScore
  endpoint = GLAlumBoxScoreSimilarityScore(person2_id='…', person1_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `Person1Id` | `person1_id` | yes |
  | `Person2Id` | `person2_id` | yes |
  | `Person1LeagueId` | `person1_league_id` | no |
  | `Person1Season` | `person1_season_year` | no |
  | `Person1SeasonType` | `person1_season_type` | no |
  | `Person2LeagueId` | `person2_league_id` | no |
  | `Person2Season` | `person2_season_year` | no |
  | `Person2SeasonType` | `person2_season_type` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `GLeagueAlumBoxScoreSimilarityScores` (4): `PERSON_2_ID`, `PERSON_2`, `TEAM_ID`, `SIMILARITY_SCORE`

  </details>

### HomePageLeaders

- HTTP: `GET https://stats.nba.com/stats/homepageleaders`
- Repo docs: `docs/nba_api/stats/endpoints/homepageleaders.md`
- Example output: `docs/nba_api/stats/endpoints_output/homepageleaders_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import HomePageLeaders
  endpoint = HomePageLeaders()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `GameScope` | `game_scope_detailed` | no |
  | `LeagueID` | `league_id` | no |
  | `PlayerOrTeam` | `player_or_team` | no |
  | `PlayerScope` | `player_scope` | no |
  | `Season` | `season` | no |
  | `SeasonType` | `season_type_playoffs` | no |
  | `StatCategory` | `stat_category` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `HomePageLeaders` (11): `RANK`, `TEAM_ID`, `TEAM_NAME`, `TEAM_ABBREVIATION`, `PTS`, `FG_PCT`, `FG3_PCT`, `FT_PCT`, `EFG_PCT`, `TS_PCT`, `PTS_PER48`
  - `LeagueAverage` (7): `PTS`, `FG_PCT`, `FG3_PCT`, `FT_PCT`, `EFG_PCT`, `TS_PCT`, `PTS_PER48`
  - `LeagueMax` (7): `PTS`, `FG_PCT`, `FG3_PCT`, `FT_PCT`, `EFG_PCT`, `TS_PCT`, `PTS_PER48`

  </details>

### HomePageV2

- HTTP: `GET https://stats.nba.com/stats/homepagev2`
- Repo docs: `docs/nba_api/stats/endpoints/homepagev2.md`
- Example output: `docs/nba_api/stats/endpoints_output/homepagev2_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import HomePageV2
  endpoint = HomePageV2()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `GameScope` | `game_scope_detailed` | no |
  | `LeagueID` | `league_id` | no |
  | `PlayerOrTeam` | `player_or_team` | no |
  | `PlayerScope` | `player_scope` | no |
  | `Season` | `season` | no |
  | `SeasonType` | `season_type_playoffs` | no |
  | `StatType` | `stat_type` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `HomePageStat1` (5): `RANK`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_NAME`, `PTS`
  - `HomePageStat2` (5): `RANK`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_NAME`, `REB`
  - `HomePageStat3` (5): `RANK`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_NAME`, `AST`
  - `HomePageStat4` (5): `RANK`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_NAME`, `STL`
  - `HomePageStat5` (5): `RANK`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_NAME`, `FG_PCT`
  - `HomePageStat6` (5): `RANK`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_NAME`, `FT_PCT`
  - `HomePageStat7` (5): `RANK`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_NAME`, `FG3_PCT`
  - `HomePageStat8` (5): `RANK`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_NAME`, `BLK`

  </details>

### HustleStatsBoxScore

- HTTP: `GET https://stats.nba.com/stats/hustlestatsboxscore`
- Repo docs: `docs/nba_api/stats/endpoints/hustlestatsboxscore.md`
- Example output: `docs/nba_api/stats/endpoints_output/hustlestatsboxscore_output.md`
- Required python args: `game_id`
- Python:
  ```python
  from nba_api.stats.endpoints import HustleStatsBoxScore
  endpoint = HustleStatsBoxScore(game_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `GameID` | `game_id` | yes |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `HustleStatsAvailable` (2): `GAME_ID`, `HUSTLE_STATUS`
  - `PlayerStats` (25): `GAME_ID`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_CITY`, `PLAYER_ID`, `PLAYER_NAME`, `START_POSITION`, `COMMENT`, `MINUTES`, `PTS`, `CONTESTED_SHOTS`, `CONTESTED_SHOTS_2PT`, `CONTESTED_SHOTS_3PT`, `DEFLECTIONS`, `CHARGES_DRAWN`, `SCREEN_ASSISTS`, `SCREEN_AST_PTS`, `OFF_LOOSE_BALLS_RECOVERED`, `DEF_LOOSE_BALLS_RECOVERED`, `LOOSE_BALLS_RECOVERED`, `OFF_BOXOUTS`, `DEF_BOXOUTS`, `BOX_OUT_PLAYER_TEAM_REBS`, `BOX_OUT_PLAYER_REBS`, `BOX_OUTS`
  - `TeamStats` (22): `GAME_ID`, `TEAM_ID`, `TEAM_NAME`, `TEAM_ABBREVIATION`, `TEAM_CITY`, `MINUTES`, `PTS`, `CONTESTED_SHOTS`, `CONTESTED_SHOTS_2PT`, `CONTESTED_SHOTS_3PT`, `DEFLECTIONS`, `CHARGES_DRAWN`, `SCREEN_ASSISTS`, `SCREEN_AST_PTS`, `OFF_LOOSE_BALLS_RECOVERED`, `DEF_LOOSE_BALLS_RECOVERED`, `LOOSE_BALLS_RECOVERED`, `OFF_BOXOUTS`, `DEF_BOXOUTS`, `BOX_OUT_PLAYER_TEAM_REBS`, `BOX_OUT_PLAYER_REBS`, `BOX_OUTS`

  </details>

### InfographicFanDuelPlayer

- HTTP: `GET https://stats.nba.com/stats/infographicfanduelplayer`
- Repo docs: `docs/nba_api/stats/endpoints/infographicfanduelplayer.md`
- Example output: `docs/nba_api/stats/endpoints_output/infographicfanduelplayer_output.md`
- Required python args: `game_id`
- Python:
  ```python
  from nba_api.stats.endpoints import InfographicFanDuelPlayer
  endpoint = InfographicFanDuelPlayer(game_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `GameID` | `game_id` | yes |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `FanDuelPlayer` (33): `PLAYER_ID`, `PLAYER_NAME`, `TEAM_ID`, `TEAM_NAME`, `TEAM_ABBREVIATION`, `JERSEY_NUM`, `PLAYER_POSITION`, `LOCATION`, `FAN_DUEL_PTS`, `NBA_FANTASY_PTS`, `USG_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`

  </details>

### ISTStandings

- HTTP: `GET https://stats.nba.com/stats/iststandings`
- Repo docs: `docs/nba_api/stats/endpoints/iststandings.md`
- Example output: `docs/nba_api/stats/endpoints_output/iststandings_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import ISTStandings
  endpoint = ISTStandings()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `LeagueID` | `league_id` | no |
  | `Season` | `season` | no |
  | `Section` | `section` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `Standings` (48): `leagueId`, `seasonYear`, `teamId`, `teamCity`, `teamName`, `teamAbbreviation`, `teamSlug`, `conference`, `istGroup`, `clinchIndicator`, `clinchedIstKnockout`, `clinchedIstGroup`, `clinchedIstWildcard`, `istWildcardRank`, `istGroupRank`, `istKnockoutRank`, `wins`, `losses`, `pct`, `istGroupGb`, `istWildcardGb`, `diff`, `pts`, `oppPts`, `gameId1`, `opponentTeamAbbreviation1`, `location1`, `gameStatus1`, `gameStatusText1`, `outcome1`, `gameId2`, `opponentTeamAbbreviation2`, `location2`, `gameStatus2`, `gameStatusText2`, `outcome2`, `gameId3`, `opponentTeamAbbreviation3`, `location3`, `gameStatus3`, `gameStatusText3`, `outcome3`, `gameId4`, `opponentTeamAbbreviation4`, `location4`, `gameStatus4`, `gameStatusText4`, `outcome4`

  </details>

### LeadersTiles

- HTTP: `GET https://stats.nba.com/stats/leaderstiles`
- Repo docs: `docs/nba_api/stats/endpoints/leaderstiles.md`
- Example output: `docs/nba_api/stats/endpoints_output/leaderstiles_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import LeadersTiles
  endpoint = LeadersTiles()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `GameScope` | `game_scope_detailed` | no |
  | `LeagueID` | `league_id` | no |
  | `PlayerOrTeam` | `player_or_team` | no |
  | `PlayerScope` | `player_scope` | no |
  | `Season` | `season` | no |
  | `SeasonType` | `season_type_playoffs` | no |
  | `Stat` | `stat` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `AllTimeSeasonHigh` (5): `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_NAME`, `SEASON_YEAR`, `PTS`
  - `LastSeasonHigh` (5): `RANK`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_NAME`, `PTS`
  - `LeadersTiles` (5): `RANK`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_NAME`, `PTS`
  - `LowSeasonHigh` (5): `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_NAME`, `SEASON_YEAR`, `PTS`

  </details>

### LeagueDashLineups

- HTTP: `GET https://stats.nba.com/stats/leaguedashlineups`
- Repo docs: `docs/nba_api/stats/endpoints/leaguedashlineups.md`
- Example output: `docs/nba_api/stats/endpoints_output/leaguedashlineups_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import LeagueDashLineups
  endpoint = LeagueDashLineups()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `Conference` | `conference_nullable` | no |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `Division` | `division_simple_nullable` | no |
  | `GameSegment` | `game_segment_nullable` | no |
  | `GroupQuantity` | `group_quantity` | no |
  | `LastNGames` | `last_n_games` | no |
  | `LeagueID` | `league_id_nullable` | no |
  | `Location` | `location_nullable` | no |
  | `MeasureType` | `measure_type_detailed_defense` | no |
  | `Month` | `month` | no |
  | `OpponentTeamID` | `opponent_team_id` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `PORound` | `po_round_nullable` | no |
  | `PaceAdjust` | `pace_adjust` | no |
  | `PerMode` | `per_mode_detailed` | no |
  | `Period` | `period` | no |
  | `PlusMinus` | `plus_minus` | no |
  | `Rank` | `rank` | no |
  | `Season` | `season` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_all_star` | no |
  | `ShotClockRange` | `shot_clock_range_nullable` | no |
  | `TeamID` | `team_id_nullable` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `Lineups` (57): `GROUP_SET`, `GROUP_ID`, `GROUP_NAME`, `TEAM_ID`, `TEAM_ABBREVIATION`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`

  </details>

### LeagueDashOppPtShot

- HTTP: `GET https://stats.nba.com/stats/leaguedashoppptshot`
- Repo docs: `docs/nba_api/stats/endpoints/leaguedashoppptshot.md`
- Example output: `docs/nba_api/stats/endpoints_output/leaguedashoppptshot_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import LeagueDashOppPtShot
  endpoint = LeagueDashOppPtShot()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `CloseDefDistRange` | `close_def_dist_range_nullable` | no |
  | `Conference` | `conference_nullable` | no |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `Division` | `division_nullable` | no |
  | `DribbleRange` | `dribble_range_nullable` | no |
  | `GameSegment` | `game_segment_nullable` | no |
  | `GeneralRange` | `general_range_nullable` | no |
  | `LastNGames` | `last_n_games_nullable` | no |
  | `LeagueID` | `league_id` | no |
  | `Location` | `location_nullable` | no |
  | `Month` | `month_nullable` | no |
  | `OpponentTeamID` | `opponent_team_id_nullable` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `PORound` | `po_round_nullable` | no |
  | `PerMode` | `per_mode_simple` | no |
  | `Period` | `period_nullable` | no |
  | `Season` | `season` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_all_star` | no |
  | `ShotClockRange` | `shot_clock_range_nullable` | no |
  | `ShotDistRange` | `shot_dist_range_nullable` | no |
  | `TeamID` | `team_id_nullable` | no |
  | `TouchTimeRange` | `touch_time_range_nullable` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `LeagueDashPTShots` (18): `TEAM_ID`, `TEAM_NAME`, `TEAM_ABBREVIATION`, `GP`, `G`, `FGA_FREQUENCY`, `FGM`, `FGA`, `FG_PCT`, `EFG_PCT`, `FG2A_FREQUENCY`, `FG2M`, `FG2A`, `FG2_PCT`, `FG3A_FREQUENCY`, `FG3M`, `FG3A`, `FG3_PCT`

  </details>

### LeagueDashPlayerBioStats

- HTTP: `GET https://stats.nba.com/stats/leaguedashplayerbiostats`
- Repo docs: `docs/nba_api/stats/endpoints/leaguedashplayerbiostats.md`
- Example output: `docs/nba_api/stats/endpoints_output/leaguedashplayerbiostats_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import LeagueDashPlayerBioStats
  endpoint = LeagueDashPlayerBioStats()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `College` | `college_nullable` | no |
  | `Conference` | `conference_nullable` | no |
  | `Country` | `country_nullable` | no |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `Division` | `division_simple_nullable` | no |
  | `DraftPick` | `draft_pick_nullable` | no |
  | `DraftYear` | `draft_year_nullable` | no |
  | `GameScope` | `game_scope_simple_nullable` | no |
  | `GameSegment` | `game_segment_nullable` | no |
  | `Height` | `height_nullable` | no |
  | `LastNGames` | `last_n_games_nullable` | no |
  | `LeagueID` | `league_id` | no |
  | `Location` | `location_nullable` | no |
  | `Month` | `month_nullable` | no |
  | `OpponentTeamID` | `opponent_team_id_nullable` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `PORound` | `po_round_nullable` | no |
  | `PerMode` | `per_mode_simple` | no |
  | `Period` | `period_nullable` | no |
  | `PlayerExperience` | `player_experience_nullable` | no |
  | `PlayerPosition` | `player_position_abbreviation_nullable` | no |
  | `Season` | `season` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_all_star` | no |
  | `ShotClockRange` | `shot_clock_range_nullable` | no |
  | `StarterBench` | `starter_bench_nullable` | no |
  | `TeamID` | `team_id_nullable` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |
  | `Weight` | `weight_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `LeagueDashPlayerBioStats` (23): `PLAYER_ID`, `PLAYER_NAME`, `TEAM_ID`, `TEAM_ABBREVIATION`, `AGE`, `PLAYER_HEIGHT`, `PLAYER_HEIGHT_INCHES`, `PLAYER_WEIGHT`, `COLLEGE`, `COUNTRY`, `DRAFT_YEAR`, `DRAFT_ROUND`, `DRAFT_NUMBER`, `GP`, `PTS`, `REB`, `AST`, `NET_RATING`, `OREB_PCT`, `DREB_PCT`, `USG_PCT`, `TS_PCT`, `AST_PCT`

  </details>

### LeagueDashPlayerClutch

- HTTP: `GET https://stats.nba.com/stats/leaguedashplayerclutch`
- Repo docs: `docs/nba_api/stats/endpoints/leaguedashplayerclutch.md`
- Example output: `docs/nba_api/stats/endpoints_output/leaguedashplayerclutch_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import LeagueDashPlayerClutch
  endpoint = LeagueDashPlayerClutch()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `AheadBehind` | `ahead_behind` | no |
  | `ClutchTime` | `clutch_time` | no |
  | `College` | `college_nullable` | no |
  | `Conference` | `conference_nullable` | no |
  | `Country` | `country_nullable` | no |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `Division` | `division_simple_nullable` | no |
  | `DraftPick` | `draft_pick_nullable` | no |
  | `DraftYear` | `draft_year_nullable` | no |
  | `GameScope` | `game_scope_simple_nullable` | no |
  | `GameSegment` | `game_segment_nullable` | no |
  | `Height` | `height_nullable` | no |
  | `LastNGames` | `last_n_games` | no |
  | `LeagueID` | `league_id_nullable` | no |
  | `Location` | `location_nullable` | no |
  | `MeasureType` | `measure_type_detailed_defense` | no |
  | `Month` | `month` | no |
  | `OpponentTeamID` | `opponent_team_id` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `PORound` | `po_round_nullable` | no |
  | `PaceAdjust` | `pace_adjust` | no |
  | `PerMode` | `per_mode_detailed` | no |
  | `Period` | `period` | no |
  | `PlayerExperience` | `player_experience_nullable` | no |
  | `PlayerPosition` | `player_position_abbreviation_nullable` | no |
  | `PlusMinus` | `plus_minus` | no |
  | `PointDiff` | `point_diff` | no |
  | `Rank` | `rank` | no |
  | `Season` | `season` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_all_star` | no |
  | `ShotClockRange` | `shot_clock_range_nullable` | no |
  | `StarterBench` | `starter_bench_nullable` | no |
  | `TeamID` | `team_id_nullable` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |
  | `Weight` | `weight_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `LeagueDashPlayerClutch` (66): `GROUP_SET`, `PLAYER_ID`, `PLAYER_NAME`, `TEAM_ID`, `TEAM_ABBREVIATION`, `AGE`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `NBA_FANTASY_PTS`, `DD2`, `TD3`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `NBA_FANTASY_PTS_RANK`, `DD2_RANK`, `TD3_RANK`, `CFID`, `CFPARAMS`

  </details>

### LeagueDashPlayerPtShot

- HTTP: `GET https://stats.nba.com/stats/leaguedashplayerptshot`
- Repo docs: `docs/nba_api/stats/endpoints/leaguedashplayerptshot.md`
- Example output: `docs/nba_api/stats/endpoints_output/leaguedashplayerptshot_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import LeagueDashPlayerPtShot
  endpoint = LeagueDashPlayerPtShot()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `CloseDefDistRange` | `close_def_dist_range_nullable` | no |
  | `College` | `college_nullable` | no |
  | `Conference` | `conference_nullable` | no |
  | `Country` | `country_nullable` | no |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `Division` | `division_nullable` | no |
  | `DraftPick` | `draft_pick_nullable` | no |
  | `DraftYear` | `draft_year_nullable` | no |
  | `DribbleRange` | `dribble_range_nullable` | no |
  | `GameSegment` | `game_segment_nullable` | no |
  | `GeneralRange` | `general_range_nullable` | no |
  | `Height` | `height_nullable` | no |
  | `LastNGames` | `last_n_games_nullable` | no |
  | `LeagueID` | `league_id` | no |
  | `Location` | `location_nullable` | no |
  | `Month` | `month_nullable` | no |
  | `OpponentTeamID` | `opponent_team_id_nullable` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `PORound` | `po_round_nullable` | no |
  | `PerMode` | `per_mode_simple` | no |
  | `Period` | `period_nullable` | no |
  | `PlayerExperience` | `player_experience_nullable` | no |
  | `PlayerPosition` | `player_position_nullable` | no |
  | `Season` | `season` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_all_star` | no |
  | `ShotClockRange` | `shot_clock_range_nullable` | no |
  | `ShotDistRange` | `shot_dist_range_nullable` | no |
  | `StarterBench` | `starter_bench_nullable` | no |
  | `TeamID` | `team_id_nullable` | no |
  | `TouchTimeRange` | `touch_time_range_nullable` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |
  | `Weight` | `weight_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `LeagueDashPTShots` (20): `PLAYER_ID`, `PLAYER_NAME`, `PLAYER_LAST_TEAM_ID`, `PLAYER_LAST_TEAM_ABBREVIATION`, `AGE`, `GP`, `G`, `FGA_FREQUENCY`, `FGM`, `FGA`, `FG_PCT`, `EFG_PCT`, `FG2A_FREQUENCY`, `FG2M`, `FG2A`, `FG2_PCT`, `FG3A_FREQUENCY`, `FG3M`, `FG3A`, `FG3_PCT`

  </details>

### LeagueDashPlayerShotLocations

- HTTP: `GET https://stats.nba.com/stats/leaguedashplayershotlocations`
- Repo docs: `docs/nba_api/stats/endpoints/leaguedashplayershotlocations.md`
- Example output: `docs/nba_api/stats/endpoints_output/leaguedashplayershotlocations_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import LeagueDashPlayerShotLocations
  endpoint = LeagueDashPlayerShotLocations()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `College` | `college_nullable` | no |
  | `Conference` | `conference_nullable` | no |
  | `Country` | `country_nullable` | no |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `DistanceRange` | `distance_range` | no |
  | `Division` | `division_simple_nullable` | no |
  | `DraftPick` | `draft_pick_nullable` | no |
  | `DraftYear` | `draft_year_nullable` | no |
  | `GameScope` | `game_scope_simple_nullable` | no |
  | `GameSegment` | `game_segment_nullable` | no |
  | `Height` | `height_nullable` | no |
  | `LastNGames` | `last_n_games` | no |
  | `LeagueID` | `league_id_nullable` | no |
  | `Location` | `location_nullable` | no |
  | `MeasureType` | `measure_type_simple` | no |
  | `Month` | `month` | no |
  | `OpponentTeamID` | `opponent_team_id` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `PORound` | `po_round_nullable` | no |
  | `PaceAdjust` | `pace_adjust` | no |
  | `PerMode` | `per_mode_detailed` | no |
  | `Period` | `period` | no |
  | `PlayerExperience` | `player_experience_nullable` | no |
  | `PlayerPosition` | `player_position_abbreviation_nullable` | no |
  | `PlusMinus` | `plus_minus` | no |
  | `Rank` | `rank` | no |
  | `Season` | `season` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_all_star` | no |
  | `ShotClockRange` | `shot_clock_range_nullable` | no |
  | `StarterBench` | `starter_bench_nullable` | no |
  | `TeamID` | `team_id_nullable` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |
  | `Weight` | `weight_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `ShotLocations`

  </details>

### LeagueDashPlayerStats

- HTTP: `GET https://stats.nba.com/stats/leaguedashplayerstats`
- Repo docs: `docs/nba_api/stats/endpoints/leaguedashplayerstats.md`
- Example output: `docs/nba_api/stats/endpoints_output/leaguedashplayerstats_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import LeagueDashPlayerStats
  endpoint = LeagueDashPlayerStats()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `College` | `college_nullable` | no |
  | `Conference` | `conference_nullable` | no |
  | `Country` | `country_nullable` | no |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `Division` | `division_simple_nullable` | no |
  | `DraftPick` | `draft_pick_nullable` | no |
  | `DraftYear` | `draft_year_nullable` | no |
  | `GameScope` | `game_scope_simple_nullable` | no |
  | `GameSegment` | `game_segment_nullable` | no |
  | `Height` | `height_nullable` | no |
  | `LastNGames` | `last_n_games` | no |
  | `LeagueID` | `league_id_nullable` | no |
  | `Location` | `location_nullable` | no |
  | `MeasureType` | `measure_type_detailed_defense` | no |
  | `Month` | `month` | no |
  | `OpponentTeamID` | `opponent_team_id` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `PORound` | `po_round_nullable` | no |
  | `PaceAdjust` | `pace_adjust` | no |
  | `PerMode` | `per_mode_detailed` | no |
  | `Period` | `period` | no |
  | `PlayerExperience` | `player_experience_nullable` | no |
  | `PlayerPosition` | `player_position_abbreviation_nullable` | no |
  | `PlusMinus` | `plus_minus` | no |
  | `Rank` | `rank` | no |
  | `Season` | `season` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_all_star` | no |
  | `ShotClockRange` | `shot_clock_range_nullable` | no |
  | `StarterBench` | `starter_bench_nullable` | no |
  | `TeamID` | `team_id_nullable` | no |
  | `TwoWay` | `two_way_nullable` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |
  | `Weight` | `weight_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `LeagueDashPlayerStats` (65): `PLAYER_ID`, `PLAYER_NAME`, `TEAM_ID`, `TEAM_ABBREVIATION`, `AGE`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `NBA_FANTASY_PTS`, `DD2`, `TD3`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `NBA_FANTASY_PTS_RANK`, `DD2_RANK`, `TD3_RANK`, `CFID`, `CFPARAMS`

  </details>

### LeagueDashPtDefend

- HTTP: `GET https://stats.nba.com/stats/leaguedashptdefend`
- Repo docs: `docs/nba_api/stats/endpoints/leaguedashptdefend.md`
- Example output: `docs/nba_api/stats/endpoints_output/leaguedashptdefend_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import LeagueDashPtDefend
  endpoint = LeagueDashPtDefend()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `College` | `college_nullable` | no |
  | `Conference` | `conference_nullable` | no |
  | `Country` | `country_nullable` | no |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `DefenseCategory` | `defense_category` | no |
  | `Division` | `division_nullable` | no |
  | `DraftPick` | `draft_pick_nullable` | no |
  | `DraftYear` | `draft_year_nullable` | no |
  | `GameSegment` | `game_segment_nullable` | no |
  | `Height` | `height_nullable` | no |
  | `LastNGames` | `last_n_games_nullable` | no |
  | `LeagueID` | `league_id` | no |
  | `Location` | `location_nullable` | no |
  | `Month` | `month_nullable` | no |
  | `OpponentTeamID` | `opponent_team_id_nullable` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `PORound` | `po_round_nullable` | no |
  | `PerMode` | `per_mode_simple` | no |
  | `Period` | `period_nullable` | no |
  | `PlayerExperience` | `player_experience_nullable` | no |
  | `PlayerID` | `player_id_nullable` | no |
  | `PlayerPosition` | `player_position_nullable` | no |
  | `Season` | `season` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_all_star` | no |
  | `StarterBench` | `starter_bench_nullable` | no |
  | `TeamID` | `team_id_nullable` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |
  | `Weight` | `weight_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `LeagueDashPTDefend` (14): `CLOSE_DEF_PERSON_ID`, `PLAYER_NAME`, `PLAYER_LAST_TEAM_ID`, `PLAYER_LAST_TEAM_ABBREVIATION`, `PLAYER_POSITION`, `AGE`, `GP`, `G`, `FREQ`, `D_FGM`, `D_FGA`, `D_FG_PCT`, `NORMAL_FG_PCT`, `PCT_PLUSMINUS`

  </details>

### LeagueDashPtStats

- HTTP: `GET https://stats.nba.com/stats/leaguedashptstats`
- Repo docs: `docs/nba_api/stats/endpoints/leaguedashptstats.md`
- Example output: `docs/nba_api/stats/endpoints_output/leaguedashptstats_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import LeagueDashPtStats
  endpoint = LeagueDashPtStats()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `College` | `college_nullable` | no |
  | `Conference` | `conference_nullable` | no |
  | `Country` | `country_nullable` | no |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `Division` | `division_simple_nullable` | no |
  | `DraftPick` | `draft_pick_nullable` | no |
  | `DraftYear` | `draft_year_nullable` | no |
  | `GameScope` | `game_scope_simple_nullable` | no |
  | `Height` | `height_nullable` | no |
  | `LastNGames` | `last_n_games` | no |
  | `LeagueID` | `league_id_nullable` | no |
  | `Location` | `location_nullable` | no |
  | `Month` | `month` | no |
  | `OpponentTeamID` | `opponent_team_id` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `PORound` | `po_round_nullable` | no |
  | `PerMode` | `per_mode_simple` | no |
  | `PlayerExperience` | `player_experience_nullable` | no |
  | `PlayerOrTeam` | `player_or_team` | no |
  | `PlayerPosition` | `player_position_abbreviation_nullable` | no |
  | `PtMeasureType` | `pt_measure_type` | no |
  | `Season` | `season` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_all_star` | no |
  | `StarterBench` | `starter_bench_nullable` | no |
  | `TeamID` | `team_id_nullable` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |
  | `Weight` | `weight_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `LeagueDashPtStats` (14): `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_NAME`, `GP`, `W`, `L`, `MIN`, `DIST_FEET`, `DIST_MILES`, `DIST_MILES_OFF`, `DIST_MILES_DEF`, `AVG_SPEED`, `AVG_SPEED_OFF`, `AVG_SPEED_DEF`

  </details>

### LeagueDashPtTeamDefend

- HTTP: `GET https://stats.nba.com/stats/leaguedashptteamdefend`
- Repo docs: `docs/nba_api/stats/endpoints/leaguedashptteamdefend.md`
- Example output: `docs/nba_api/stats/endpoints_output/leaguedashptteamdefend_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import LeagueDashPtTeamDefend
  endpoint = LeagueDashPtTeamDefend()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `Conference` | `conference_nullable` | no |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `DefenseCategory` | `defense_category` | no |
  | `Division` | `division_nullable` | no |
  | `GameSegment` | `game_segment_nullable` | no |
  | `LastNGames` | `last_n_games_nullable` | no |
  | `LeagueID` | `league_id` | no |
  | `Location` | `location_nullable` | no |
  | `Month` | `month_nullable` | no |
  | `OpponentTeamID` | `opponent_team_id_nullable` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `PORound` | `po_round_nullable` | no |
  | `PerMode` | `per_mode_simple` | no |
  | `Period` | `period_nullable` | no |
  | `Season` | `season` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_all_star` | no |
  | `TeamID` | `team_id_nullable` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `LeagueDashPtTeamDefend` (11): `TEAM_ID`, `TEAM_NAME`, `TEAM_ABBREVIATION`, `GP`, `G`, `FREQ`, `D_FGM`, `D_FGA`, `D_FG_PCT`, `NORMAL_FG_PCT`, `PCT_PLUSMINUS`

  </details>

### LeagueDashTeamClutch

- HTTP: `GET https://stats.nba.com/stats/leaguedashteamclutch`
- Repo docs: `docs/nba_api/stats/endpoints/leaguedashteamclutch.md`
- Example output: `docs/nba_api/stats/endpoints_output/leaguedashteamclutch_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import LeagueDashTeamClutch
  endpoint = LeagueDashTeamClutch()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `AheadBehind` | `ahead_behind` | no |
  | `ClutchTime` | `clutch_time` | no |
  | `Conference` | `conference_nullable` | no |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `Division` | `division_simple_nullable` | no |
  | `GameScope` | `game_scope_simple_nullable` | no |
  | `GameSegment` | `game_segment_nullable` | no |
  | `LastNGames` | `last_n_games` | no |
  | `LeagueID` | `league_id_nullable` | no |
  | `Location` | `location_nullable` | no |
  | `MeasureType` | `measure_type_detailed_defense` | no |
  | `Month` | `month` | no |
  | `OpponentTeamID` | `opponent_team_id` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `PORound` | `po_round_nullable` | no |
  | `PaceAdjust` | `pace_adjust` | no |
  | `PerMode` | `per_mode_detailed` | no |
  | `Period` | `period` | no |
  | `PlayerExperience` | `player_experience_nullable` | no |
  | `PlayerPosition` | `player_position_abbreviation_nullable` | no |
  | `PlusMinus` | `plus_minus` | no |
  | `PointDiff` | `point_diff` | no |
  | `Rank` | `rank` | no |
  | `Season` | `season` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_all_star` | no |
  | `ShotClockRange` | `shot_clock_range_nullable` | no |
  | `StarterBench` | `starter_bench_nullable` | no |
  | `TeamID` | `team_id_nullable` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `LeagueDashTeamClutch` (56): `TEAM_ID`, `TEAM_NAME`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `CFID`, `CFPARAMS`

  </details>

### LeagueDashTeamPtShot

- HTTP: `GET https://stats.nba.com/stats/leaguedashteamptshot`
- Repo docs: `docs/nba_api/stats/endpoints/leaguedashteamptshot.md`
- Example output: `docs/nba_api/stats/endpoints_output/leaguedashteamptshot_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import LeagueDashTeamPtShot
  endpoint = LeagueDashTeamPtShot()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `CloseDefDistRange` | `close_def_dist_range_nullable` | no |
  | `Conference` | `conference_nullable` | no |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `Division` | `division_nullable` | no |
  | `DribbleRange` | `dribble_range_nullable` | no |
  | `GameSegment` | `game_segment_nullable` | no |
  | `GeneralRange` | `general_range_nullable` | no |
  | `LastNGames` | `last_n_games_nullable` | no |
  | `LeagueID` | `league_id` | no |
  | `Location` | `location_nullable` | no |
  | `Month` | `month_nullable` | no |
  | `OpponentTeamID` | `opponent_team_id_nullable` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `PORound` | `po_round_nullable` | no |
  | `PerMode` | `per_mode_simple` | no |
  | `Period` | `period_nullable` | no |
  | `Season` | `season` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_all_star` | no |
  | `ShotClockRange` | `shot_clock_range_nullable` | no |
  | `ShotDistRange` | `shot_dist_range_nullable` | no |
  | `TeamID` | `team_id_nullable` | no |
  | `TouchTimeRange` | `touch_time_range_nullable` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `LeagueDashPTShots` (18): `TEAM_ID`, `TEAM_NAME`, `TEAM_ABBREVIATION`, `GP`, `G`, `FGA_FREQUENCY`, `FGM`, `FGA`, `FG_PCT`, `EFG_PCT`, `FG2A_FREQUENCY`, `FG2M`, `FG2A`, `FG2_PCT`, `FG3A_FREQUENCY`, `FG3M`, `FG3A`, `FG3_PCT`

  </details>

### LeagueDashTeamShotLocations

- HTTP: `GET https://stats.nba.com/stats/leaguedashteamshotlocations`
- Repo docs: `docs/nba_api/stats/endpoints/leaguedashteamshotlocations.md`
- Example output: `docs/nba_api/stats/endpoints_output/leaguedashteamshotlocations_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import LeagueDashTeamShotLocations
  endpoint = LeagueDashTeamShotLocations()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `Conference` | `conference_nullable` | no |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `DistanceRange` | `distance_range` | no |
  | `Division` | `division_simple_nullable` | no |
  | `GameScope` | `game_scope_simple_nullable` | no |
  | `GameSegment` | `game_segment_nullable` | no |
  | `LastNGames` | `last_n_games` | no |
  | `LeagueID` | `league_id_nullable` | no |
  | `Location` | `location_nullable` | no |
  | `MeasureType` | `measure_type_simple` | no |
  | `Month` | `month` | no |
  | `OpponentTeamID` | `opponent_team_id` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `PORound` | `po_round_nullable` | no |
  | `PaceAdjust` | `pace_adjust` | no |
  | `PerMode` | `per_mode_detailed` | no |
  | `Period` | `period` | no |
  | `PlayerExperience` | `player_experience_nullable` | no |
  | `PlayerPosition` | `player_position_abbreviation_nullable` | no |
  | `PlusMinus` | `plus_minus` | no |
  | `Rank` | `rank` | no |
  | `Season` | `season` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_all_star` | no |
  | `ShotClockRange` | `shot_clock_range_nullable` | no |
  | `StarterBench` | `starter_bench_nullable` | no |
  | `TeamID` | `team_id_nullable` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `ShotLocations`

  </details>

### LeagueDashTeamStats

- HTTP: `GET https://stats.nba.com/stats/leaguedashteamstats`
- Repo docs: `docs/nba_api/stats/endpoints/leaguedashteamstats.md`
- Example output: `docs/nba_api/stats/endpoints_output/leaguedashteamstats_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import LeagueDashTeamStats
  endpoint = LeagueDashTeamStats()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `Conference` | `conference_nullable` | no |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `Division` | `division_simple_nullable` | no |
  | `GameScope` | `game_scope_simple_nullable` | no |
  | `GameSegment` | `game_segment_nullable` | no |
  | `LastNGames` | `last_n_games` | no |
  | `LeagueID` | `league_id_nullable` | no |
  | `Location` | `location_nullable` | no |
  | `MeasureType` | `measure_type_detailed_defense` | no |
  | `Month` | `month` | no |
  | `OpponentTeamID` | `opponent_team_id` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `PORound` | `po_round_nullable` | no |
  | `PaceAdjust` | `pace_adjust` | no |
  | `PerMode` | `per_mode_detailed` | no |
  | `Period` | `period` | no |
  | `PlayerExperience` | `player_experience_nullable` | no |
  | `PlayerPosition` | `player_position_abbreviation_nullable` | no |
  | `PlusMinus` | `plus_minus` | no |
  | `Rank` | `rank` | no |
  | `Season` | `season` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_all_star` | no |
  | `ShotClockRange` | `shot_clock_range_nullable` | no |
  | `StarterBench` | `starter_bench_nullable` | no |
  | `TeamID` | `team_id_nullable` | no |
  | `TwoWay` | `two_way_nullable` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `LeagueDashTeamStats` (56): `TEAM_ID`, `TEAM_NAME`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `CFID`, `CFPARAMS`

  </details>

### LeagueGameFinder

- HTTP: `GET https://stats.nba.com/stats/leaguegamefinder`
- Repo docs: `docs/nba_api/stats/endpoints/leaguegamefinder.md`
- Example output: `docs/nba_api/stats/endpoints_output/leaguegamefinder_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import LeagueGameFinder
  endpoint = LeagueGameFinder()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `Conference` | `conference_nullable` | no |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `Division` | `division_simple_nullable` | no |
  | `DraftNumber` | `draft_number_nullable` | no |
  | `DraftRound` | `draft_round_nullable` | no |
  | `DraftTeamID` | `draft_team_id_nullable` | no |
  | `DraftYear` | `draft_year_nullable` | no |
  | `EqAST` | `eq_ast_nullable` | no |
  | `EqBLK` | `eq_blk_nullable` | no |
  | `EqDD` | `eq_dd_nullable` | no |
  | `EqDREB` | `eq_dreb_nullable` | no |
  | `EqFG3A` | `eq_fg3a_nullable` | no |
  | `EqFG3M` | `eq_fg3m_nullable` | no |
  | `EqFG3_PCT` | `eq_fg3_pct_nullable` | no |
  | `EqFGA` | `eq_fga_nullable` | no |
  | `EqFGM` | `eq_fgm_nullable` | no |
  | `EqFG_PCT` | `eq_fg_pct_nullable` | no |
  | `EqFTA` | `eq_fta_nullable` | no |
  | `EqFTM` | `eq_ftm_nullable` | no |
  | `EqFT_PCT` | `eq_ft_pct_nullable` | no |
  | `EqMINUTES` | `eq_minutes_nullable` | no |
  | `EqOREB` | `eq_oreb_nullable` | no |
  | `EqPF` | `eq_pf_nullable` | no |
  | `EqPTS` | `eq_pts_nullable` | no |
  | `EqREB` | `eq_reb_nullable` | no |
  | `EqSTL` | `eq_stl_nullable` | no |
  | `EqTD` | `eq_td_nullable` | no |
  | `EqTOV` | `eq_tov_nullable` | no |
  | `GameID` | `game_id_nullable` | no |
  | `GtAST` | `gt_ast_nullable` | no |
  | `GtBLK` | `gt_blk_nullable` | no |
  | `GtDD` | `gt_dd_nullable` | no |
  | `GtDREB` | `gt_dreb_nullable` | no |
  | `GtFG3A` | `gt_fg3a_nullable` | no |
  | `GtFG3M` | `gt_fg3m_nullable` | no |
  | `GtFG3_PCT` | `gt_fg3_pct_nullable` | no |
  | `GtFGA` | `gt_fga_nullable` | no |
  | `GtFGM` | `gt_fgm_nullable` | no |
  | `GtFG_PCT` | `gt_fg_pct_nullable` | no |
  | `GtFTA` | `gt_fta_nullable` | no |
  | `GtFTM` | `gt_ftm_nullable` | no |
  | `GtFT_PCT` | `gt_ft_pct_nullable` | no |
  | `GtMINUTES` | `gt_minutes_nullable` | no |
  | `GtOREB` | `gt_oreb_nullable` | no |
  | `GtPF` | `gt_pf_nullable` | no |
  | `GtPTS` | `gt_pts_nullable` | no |
  | `GtREB` | `gt_reb_nullable` | no |
  | `GtSTL` | `gt_stl_nullable` | no |
  | `GtTD` | `gt_td_nullable` | no |
  | `GtTOV` | `gt_tov_nullable` | no |
  | `LeagueID` | `league_id_nullable` | no |
  | `Location` | `location_nullable` | no |
  | `LtAST` | `lt_ast_nullable` | no |
  | `LtBLK` | `lt_blk_nullable` | no |
  | `LtDD` | `lt_dd_nullable` | no |
  | `LtDREB` | `lt_dreb_nullable` | no |
  | `LtFG3A` | `lt_fg3a_nullable` | no |
  | `LtFG3M` | `lt_fg3m_nullable` | no |
  | `LtFG3_PCT` | `lt_fg3_pct_nullable` | no |
  | `LtFGA` | `lt_fga_nullable` | no |
  | `LtFGM` | `lt_fgm_nullable` | no |
  | `LtFG_PCT` | `lt_fg_pct_nullable` | no |
  | `LtFTA` | `lt_fta_nullable` | no |
  | `LtFTM` | `lt_ftm_nullable` | no |
  | `LtFT_PCT` | `lt_ft_pct_nullable` | no |
  | `LtMINUTES` | `lt_minutes_nullable` | no |
  | `LtOREB` | `lt_oreb_nullable` | no |
  | `LtPF` | `lt_pf_nullable` | no |
  | `LtPTS` | `lt_pts_nullable` | no |
  | `LtREB` | `lt_reb_nullable` | no |
  | `LtSTL` | `lt_stl_nullable` | no |
  | `LtTD` | `lt_td_nullable` | no |
  | `LtTOV` | `lt_tov_nullable` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `PORound` | `po_round_nullable` | no |
  | `PlayerID` | `player_id_nullable` | no |
  | `PlayerOrTeam` | `player_or_team_abbreviation` | no |
  | `RookieYear` | `rookie_year_nullable` | no |
  | `Season` | `season_nullable` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_nullable` | no |
  | `StarterBench` | `starter_bench_nullable` | no |
  | `TeamID` | `team_id_nullable` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |
  | `VsTeamID` | `vs_team_id_nullable` | no |
  | `YearsExperience` | `years_experience_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `LeagueGameFinderResults` (28): `SEASON_ID`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_NAME`, `GAME_ID`, `GAME_DATE`, `MATCHUP`, `WL`, `MIN`, `PTS`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `STL`, `BLK`, `TOV`, `PF`, `PLUS_MINUS`

  </details>

### LeagueGameLog

- HTTP: `GET https://stats.nba.com/stats/leaguegamelog`
- Repo docs: `docs/nba_api/stats/endpoints/leaguegamelog.md`
- Example output: `docs/nba_api/stats/endpoints_output/leaguegamelog_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import LeagueGameLog
  endpoint = LeagueGameLog()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `Counter` | `counter` | no |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `Direction` | `direction` | no |
  | `LeagueID` | `league_id` | no |
  | `PlayerOrTeam` | `player_or_team_abbreviation` | no |
  | `Season` | `season` | no |
  | `SeasonType` | `season_type_all_star` | no |
  | `Sorter` | `sorter` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `LeagueGameLog` (29): `SEASON_ID`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_NAME`, `GAME_ID`, `GAME_DATE`, `MATCHUP`, `WL`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `STL`, `BLK`, `TOV`, `PF`, `PTS`, `PLUS_MINUS`, `VIDEO_AVAILABLE`

  </details>

### LeagueHustleStatsPlayer

- HTTP: `GET https://stats.nba.com/stats/leaguehustlestatsplayer`
- Repo docs: `docs/nba_api/stats/endpoints/leaguehustlestatsplayer.md`
- Example output: `docs/nba_api/stats/endpoints_output/leaguehustlestatsplayer_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import LeagueHustleStatsPlayer
  endpoint = LeagueHustleStatsPlayer()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `College` | `college_nullable` | no |
  | `Conference` | `conference_nullable` | no |
  | `Country` | `country_nullable` | no |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `Division` | `division_simple_nullable` | no |
  | `DraftPick` | `draft_pick_nullable` | no |
  | `DraftYear` | `draft_year_nullable` | no |
  | `Height` | `height_nullable` | no |
  | `LeagueID` | `league_id_nullable` | no |
  | `Location` | `location_nullable` | no |
  | `Month` | `month_nullable` | no |
  | `OpponentTeamID` | `opponent_team_id_nullable` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `PORound` | `po_round_nullable` | no |
  | `PerMode` | `per_mode_time` | no |
  | `PlayerExperience` | `player_experience_nullable` | no |
  | `PlayerPosition` | `player_position_nullable` | no |
  | `Season` | `season` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_all_star` | no |
  | `TeamID` | `team_id_nullable` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |
  | `Weight` | `weight_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `HustleStatsPlayer` (28): `PLAYER_ID`, `PLAYER_NAME`, `TEAM_ID`, `TEAM_ABBREVIATION`, `AGE`, `G`, `MIN`, `CONTESTED_SHOTS`, `CONTESTED_SHOTS_2PT`, `CONTESTED_SHOTS_3PT`, `DEFLECTIONS`, `CHARGES_DRAWN`, `SCREEN_ASSISTS`, `SCREEN_AST_PTS`, `OFF_LOOSE_BALLS_RECOVERED`, `DEF_LOOSE_BALLS_RECOVERED`, `LOOSE_BALLS_RECOVERED`, `PCT_LOOSE_BALLS_RECOVERED_OFF`, `PCT_LOOSE_BALLS_RECOVERED_DEF`, `OFF_BOXOUTS`, `DEF_BOXOUTS`, `BOX_OUT_PLAYER_TEAM_REBS`, `BOX_OUT_PLAYER_REBS`, `BOX_OUTS`, `PCT_BOX_OUTS_OFF`, `PCT_BOX_OUTS_DEF`, `PCT_BOX_OUTS_TEAM_REB`, `PCT_BOX_OUTS_REB`

  </details>

### LeagueHustleStatsTeam

- HTTP: `GET https://stats.nba.com/stats/leaguehustlestatsteam`
- Repo docs: `docs/nba_api/stats/endpoints/leaguehustlestatsteam.md`
- Example output: `docs/nba_api/stats/endpoints_output/leaguehustlestatsteam_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import LeagueHustleStatsTeam
  endpoint = LeagueHustleStatsTeam()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `College` | `college_nullable` | no |
  | `Conference` | `conference_nullable` | no |
  | `Country` | `country_nullable` | no |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `Division` | `division_simple_nullable` | no |
  | `DraftPick` | `draft_pick_nullable` | no |
  | `DraftYear` | `draft_year_nullable` | no |
  | `Height` | `height_nullable` | no |
  | `LeagueID` | `league_id_nullable` | no |
  | `Location` | `location_nullable` | no |
  | `Month` | `month_nullable` | no |
  | `OpponentTeamID` | `opponent_team_id_nullable` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `PORound` | `po_round_nullable` | no |
  | `PerMode` | `per_mode_time` | no |
  | `PlayerExperience` | `player_experience_nullable` | no |
  | `PlayerPosition` | `player_position_nullable` | no |
  | `Season` | `season` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_all_star` | no |
  | `TeamID` | `team_id_nullable` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |
  | `Weight` | `weight_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `HustleStatsTeam` (20): `TEAM_ID`, `TEAM_NAME`, `MIN`, `CONTESTED_SHOTS`, `CONTESTED_SHOTS_2PT`, `CONTESTED_SHOTS_3PT`, `DEFLECTIONS`, `CHARGES_DRAWN`, `SCREEN_ASSISTS`, `SCREEN_AST_PTS`, `OFF_LOOSE_BALLS_RECOVERED`, `DEF_LOOSE_BALLS_RECOVERED`, `LOOSE_BALLS_RECOVERED`, `PCT_LOOSE_BALLS_RECOVERED_OFF`, `PCT_LOOSE_BALLS_RECOVERED_DEF`, `OFF_BOXOUTS`, `DEF_BOXOUTS`, `BOX_OUTS`, `PCT_BOX_OUTS_OFF`, `PCT_BOX_OUTS_DEF`

  </details>

### LeagueLeaders

- HTTP: `GET https://stats.nba.com/stats/leagueleaders`
- Repo docs: `docs/nba_api/stats/endpoints/leagueleaders.md`
- Example output: `docs/nba_api/stats/endpoints_output/leagueleaders_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import LeagueLeaders
  endpoint = LeagueLeaders()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `ActiveFlag` | `active_flag_nullable` | no |
  | `LeagueID` | `league_id` | no |
  | `PerMode` | `per_mode48` | no |
  | `Scope` | `scope` | no |
  | `Season` | `season` | no |
  | `SeasonType` | `season_type_all_star` | no |
  | `StatCategory` | `stat_category_abbreviation` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `LeagueLeaders` (27): `PLAYER_ID`, `RANK`, `PLAYER`, `TEAM`, `GP`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `STL`, `BLK`, `TOV`, `PF`, `PTS`, `EFF`, `AST_TOV`, `STL_TOV`

  </details>

### LeagueLineupViz

- HTTP: `GET https://stats.nba.com/stats/leaguelineupviz`
- Repo docs: `docs/nba_api/stats/endpoints/leaguelineupviz.md`
- Required python args: `minutes_min`
- Python:
  ```python
  from nba_api.stats.endpoints import LeagueLineupViz
  endpoint = LeagueLineupViz(minutes_min='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `MinutesMin` | `minutes_min` | yes |
  | `Conference` | `conference_nullable` | no |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `Division` | `division_simple_nullable` | no |
  | `GameSegment` | `game_segment_nullable` | no |
  | `GroupQuantity` | `group_quantity` | no |
  | `LastNGames` | `last_n_games` | no |
  | `LeagueID` | `league_id_nullable` | no |
  | `Location` | `location_nullable` | no |
  | `MeasureType` | `measure_type_detailed_defense` | no |
  | `Month` | `month` | no |
  | `OpponentTeamID` | `opponent_team_id` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `PORound` | `po_round_nullable` | no |
  | `PaceAdjust` | `pace_adjust` | no |
  | `PerMode` | `per_mode_detailed` | no |
  | `Period` | `period` | no |
  | `PlusMinus` | `plus_minus` | no |
  | `Rank` | `rank` | no |
  | `Season` | `season` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_all_star` | no |
  | `ShotClockRange` | `shot_clock_range_nullable` | no |
  | `TeamID` | `team_id_nullable` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `LeagueLineupViz` (24): `GROUP_ID`, `GROUP_NAME`, `TEAM_ID`, `TEAM_ABBREVIATION`, `MIN`, `OFF_RATING`, `DEF_RATING`, `NET_RATING`, `PACE`, `TS_PCT`, `FTA_RATE`, `TM_AST_PCT`, `PCT_FGA_2PT`, `PCT_FGA_3PT`, `PCT_PTS_2PT_MR`, `PCT_PTS_FB`, `PCT_PTS_FT`, `PCT_PTS_PAINT`, `PCT_AST_FGM`, `PCT_UAST_FGM`, `OPP_FG3_PCT`, `OPP_EFG_PCT`, `OPP_FTA_RATE`, `OPP_TOV_PCT`

  </details>

### LeaguePlayerOnDetails

- HTTP: `GET https://stats.nba.com/stats/leagueplayerondetails`
- Repo docs: `docs/nba_api/stats/endpoints/leagueplayerondetails.md`
- Example output: `docs/nba_api/stats/endpoints_output/leagueplayerondetails_output.md`
- Required python args: `team_id`
- Python:
  ```python
  from nba_api.stats.endpoints import LeaguePlayerOnDetails
  endpoint = LeaguePlayerOnDetails(team_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `TeamID` | `team_id` | yes |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `GameSegment` | `game_segment_nullable` | no |
  | `LastNGames` | `last_n_games` | no |
  | `LeagueID` | `league_id_nullable` | no |
  | `Location` | `location_nullable` | no |
  | `MeasureType` | `measure_type_detailed_defense` | no |
  | `Month` | `month` | no |
  | `OpponentTeamID` | `opponent_team_id` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `PaceAdjust` | `pace_adjust` | no |
  | `PerMode` | `per_mode_detailed` | no |
  | `Period` | `period` | no |
  | `PlusMinus` | `plus_minus` | no |
  | `Rank` | `rank` | no |
  | `Season` | `season` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_all_star` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `PlayersOnCourtLeaguePlayerDetails` (59): `GROUP_SET`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_NAME`, `VS_PLAYER_ID`, `VS_PLAYER_NAME`, `COURT_STATUS`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`

  </details>

### LeagueSeasonMatchups

- HTTP: `GET https://stats.nba.com/stats/leagueseasonmatchups`
- Repo docs: `docs/nba_api/stats/endpoints/leagueseasonmatchups.md`
- Example output: `docs/nba_api/stats/endpoints_output/leagueseasonmatchups_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import LeagueSeasonMatchups
  endpoint = LeagueSeasonMatchups()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `DefPlayerID` | `def_player_id_nullable` | no |
  | `DefTeamID` | `def_team_id_nullable` | no |
  | `LeagueID` | `league_id` | no |
  | `OffPlayerID` | `off_player_id_nullable` | no |
  | `OffTeamID` | `off_team_id_nullable` | no |
  | `PerMode` | `per_mode_simple` | no |
  | `Season` | `season` | no |
  | `SeasonType` | `season_type_playoffs` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `SeasonMatchups` (26): `SEASON_ID`, `OFF_PLAYER_ID`, `OFF_PLAYER_NAME`, `DEF_PLAYER_ID`, `DEF_PLAYER_NAME`, `GP`, `MATCHUP_MIN`, `PARTIAL_POSS`, `PLAYER_PTS`, `TEAM_PTS`, `MATCHUP_AST`, `MATCHUP_TOV`, `MATCHUP_BLK`, `MATCHUP_FGM`, `MATCHUP_FGA`, `MATCHUP_FG_PCT`, `MATCHUP_FG3M`, `MATCHUP_FG3A`, `MATCHUP_FG3_PCT`, `HELP_BLK`, `HELP_FGM`, `HELP_FGA`, `HELP_FG_PERC`, `MATCHUP_FTM`, `MATCHUP_FTA`, `SFL`

  </details>

### LeagueStandings

- HTTP: `GET https://stats.nba.com/stats/leaguestandings`
- Repo docs: `docs/nba_api/stats/endpoints/leaguestandings.md`
- Example output: `docs/nba_api/stats/endpoints_output/leaguestandings_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import LeagueStandings
  endpoint = LeagueStandings()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `LeagueID` | `league_id` | no |
  | `Season` | `season` | no |
  | `SeasonType` | `season_type` | no |
  | `SeasonYear` | `season_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `Standings` (81): `LeagueID`, `SeasonID`, `TeamID`, `TeamCity`, `TeamName`, `Conference`, `ConferenceRecord`, `PlayoffRank`, `ClinchIndicator`, `Division`, `DivisionRecord`, `DivisionRank`, `WINS`, `LOSSES`, `WinPCT`, `LeagueRank`, `Record`, `HOME`, `ROAD`, `L10`, `Last10Home`, `Last10Road`, `OT`, `ThreePTSOrLess`, `TenPTSOrMore`, `LongHomeStreak`, `strLongHomeStreak`, `LongRoadStreak`, `strLongRoadStreak`, `LongWinStreak`, `LongLossStreak`, `CurrentHomeStreak`, `strCurrentHomeStreak`, `CurrentRoadStreak`, `strCurrentRoadStreak`, `CurrentStreak`, `strCurrentStreak`, `ConferenceGamesBack`, `DivisionGamesBack`, `ClinchedConferenceTitle`, `ClinchedDivisionTitle`, `ClinchedPlayoffBirth`, `EliminatedConference`, `EliminatedDivision`, `AheadAtHalf`, `BehindAtHalf`, `TiedAtHalf`, `AheadAtThird`, `BehindAtThird`, `TiedAtThird`, `Score100PTS`, `OppScore100PTS`, `OppOver500`, `LeadInFGPCT`, `LeadInReb`, `FewerTurnovers`, `PointsPG`, `OppPointsPG`, `DiffPointsPG`, `vsEast`, `vsAtlantic`, `vsCentral`, `vsSoutheast`, `vsWest`, `vsNorthwest`, `vsPacific`, `vsSouthwest`, `Jan`, `Feb`, `Mar`, `Apr`, `May`, `Jun`, `Jul`, `Aug`, `Sep`, `Oct`, `Nov`, `Dec`, `PreAS`, `PostAS`

  </details>

### LeagueStandingsV3

- HTTP: `GET https://stats.nba.com/stats/leaguestandingsv3`
- Repo docs: `docs/nba_api/stats/endpoints/leaguestandingsv3.md`
- Example output: `docs/nba_api/stats/endpoints_output/leaguestandingsv3_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import LeagueStandingsV3
  endpoint = LeagueStandingsV3()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `LeagueID` | `league_id` | no |
  | `Season` | `season` | no |
  | `SeasonType` | `season_type` | no |
  | `SeasonYear` | `season_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `Standings` (115): `LeagueID`, `SeasonID`, `TeamID`, `TeamCity`, `TeamName`, `TeamSlug`, `Conference`, `ConferenceRecord`, `PlayoffRank`, `ClinchIndicator`, `Division`, `DivisionRecord`, `DivisionRank`, `WINS`, `LOSSES`, `WinPCT`, `LeagueRank`, `Record`, `HOME`, `ROAD`, `L10`, `Last10Home`, `Last10Road`, `OT`, `ThreePTSOrLess`, `TenPTSOrMore`, `LongHomeStreak`, `strLongHomeStreak`, `LongRoadStreak`, `strLongRoadStreak`, `LongWinStreak`, `LongLossStreak`, `CurrentHomeStreak`, `strCurrentHomeStreak`, `CurrentRoadStreak`, `strCurrentRoadStreak`, `CurrentStreak`, `strCurrentStreak`, `ConferenceGamesBack`, `DivisionGamesBack`, `ClinchedConferenceTitle`, `ClinchedDivisionTitle`, `ClinchedPlayoffBirth`, `EliminatedConference`, `EliminatedDivision`, `AheadAtHalf`, `BehindAtHalf`, `TiedAtHalf`, `AheadAtThird`, `BehindAtThird`, `TiedAtThird`, `Score100PTS`, `OppScore100PTS`, `OppOver500`, `LeadInFGPCT`, `LeadInReb`, `FewerTurnovers`, `PointsPG`, `OppPointsPG`, `DiffPointsPG`, `vsEast`, `vsAtlantic`, `vsCentral`, `vsSoutheast`, `vsWest`, `vsNorthwest`, `vsPacific`, `vsSouthwest`, `Jan`, `Feb`, `Mar`, `Apr`, `May`, `Jun`, `Jul`, `Aug`, `Sep`, `Oct`, `Nov`, `Dec`, `ReturnToPlay_East_PI_Flag`, `ReturnToPlay_West_PI_Flag`, `ReturnToPlay_Already_Eliminated`, `Seeding_Game_1_Outcome`, `Seeding_Game_2_Outcome`, `Seeding_Game_3_Outcome`, `Seeding_Game_4_Outcome`, `Seeding_Game_5_Outcome`, `Seeding_Game_6_Outcome`, `Seeding_Game_7_Outcome`, `Seeding_Game_8_Outcome`, `Seeding_Game_1_ID`, `Seeding_Game_2_ID`, `Seeding_Game_3_ID`, `Seeding_Game_4_ID`, `Seeding_Game_5_ID`, `Seeding_Game_6_ID`, `Seeding_Game_7_ID`, `Seeding_Game_8_ID`, `Seeding_Game_1_Opponent`, `Seeding_Game_2_Opponent`, `Seeding_Game_3_Opponent`, `Seeding_Game_4_Opponent`, `Seeding_Game_5_Opponent`, `Seeding_Game_6_Opponent`, `Seeding_Game_7_Opponent`, `Seeding_Game_8_Opponent`, `Seeding_Game_1_Label`, `Seeding_Game_2_Label`, `Seeding_Game_3_Label`, `Seeding_Game_4_Label`, `Seeding_Game_5_Label`, `Seeding_Game_6_Label`, `Seeding_Game_7_Label`, `Seeding_Game_8_Label`

  </details>

### MatchupsRollup

- HTTP: `GET https://stats.nba.com/stats/matchupsrollup`
- Repo docs: `docs/nba_api/stats/endpoints/matchupsrollup.md`
- Example output: `docs/nba_api/stats/endpoints_output/matchupsrollup_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import MatchupsRollup
  endpoint = MatchupsRollup()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `DefPlayerID` | `def_player_id_nullable` | no |
  | `DefTeamID` | `def_team_id_nullable` | no |
  | `LeagueID` | `league_id` | no |
  | `OffPlayerID` | `off_player_id_nullable` | no |
  | `OffTeamID` | `off_team_id_nullable` | no |
  | `PerMode` | `per_mode_simple` | no |
  | `Season` | `season` | no |
  | `SeasonType` | `season_type_playoffs` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `MatchupsRollup` (22): `SEASON_ID`, `POSITION`, `PERCENT_OF_TIME`, `DEF_PLAYER_ID`, `DEF_PLAYER_NAME`, `GP`, `MATCHUP_MIN`, `PARTIAL_POSS`, `PLAYER_PTS`, `TEAM_PTS`, `MATCHUP_AST`, `MATCHUP_TOV`, `MATCHUP_BLK`, `MATCHUP_FGM`, `MATCHUP_FGA`, `MATCHUP_FG_PCT`, `MATCHUP_FG3M`, `MATCHUP_FG3A`, `MATCHUP_FG3_PCT`, `MATCHUP_FTM`, `MATCHUP_FTA`, `SFL`

  </details>

### PlayByPlay

- HTTP: `GET https://stats.nba.com/stats/playbyplay`
- Repo docs: `docs/nba_api/stats/endpoints/playbyplay.md`
- Example output: `docs/nba_api/stats/endpoints_output/playbyplay_output.md`
- Required python args: `game_id`
- Python:
  ```python
  from nba_api.stats.endpoints import PlayByPlay
  endpoint = PlayByPlay(game_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `GameID` | `game_id` | yes |
  | `EndPeriod` | `end_period` | no |
  | `StartPeriod` | `start_period` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `AvailableVideo` (1): `VIDEO_AVAILABLE_FLAG`
  - `PlayByPlay` (12): `GAME_ID`, `EVENTNUM`, `EVENTMSGTYPE`, `EVENTMSGACTIONTYPE`, `PERIOD`, `WCTIMESTRING`, `PCTIMESTRING`, `HOMEDESCRIPTION`, `NEUTRALDESCRIPTION`, `VISITORDESCRIPTION`, `SCORE`, `SCOREMARGIN`

  </details>

### PlayByPlayV2

- HTTP: `GET https://stats.nba.com/stats/playbyplayv2`
- Repo docs: `docs/nba_api/stats/endpoints/playbyplayv2.md`
- Example output: `docs/nba_api/stats/endpoints_output/playbyplayv2_output.md`
- Required python args: `game_id`
- Python:
  ```python
  from nba_api.stats.endpoints import PlayByPlayV2
  endpoint = PlayByPlayV2(game_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `GameID` | `game_id` | yes |
  | `EndPeriod` | `end_period` | no |
  | `StartPeriod` | `start_period` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `AvailableVideo` (1): `VIDEO_AVAILABLE_FLAG`
  - `PlayByPlay` (34): `GAME_ID`, `EVENTNUM`, `EVENTMSGTYPE`, `EVENTMSGACTIONTYPE`, `PERIOD`, `WCTIMESTRING`, `PCTIMESTRING`, `HOMEDESCRIPTION`, `NEUTRALDESCRIPTION`, `VISITORDESCRIPTION`, `SCORE`, `SCOREMARGIN`, `PERSON1TYPE`, `PLAYER1_ID`, `PLAYER1_NAME`, `PLAYER1_TEAM_ID`, `PLAYER1_TEAM_CITY`, `PLAYER1_TEAM_NICKNAME`, `PLAYER1_TEAM_ABBREVIATION`, `PERSON2TYPE`, `PLAYER2_ID`, `PLAYER2_NAME`, `PLAYER2_TEAM_ID`, `PLAYER2_TEAM_CITY`, `PLAYER2_TEAM_NICKNAME`, `PLAYER2_TEAM_ABBREVIATION`, `PERSON3TYPE`, `PLAYER3_ID`, `PLAYER3_NAME`, `PLAYER3_TEAM_ID`, `PLAYER3_TEAM_CITY`, `PLAYER3_TEAM_NICKNAME`, `PLAYER3_TEAM_ABBREVIATION`, `VIDEO_AVAILABLE_FLAG`

  </details>

### PlayByPlayV3

- HTTP: `GET https://stats.nba.com/stats/playbyplayv3`
- Repo docs: `docs/nba_api/stats/endpoints/playbyplayv3.md`
- Example output: `docs/nba_api/stats/endpoints_output/playbyplayv3_output.md`
- Required python args: `game_id`
- Python:
  ```python
  from nba_api.stats.endpoints import PlayByPlayV3
  endpoint = PlayByPlayV3(game_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `GameID` | `game_id` | yes |
  | `EndPeriod` | `end_period` | no |
  | `StartPeriod` | `start_period` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `AvailableVideo` (1): `videoAvailable`
  - `PlayByPlay` (23): `gameId`, `actionNumber`, `clock`, `period`, `teamId`, `teamTricode`, `personId`, `playerName`, `playerNameI`, `xLegacy`, `yLegacy`, `shotDistance`, `shotResult`, `isFieldGoal`, `scoreHome`, `scoreAway`, `pointsTotal`, `location`, `description`, `actionType`, `subType`, `videoAvailable`, `actionId`

  </details>

### PlayerAwards

- HTTP: `GET https://stats.nba.com/stats/playerawards`
- Repo docs: `docs/nba_api/stats/endpoints/playerawards.md`
- Example output: `docs/nba_api/stats/endpoints_output/playerawards_output.md`
- Required python args: `player_id`
- Python:
  ```python
  from nba_api.stats.endpoints import PlayerAwards
  endpoint = PlayerAwards(player_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `PlayerID` | `player_id` | yes |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `PlayerAwards` (14): `PERSON_ID`, `FIRST_NAME`, `LAST_NAME`, `TEAM`, `DESCRIPTION`, `ALL_NBA_TEAM_NUMBER`, `SEASON`, `MONTH`, `WEEK`, `CONFERENCE`, `TYPE`, `SUBTYPE1`, `SUBTYPE2`, `SUBTYPE3`

  </details>

### PlayerCareerByCollege

- HTTP: `GET https://stats.nba.com/stats/playercareerbycollege`
- Repo docs: `docs/nba_api/stats/endpoints/playercareerbycollege.md`
- Example output: `docs/nba_api/stats/endpoints_output/playercareerbycollege_output.md`
- Required python args: `college`
- Python:
  ```python
  from nba_api.stats.endpoints import PlayerCareerByCollege
  endpoint = PlayerCareerByCollege(college='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `College` | `college` | yes |
  | `LeagueID` | `league_id` | no |
  | `PerMode` | `per_mode_simple` | no |
  | `Season` | `season_nullable` | no |
  | `SeasonType` | `season_type_all_star` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `PlayerCareerByCollege` (23): `PLAYER_ID`, `PLAYER_NAME`, `COLLEGE`, `GP`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `STL`, `BLK`, `TOV`, `PF`, `PTS`

  </details>

### PlayerCareerByCollegeRollup

- HTTP: `GET https://stats.nba.com/stats/playercareerbycollegerollup`
- Repo docs: `docs/nba_api/stats/endpoints/playercareerbycollegerollup.md`
- Example output: `docs/nba_api/stats/endpoints_output/playercareerbycollegerollup_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import PlayerCareerByCollegeRollup
  endpoint = PlayerCareerByCollegeRollup()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `LeagueID` | `league_id` | no |
  | `PerMode` | `per_mode_simple` | no |
  | `Season` | `season_nullable` | no |
  | `SeasonType` | `season_type_all_star` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `East` (24): `REGION`, `SEED`, `COLLEGE`, `PLAYERS`, `GP`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `STL`, `BLK`, `TOV`, `PF`, `PTS`
  - `Midwest` (24): `REGION`, `SEED`, `COLLEGE`, `PLAYERS`, `GP`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `STL`, `BLK`, `TOV`, `PF`, `PTS`
  - `South` (24): `REGION`, `SEED`, `COLLEGE`, `PLAYERS`, `GP`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `STL`, `BLK`, `TOV`, `PF`, `PTS`
  - `West` (24): `REGION`, `SEED`, `COLLEGE`, `PLAYERS`, `GP`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `STL`, `BLK`, `TOV`, `PF`, `PTS`

  </details>

### PlayerCareerStats

- HTTP: `GET https://stats.nba.com/stats/playercareerstats`
- Repo docs: `docs/nba_api/stats/endpoints/playercareerstats.md`
- Example output: `docs/nba_api/stats/endpoints_output/playercareerstats_output.md`
- Required python args: `player_id`
- Python:
  ```python
  from nba_api.stats.endpoints import PlayerCareerStats
  endpoint = PlayerCareerStats(player_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `PlayerID` | `player_id` | yes |
  | `LeagueID` | `league_id_nullable` | no |
  | `PerMode` | `per_mode36` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `CareerTotalsAllStarSeason` (24): `PLAYER_ID`, `LEAGUE_ID`, `Team_ID`, `GP`, `GS`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `STL`, `BLK`, `TOV`, `PF`, `PTS`
  - `CareerTotalsCollegeSeason` (24): `PLAYER_ID`, `LEAGUE_ID`, `ORGANIZATION_ID`, `GP`, `GS`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `STL`, `BLK`, `TOV`, `PF`, `PTS`
  - `CareerTotalsPostSeason` (24): `PLAYER_ID`, `LEAGUE_ID`, `Team_ID`, `GP`, `GS`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `STL`, `BLK`, `TOV`, `PF`, `PTS`
  - `CareerTotalsRegularSeason` (24): `PLAYER_ID`, `LEAGUE_ID`, `Team_ID`, `GP`, `GS`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `STL`, `BLK`, `TOV`, `PF`, `PTS`
  - `SeasonRankingsPostSeason` (27): `PLAYER_ID`, `SEASON_ID`, `LEAGUE_ID`, `TEAM_ID`, `TEAM_ABBREVIATION`, `PLAYER_AGE`, `GP`, `GS`, `RANK_MIN`, `RANK_FGM`, `RANK_FGA`, `RANK_FG_PCT`, `RANK_FG3M`, `RANK_FG3A`, `RANK_FG3_PCT`, `RANK_FTM`, `RANK_FTA`, `RANK_FT_PCT`, `RANK_OREB`, `RANK_DREB`, `RANK_REB`, `RANK_AST`, `RANK_STL`, `RANK_BLK`, `RANK_TOV`, `RANK_PTS`, `RANK_EFF`
  - `SeasonRankingsRegularSeason` (27): `PLAYER_ID`, `SEASON_ID`, `LEAGUE_ID`, `TEAM_ID`, `TEAM_ABBREVIATION`, `PLAYER_AGE`, `GP`, `GS`, `RANK_MIN`, `RANK_FGM`, `RANK_FGA`, `RANK_FG_PCT`, `RANK_FG3M`, `RANK_FG3A`, `RANK_FG3_PCT`, `RANK_FTM`, `RANK_FTA`, `RANK_FT_PCT`, `RANK_OREB`, `RANK_DREB`, `RANK_REB`, `RANK_AST`, `RANK_STL`, `RANK_BLK`, `RANK_TOV`, `RANK_PTS`, `RANK_EFF`
  - `SeasonTotalsAllStarSeason` (27): `PLAYER_ID`, `SEASON_ID`, `LEAGUE_ID`, `TEAM_ID`, `TEAM_ABBREVIATION`, `PLAYER_AGE`, `GP`, `GS`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `STL`, `BLK`, `TOV`, `PF`, `PTS`
  - `SeasonTotalsCollegeSeason` (27): `PLAYER_ID`, `SEASON_ID`, `LEAGUE_ID`, `ORGANIZATION_ID`, `SCHOOL_NAME`, `PLAYER_AGE`, `GP`, `GS`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `STL`, `BLK`, `TOV`, `PF`, `PTS`
  - `SeasonTotalsPostSeason` (27): `PLAYER_ID`, `SEASON_ID`, `LEAGUE_ID`, `TEAM_ID`, `TEAM_ABBREVIATION`, `PLAYER_AGE`, `GP`, `GS`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `STL`, `BLK`, `TOV`, `PF`, `PTS`
  - `SeasonTotalsRegularSeason` (27): `PLAYER_ID`, `SEASON_ID`, `LEAGUE_ID`, `TEAM_ID`, `TEAM_ABBREVIATION`, `PLAYER_AGE`, `GP`, `GS`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `STL`, `BLK`, `TOV`, `PF`, `PTS`

  </details>

### PlayerCompare

- HTTP: `GET https://stats.nba.com/stats/playercompare`
- Repo docs: `docs/nba_api/stats/endpoints/playercompare.md`
- Required python args: `vs_player_id_list`, `player_id_list`
- Python:
  ```python
  from nba_api.stats.endpoints import PlayerCompare
  endpoint = PlayerCompare(vs_player_id_list='…', player_id_list='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `PlayerIDList` | `player_id_list` | yes |
  | `VsPlayerIDList` | `vs_player_id_list` | yes |
  | `Conference` | `conference_nullable` | no |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `Division` | `division_simple_nullable` | no |
  | `GameSegment` | `game_segment_nullable` | no |
  | `LastNGames` | `last_n_games` | no |
  | `LeagueID` | `league_id_nullable` | no |
  | `Location` | `location_nullable` | no |
  | `MeasureType` | `measure_type_detailed_defense` | no |
  | `Month` | `month` | no |
  | `OpponentTeamID` | `opponent_team_id` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `PaceAdjust` | `pace_adjust` | no |
  | `PerMode` | `per_mode_detailed` | no |
  | `Period` | `period` | no |
  | `PlusMinus` | `plus_minus` | no |
  | `Rank` | `rank` | no |
  | `Season` | `season` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_playoffs` | no |
  | `ShotClockRange` | `shot_clock_range_nullable` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `Individual` (24): `GROUP_SET`, `DESCRIPTION`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`
  - `OverallCompare` (24): `GROUP_SET`, `DESCRIPTION`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`

  </details>

### PlayerDashboardByClutch

- HTTP: `GET https://stats.nba.com/stats/playerdashboardbyclutch`
- Repo docs: `docs/nba_api/stats/endpoints/playerdashboardbyclutch.md`
- Example output: `docs/nba_api/stats/endpoints_output/playerdashboardbyclutch_output.md`
- Required python args: `player_id`
- Python:
  ```python
  from nba_api.stats.endpoints import PlayerDashboardByClutch
  endpoint = PlayerDashboardByClutch(player_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `PlayerID` | `player_id` | yes |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `GameSegment` | `game_segment_nullable` | no |
  | `LastNGames` | `last_n_games` | no |
  | `LeagueID` | `league_id_nullable` | no |
  | `Location` | `location_nullable` | no |
  | `MeasureType` | `measure_type_detailed` | no |
  | `Month` | `month` | no |
  | `OpponentTeamID` | `opponent_team_id` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `PORound` | `po_round_nullable` | no |
  | `PaceAdjust` | `pace_adjust` | no |
  | `PerMode` | `per_mode_detailed` | no |
  | `Period` | `period` | no |
  | `PlusMinus` | `plus_minus` | no |
  | `Rank` | `rank` | no |
  | `Season` | `season` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_playoffs` | no |
  | `ShotClockRange` | `shot_clock_range_nullable` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `Last10Sec3Point2PlayerDashboard` (62): `GROUP_SET`, `GROUP_VALUE`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `NBA_FANTASY_PTS`, `DD2`, `TD3`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `NBA_FANTASY_PTS_RANK`, `DD2_RANK`, `TD3_RANK`, `CFID`, `CFPARAMS`
  - `Last10Sec3PointPlayerDashboard` (62): `GROUP_SET`, `GROUP_VALUE`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `NBA_FANTASY_PTS`, `DD2`, `TD3`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `NBA_FANTASY_PTS_RANK`, `DD2_RANK`, `TD3_RANK`, `CFID`, `CFPARAMS`
  - `Last1Min5PointPlayerDashboard` (62): `GROUP_SET`, `GROUP_VALUE`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `NBA_FANTASY_PTS`, `DD2`, `TD3`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `NBA_FANTASY_PTS_RANK`, `DD2_RANK`, `TD3_RANK`, `CFID`, `CFPARAMS`
  - `Last1MinPlusMinus5PointPlayerDashboard` (62): `GROUP_SET`, `GROUP_VALUE`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `NBA_FANTASY_PTS`, `DD2`, `TD3`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `NBA_FANTASY_PTS_RANK`, `DD2_RANK`, `TD3_RANK`, `CFID`, `CFPARAMS`
  - `Last30Sec3Point2PlayerDashboard` (62): `GROUP_SET`, `GROUP_VALUE`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `NBA_FANTASY_PTS`, `DD2`, `TD3`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `NBA_FANTASY_PTS_RANK`, `DD2_RANK`, `TD3_RANK`, `CFID`, `CFPARAMS`
  - `Last30Sec3PointPlayerDashboard` (62): `GROUP_SET`, `GROUP_VALUE`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `NBA_FANTASY_PTS`, `DD2`, `TD3`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `NBA_FANTASY_PTS_RANK`, `DD2_RANK`, `TD3_RANK`, `CFID`, `CFPARAMS`
  - `Last3Min5PointPlayerDashboard` (62): `GROUP_SET`, `GROUP_VALUE`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `NBA_FANTASY_PTS`, `DD2`, `TD3`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `NBA_FANTASY_PTS_RANK`, `DD2_RANK`, `TD3_RANK`, `CFID`, `CFPARAMS`
  - `Last3MinPlusMinus5PointPlayerDashboard` (62): `GROUP_SET`, `GROUP_VALUE`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `NBA_FANTASY_PTS`, `DD2`, `TD3`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `NBA_FANTASY_PTS_RANK`, `DD2_RANK`, `TD3_RANK`, `CFID`, `CFPARAMS`
  - `Last5Min5PointPlayerDashboard` (62): `GROUP_SET`, `GROUP_VALUE`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `NBA_FANTASY_PTS`, `DD2`, `TD3`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `NBA_FANTASY_PTS_RANK`, `DD2_RANK`, `TD3_RANK`, `CFID`, `CFPARAMS`
  - `Last5MinPlusMinus5PointPlayerDashboard` (62): `GROUP_SET`, `GROUP_VALUE`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `NBA_FANTASY_PTS`, `DD2`, `TD3`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `NBA_FANTASY_PTS_RANK`, `DD2_RANK`, `TD3_RANK`, `CFID`, `CFPARAMS`
  - `OverallPlayerDashboard` (62): `GROUP_SET`, `GROUP_VALUE`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `NBA_FANTASY_PTS`, `DD2`, `TD3`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `NBA_FANTASY_PTS_RANK`, `DD2_RANK`, `TD3_RANK`, `CFID`, `CFPARAMS`

  </details>

### PlayerDashboardByGameSplits

- HTTP: `GET https://stats.nba.com/stats/playerdashboardbygamesplits`
- Repo docs: `docs/nba_api/stats/endpoints/playerdashboardbygamesplits.md`
- Example output: `docs/nba_api/stats/endpoints_output/playerdashboardbygamesplits_output.md`
- Required python args: `player_id`
- Python:
  ```python
  from nba_api.stats.endpoints import PlayerDashboardByGameSplits
  endpoint = PlayerDashboardByGameSplits(player_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `PlayerID` | `player_id` | yes |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `GameSegment` | `game_segment_nullable` | no |
  | `LastNGames` | `last_n_games` | no |
  | `LeagueID` | `league_id_nullable` | no |
  | `Location` | `location_nullable` | no |
  | `MeasureType` | `measure_type_detailed` | no |
  | `Month` | `month` | no |
  | `OpponentTeamID` | `opponent_team_id` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `PORound` | `po_round_nullable` | no |
  | `PaceAdjust` | `pace_adjust` | no |
  | `PerMode` | `per_mode_detailed` | no |
  | `Period` | `period` | no |
  | `PlusMinus` | `plus_minus` | no |
  | `Rank` | `rank` | no |
  | `Season` | `season` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_playoffs` | no |
  | `ShotClockRange` | `shot_clock_range_nullable` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `ByActualMarginPlayerDashboard` (62): `GROUP_SET`, `GROUP_VALUE`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `NBA_FANTASY_PTS`, `DD2`, `TD3`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `NBA_FANTASY_PTS_RANK`, `DD2_RANK`, `TD3_RANK`, `CFID`, `CFPARAMS`
  - `ByHalfPlayerDashboard` (62): `GROUP_SET`, `GROUP_VALUE`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `NBA_FANTASY_PTS`, `DD2`, `TD3`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `NBA_FANTASY_PTS_RANK`, `DD2_RANK`, `TD3_RANK`, `CFID`, `CFPARAMS`
  - `ByPeriodPlayerDashboard` (62): `GROUP_SET`, `GROUP_VALUE`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `NBA_FANTASY_PTS`, `DD2`, `TD3`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `NBA_FANTASY_PTS_RANK`, `DD2_RANK`, `TD3_RANK`, `CFID`, `CFPARAMS`
  - `ByScoreMarginPlayerDashboard` (62): `GROUP_SET`, `GROUP_VALUE`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `NBA_FANTASY_PTS`, `DD2`, `TD3`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `NBA_FANTASY_PTS_RANK`, `DD2_RANK`, `TD3_RANK`, `CFID`, `CFPARAMS`
  - `OverallPlayerDashboard` (62): `GROUP_SET`, `GROUP_VALUE`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `NBA_FANTASY_PTS`, `DD2`, `TD3`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `NBA_FANTASY_PTS_RANK`, `DD2_RANK`, `TD3_RANK`, `CFID`, `CFPARAMS`

  </details>

### PlayerDashboardByGeneralSplits

- HTTP: `GET https://stats.nba.com/stats/playerdashboardbygeneralsplits`
- Repo docs: `docs/nba_api/stats/endpoints/playerdashboardbygeneralsplits.md`
- Example output: `docs/nba_api/stats/endpoints_output/playerdashboardbygeneralsplits_output.md`
- Required python args: `player_id`
- Python:
  ```python
  from nba_api.stats.endpoints import PlayerDashboardByGeneralSplits
  endpoint = PlayerDashboardByGeneralSplits(player_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `PlayerID` | `player_id` | yes |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `GameSegment` | `game_segment_nullable` | no |
  | `LastNGames` | `last_n_games` | no |
  | `LeagueID` | `league_id_nullable` | no |
  | `Location` | `location_nullable` | no |
  | `MeasureType` | `measure_type_detailed` | no |
  | `Month` | `month` | no |
  | `OpponentTeamID` | `opponent_team_id` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `PORound` | `po_round_nullable` | no |
  | `PaceAdjust` | `pace_adjust` | no |
  | `PerMode` | `per_mode_detailed` | no |
  | `Period` | `period` | no |
  | `PlusMinus` | `plus_minus` | no |
  | `Rank` | `rank` | no |
  | `Season` | `season` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_playoffs` | no |
  | `ShotClockRange` | `shot_clock_range_nullable` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `DaysRestPlayerDashboard` (62): `GROUP_SET`, `GROUP_VALUE`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `NBA_FANTASY_PTS`, `DD2`, `TD3`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `NBA_FANTASY_PTS_RANK`, `DD2_RANK`, `TD3_RANK`, `CFID`, `CFPARAMS`
  - `LocationPlayerDashboard` (62): `GROUP_SET`, `GROUP_VALUE`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `NBA_FANTASY_PTS`, `DD2`, `TD3`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `NBA_FANTASY_PTS_RANK`, `DD2_RANK`, `TD3_RANK`, `CFID`, `CFPARAMS`
  - `MonthPlayerDashboard` (62): `GROUP_SET`, `GROUP_VALUE`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `NBA_FANTASY_PTS`, `DD2`, `TD3`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `NBA_FANTASY_PTS_RANK`, `DD2_RANK`, `TD3_RANK`, `CFID`, `CFPARAMS`
  - `OverallPlayerDashboard` (62): `GROUP_SET`, `GROUP_VALUE`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `NBA_FANTASY_PTS`, `DD2`, `TD3`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `NBA_FANTASY_PTS_RANK`, `DD2_RANK`, `TD3_RANK`, `CFID`, `CFPARAMS`
  - `PrePostAllStarPlayerDashboard` (62): `GROUP_SET`, `GROUP_VALUE`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `NBA_FANTASY_PTS`, `DD2`, `TD3`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `NBA_FANTASY_PTS_RANK`, `DD2_RANK`, `TD3_RANK`, `CFID`, `CFPARAMS`
  - `StartingPosition` (62): `GROUP_SET`, `GROUP_VALUE`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `NBA_FANTASY_PTS`, `DD2`, `TD3`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `NBA_FANTASY_PTS_RANK`, `DD2_RANK`, `TD3_RANK`, `CFID`, `CFPARAMS`
  - `WinsLossesPlayerDashboard` (62): `GROUP_SET`, `GROUP_VALUE`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `NBA_FANTASY_PTS`, `DD2`, `TD3`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `NBA_FANTASY_PTS_RANK`, `DD2_RANK`, `TD3_RANK`, `CFID`, `CFPARAMS`

  </details>

### PlayerDashboardByLastNGames

- HTTP: `GET https://stats.nba.com/stats/playerdashboardbylastngames`
- Repo docs: `docs/nba_api/stats/endpoints/playerdashboardbylastngames.md`
- Example output: `docs/nba_api/stats/endpoints_output/playerdashboardbylastngames_output.md`
- Required python args: `player_id`
- Python:
  ```python
  from nba_api.stats.endpoints import PlayerDashboardByLastNGames
  endpoint = PlayerDashboardByLastNGames(player_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `PlayerID` | `player_id` | yes |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `GameSegment` | `game_segment_nullable` | no |
  | `LastNGames` | `last_n_games` | no |
  | `LeagueID` | `league_id_nullable` | no |
  | `Location` | `location_nullable` | no |
  | `MeasureType` | `measure_type_detailed` | no |
  | `Month` | `month` | no |
  | `OpponentTeamID` | `opponent_team_id` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `PORound` | `po_round_nullable` | no |
  | `PaceAdjust` | `pace_adjust` | no |
  | `PerMode` | `per_mode_detailed` | no |
  | `Period` | `period` | no |
  | `PlusMinus` | `plus_minus` | no |
  | `Rank` | `rank` | no |
  | `Season` | `season` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_playoffs` | no |
  | `ShotClockRange` | `shot_clock_range_nullable` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `GameNumberPlayerDashboard` (62): `GROUP_SET`, `GROUP_VALUE`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `NBA_FANTASY_PTS`, `DD2`, `TD3`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `NBA_FANTASY_PTS_RANK`, `DD2_RANK`, `TD3_RANK`, `CFID`, `CFPARAMS`
  - `Last10PlayerDashboard` (62): `GROUP_SET`, `GROUP_VALUE`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `NBA_FANTASY_PTS`, `DD2`, `TD3`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `NBA_FANTASY_PTS_RANK`, `DD2_RANK`, `TD3_RANK`, `CFID`, `CFPARAMS`
  - `Last15PlayerDashboard` (62): `GROUP_SET`, `GROUP_VALUE`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `NBA_FANTASY_PTS`, `DD2`, `TD3`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `NBA_FANTASY_PTS_RANK`, `DD2_RANK`, `TD3_RANK`, `CFID`, `CFPARAMS`
  - `Last20PlayerDashboard` (62): `GROUP_SET`, `GROUP_VALUE`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `NBA_FANTASY_PTS`, `DD2`, `TD3`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `NBA_FANTASY_PTS_RANK`, `DD2_RANK`, `TD3_RANK`, `CFID`, `CFPARAMS`
  - `Last5PlayerDashboard` (62): `GROUP_SET`, `GROUP_VALUE`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `NBA_FANTASY_PTS`, `DD2`, `TD3`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `NBA_FANTASY_PTS_RANK`, `DD2_RANK`, `TD3_RANK`, `CFID`, `CFPARAMS`
  - `OverallPlayerDashboard` (62): `GROUP_SET`, `GROUP_VALUE`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `NBA_FANTASY_PTS`, `DD2`, `TD3`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `NBA_FANTASY_PTS_RANK`, `DD2_RANK`, `TD3_RANK`, `CFID`, `CFPARAMS`

  </details>

### PlayerDashboardByShootingSplits

- HTTP: `GET https://stats.nba.com/stats/playerdashboardbyshootingsplits`
- Repo docs: `docs/nba_api/stats/endpoints/playerdashboardbyshootingsplits.md`
- Example output: `docs/nba_api/stats/endpoints_output/playerdashboardbyshootingsplits_output.md`
- Required python args: `player_id`
- Python:
  ```python
  from nba_api.stats.endpoints import PlayerDashboardByShootingSplits
  endpoint = PlayerDashboardByShootingSplits(player_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `PlayerID` | `player_id` | yes |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `GameSegment` | `game_segment_nullable` | no |
  | `LastNGames` | `last_n_games` | no |
  | `LeagueID` | `league_id_nullable` | no |
  | `Location` | `location_nullable` | no |
  | `MeasureType` | `measure_type_detailed` | no |
  | `Month` | `month` | no |
  | `OpponentTeamID` | `opponent_team_id` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `PORound` | `po_round_nullable` | no |
  | `PaceAdjust` | `pace_adjust` | no |
  | `PerMode` | `per_mode_detailed` | no |
  | `Period` | `period` | no |
  | `PlusMinus` | `plus_minus` | no |
  | `Rank` | `rank` | no |
  | `Season` | `season` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_playoffs` | no |
  | `ShotClockRange` | `shot_clock_range_nullable` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `AssistedBy` (33): `GROUP_SET`, `PLAYER_ID`, `PLAYER_NAME`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `EFG_PCT`, `BLKA`, `PCT_AST_2PM`, `PCT_UAST_2PM`, `PCT_AST_3PM`, `PCT_UAST_3PM`, `PCT_AST_FGM`, `PCT_UAST_FGM`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `EFG_PCT_RANK`, `BLKA_RANK`, `PCT_AST_2PM_RANK`, `PCT_UAST_2PM_RANK`, `PCT_AST_3PM_RANK`, `PCT_UAST_3PM_RANK`, `PCT_AST_FGM_RANK`, `PCT_UAST_FGM_RANK`, `CFID`, `CFPARAMS`
  - `AssitedShotPlayerDashboard` (32): `GROUP_SET`, `GROUP_VALUE`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `EFG_PCT`, `BLKA`, `PCT_AST_2PM`, `PCT_UAST_2PM`, `PCT_AST_3PM`, `PCT_UAST_3PM`, `PCT_AST_FGM`, `PCT_UAST_FGM`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `EFG_PCT_RANK`, `BLKA_RANK`, `PCT_AST_2PM_RANK`, `PCT_UAST_2PM_RANK`, `PCT_AST_3PM_RANK`, `PCT_UAST_3PM_RANK`, `PCT_AST_FGM_RANK`, `PCT_UAST_FGM_RANK`, `CFID`, `CFPARAMS`
  - `OverallPlayerDashboard` (32): `GROUP_SET`, `GROUP_VALUE`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `EFG_PCT`, `BLKA`, `PCT_AST_2PM`, `PCT_UAST_2PM`, `PCT_AST_3PM`, `PCT_UAST_3PM`, `PCT_AST_FGM`, `PCT_UAST_FGM`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `EFG_PCT_RANK`, `BLKA_RANK`, `PCT_AST_2PM_RANK`, `PCT_UAST_2PM_RANK`, `PCT_AST_3PM_RANK`, `PCT_UAST_3PM_RANK`, `PCT_AST_FGM_RANK`, `PCT_UAST_FGM_RANK`, `CFID`, `CFPARAMS`
  - `Shot5FTPlayerDashboard` (32): `GROUP_SET`, `GROUP_VALUE`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `EFG_PCT`, `BLKA`, `PCT_AST_2PM`, `PCT_UAST_2PM`, `PCT_AST_3PM`, `PCT_UAST_3PM`, `PCT_AST_FGM`, `PCT_UAST_FGM`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `EFG_PCT_RANK`, `BLKA_RANK`, `PCT_AST_2PM_RANK`, `PCT_UAST_2PM_RANK`, `PCT_AST_3PM_RANK`, `PCT_UAST_3PM_RANK`, `PCT_AST_FGM_RANK`, `PCT_UAST_FGM_RANK`, `CFID`, `CFPARAMS`
  - `Shot8FTPlayerDashboard` (32): `GROUP_SET`, `GROUP_VALUE`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `EFG_PCT`, `BLKA`, `PCT_AST_2PM`, `PCT_UAST_2PM`, `PCT_AST_3PM`, `PCT_UAST_3PM`, `PCT_AST_FGM`, `PCT_UAST_FGM`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `EFG_PCT_RANK`, `BLKA_RANK`, `PCT_AST_2PM_RANK`, `PCT_UAST_2PM_RANK`, `PCT_AST_3PM_RANK`, `PCT_UAST_3PM_RANK`, `PCT_AST_FGM_RANK`, `PCT_UAST_FGM_RANK`, `CFID`, `CFPARAMS`
  - `ShotAreaPlayerDashboard` (32): `GROUP_SET`, `GROUP_VALUE`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `EFG_PCT`, `BLKA`, `PCT_AST_2PM`, `PCT_UAST_2PM`, `PCT_AST_3PM`, `PCT_UAST_3PM`, `PCT_AST_FGM`, `PCT_UAST_FGM`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `EFG_PCT_RANK`, `BLKA_RANK`, `PCT_AST_2PM_RANK`, `PCT_UAST_2PM_RANK`, `PCT_AST_3PM_RANK`, `PCT_UAST_3PM_RANK`, `PCT_AST_FGM_RANK`, `PCT_UAST_FGM_RANK`, `CFID`, `CFPARAMS`
  - `ShotTypePlayerDashboard` (32): `GROUP_SET`, `GROUP_VALUE`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `EFG_PCT`, `BLKA`, `PCT_AST_2PM`, `PCT_UAST_2PM`, `PCT_AST_3PM`, `PCT_UAST_3PM`, `PCT_AST_FGM`, `PCT_UAST_FGM`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `EFG_PCT_RANK`, `BLKA_RANK`, `PCT_AST_2PM_RANK`, `PCT_UAST_2PM_RANK`, `PCT_AST_3PM_RANK`, `PCT_UAST_3PM_RANK`, `PCT_AST_FGM_RANK`, `PCT_UAST_FGM_RANK`, `CFID`, `CFPARAMS`
  - `ShotTypeSummaryPlayerDashboard` (18): `GROUP_SET`, `GROUP_VALUE`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `EFG_PCT`, `BLKA`, `PCT_AST_2PM`, `PCT_UAST_2PM`, `PCT_AST_3PM`, `PCT_UAST_3PM`, `PCT_AST_FGM`, `PCT_UAST_FGM`, `CFID`, `CFPARAMS`

  </details>

### PlayerDashboardByTeamPerformance

- HTTP: `GET https://stats.nba.com/stats/playerdashboardbyteamperformance`
- Repo docs: `docs/nba_api/stats/endpoints/playerdashboardbyteamperformance.md`
- Example output: `docs/nba_api/stats/endpoints_output/playerdashboardbyteamperformance_output.md`
- Required python args: `player_id`
- Python:
  ```python
  from nba_api.stats.endpoints import PlayerDashboardByTeamPerformance
  endpoint = PlayerDashboardByTeamPerformance(player_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `PlayerID` | `player_id` | yes |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `GameSegment` | `game_segment_nullable` | no |
  | `LastNGames` | `last_n_games` | no |
  | `LeagueID` | `league_id_nullable` | no |
  | `Location` | `location_nullable` | no |
  | `MeasureType` | `measure_type_detailed` | no |
  | `Month` | `month` | no |
  | `OpponentTeamID` | `opponent_team_id` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `PORound` | `po_round_nullable` | no |
  | `PaceAdjust` | `pace_adjust` | no |
  | `PerMode` | `per_mode_detailed` | no |
  | `Period` | `period` | no |
  | `PlusMinus` | `plus_minus` | no |
  | `Rank` | `rank` | no |
  | `Season` | `season` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_playoffs` | no |
  | `ShotClockRange` | `shot_clock_range_nullable` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `OverallPlayerDashboard` (62): `GROUP_SET`, `GROUP_VALUE`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `NBA_FANTASY_PTS`, `DD2`, `TD3`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `NBA_FANTASY_PTS_RANK`, `DD2_RANK`, `TD3_RANK`, `CFID`, `CFPARAMS`
  - `PointsScoredPlayerDashboard` (64): `GROUP_SET`, `GROUP_VALUE_ORDER`, `GROUP_VALUE`, `GROUP_VALUE_2`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `NBA_FANTASY_PTS`, `DD2`, `TD3`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `NBA_FANTASY_PTS_RANK`, `DD2_RANK`, `TD3_RANK`, `CFID`, `CFPARAMS`
  - `PontsAgainstPlayerDashboard` (64): `GROUP_SET`, `GROUP_VALUE_ORDER`, `GROUP_VALUE`, `GROUP_VALUE_2`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `NBA_FANTASY_PTS`, `DD2`, `TD3`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `NBA_FANTASY_PTS_RANK`, `DD2_RANK`, `TD3_RANK`, `CFID`, `CFPARAMS`
  - `ScoreDifferentialPlayerDashboard` (64): `GROUP_SET`, `GROUP_VALUE_ORDER`, `GROUP_VALUE`, `GROUP_VALUE_2`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `NBA_FANTASY_PTS`, `DD2`, `TD3`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `NBA_FANTASY_PTS_RANK`, `DD2_RANK`, `TD3_RANK`, `CFID`, `CFPARAMS`

  </details>

### PlayerDashboardByYearOverYear

- HTTP: `GET https://stats.nba.com/stats/playerdashboardbyyearoveryear`
- Repo docs: `docs/nba_api/stats/endpoints/playerdashboardbyyearoveryear.md`
- Example output: `docs/nba_api/stats/endpoints_output/playerdashboardbyyearoveryear_output.md`
- Required python args: `player_id`
- Python:
  ```python
  from nba_api.stats.endpoints import PlayerDashboardByYearOverYear
  endpoint = PlayerDashboardByYearOverYear(player_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `PlayerID` | `player_id` | yes |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `GameSegment` | `game_segment_nullable` | no |
  | `LastNGames` | `last_n_games` | no |
  | `LeagueID` | `league_id_nullable` | no |
  | `Location` | `location_nullable` | no |
  | `MeasureType` | `measure_type_detailed` | no |
  | `Month` | `month` | no |
  | `OpponentTeamID` | `opponent_team_id` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `PORound` | `po_round_nullable` | no |
  | `PaceAdjust` | `pace_adjust` | no |
  | `PerMode` | `per_mode_detailed` | no |
  | `Period` | `period` | no |
  | `PlusMinus` | `plus_minus` | no |
  | `Rank` | `rank` | no |
  | `Season` | `season` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_playoffs` | no |
  | `ShotClockRange` | `shot_clock_range_nullable` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `ByYearPlayerDashboard` (65): `GROUP_SET`, `GROUP_VALUE`, `TEAM_ID`, `TEAM_ABBREVIATION`, `MAX_GAME_DATE`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `NBA_FANTASY_PTS`, `DD2`, `TD3`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `NBA_FANTASY_PTS_RANK`, `DD2_RANK`, `TD3_RANK`, `CFID`, `CFPARAMS`
  - `OverallPlayerDashboard` (65): `GROUP_SET`, `GROUP_VALUE`, `TEAM_ID`, `TEAM_ABBREVIATION`, `MAX_GAME_DATE`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `NBA_FANTASY_PTS`, `DD2`, `TD3`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `NBA_FANTASY_PTS_RANK`, `DD2_RANK`, `TD3_RANK`, `CFID`, `CFPARAMS`

  </details>

### PlayerDashPtPass

- HTTP: `GET https://stats.nba.com/stats/playerdashptpass`
- Repo docs: `docs/nba_api/stats/endpoints/playerdashptpass.md`
- Example output: `docs/nba_api/stats/endpoints_output/playerdashptpass_output.md`
- Required python args: `team_id`, `player_id`
- Python:
  ```python
  from nba_api.stats.endpoints import PlayerDashPtPass
  endpoint = PlayerDashPtPass(team_id='…', player_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `PlayerID` | `player_id` | yes |
  | `TeamID` | `team_id` | yes |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `LastNGames` | `last_n_games` | no |
  | `LeagueID` | `league_id` | no |
  | `Location` | `location_nullable` | no |
  | `Month` | `month` | no |
  | `OpponentTeamID` | `opponent_team_id` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `PerMode` | `per_mode_simple` | no |
  | `Season` | `season` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_all_star` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `PassesMade` (21): `PLAYER_ID`, `PLAYER_NAME_LAST_FIRST`, `TEAM_NAME`, `TEAM_ID`, `TEAM_ABBREVIATION`, `PASS_TYPE`, `G`, `PASS_TO`, `PASS_TEAMMATE_PLAYER_ID`, `FREQUENCY`, `PASS`, `AST`, `FGM`, `FGA`, `FG_PCT`, `FG2M`, `FG2A`, `FG2_PCT`, `FG3M`, `FG3A`, `FG3_PCT`
  - `PassesReceived` (21): `PLAYER_ID`, `PLAYER_NAME_LAST_FIRST`, `TEAM_NAME`, `TEAM_ID`, `TEAM_ABBREVIATION`, `PASS_TYPE`, `G`, `PASS_FROM`, `PASS_TEAMMATE_PLAYER_ID`, `FREQUENCY`, `PASS`, `AST`, `FGM`, `FGA`, `FG_PCT`, `FG2M`, `FG2A`, `FG2_PCT`, `FG3M`, `FG3A`, `FG3_PCT`

  </details>

### PlayerDashPtReb

- HTTP: `GET https://stats.nba.com/stats/playerdashptreb`
- Repo docs: `docs/nba_api/stats/endpoints/playerdashptreb.md`
- Example output: `docs/nba_api/stats/endpoints_output/playerdashptreb_output.md`
- Required python args: `team_id`, `player_id`
- Python:
  ```python
  from nba_api.stats.endpoints import PlayerDashPtReb
  endpoint = PlayerDashPtReb(team_id='…', player_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `PlayerID` | `player_id` | yes |
  | `TeamID` | `team_id` | yes |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `GameSegment` | `game_segment_nullable` | no |
  | `LastNGames` | `last_n_games` | no |
  | `LeagueID` | `league_id` | no |
  | `Location` | `location_nullable` | no |
  | `Month` | `month` | no |
  | `OpponentTeamID` | `opponent_team_id` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `PerMode` | `per_mode_simple` | no |
  | `Period` | `period` | no |
  | `Season` | `season` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_all_star` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `NumContestedRebounding` (17): `PLAYER_ID`, `PLAYER_NAME_LAST_FIRST`, `SORT_ORDER`, `G`, `REB_NUM_CONTESTING_RANGE`, `REB_FREQUENCY`, `OREB`, `DREB`, `REB`, `C_OREB`, `C_DREB`, `C_REB`, `C_REB_PCT`, `UC_OREB`, `UC_DREB`, `UC_REB`, `UC_REB_PCT`
  - `OverallRebounding` (16): `PLAYER_ID`, `PLAYER_NAME_LAST_FIRST`, `G`, `OVERALL`, `REB_FREQUENCY`, `OREB`, `DREB`, `REB`, `C_OREB`, `C_DREB`, `C_REB`, `C_REB_PCT`, `UC_OREB`, `UC_DREB`, `UC_REB`, `UC_REB_PCT`
  - `RebDistanceRebounding` (17): `PLAYER_ID`, `PLAYER_NAME_LAST_FIRST`, `SORT_ORDER`, `G`, `REB_DIST_RANGE`, `REB_FREQUENCY`, `OREB`, `DREB`, `REB`, `C_OREB`, `C_DREB`, `C_REB`, `C_REB_PCT`, `UC_OREB`, `UC_DREB`, `UC_REB`, `UC_REB_PCT`
  - `ShotDistanceRebounding` (17): `PLAYER_ID`, `PLAYER_NAME_LAST_FIRST`, `SORT_ORDER`, `G`, `SHOT_DIST_RANGE`, `REB_FREQUENCY`, `OREB`, `DREB`, `REB`, `C_OREB`, `C_DREB`, `C_REB`, `C_REB_PCT`, `UC_OREB`, `UC_DREB`, `UC_REB`, `UC_REB_PCT`
  - `ShotTypeRebounding` (17): `PLAYER_ID`, `PLAYER_NAME_LAST_FIRST`, `SORT_ORDER`, `G`, `SHOT_TYPE_RANGE`, `REB_FREQUENCY`, `OREB`, `DREB`, `REB`, `C_OREB`, `C_DREB`, `C_REB`, `C_REB_PCT`, `UC_OREB`, `UC_DREB`, `UC_REB`, `UC_REB_PCT`

  </details>

### PlayerDashPtShotDefend

- HTTP: `GET https://stats.nba.com/stats/playerdashptshotdefend`
- Repo docs: `docs/nba_api/stats/endpoints/playerdashptshotdefend.md`
- Example output: `docs/nba_api/stats/endpoints_output/playerdashptshotdefend_output.md`
- Required python args: `team_id`, `player_id`
- Python:
  ```python
  from nba_api.stats.endpoints import PlayerDashPtShotDefend
  endpoint = PlayerDashPtShotDefend(team_id='…', player_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `PlayerID` | `player_id` | yes |
  | `TeamID` | `team_id` | yes |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `GameSegment` | `game_segment_nullable` | no |
  | `LastNGames` | `last_n_games` | no |
  | `LeagueID` | `league_id` | no |
  | `Location` | `location_nullable` | no |
  | `Month` | `month` | no |
  | `OpponentTeamID` | `opponent_team_id` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `PerMode` | `per_mode_simple` | no |
  | `Period` | `period` | no |
  | `Season` | `season` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_all_star` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `DefendingShots` (10): `CLOSE_DEF_PERSON_ID`, `GP`, `G`, `DEFENSE_CATEGORY`, `FREQ`, `D_FGM`, `D_FGA`, `D_FG_PCT`, `NORMAL_FG_PCT`, `PCT_PLUSMINUS`

  </details>

### PlayerDashPtShots

- HTTP: `GET https://stats.nba.com/stats/playerdashptshots`
- Repo docs: `docs/nba_api/stats/endpoints/playerdashptshots.md`
- Example output: `docs/nba_api/stats/endpoints_output/playerdashptshots_output.md`
- Required python args: `team_id`, `player_id`
- Python:
  ```python
  from nba_api.stats.endpoints import PlayerDashPtShots
  endpoint = PlayerDashPtShots(team_id='…', player_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `PlayerID` | `player_id` | yes |
  | `TeamID` | `team_id` | yes |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `GameSegment` | `game_segment_nullable` | no |
  | `LastNGames` | `last_n_games` | no |
  | `LeagueID` | `league_id` | no |
  | `Location` | `location_nullable` | no |
  | `Month` | `month` | no |
  | `OpponentTeamID` | `opponent_team_id` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `PerMode` | `per_mode_simple` | no |
  | `Period` | `period` | no |
  | `Season` | `season` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_all_star` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `ClosestDefender10ftPlusShooting` (19): `PLAYER_ID`, `PLAYER_NAME_LAST_FIRST`, `SORT_ORDER`, `GP`, `G`, `CLOSE_DEF_DIST_RANGE`, `FGA_FREQUENCY`, `FGM`, `FGA`, `FG_PCT`, `EFG_PCT`, `FG2A_FREQUENCY`, `FG2M`, `FG2A`, `FG2_PCT`, `FG3A_FREQUENCY`, `FG3M`, `FG3A`, `FG3_PCT`
  - `ClosestDefenderShooting` (19): `PLAYER_ID`, `PLAYER_NAME_LAST_FIRST`, `SORT_ORDER`, `GP`, `G`, `CLOSE_DEF_DIST_RANGE`, `FGA_FREQUENCY`, `FGM`, `FGA`, `FG_PCT`, `EFG_PCT`, `FG2A_FREQUENCY`, `FG2M`, `FG2A`, `FG2_PCT`, `FG3A_FREQUENCY`, `FG3M`, `FG3A`, `FG3_PCT`
  - `DribbleShooting` (19): `PLAYER_ID`, `PLAYER_NAME_LAST_FIRST`, `SORT_ORDER`, `GP`, `G`, `DRIBBLE_RANGE`, `FGA_FREQUENCY`, `FGM`, `FGA`, `FG_PCT`, `EFG_PCT`, `FG2A_FREQUENCY`, `FG2M`, `FG2A`, `FG2_PCT`, `FG3A_FREQUENCY`, `FG3M`, `FG3A`, `FG3_PCT`
  - `GeneralShooting` (19): `PLAYER_ID`, `PLAYER_NAME_LAST_FIRST`, `SORT_ORDER`, `GP`, `G`, `SHOT_TYPE`, `FGA_FREQUENCY`, `FGM`, `FGA`, `FG_PCT`, `EFG_PCT`, `FG2A_FREQUENCY`, `FG2M`, `FG2A`, `FG2_PCT`, `FG3A_FREQUENCY`, `FG3M`, `FG3A`, `FG3_PCT`
  - `Overall` (19): `PLAYER_ID`, `PLAYER_NAME_LAST_FIRST`, `SORT_ORDER`, `GP`, `G`, `SHOT_TYPE`, `FGA_FREQUENCY`, `FGM`, `FGA`, `FG_PCT`, `EFG_PCT`, `FG2A_FREQUENCY`, `FG2M`, `FG2A`, `FG2_PCT`, `FG3A_FREQUENCY`, `FG3M`, `FG3A`, `FG3_PCT`
  - `ShotClockShooting` (19): `PLAYER_ID`, `PLAYER_NAME_LAST_FIRST`, `SORT_ORDER`, `GP`, `G`, `SHOT_CLOCK_RANGE`, `FGA_FREQUENCY`, `FGM`, `FGA`, `FG_PCT`, `EFG_PCT`, `FG2A_FREQUENCY`, `FG2M`, `FG2A`, `FG2_PCT`, `FG3A_FREQUENCY`, `FG3M`, `FG3A`, `FG3_PCT`
  - `TouchTimeShooting` (19): `PLAYER_ID`, `PLAYER_NAME_LAST_FIRST`, `SORT_ORDER`, `GP`, `G`, `TOUCH_TIME_RANGE`, `FGA_FREQUENCY`, `FGM`, `FGA`, `FG_PCT`, `EFG_PCT`, `FG2A_FREQUENCY`, `FG2M`, `FG2A`, `FG2_PCT`, `FG3A_FREQUENCY`, `FG3M`, `FG3A`, `FG3_PCT`

  </details>

### PlayerEstimatedMetrics

- HTTP: `GET https://stats.nba.com/stats/playerestimatedmetrics`
- Repo docs: `docs/nba_api/stats/endpoints/playerestimatedmetrics.md`
- Example output: `docs/nba_api/stats/endpoints_output/playerestimatedmetrics_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import PlayerEstimatedMetrics
  endpoint = PlayerEstimatedMetrics()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `LeagueID` | `league_id` | no |
  | `Season` | `season` | no |
  | `SeasonType` | `season_type` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `PlayerEstimatedMetrics` (32): `PLAYER_ID`, `PLAYER_NAME`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `E_OFF_RATING`, `E_DEF_RATING`, `E_NET_RATING`, `E_AST_RATIO`, `E_OREB_PCT`, `E_DREB_PCT`, `E_REB_PCT`, `E_TOV_PCT`, `E_USG_PCT`, `E_PACE`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `E_OFF_RATING_RANK`, `E_DEF_RATING_RANK`, `E_NET_RATING_RANK`, `E_AST_RATIO_RANK`, `E_OREB_PCT_RANK`, `E_DREB_PCT_RANK`, `E_REB_PCT_RANK`, `E_TOV_PCT_RANK`, `E_USG_PCT_RANK`, `E_PACE_RANK`

  </details>

### PlayerFantasyProfileBarGraph

- HTTP: `GET https://stats.nba.com/stats/playerfantasyprofilebargraph`
- Repo docs: `docs/nba_api/stats/endpoints/playerfantasyprofilebargraph.md`
- Example output: `docs/nba_api/stats/endpoints_output/playerfantasyprofilebargraph_output.md`
- Required python args: `player_id`
- Python:
  ```python
  from nba_api.stats.endpoints import PlayerFantasyProfileBarGraph
  endpoint = PlayerFantasyProfileBarGraph(player_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `PlayerID` | `player_id` | yes |
  | `LeagueID` | `league_id_nullable` | no |
  | `Season` | `season` | no |
  | `SeasonType` | `season_type_all_star_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `LastFiveGamesAvg` (15): `PLAYER_ID`, `PLAYER_NAME`, `TEAM_ID`, `TEAM_ABBREVIATION`, `FAN_DUEL_PTS`, `NBA_FANTASY_PTS`, `PTS`, `REB`, `AST`, `FG3M`, `FT_PCT`, `STL`, `BLK`, `TOV`, `FG_PCT`
  - `SeasonAvg` (15): `PLAYER_ID`, `PLAYER_NAME`, `TEAM_ID`, `TEAM_ABBREVIATION`, `FAN_DUEL_PTS`, `NBA_FANTASY_PTS`, `PTS`, `REB`, `AST`, `FG3M`, `FT_PCT`, `STL`, `BLK`, `TOV`, `FG_PCT`

  </details>

### PlayerGameLog

- HTTP: `GET https://stats.nba.com/stats/playergamelog`
- Repo docs: `docs/nba_api/stats/endpoints/playergamelog.md`
- Example output: `docs/nba_api/stats/endpoints_output/playergamelog_output.md`
- Required python args: `player_id`
- Python:
  ```python
  from nba_api.stats.endpoints import PlayerGameLog
  endpoint = PlayerGameLog(player_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `PlayerID` | `player_id` | yes |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `LeagueID` | `league_id_nullable` | no |
  | `Season` | `season` | no |
  | `SeasonType` | `season_type_all_star` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `PlayerGameLog` (27): `SEASON_ID`, `Player_ID`, `Game_ID`, `GAME_DATE`, `MATCHUP`, `WL`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `STL`, `BLK`, `TOV`, `PF`, `PTS`, `PLUS_MINUS`, `VIDEO_AVAILABLE`

  </details>

### PlayerGameLogs

- HTTP: `GET https://stats.nba.com/stats/playergamelogs`
- Repo docs: `docs/nba_api/stats/endpoints/playergamelogs.md`
- Example output: `docs/nba_api/stats/endpoints_output/playergamelogs_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import PlayerGameLogs
  endpoint = PlayerGameLogs()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `GameSegment` | `game_segment_nullable` | no |
  | `LastNGames` | `last_n_games_nullable` | no |
  | `LeagueID` | `league_id_nullable` | no |
  | `Location` | `location_nullable` | no |
  | `MeasureType` | `measure_type_player_game_logs_nullable` | no |
  | `Month` | `month_nullable` | no |
  | `OpponentTeamID` | `opp_team_id_nullable` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `PORound` | `po_round_nullable` | no |
  | `PerMode` | `per_mode_simple_nullable` | no |
  | `Period` | `period_nullable` | no |
  | `PlayerID` | `player_id_nullable` | no |
  | `Season` | `season_nullable` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_nullable` | no |
  | `ShotClockRange` | `shot_clock_range_nullable` | no |
  | `TeamID` | `team_id_nullable` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `PlayerGameLogs` (64): `SEASON_YEAR`, `PLAYER_ID`, `PLAYER_NAME`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_NAME`, `GAME_ID`, `GAME_DATE`, `MATCHUP`, `WL`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `NBA_FANTASY_PTS`, `DD2`, `TD3`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `NBA_FANTASY_PTS_RANK`, `DD2_RANK`, `TD3_RANK`

  </details>

### PlayerGameStreakFinder

- HTTP: `GET https://stats.nba.com/stats/playergamestreakfinder`
- Repo docs: `docs/nba_api/stats/endpoints/playergamestreakfinder.md`
- Example output: `docs/nba_api/stats/endpoints_output/playergamestreakfinder_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import PlayerGameStreakFinder
  endpoint = PlayerGameStreakFinder()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `ActiveStreaksOnly` | `active_streaks_only_nullable` | no |
  | `Conference` | `conference_nullable` | no |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `Division` | `division_simple_nullable` | no |
  | `DraftNumber` | `draft_number_nullable` | no |
  | `DraftRound` | `draft_round_nullable` | no |
  | `DraftTeamID` | `draft_team_id_nullable` | no |
  | `DraftYear` | `draft_year_nullable` | no |
  | `EqAST` | `eq_ast_nullable` | no |
  | `EqBLK` | `eq_blk_nullable` | no |
  | `EqDD` | `eq_dd_nullable` | no |
  | `EqDREB` | `eq_dreb_nullable` | no |
  | `EqFG3A` | `eq_fg3a_nullable` | no |
  | `EqFG3M` | `eq_fg3m_nullable` | no |
  | `EqFG3_PCT` | `eq_fg3_pct_nullable` | no |
  | `EqFGA` | `eq_fga_nullable` | no |
  | `EqFGM` | `eq_fgm_nullable` | no |
  | `EqFG_PCT` | `eq_fg_pct_nullable` | no |
  | `EqFTA` | `eq_fta_nullable` | no |
  | `EqFTM` | `eq_ftm_nullable` | no |
  | `EqFT_PCT` | `eq_ft_pct_nullable` | no |
  | `EqMINUTES` | `eq_minutes_nullable` | no |
  | `EqOREB` | `eq_oreb_nullable` | no |
  | `EqPF` | `eq_pf_nullable` | no |
  | `EqPTS` | `eq_pts_nullable` | no |
  | `EqREB` | `eq_reb_nullable` | no |
  | `EqSTL` | `eq_stl_nullable` | no |
  | `EqTD` | `eq_td_nullable` | no |
  | `EqTOV` | `eq_tov_nullable` | no |
  | `GameID` | `game_id_nullable` | no |
  | `GtAST` | `gt_ast_nullable` | no |
  | `GtBLK` | `gt_blk_nullable` | no |
  | `GtDD` | `gt_dd_nullable` | no |
  | `GtDREB` | `gt_dreb_nullable` | no |
  | `GtFG3A` | `gt_fg3a_nullable` | no |
  | `GtFG3M` | `gt_fg3m_nullable` | no |
  | `GtFG3_PCT` | `gt_fg3_pct_nullable` | no |
  | `GtFGA` | `gt_fga_nullable` | no |
  | `GtFGM` | `gt_fgm_nullable` | no |
  | `GtFG_PCT` | `gt_fg_pct_nullable` | no |
  | `GtFTA` | `gt_fta_nullable` | no |
  | `GtFTM` | `gt_ftm_nullable` | no |
  | `GtFT_PCT` | `gt_ft_pct_nullable` | no |
  | `GtMINUTES` | `gt_minutes_nullable` | no |
  | `GtOREB` | `gt_oreb_nullable` | no |
  | `GtPF` | `gt_pf_nullable` | no |
  | `GtPTS` | `gt_pts_nullable` | no |
  | `GtREB` | `gt_reb_nullable` | no |
  | `GtSTL` | `gt_stl_nullable` | no |
  | `GtTD` | `gt_td_nullable` | no |
  | `GtTOV` | `gt_tov_nullable` | no |
  | `LeagueID` | `league_id_nullable` | no |
  | `Location` | `location_nullable` | no |
  | `LtAST` | `lt_ast_nullable` | no |
  | `LtBLK` | `lt_blk_nullable` | no |
  | `LtDD` | `lt_dd_nullable` | no |
  | `LtDREB` | `lt_dreb_nullable` | no |
  | `LtFG3A` | `lt_fg3a_nullable` | no |
  | `LtFG3M` | `lt_fg3m_nullable` | no |
  | `LtFG3_PCT` | `lt_fg3_pct_nullable` | no |
  | `LtFGA` | `lt_fga_nullable` | no |
  | `LtFGM` | `lt_fgm_nullable` | no |
  | `LtFG_PCT` | `lt_fg_pct_nullable` | no |
  | `LtFTA` | `lt_fta_nullable` | no |
  | `LtFTM` | `lt_ftm_nullable` | no |
  | `LtFT_PCT` | `lt_ft_pct_nullable` | no |
  | `LtMINUTES` | `lt_minutes_nullable` | no |
  | `LtOREB` | `lt_oreb_nullable` | no |
  | `LtPF` | `lt_pf_nullable` | no |
  | `LtPTS` | `lt_pts_nullable` | no |
  | `LtREB` | `lt_reb_nullable` | no |
  | `LtSTL` | `lt_stl_nullable` | no |
  | `LtTD` | `lt_td_nullable` | no |
  | `LtTOV` | `lt_tov_nullable` | no |
  | `MinGames` | `min_games_nullable` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `PORound` | `po_round_nullable` | no |
  | `PlayerID` | `player_id_nullable` | no |
  | `RookieYear` | `rookie_year_nullable` | no |
  | `Season` | `season_nullable` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_nullable` | no |
  | `StarterBench` | `starter_bench_nullable` | no |
  | `TeamID` | `team_id_nullable` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |
  | `VsTeamID` | `vs_team_id_nullable` | no |
  | `YearsExperience` | `years_experience_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `PlayerGameStreakFinderResults` (9): `PLAYER_NAME_LAST_FIRST`, `PLAYER_ID`, `GAMESTREAK`, `STARTDATE`, `ENDDATE`, `ACTIVESTREAK`, `NUMSEASONS`, `LASTSEASON`, `FIRSTSEASON`

  </details>

### PlayerIndex

- HTTP: `GET https://stats.nba.com/stats/playerindex`
- Repo docs: `docs/nba_api/stats/endpoints/playerindex.md`
- Example output: `docs/nba_api/stats/endpoints_output/playerindex_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import PlayerIndex
  endpoint = PlayerIndex()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `Active` | `active_nullable` | no |
  | `AllStar` | `allstar_nullable` | no |
  | `College` | `college_nullable` | no |
  | `Country` | `country_nullable` | no |
  | `DraftPick` | `draft_pick_nullable` | no |
  | `DraftYear` | `draft_year_nullable` | no |
  | `Height` | `height_nullable` | no |
  | `Historical` | `historical_nullable` | no |
  | `LeagueID` | `league_id` | no |
  | `PlayerPosition` | `player_position_abbreviation_nullable` | no |
  | `Season` | `season` | no |
  | `TeamID` | `team_id_nullable` | no |
  | `Weight` | `weight_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `PlayerIndex` (26): `PERSON_ID`, `PLAYER_LAST_NAME`, `PLAYER_FIRST_NAME`, `PLAYER_SLUG`, `TEAM_ID`, `TEAM_SLUG`, `IS_DEFUNCT`, `TEAM_CITY`, `TEAM_NAME`, `TEAM_ABBREVIATION`, `JERSEY_NUMBER`, `POSITION`, `HEIGHT`, `WEIGHT`, `COLLEGE`, `COUNTRY`, `DRAFT_YEAR`, `DRAFT_ROUND`, `DRAFT_NUMBER`, `ROSTER_STATUS`, `PTS`, `REB`, `AST`, `STATS_TIMEFRAME`, `FROM_YEAR`, `TO_YEAR`

  </details>

### PlayerNextNGames

- HTTP: `GET https://stats.nba.com/stats/playernextngames`
- Repo docs: `docs/nba_api/stats/endpoints/playernextngames.md`
- Required python args: `player_id`
- Python:
  ```python
  from nba_api.stats.endpoints import PlayerNextNGames
  endpoint = PlayerNextNGames(player_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `PlayerID` | `player_id` | yes |
  | `LeagueID` | `league_id_nullable` | no |
  | `NumberOfGames` | `number_of_games` | no |
  | `Season` | `season_all` | no |
  | `SeasonType` | `season_type_all_star` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `NextNGames` (13): `GAME_ID`, `GAME_DATE`, `HOME_TEAM_ID`, `VISITOR_TEAM_ID`, `HOME_TEAM_NAME`, `VISITOR_TEAM_NAME`, `HOME_TEAM_ABBREVIATION`, `VISITOR_TEAM_ABBREVIATION`, `HOME_TEAM_NICKNAME`, `VISITOR_TEAM_NICKNAME`, `GAME_TIME`, `HOME_WL`, `VISITOR_WL`

  </details>

### PlayerProfileV2

- HTTP: `GET https://stats.nba.com/stats/playerprofilev2`
- Repo docs: `docs/nba_api/stats/endpoints/playerprofilev2.md`
- Example output: `docs/nba_api/stats/endpoints_output/playerprofilev2_output.md`
- Required python args: `player_id`
- Python:
  ```python
  from nba_api.stats.endpoints import PlayerProfileV2
  endpoint = PlayerProfileV2(player_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `PlayerID` | `player_id` | yes |
  | `LeagueID` | `league_id_nullable` | no |
  | `PerMode` | `per_mode36` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `CareerHighs` (11): `PLAYER_ID`, `GAME_ID`, `GAME_DATE`, `VS_TEAM_ID`, `VS_TEAM_CITY`, `VS_TEAM_NAME`, `VS_TEAM_ABBREVIATION`, `STAT`, `STAT_VALUE`, `STAT_ORDER`, `DATE_EST`
  - `CareerTotalsAllStarSeason` (24): `PLAYER_ID`, `LEAGUE_ID`, `TEAM_ID`, `GP`, `GS`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `STL`, `BLK`, `TOV`, `PF`, `PTS`
  - `CareerTotalsCollegeSeason` (24): `PLAYER_ID`, `LEAGUE_ID`, `ORGANIZATION_ID`, `GP`, `GS`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `STL`, `BLK`, `TOV`, `PF`, `PTS`
  - `CareerTotalsPostSeason` (24): `PLAYER_ID`, `LEAGUE_ID`, `TEAM_ID`, `GP`, `GS`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `STL`, `BLK`, `TOV`, `PF`, `PTS`
  - `CareerTotalsPreseason` (24): `PLAYER_ID`, `LEAGUE_ID`, `TEAM_ID`, `GP`, `GS`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `STL`, `BLK`, `TOV`, `PF`, `PTS`
  - `CareerTotalsRegularSeason` (24): `PLAYER_ID`, `LEAGUE_ID`, `TEAM_ID`, `GP`, `GS`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `STL`, `BLK`, `TOV`, `PF`, `PTS`
  - `NextGame` (12): `GAME_ID`, `GAME_DATE`, `GAME_TIME`, `LOCATION`, `PLAYER_TEAM_ID`, `PLAYER_TEAM_CITY`, `PLAYER_TEAM_NICKNAME`, `PLAYER_TEAM_ABBREVIATION`, `VS_TEAM_ID`, `VS_TEAM_CITY`, `VS_TEAM_NICKNAME`, `VS_TEAM_ABBREVIATION`
  - `SeasonHighs` (10): `PLAYER_ID`, `GAME_DATE`, `VS_TEAM_ID`, `VS_TEAM_CITY`, `VS_TEAM_NAME`, `VS_TEAM_ABBREVIATION`, `STAT`, `STATS_VALUE`, `STAT_ORDER`, `DATE_EST`
  - `SeasonRankingsPostSeason` (27): `PLAYER_ID`, `SEASON_ID`, `LEAGUE_ID`, `TEAM_ID`, `TEAM_ABBREVIATION`, `PLAYER_AGE`, `GP`, `GS`, `RANK_MIN`, `RANK_FGM`, `RANK_FGA`, `RANK_FG_PCT`, `RANK_FG3M`, `RANK_FG3A`, `RANK_FG3_PCT`, `RANK_FTM`, `RANK_FTA`, `RANK_FT_PCT`, `RANK_OREB`, `RANK_DREB`, `RANK_REB`, `RANK_AST`, `RANK_STL`, `RANK_BLK`, `RANK_TOV`, `RANK_PTS`, `RANK_EFF`
  - `SeasonRankingsRegularSeason` (27): `PLAYER_ID`, `SEASON_ID`, `LEAGUE_ID`, `TEAM_ID`, `TEAM_ABBREVIATION`, `PLAYER_AGE`, `GP`, `GS`, `RANK_MIN`, `RANK_FGM`, `RANK_FGA`, `RANK_FG_PCT`, `RANK_FG3M`, `RANK_FG3A`, `RANK_FG3_PCT`, `RANK_FTM`, `RANK_FTA`, `RANK_FT_PCT`, `RANK_OREB`, `RANK_DREB`, `RANK_REB`, `RANK_AST`, `RANK_STL`, `RANK_BLK`, `RANK_TOV`, `RANK_PTS`, `RANK_EFF`
  - `SeasonTotalsAllStarSeason` (27): `PLAYER_ID`, `SEASON_ID`, `LEAGUE_ID`, `TEAM_ID`, `TEAM_ABBREVIATION`, `PLAYER_AGE`, `GP`, `GS`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `STL`, `BLK`, `TOV`, `PF`, `PTS`
  - `SeasonTotalsCollegeSeason` (27): `PLAYER_ID`, `SEASON_ID`, `LEAGUE_ID`, `ORGANIZATION_ID`, `SCHOOL_NAME`, `PLAYER_AGE`, `GP`, `GS`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `STL`, `BLK`, `TOV`, `PF`, `PTS`
  - `SeasonTotalsPostSeason` (27): `PLAYER_ID`, `SEASON_ID`, `LEAGUE_ID`, `TEAM_ID`, `TEAM_ABBREVIATION`, `PLAYER_AGE`, `GP`, `GS`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `STL`, `BLK`, `TOV`, `PF`, `PTS`
  - `SeasonTotalsPreseason` (27): `PLAYER_ID`, `SEASON_ID`, `LEAGUE_ID`, `TEAM_ID`, `TEAM_ABBREVIATION`, `PLAYER_AGE`, `GP`, `GS`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `STL`, `BLK`, `TOV`, `PF`, `PTS`
  - `SeasonTotalsRegularSeason` (27): `PLAYER_ID`, `SEASON_ID`, `LEAGUE_ID`, `TEAM_ID`, `TEAM_ABBREVIATION`, `PLAYER_AGE`, `GP`, `GS`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `STL`, `BLK`, `TOV`, `PF`, `PTS`

  </details>

### PlayerVsPlayer

- HTTP: `GET https://stats.nba.com/stats/playervsplayer`
- Repo docs: `docs/nba_api/stats/endpoints/playervsplayer.md`
- Example output: `docs/nba_api/stats/endpoints_output/playervsplayer_output.md`
- Required python args: `vs_player_id`, `player_id`
- Python:
  ```python
  from nba_api.stats.endpoints import PlayerVsPlayer
  endpoint = PlayerVsPlayer(vs_player_id='…', player_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `PlayerID` | `player_id` | yes |
  | `VsPlayerID` | `vs_player_id` | yes |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `GameSegment` | `game_segment_nullable` | no |
  | `LastNGames` | `last_n_games` | no |
  | `LeagueID` | `league_id_nullable` | no |
  | `Location` | `location_nullable` | no |
  | `MeasureType` | `measure_type_detailed_defense` | no |
  | `Month` | `month` | no |
  | `OpponentTeamID` | `opponent_team_id` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `PaceAdjust` | `pace_adjust` | no |
  | `PerMode` | `per_mode_detailed` | no |
  | `Period` | `period` | no |
  | `PlusMinus` | `plus_minus` | no |
  | `Rank` | `rank` | no |
  | `Season` | `season` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_playoffs` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `OnOffCourt` (35): `GROUP_SET`, `PLAYER_ID`, `PLAYER_NAME`, `VS_PLAYER_ID`, `VS_PLAYER_NAME`, `COURT_STATUS`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `NBA_FANTASY_PTS`, `CFID`, `CFPARAMS`
  - `Overall` (33): `GROUP_SET`, `GROUP_VALUE`, `PLAYER_ID`, `PLAYER_NAME`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `NBA_FANTASY_PTS`, `CFID`, `CFPARAMS`
  - `PlayerInfo` (10): `PERSON_ID`, `FIRST_NAME`, `LAST_NAME`, `DISPLAY_FIRST_LAST`, `DISPLAY_LAST_COMMA_FIRST`, `DISPLAY_FI_LAST`, `BIRTHDATE`, `SCHOOL`, `COUNTRY`, `LAST_AFFILIATION`
  - `ShotAreaOffCourt` (12): `GROUP_SET`, `PLAYER_ID`, `PLAYER_NAME`, `VS_PLAYER_ID`, `VS_PLAYER_NAME`, `COURT_STATUS`, `GROUP_VALUE`, `FGM`, `FGA`, `FG_PCT`, `CFID`, `CFPARAMS`
  - `ShotAreaOnCourt` (12): `GROUP_SET`, `PLAYER_ID`, `PLAYER_NAME`, `VS_PLAYER_ID`, `VS_PLAYER_NAME`, `COURT_STATUS`, `GROUP_VALUE`, `FGM`, `FGA`, `FG_PCT`, `CFID`, `CFPARAMS`
  - `ShotAreaOverall` (9): `GROUP_SET`, `GROUP_VALUE`, `PLAYER_ID`, `PLAYER_NAME`, `FGM`, `FGA`, `FG_PCT`, `CFID`, `CFPARAMS`
  - `ShotDistanceOffCourt` (12): `GROUP_SET`, `PLAYER_ID`, `PLAYER_NAME`, `VS_PLAYER_ID`, `VS_PLAYER_NAME`, `COURT_STATUS`, `GROUP_VALUE`, `FGM`, `FGA`, `FG_PCT`, `CFID`, `CFPARAMS`
  - `ShotDistanceOnCourt` (12): `GROUP_SET`, `PLAYER_ID`, `PLAYER_NAME`, `VS_PLAYER_ID`, `VS_PLAYER_NAME`, `COURT_STATUS`, `GROUP_VALUE`, `FGM`, `FGA`, `FG_PCT`, `CFID`, `CFPARAMS`
  - `ShotDistanceOverall` (9): `GROUP_SET`, `GROUP_VALUE`, `PLAYER_ID`, `PLAYER_NAME`, `FGM`, `FGA`, `FG_PCT`, `CFID`, `CFPARAMS`
  - `VsPlayerInfo` (10): `PERSON_ID`, `FIRST_NAME`, `LAST_NAME`, `DISPLAY_FIRST_LAST`, `DISPLAY_LAST_COMMA_FIRST`, `DISPLAY_FI_LAST`, `BIRTHDATE`, `SCHOOL`, `COUNTRY`, `LAST_AFFILIATION`

  </details>

### PlayoffPicture

- HTTP: `GET https://stats.nba.com/stats/playoffpicture`
- Repo docs: `docs/nba_api/stats/endpoints/playoffpicture.md`
- Example output: `docs/nba_api/stats/endpoints_output/playoffpicture_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import PlayoffPicture
  endpoint = PlayoffPicture()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `LeagueID` | `league_id` | no |
  | `SeasonID` | `season_id` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `EastConfPlayoffPicture` (12): `CONFERENCE`, `HIGH_SEED_RANK`, `HIGH_SEED_TEAM`, `HIGH_SEED_TEAM_ID`, `LOW_SEED_RANK`, `LOW_SEED_TEAM`, `LOW_SEED_TEAM_ID`, `HIGH_SEED_SERIES_W`, `HIGH_SEED_SERIES_L`, `HIGH_SEED_SERIES_REMAINING_G`, `HIGH_SEED_SERIES_REMAINING_HOME_G`, `HIGH_SEED_SERIES_REMAINING_AWAY_G`
  - `EastConfRemainingGames` (5): `TEAM`, `TEAM_ID`, `REMAINING_G`, `REMAINING_HOME_G`, `REMAINING_AWAY_G`
  - `EastConfStandings` (60): `CONFERENCE`, `RANK`, `TEAM`, `TEAM_SLUG`, `TEAM_ID`, `WINS`, `LOSSES`, `PCT`, `DIV`, `CONF`, `HOME`, `AWAY`, `GB`, `GR_OVER_500`, `GR_OVER_500_HOME`, `GR_OVER_500_AWAY`, `GR_UNDER_500`, `GR_UNDER_500_HOME`, `GR_UNDER_500_AWAY`, `RANKING_CRITERIA`, `CLINCHED_PLAYOFFS`, `CLINCHED_CONFERENCE`, `CLINCHED_DIVISION`, `Clinched_Play_In`, `ELIMINATED_PLAYOFFS`, `SOSA_REMAINING`, `ReturnToPlay_East_PI_Flag`, `ReturnToPlay_Already_Eliminated`, `Seeding_Game_1_Outcome`, `Seeding_Game_2_Outcome`, `Seeding_Game_3_Outcome`, `Seeding_Game_4_Outcome`, `Seeding_Game_5_Outcome`, `Seeding_Game_6_Outcome`, `Seeding_Game_7_Outcome`, `Seeding_Game_8_Outcome`, `Seeding_Game_1_ID`, `Seeding_Game_2_ID`, `Seeding_Game_3_ID`, `Seeding_Game_4_ID`, `Seeding_Game_5_ID`, `Seeding_Game_6_ID`, `Seeding_Game_7_ID`, `Seeding_Game_8_ID`, `Seeding_Game_1_Opponent`, `Seeding_Game_2_Opponent`, `Seeding_Game_3_Opponent`, `Seeding_Game_4_Opponent`, `Seeding_Game_5_Opponent`, `Seeding_Game_6_Opponent`, `Seeding_Game_7_Opponent`, `Seeding_Game_8_Opponent`, `Seeding_Game_1_Label`, `Seeding_Game_2_Label`, `Seeding_Game_3_Label`, `Seeding_Game_4_Label`, `Seeding_Game_5_Label`, `Seeding_Game_6_Label`, `Seeding_Game_7_Label`, `Seeding_Game_8_Label`
  - `WestConfPlayoffPicture` (12): `CONFERENCE`, `HIGH_SEED_RANK`, `HIGH_SEED_TEAM`, `HIGH_SEED_TEAM_ID`, `LOW_SEED_RANK`, `LOW_SEED_TEAM`, `LOW_SEED_TEAM_ID`, `HIGH_SEED_SERIES_W`, `HIGH_SEED_SERIES_L`, `HIGH_SEED_SERIES_REMAINING_G`, `HIGH_SEED_SERIES_REMAINING_HOME_G`, `HIGH_SEED_SERIES_REMAINING_AWAY_G`
  - `WestConfRemainingGames` (5): `TEAM`, `TEAM_ID`, `REMAINING_G`, `REMAINING_HOME_G`, `REMAINING_AWAY_G`
  - `WestConfStandings` (60): `CONFERENCE`, `RANK`, `TEAM`, `TEAM_SLUG`, `TEAM_ID`, `WINS`, `LOSSES`, `PCT`, `DIV`, `CONF`, `HOME`, `AWAY`, `GB`, `GR_OVER_500`, `GR_OVER_500_HOME`, `GR_OVER_500_AWAY`, `GR_UNDER_500`, `GR_UNDER_500_HOME`, `GR_UNDER_500_AWAY`, `RANKING_CRITERIA`, `CLINCHED_PLAYOFFS`, `CLINCHED_CONFERENCE`, `CLINCHED_DIVISION`, `Clinched_Play_In`, `ELIMINATED_PLAYOFFS`, `SOSA_REMAINING`, `ReturnToPlay_West_PI_Flag`, `ReturnToPlay_Already_Eliminated`, `Seeding_Game_1_Outcome`, `Seeding_Game_2_Outcome`, `Seeding_Game_3_Outcome`, `Seeding_Game_4_Outcome`, `Seeding_Game_5_Outcome`, `Seeding_Game_6_Outcome`, `Seeding_Game_7_Outcome`, `Seeding_Game_8_Outcome`, `Seeding_Game_1_ID`, `Seeding_Game_2_ID`, `Seeding_Game_3_ID`, `Seeding_Game_4_ID`, `Seeding_Game_5_ID`, `Seeding_Game_6_ID`, `Seeding_Game_7_ID`, `Seeding_Game_8_ID`, `Seeding_Game_1_Opponent`, `Seeding_Game_2_Opponent`, `Seeding_Game_3_Opponent`, `Seeding_Game_4_Opponent`, `Seeding_Game_5_Opponent`, `Seeding_Game_6_Opponent`, `Seeding_Game_7_Opponent`, `Seeding_Game_8_Opponent`, `Seeding_Game_1_Label`, `Seeding_Game_2_Label`, `Seeding_Game_3_Label`, `Seeding_Game_4_Label`, `Seeding_Game_5_Label`, `Seeding_Game_6_Label`, `Seeding_Game_7_Label`, `Seeding_Game_8_Label`

  </details>

### ScheduleLeagueV2

- HTTP: `GET https://stats.nba.com/stats/scheduleleaguev2`
- Repo docs: `docs/nba_api/stats/endpoints/scheduleleaguev2.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import ScheduleLeagueV2
  endpoint = ScheduleLeagueV2()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `LeagueID` | `league_id` | no |
  | `Season` | `season` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `SeasonGames` (139): `leagueId`, `seasonYear`, `gameDate`, `gameId`, `gameCode`, `gameStatus`, `gameStatusText`, `gameSequence`, `gameDateEst`, `gameTimeEst`, `gameDateTimeEst`, `gameDateUTC`, `gameTimeUTC`, `gameDateTimeUTC`, `awayTeamTime`, `homeTeamTime`, `day`, `monthNum`, `weekNumber`, `weekName`, `ifNecessary`, `seriesGameNumber`, `gameLabel`, `gameSubLabel`, `seriesText`, `arenaName`, `arenaState`, `arenaCity`, `postponedStatus`, `branchLink`, `gameSubtype`, `isNeutral`, `homeTeam_teamId`, `homeTeam_teamName`, `homeTeam_teamCity`, `homeTeam_teamTricode`, `homeTeam_teamSlug`, `homeTeam_wins`, `homeTeam_losses`, `homeTeam_score`, `homeTeam_seed`, `awayTeam_teamId`, `awayTeam_teamName`, `awayTeam_teamCity`, `awayTeam_teamTricode`, `awayTeam_teamSlug`, `awayTeam_wins`, `awayTeam_losses`, `awayTeam_score`, `awayTeam_seed`, `pointsLeaders_personId`, `pointsLeaders_firstName`, `pointsLeaders_lastName`, `pointsLeaders_teamId`, `pointsLeaders_teamCity`, `pointsLeaders_teamName`, `pointsLeaders_teamTricode`, `pointsLeaders_points`, `nationalBroadcasters_broadcasterScope`, `nationalBroadcasters_broadcasterMedia`, `nationalBroadcasters_broadcasterId`, `nationalBroadcasters_broadcasterDisplay`, `nationalBroadcasters_broadcasterAbbreviation`, `nationalBroadcasters_tapeDelayComments`, `nationalBroadcasters_broadcasterVideoLink`, `nationalBroadcasters_broadcasterDescription`, `nationalBroadcasters_broadcasterTeamId`, `nationalRadioBroadcasters_broadcasterScope`, `nationalRadioBroadcasters_broadcasterMedia`, `nationalRadioBroadcasters_broadcasterId`, `nationalRadioBroadcasters_broadcasterDisplay`, `nationalRadioBroadcasters_broadcasterAbbreviation`, `nationalRadioBroadcasters_tapeDelayComments`, `nationalRadioBroadcasters_broadcasterVideoLink`, `nationalRadioBroadcasters_broadcasterDescription`, `nationalRadioBroadcasters_broadcasterTeamId`, `nationalOttBroadcasters_broadcasterScope`, `nationalOttBroadcasters_broadcasterMedia`, `nationalOttBroadcasters_broadcasterId`, `nationalOttBroadcasters_broadcasterDisplay`, `nationalOttBroadcasters_broadcasterAbbreviation`, `nationalOttBroadcasters_tapeDelayComments`, `nationalOttBroadcasters_broadcasterVideoLink`, `nationalOttBroadcasters_broadcasterDescription`, `nationalOttBroadcasters_broadcasterTeamId`, `homeTvBroadcasters_broadcasterScope`, `homeTvBroadcasters_broadcasterMedia`, `homeTvBroadcasters_broadcasterId`, `homeTvBroadcasters_broadcasterDisplay`, `homeTvBroadcasters_broadcasterAbbreviation`, `homeTvBroadcasters_tapeDelayComments`, `homeTvBroadcasters_broadcasterVideoLink`, `homeTvBroadcasters_broadcasterDescription`, `homeTvBroadcasters_broadcasterTeamId`, `homeRadioBroadcasters_broadcasterScope`, `homeRadioBroadcasters_broadcasterMedia`, `homeRadioBroadcasters_broadcasterId`, `homeRadioBroadcasters_broadcasterDisplay`, `homeRadioBroadcasters_broadcasterAbbreviation`, `homeRadioBroadcasters_tapeDelayComments`, `homeRadioBroadcasters_broadcasterVideoLink`, `homeRadioBroadcasters_broadcasterDescription`, `homeRadioBroadcasters_broadcasterTeamId`, `homeOttBroadcasters_broadcasterScope`, `homeOttBroadcasters_broadcasterMedia`, `homeOttBroadcasters_broadcasterId`, `homeOttBroadcasters_broadcasterDisplay`, `homeOttBroadcasters_broadcasterAbbreviation`, `homeOttBroadcasters_tapeDelayComments`, `homeOttBroadcasters_broadcasterVideoLink`, `homeOttBroadcasters_broadcasterDescription`, `homeOttBroadcasters_broadcasterTeamId`, `awayTvBroadcasters_broadcasterScope`, `awayTvBroadcasters_broadcasterMedia`, `awayTvBroadcasters_broadcasterId`, `awayTvBroadcasters_broadcasterDisplay`, `awayTvBroadcasters_broadcasterAbbreviation`, `awayTvBroadcasters_tapeDelayComments`, `awayTvBroadcasters_broadcasterVideoLink`, `awayTvBroadcasters_broadcasterDescription`, `awayTvBroadcasters_broadcasterTeamId`, `awayRadioBroadcasters_broadcasterScope`, `awayRadioBroadcasters_broadcasterMedia`, `awayRadioBroadcasters_broadcasterId`, `awayRadioBroadcasters_broadcasterDisplay`, `awayRadioBroadcasters_broadcasterAbbreviation`, `awayRadioBroadcasters_tapeDelayComments`, `awayRadioBroadcasters_broadcasterVideoLink`, `awayRadioBroadcasters_broadcasterDescription`, `awayRadioBroadcasters_broadcasterTeamId`, `awayOttBroadcasters_broadcasterScope`, `awayOttBroadcasters_broadcasterMedia`, `awayOttBroadcasters_broadcasterId`, `awayOttBroadcasters_broadcasterDisplay`, `awayOttBroadcasters_broadcasterAbbreviation`, `awayOttBroadcasters_tapeDelayComments`, `awayOttBroadcasters_broadcasterVideoLink`, `awayOttBroadcasters_broadcasterDescription`, `awayOttBroadcasters_broadcasterTeamId`
  - `SeasonWeeks` (6): `leagueId`, `seasonYear`, `weekNumber`, `weekName`, `startDate`, `endDate`

  </details>

### ScheduleLeagueV2Int

- HTTP: `GET https://stats.nba.com/stats/scheduleleaguev2int`
- Repo docs: `docs/nba_api/stats/endpoints/scheduleleaguev2int.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import ScheduleLeagueV2Int
  endpoint = ScheduleLeagueV2Int()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `LeagueID` | `league_id` | no |
  | `Season` | `season` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `SeasonGames` (139): `leagueId`, `seasonYear`, `gameDate`, `gameId`, `gameCode`, `gameStatus`, `gameStatusText`, `gameSequence`, `gameDateEst`, `gameTimeEst`, `gameDateTimeEst`, `gameDateUTC`, `gameTimeUTC`, `gameDateTimeUTC`, `awayTeamTime`, `homeTeamTime`, `day`, `monthNum`, `weekNumber`, `weekName`, `ifNecessary`, `seriesGameNumber`, `gameLabel`, `gameSubLabel`, `seriesText`, `arenaName`, `arenaState`, `arenaCity`, `postponedStatus`, `branchLink`, `gameSubtype`, `isNeutral`, `homeTeam_teamId`, `homeTeam_teamName`, `homeTeam_teamCity`, `homeTeam_teamTricode`, `homeTeam_teamSlug`, `homeTeam_wins`, `homeTeam_losses`, `homeTeam_score`, `homeTeam_seed`, `awayTeam_teamId`, `awayTeam_teamName`, `awayTeam_teamCity`, `awayTeam_teamTricode`, `awayTeam_teamSlug`, `awayTeam_wins`, `awayTeam_losses`, `awayTeam_score`, `awayTeam_seed`, `pointsLeaders_personId`, `pointsLeaders_firstName`, `pointsLeaders_lastName`, `pointsLeaders_teamId`, `pointsLeaders_teamCity`, `pointsLeaders_teamName`, `pointsLeaders_teamTricode`, `pointsLeaders_points`, `nationalBroadcasters_broadcasterScope`, `nationalBroadcasters_broadcasterMedia`, `nationalBroadcasters_broadcasterId`, `nationalBroadcasters_broadcasterDisplay`, `nationalBroadcasters_broadcasterAbbreviation`, `nationalBroadcasters_tapeDelayComments`, `nationalBroadcasters_broadcasterVideoLink`, `nationalBroadcasters_broadcasterDescription`, `nationalBroadcasters_broadcasterTeamId`, `nationalRadioBroadcasters_broadcasterScope`, `nationalRadioBroadcasters_broadcasterMedia`, `nationalRadioBroadcasters_broadcasterId`, `nationalRadioBroadcasters_broadcasterDisplay`, `nationalRadioBroadcasters_broadcasterAbbreviation`, `nationalRadioBroadcasters_tapeDelayComments`, `nationalRadioBroadcasters_broadcasterVideoLink`, `nationalRadioBroadcasters_broadcasterDescription`, `nationalRadioBroadcasters_broadcasterTeamId`, `nationalOttBroadcasters_broadcasterScope`, `nationalOttBroadcasters_broadcasterMedia`, `nationalOttBroadcasters_broadcasterId`, `nationalOttBroadcasters_broadcasterDisplay`, `nationalOttBroadcasters_broadcasterAbbreviation`, `nationalOttBroadcasters_tapeDelayComments`, `nationalOttBroadcasters_broadcasterVideoLink`, `nationalOttBroadcasters_broadcasterDescription`, `nationalOttBroadcasters_broadcasterTeamId`, `homeTvBroadcasters_broadcasterScope`, `homeTvBroadcasters_broadcasterMedia`, `homeTvBroadcasters_broadcasterId`, `homeTvBroadcasters_broadcasterDisplay`, `homeTvBroadcasters_broadcasterAbbreviation`, `homeTvBroadcasters_tapeDelayComments`, `homeTvBroadcasters_broadcasterVideoLink`, `homeTvBroadcasters_broadcasterDescription`, `homeTvBroadcasters_broadcasterTeamId`, `homeRadioBroadcasters_broadcasterScope`, `homeRadioBroadcasters_broadcasterMedia`, `homeRadioBroadcasters_broadcasterId`, `homeRadioBroadcasters_broadcasterDisplay`, `homeRadioBroadcasters_broadcasterAbbreviation`, `homeRadioBroadcasters_tapeDelayComments`, `homeRadioBroadcasters_broadcasterVideoLink`, `homeRadioBroadcasters_broadcasterDescription`, `homeRadioBroadcasters_broadcasterTeamId`, `homeOttBroadcasters_broadcasterScope`, `homeOttBroadcasters_broadcasterMedia`, `homeOttBroadcasters_broadcasterId`, `homeOttBroadcasters_broadcasterDisplay`, `homeOttBroadcasters_broadcasterAbbreviation`, `homeOttBroadcasters_tapeDelayComments`, `homeOttBroadcasters_broadcasterVideoLink`, `homeOttBroadcasters_broadcasterDescription`, `homeOttBroadcasters_broadcasterTeamId`, `awayTvBroadcasters_broadcasterScope`, `awayTvBroadcasters_broadcasterMedia`, `awayTvBroadcasters_broadcasterId`, `awayTvBroadcasters_broadcasterDisplay`, `awayTvBroadcasters_broadcasterAbbreviation`, `awayTvBroadcasters_tapeDelayComments`, `awayTvBroadcasters_broadcasterVideoLink`, `awayTvBroadcasters_broadcasterDescription`, `awayTvBroadcasters_broadcasterTeamId`, `awayRadioBroadcasters_broadcasterScope`, `awayRadioBroadcasters_broadcasterMedia`, `awayRadioBroadcasters_broadcasterId`, `awayRadioBroadcasters_broadcasterDisplay`, `awayRadioBroadcasters_broadcasterAbbreviation`, `awayRadioBroadcasters_tapeDelayComments`, `awayRadioBroadcasters_broadcasterVideoLink`, `awayRadioBroadcasters_broadcasterDescription`, `awayRadioBroadcasters_broadcasterTeamId`, `awayOttBroadcasters_broadcasterScope`, `awayOttBroadcasters_broadcasterMedia`, `awayOttBroadcasters_broadcasterId`, `awayOttBroadcasters_broadcasterDisplay`, `awayOttBroadcasters_broadcasterAbbreviation`, `awayOttBroadcasters_tapeDelayComments`, `awayOttBroadcasters_broadcasterVideoLink`, `awayOttBroadcasters_broadcasterDescription`, `awayOttBroadcasters_broadcasterTeamId`
  - `SeasonWeeks` (6): `leagueId`, `seasonYear`, `weekNumber`, `weekName`, `startDate`, `endDate`
  - `BroadcasterList` (6): `leagueId`, `seasonYear`, `broadcasterAbbreviation`, `broadcasterDisplay`, `broadcasterId`, `regionId`

  </details>

### ScoreboardV2

- HTTP: `GET https://stats.nba.com/stats/scoreboardv2`
- Repo docs: `docs/nba_api/stats/endpoints/scoreboardv2.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import ScoreboardV2
  endpoint = ScoreboardV2()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `DayOffset` | `day_offset` | no |
  | `GameDate` | `game_date` | no |
  | `LeagueID` | `league_id` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `Available` (2): `GAME_ID`, `PT_AVAILABLE`
  - `EastConfStandingsByDay` (13): `TEAM_ID`, `LEAGUE_ID`, `SEASON_ID`, `STANDINGSDATE`, `CONFERENCE`, `TEAM`, `G`, `W`, `L`, `W_PCT`, `HOME_RECORD`, `ROAD_RECORD`, `RETURNTOPLAY`
  - `GameHeader` (17): `GAME_DATE_EST`, `GAME_SEQUENCE`, `GAME_ID`, `GAME_STATUS_ID`, `GAME_STATUS_TEXT`, `GAMECODE`, `HOME_TEAM_ID`, `VISITOR_TEAM_ID`, `SEASON`, `LIVE_PERIOD`, `LIVE_PC_TIME`, `NATL_TV_BROADCASTER_ABBREVIATION`, `HOME_TV_BROADCASTER_ABBREVIATION`, `AWAY_TV_BROADCASTER_ABBREVIATION`, `LIVE_PERIOD_TIME_BCAST`, `ARENA_NAME`, `WH_STATUS`
  - `LastMeeting` (13): `GAME_ID`, `LAST_GAME_ID`, `LAST_GAME_DATE_EST`, `LAST_GAME_HOME_TEAM_ID`, `LAST_GAME_HOME_TEAM_CITY`, `LAST_GAME_HOME_TEAM_NAME`, `LAST_GAME_HOME_TEAM_ABBREVIATION`, `LAST_GAME_HOME_TEAM_POINTS`, `LAST_GAME_VISITOR_TEAM_ID`, `LAST_GAME_VISITOR_TEAM_CITY`, `LAST_GAME_VISITOR_TEAM_NAME`, `LAST_GAME_VISITOR_TEAM_CITY1`, `LAST_GAME_VISITOR_TEAM_POINTS`
  - `LineScore` (29): `GAME_DATE_EST`, `GAME_SEQUENCE`, `GAME_ID`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_CITY_NAME`, `TEAM_NAME`, `TEAM_WINS_LOSSES`, `PTS_QTR1`, `PTS_QTR2`, `PTS_QTR3`, `PTS_QTR4`, `PTS_OT1`, `PTS_OT2`, `PTS_OT3`, `PTS_OT4`, `PTS_OT5`, `PTS_OT6`, `PTS_OT7`, `PTS_OT8`, `PTS_OT9`, `PTS_OT10`, `PTS`, `FG_PCT`, `FT_PCT`, `FG3_PCT`, `AST`, `REB`, `TOV`
  - `SeriesStandings` (7): `GAME_ID`, `HOME_TEAM_ID`, `VISITOR_TEAM_ID`, `GAME_DATE_EST`, `HOME_TEAM_WINS`, `HOME_TEAM_LOSSES`, `SERIES_LEADER`
  - `TeamLeaders` (14): `GAME_ID`, `TEAM_ID`, `TEAM_CITY`, `TEAM_NICKNAME`, `TEAM_ABBREVIATION`, `PTS_PLAYER_ID`, `PTS_PLAYER_NAME`, `PTS`, `REB_PLAYER_ID`, `REB_PLAYER_NAME`, `REB`, `AST_PLAYER_ID`, `AST_PLAYER_NAME`, `AST`
  - `TicketLinks` (2): `GAME_ID`, `LEAG_TIX`
  - `WestConfStandingsByDay` (12): `TEAM_ID`, `LEAGUE_ID`, `SEASON_ID`, `STANDINGSDATE`, `CONFERENCE`, `TEAM`, `G`, `W`, `L`, `W_PCT`, `HOME_RECORD`, `ROAD_RECORD`
  - `WinProbability`

  </details>

### ScoreboardV3

- HTTP: `GET https://stats.nba.com/stats/scoreboardv3`
- Required python args: `game_date`
- Python:
  ```python
  from nba_api.stats.endpoints import ScoreboardV3
  endpoint = ScoreboardV3(game_date='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `GameDate` | `game_date` | yes |
  | `LeagueID` | `league_id` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `ScoreboardInfo` (3): `gameDate`, `leagueId`, `leagueName`
  - `GameHeader` (18): `gameId`, `gameCode`, `gameStatus`, `gameStatusText`, `period`, `gameClock`, `gameTimeUTC`, `gameEt`, `regulationPeriods`, `seriesGameNumber`, `gameLabel`, `gameSubLabel`, `seriesText`, `ifNecessary`, `seriesConference`, `poRoundDesc`, `gameSubtype`, `isNeutral`
  - `LineScore` (12): `gameId`, `teamId`, `teamCity`, `teamName`, `teamTricode`, `teamSlug`, `wins`, `losses`, `score`, `seed`, `inBonus`, `timeoutsRemaining`
  - `GameLeaders` (12): `gameId`, `teamId`, `leaderType`, `personId`, `name`, `playerSlug`, `jerseyNum`, `position`, `teamTricode`, `points`, `rebounds`, `assists`
  - `TeamLeaders` (13): `gameId`, `teamId`, `leaderType`, `personId`, `name`, `playerSlug`, `jerseyNum`, `position`, `teamTricode`, `points`, `rebounds`, `assists`, `seasonLeadersFlag`
  - `Broadcasters` (6): `gameId`, `broadcasterType`, `broadcasterId`, `broadcastDisplay`, `broadcasterTeamId`, `broadcasterDescription`

  </details>

### ShotChartDetail

- HTTP: `GET https://stats.nba.com/stats/shotchartdetail`
- Repo docs: `docs/nba_api/stats/endpoints/shotchartdetail.md`
- Example output: `docs/nba_api/stats/endpoints_output/shotchartdetail_output.md`
- Required python args: `team_id`, `player_id`
- Python:
  ```python
  from nba_api.stats.endpoints import ShotChartDetail
  endpoint = ShotChartDetail(team_id='…', player_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `PlayerID` | `player_id` | yes |
  | `TeamID` | `team_id` | yes |
  | `AheadBehind` | `ahead_behind_nullable` | no |
  | `ClutchTime` | `clutch_time_nullable` | no |
  | `ContextFilter` | `context_filter_nullable` | no |
  | `ContextMeasure` | `context_measure_simple` | no |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `EndPeriod` | `end_period_nullable` | no |
  | `EndRange` | `end_range_nullable` | no |
  | `GameID` | `game_id_nullable` | no |
  | `GameSegment` | `game_segment_nullable` | no |
  | `LastNGames` | `last_n_games` | no |
  | `LeagueID` | `league_id` | no |
  | `Location` | `location_nullable` | no |
  | `Month` | `month` | no |
  | `OpponentTeamID` | `opponent_team_id` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `Period` | `period` | no |
  | `PlayerPosition` | `player_position_nullable` | no |
  | `PointDiff` | `point_diff_nullable` | no |
  | `Position` | `position_nullable` | no |
  | `RangeType` | `range_type_nullable` | no |
  | `RookieYear` | `rookie_year_nullable` | no |
  | `Season` | `season_nullable` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_all_star` | no |
  | `StartPeriod` | `start_period_nullable` | no |
  | `StartRange` | `start_range_nullable` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `LeagueAverages` (7): `GRID_TYPE`, `SHOT_ZONE_BASIC`, `SHOT_ZONE_AREA`, `SHOT_ZONE_RANGE`, `FGA`, `FGM`, `FG_PCT`
  - `Shot_Chart_Detail` (24): `GRID_TYPE`, `GAME_ID`, `GAME_EVENT_ID`, `PLAYER_ID`, `PLAYER_NAME`, `TEAM_ID`, `TEAM_NAME`, `PERIOD`, `MINUTES_REMAINING`, `SECONDS_REMAINING`, `EVENT_TYPE`, `ACTION_TYPE`, `SHOT_TYPE`, `SHOT_ZONE_BASIC`, `SHOT_ZONE_AREA`, `SHOT_ZONE_RANGE`, `SHOT_DISTANCE`, `LOC_X`, `LOC_Y`, `SHOT_ATTEMPTED_FLAG`, `SHOT_MADE_FLAG`, `GAME_DATE`, `HTM`, `VTM`

  </details>

### ShotChartLeagueWide

- HTTP: `GET https://stats.nba.com/stats/shotchartleaguewide`
- Repo docs: `docs/nba_api/stats/endpoints/shotchartleaguewide.md`
- Example output: `docs/nba_api/stats/endpoints_output/shotchartleaguewide_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import ShotChartLeagueWide
  endpoint = ShotChartLeagueWide()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `LeagueID` | `league_id` | no |
  | `Season` | `season` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `League_Wide` (7): `GRID_TYPE`, `SHOT_ZONE_BASIC`, `SHOT_ZONE_AREA`, `SHOT_ZONE_RANGE`, `FGA`, `FGM`, `FG_PCT`

  </details>

### ShotChartLineupDetail

- HTTP: `GET https://stats.nba.com/stats/shotchartlineupdetail`
- Repo docs: `docs/nba_api/stats/endpoints/shotchartlineupdetail.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import ShotChartLineupDetail
  endpoint = ShotChartLineupDetail()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `ContextFilter` | `context_filter_nullable` | no |
  | `ContextMeasure` | `context_measure_detailed` | no |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `GROUP_ID` | `group_id` | no |
  | `GameID` | `game_id_nullable` | no |
  | `GameSegment` | `game_segment_nullable` | no |
  | `LastNGames` | `last_n_games_nullable` | no |
  | `LeagueID` | `league_id` | no |
  | `Location` | `location_nullable` | no |
  | `Month` | `month_nullable` | no |
  | `OpponentTeamID` | `opponent_team_id_nullable` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `Period` | `period` | no |
  | `Season` | `season` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_all_star` | no |
  | `TeamID` | `team_id_nullable` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `ShotChartLineupDetail` (26): `GRID_TYPE`, `GAME_ID`, `GAME_EVENT_ID`, `GROUP_ID`, `GROUP_NAME`, `PLAYER_ID`, `PLAYER_NAME`, `TEAM_ID`, `TEAM_NAME`, `PERIOD`, `MINUTES_REMAINING`, `SECONDS_REMAINING`, `EVENT_TYPE`, `ACTION_TYPE`, `SHOT_TYPE`, `SHOT_ZONE_BASIC`, `SHOT_ZONE_AREA`, `SHOT_ZONE_RANGE`, `SHOT_DISTANCE`, `LOC_X`, `LOC_Y`, `SHOT_ATTEMPTED_FLAG`, `SHOT_MADE_FLAG`, `GAME_DATE`, `HTM`, `VTM`
  - `ShotChartLineupLeagueAverage` (7): `GRID_TYPE`, `SHOT_ZONE_BASIC`, `SHOT_ZONE_AREA`, `SHOT_ZONE_RANGE`, `FGA`, `FGM`, `FG_PCT`

  </details>

### SynergyPlayTypes

- HTTP: `GET https://stats.nba.com/stats/synergyplaytypes`
- Repo docs: `docs/nba_api/stats/endpoints/synergyplaytypes.md`
- Example output: `docs/nba_api/stats/endpoints_output/synergyplaytypes_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import SynergyPlayTypes
  endpoint = SynergyPlayTypes()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `LeagueID` | `league_id` | no |
  | `PerMode` | `per_mode_simple` | no |
  | `PlayType` | `play_type_nullable` | no |
  | `PlayerOrTeam` | `player_or_team_abbreviation` | no |
  | `SeasonType` | `season_type_all_star` | no |
  | `SeasonYear` | `season` | no |
  | `TypeGrouping` | `type_grouping_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `SynergyPlayType` (22): `SEASON_ID`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_NAME`, `PLAY_TYPE`, `TYPE_GROUPING`, `PERCENTILE`, `GP`, `POSS_PCT`, `PPP`, `FG_PCT`, `FT_POSS_PCT`, `TOV_POSS_PCT`, `SF_POSS_PCT`, `PLUSONE_POSS_PCT`, `SCORE_POSS_PCT`, `EFG_PCT`, `POSS`, `PTS`, `FGM`, `FGA`, `FGMX`

  </details>

### TeamAndPlayersVsPlayers

- HTTP: `GET https://stats.nba.com/stats/teamandplayersvsplayers`
- Repo docs: `docs/nba_api/stats/endpoints/teamandplayersvsplayers.md`
- Required python args: `vs_team_id`, `vs_player_id5`, `vs_player_id4`, `vs_player_id3`, `vs_player_id2`, `vs_player_id1`, `team_id`, `player_id5`, `player_id4`, `player_id3`, `player_id2`, `player_id1`
- Python:
  ```python
  from nba_api.stats.endpoints import TeamAndPlayersVsPlayers
  endpoint = TeamAndPlayersVsPlayers(vs_team_id='…', vs_player_id5='…', vs_player_id4='…', vs_player_id3='…', vs_player_id2='…', vs_player_id1='…', team_id='…', player_id5='…', player_id4='…', player_id3='…', player_id2='…', player_id1='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `PlayerID1` | `player_id1` | yes |
  | `PlayerID2` | `player_id2` | yes |
  | `PlayerID3` | `player_id3` | yes |
  | `PlayerID4` | `player_id4` | yes |
  | `PlayerID5` | `player_id5` | yes |
  | `TeamID` | `team_id` | yes |
  | `VsPlayerID1` | `vs_player_id1` | yes |
  | `VsPlayerID2` | `vs_player_id2` | yes |
  | `VsPlayerID3` | `vs_player_id3` | yes |
  | `VsPlayerID4` | `vs_player_id4` | yes |
  | `VsPlayerID5` | `vs_player_id5` | yes |
  | `VsTeamID` | `vs_team_id` | yes |
  | `Conference` | `conference_nullable` | no |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `Division` | `division_simple_nullable` | no |
  | `GameSegment` | `game_segment_nullable` | no |
  | `LastNGames` | `last_n_games` | no |
  | `LeagueID` | `league_id_nullable` | no |
  | `Location` | `location_nullable` | no |
  | `MeasureType` | `measure_type_detailed_defense` | no |
  | `Month` | `month` | no |
  | `OpponentTeamID` | `opponent_team_id` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `PaceAdjust` | `pace_adjust` | no |
  | `PerMode` | `per_mode_detailed` | no |
  | `Period` | `period` | no |
  | `PlusMinus` | `plus_minus` | no |
  | `Rank` | `rank` | no |
  | `Season` | `season` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_playoffs` | no |
  | `ShotClockRange` | `shot_clock_range_nullable` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `PlayersVsPlayers` (25): `GROUP_SET`, `TITLE_DESCRIPTION`, `DESCRIPTION`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`
  - `TeamPlayersVsPlayersOff` (26): `GROUP_SET`, `TITLE_DESCRIPTION`, `PLAYER_ID`, `PLAYER_NAME`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`
  - `TeamPlayersVsPlayersOn` (26): `GROUP_SET`, `TITLE_DESCRIPTION`, `PLAYER_ID`, `PLAYER_NAME`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`
  - `TeamVsPlayers` (25): `GROUP_SET`, `TITLE_DESCRIPTION`, `DESCRIPTION`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`
  - `TeamVsPlayersOff` (25): `GROUP_SET`, `TITLE_DESCRIPTION`, `DESCRIPTION`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`

  </details>

### TeamDashboardByGeneralSplits

- HTTP: `GET https://stats.nba.com/stats/teamdashboardbygeneralsplits`
- Repo docs: `docs/nba_api/stats/endpoints/teamdashboardbygeneralsplits.md`
- Example output: `docs/nba_api/stats/endpoints_output/teamdashboardbygeneralsplits_output.md`
- Required python args: `team_id`
- Python:
  ```python
  from nba_api.stats.endpoints import TeamDashboardByGeneralSplits
  endpoint = TeamDashboardByGeneralSplits(team_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `TeamID` | `team_id` | yes |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `GameSegment` | `game_segment_nullable` | no |
  | `LastNGames` | `last_n_games` | no |
  | `LeagueID` | `league_id_nullable` | no |
  | `Location` | `location_nullable` | no |
  | `MeasureType` | `measure_type_detailed_defense` | no |
  | `Month` | `month` | no |
  | `OpponentTeamID` | `opponent_team_id` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `PORound` | `po_round_nullable` | no |
  | `PaceAdjust` | `pace_adjust` | no |
  | `PerMode` | `per_mode_detailed` | no |
  | `Period` | `period` | no |
  | `PlusMinus` | `plus_minus` | no |
  | `Rank` | `rank` | no |
  | `Season` | `season` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_all_star` | no |
  | `ShotClockRange` | `shot_clock_range_nullable` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `DaysRestTeamDashboard` (57): `GROUP_SET`, `GROUP_VALUE`, `TEAM_DAYS_REST_RANGE`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `CFID`, `CFPARAMS`
  - `LocationTeamDashboard` (57): `GROUP_SET`, `GROUP_VALUE`, `TEAM_GAME_LOCATION`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `CFID`, `CFPARAMS`
  - `MonthTeamDashboard` (57): `GROUP_SET`, `GROUP_VALUE`, `SEASON_MONTH_NAME`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `CFID`, `CFPARAMS`
  - `OverallTeamDashboard` (57): `GROUP_SET`, `GROUP_VALUE`, `SEASON_YEAR`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `CFID`, `CFPARAMS`
  - `PrePostAllStarTeamDashboard` (57): `GROUP_SET`, `GROUP_VALUE`, `SEASON_SEGMENT`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `CFID`, `CFPARAMS`
  - `WinsLossesTeamDashboard` (57): `GROUP_SET`, `GROUP_VALUE`, `GAME_RESULT`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `CFID`, `CFPARAMS`

  </details>

### TeamDashboardByShootingSplits

- HTTP: `GET https://stats.nba.com/stats/teamdashboardbyshootingsplits`
- Repo docs: `docs/nba_api/stats/endpoints/teamdashboardbyshootingsplits.md`
- Example output: `docs/nba_api/stats/endpoints_output/teamdashboardbyshootingsplits_output.md`
- Required python args: `team_id`
- Python:
  ```python
  from nba_api.stats.endpoints import TeamDashboardByShootingSplits
  endpoint = TeamDashboardByShootingSplits(team_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `TeamID` | `team_id` | yes |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `GameSegment` | `game_segment_nullable` | no |
  | `LastNGames` | `last_n_games` | no |
  | `LeagueID` | `league_id_nullable` | no |
  | `Location` | `location_nullable` | no |
  | `MeasureType` | `measure_type_detailed_defense` | no |
  | `Month` | `month` | no |
  | `OpponentTeamID` | `opponent_team_id` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `PORound` | `po_round_nullable` | no |
  | `PaceAdjust` | `pace_adjust` | no |
  | `PerMode` | `per_mode_detailed` | no |
  | `Period` | `period` | no |
  | `PlusMinus` | `plus_minus` | no |
  | `Rank` | `rank` | no |
  | `Season` | `season` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_all_star` | no |
  | `ShotClockRange` | `shot_clock_range_nullable` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `AssistedBy` (33): `GROUP_SET`, `PLAYER_ID`, `PLAYER_NAME`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `EFG_PCT`, `BLKA`, `PCT_AST_2PM`, `PCT_UAST_2PM`, `PCT_AST_3PM`, `PCT_UAST_3PM`, `PCT_AST_FGM`, `PCT_UAST_FGM`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `EFG_PCT_RANK`, `BLKA_RANK`, `PCT_AST_2PM_RANK`, `PCT_UAST_2PM_RANK`, `PCT_AST_3PM_RANK`, `PCT_UAST_3PM_RANK`, `PCT_AST_FGM_RANK`, `PCT_UAST_FGM_RANK`, `CFID`, `CFPARAMS`
  - `AssitedShotTeamDashboard` (32): `GROUP_SET`, `GROUP_VALUE`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `EFG_PCT`, `BLKA`, `PCT_AST_2PM`, `PCT_UAST_2PM`, `PCT_AST_3PM`, `PCT_UAST_3PM`, `PCT_AST_FGM`, `PCT_UAST_FGM`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `EFG_PCT_RANK`, `BLKA_RANK`, `PCT_AST_2PM_RANK`, `PCT_UAST_2PM_RANK`, `PCT_AST_3PM_RANK`, `PCT_UAST_3PM_RANK`, `PCT_AST_FGM_RANK`, `PCT_UAST_FGM_RANK`, `CFID`, `CFPARAMS`
  - `OverallTeamDashboard` (32): `GROUP_SET`, `GROUP_VALUE`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `EFG_PCT`, `BLKA`, `PCT_AST_2PM`, `PCT_UAST_2PM`, `PCT_AST_3PM`, `PCT_UAST_3PM`, `PCT_AST_FGM`, `PCT_UAST_FGM`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `EFG_PCT_RANK`, `BLKA_RANK`, `PCT_AST_2PM_RANK`, `PCT_UAST_2PM_RANK`, `PCT_AST_3PM_RANK`, `PCT_UAST_3PM_RANK`, `PCT_AST_FGM_RANK`, `PCT_UAST_FGM_RANK`, `CFID`, `CFPARAMS`
  - `Shot5FTTeamDashboard` (32): `GROUP_SET`, `GROUP_VALUE`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `EFG_PCT`, `BLKA`, `PCT_AST_2PM`, `PCT_UAST_2PM`, `PCT_AST_3PM`, `PCT_UAST_3PM`, `PCT_AST_FGM`, `PCT_UAST_FGM`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `EFG_PCT_RANK`, `BLKA_RANK`, `PCT_AST_2PM_RANK`, `PCT_UAST_2PM_RANK`, `PCT_AST_3PM_RANK`, `PCT_UAST_3PM_RANK`, `PCT_AST_FGM_RANK`, `PCT_UAST_FGM_RANK`, `CFID`, `CFPARAMS`
  - `Shot8FTTeamDashboard` (32): `GROUP_SET`, `GROUP_VALUE`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `EFG_PCT`, `BLKA`, `PCT_AST_2PM`, `PCT_UAST_2PM`, `PCT_AST_3PM`, `PCT_UAST_3PM`, `PCT_AST_FGM`, `PCT_UAST_FGM`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `EFG_PCT_RANK`, `BLKA_RANK`, `PCT_AST_2PM_RANK`, `PCT_UAST_2PM_RANK`, `PCT_AST_3PM_RANK`, `PCT_UAST_3PM_RANK`, `PCT_AST_FGM_RANK`, `PCT_UAST_FGM_RANK`, `CFID`, `CFPARAMS`
  - `ShotAreaTeamDashboard` (32): `GROUP_SET`, `GROUP_VALUE`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `EFG_PCT`, `BLKA`, `PCT_AST_2PM`, `PCT_UAST_2PM`, `PCT_AST_3PM`, `PCT_UAST_3PM`, `PCT_AST_FGM`, `PCT_UAST_FGM`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `EFG_PCT_RANK`, `BLKA_RANK`, `PCT_AST_2PM_RANK`, `PCT_UAST_2PM_RANK`, `PCT_AST_3PM_RANK`, `PCT_UAST_3PM_RANK`, `PCT_AST_FGM_RANK`, `PCT_UAST_FGM_RANK`, `CFID`, `CFPARAMS`
  - `ShotTypeTeamDashboard` (32): `GROUP_SET`, `GROUP_VALUE`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `EFG_PCT`, `BLKA`, `PCT_AST_2PM`, `PCT_UAST_2PM`, `PCT_AST_3PM`, `PCT_UAST_3PM`, `PCT_AST_FGM`, `PCT_UAST_FGM`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `EFG_PCT_RANK`, `BLKA_RANK`, `PCT_AST_2PM_RANK`, `PCT_UAST_2PM_RANK`, `PCT_AST_3PM_RANK`, `PCT_UAST_3PM_RANK`, `PCT_AST_FGM_RANK`, `PCT_UAST_FGM_RANK`, `CFID`, `CFPARAMS`

  </details>

### TeamDashLineups

- HTTP: `GET https://stats.nba.com/stats/teamdashlineups`
- Repo docs: `docs/nba_api/stats/endpoints/teamdashlineups.md`
- Example output: `docs/nba_api/stats/endpoints_output/teamdashlineups_output.md`
- Required python args: `team_id`
- Python:
  ```python
  from nba_api.stats.endpoints import TeamDashLineups
  endpoint = TeamDashLineups(team_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `TeamID` | `team_id` | yes |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `GameID` | `game_id_nullable` | no |
  | `GameSegment` | `game_segment_nullable` | no |
  | `GroupQuantity` | `group_quantity` | no |
  | `LastNGames` | `last_n_games` | no |
  | `LeagueID` | `league_id_nullable` | no |
  | `Location` | `location_nullable` | no |
  | `MeasureType` | `measure_type_detailed_defense` | no |
  | `Month` | `month` | no |
  | `OpponentTeamID` | `opponent_team_id` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `PORound` | `po_round_nullable` | no |
  | `PaceAdjust` | `pace_adjust` | no |
  | `PerMode` | `per_mode_detailed` | no |
  | `Period` | `period` | no |
  | `PlusMinus` | `plus_minus` | no |
  | `Rank` | `rank` | no |
  | `Season` | `season` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_all_star` | no |
  | `ShotClockRange` | `shot_clock_range_nullable` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `Lineups` (55): `GROUP_SET`, `GROUP_ID`, `GROUP_NAME`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`
  - `Overall` (57): `GROUP_SET`, `GROUP_VALUE`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_NAME`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`

  </details>

### TeamDashPtPass

- HTTP: `GET https://stats.nba.com/stats/teamdashptpass`
- Repo docs: `docs/nba_api/stats/endpoints/teamdashptpass.md`
- Example output: `docs/nba_api/stats/endpoints_output/teamdashptpass_output.md`
- Required python args: `team_id`
- Python:
  ```python
  from nba_api.stats.endpoints import TeamDashPtPass
  endpoint = TeamDashPtPass(team_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `TeamID` | `team_id` | yes |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `LastNGames` | `last_n_games` | no |
  | `LeagueID` | `league_id` | no |
  | `Location` | `location_nullable` | no |
  | `Month` | `month` | no |
  | `OpponentTeamID` | `opponent_team_id` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `PerMode` | `per_mode_simple` | no |
  | `Season` | `season` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_all_star` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `PassesMade` (18): `TEAM_ID`, `TEAM_NAME`, `PASS_TYPE`, `G`, `PASS_FROM`, `PASS_TEAMMATE_PLAYER_ID`, `FREQUENCY`, `PASS`, `AST`, `FGM`, `FGA`, `FG_PCT`, `FG2M`, `FG2A`, `FG2_PCT`, `FG3M`, `FG3A`, `FG3_PCT`
  - `PassesReceived` (18): `TEAM_ID`, `TEAM_NAME`, `PASS_TYPE`, `G`, `PASS_TO`, `PASS_TEAMMATE_PLAYER_ID`, `FREQUENCY`, `PASS`, `AST`, `FGM`, `FGA`, `FG_PCT`, `FG2M`, `FG2A`, `FG2_PCT`, `FG3M`, `FG3A`, `FG3_PCT`

  </details>

### TeamDashPtReb

- HTTP: `GET https://stats.nba.com/stats/teamdashptreb`
- Repo docs: `docs/nba_api/stats/endpoints/teamdashptreb.md`
- Example output: `docs/nba_api/stats/endpoints_output/teamdashptreb_output.md`
- Required python args: `team_id`
- Python:
  ```python
  from nba_api.stats.endpoints import TeamDashPtReb
  endpoint = TeamDashPtReb(team_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `TeamID` | `team_id` | yes |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `GameSegment` | `game_segment_nullable` | no |
  | `LastNGames` | `last_n_games` | no |
  | `LeagueID` | `league_id` | no |
  | `Location` | `location_nullable` | no |
  | `Month` | `month` | no |
  | `OpponentTeamID` | `opponent_team_id` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `PerMode` | `per_mode_simple` | no |
  | `Period` | `period` | no |
  | `Season` | `season` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_all_star` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `NumContestedRebounding` (17): `TEAM_ID`, `TEAM_NAME`, `SORT_ORDER`, `G`, `REB_NUM_CONTESTING_RANGE`, `REB_FREQUENCY`, `OREB`, `DREB`, `REB`, `C_OREB`, `C_DREB`, `C_REB`, `C_REB_PCT`, `UC_OREB`, `UC_DREB`, `UC_REB`, `UC_REB_PCT`
  - `OverallRebounding` (16): `TEAM_ID`, `TEAM_NAME`, `G`, `OVERALL`, `REB_FREQUENCY`, `OREB`, `DREB`, `REB`, `C_OREB`, `C_DREB`, `C_REB`, `C_REB_PCT`, `UC_OREB`, `UC_DREB`, `UC_REB`, `UC_REB_PCT`
  - `RebDistanceRebounding` (17): `TEAM_ID`, `TEAM_NAME`, `SORT_ORDER`, `G`, `REB_DIST_RANGE`, `REB_FREQUENCY`, `OREB`, `DREB`, `REB`, `C_OREB`, `C_DREB`, `C_REB`, `C_REB_PCT`, `UC_OREB`, `UC_DREB`, `UC_REB`, `UC_REB_PCT`
  - `ShotDistanceRebounding` (17): `TEAM_ID`, `TEAM_NAME`, `SORT_ORDER`, `G`, `SHOT_DIST_RANGE`, `REB_FREQUENCY`, `OREB`, `DREB`, `REB`, `C_OREB`, `C_DREB`, `C_REB`, `C_REB_PCT`, `UC_OREB`, `UC_DREB`, `UC_REB`, `UC_REB_PCT`
  - `ShotTypeRebounding` (17): `TEAM_ID`, `TEAM_NAME`, `SORT_ORDER`, `G`, `SHOT_TYPE_RANGE`, `REB_FREQUENCY`, `OREB`, `DREB`, `REB`, `C_OREB`, `C_DREB`, `C_REB`, `C_REB_PCT`, `UC_OREB`, `UC_DREB`, `UC_REB`, `UC_REB_PCT`

  </details>

### TeamDashPtShots

- HTTP: `GET https://stats.nba.com/stats/teamdashptshots`
- Repo docs: `docs/nba_api/stats/endpoints/teamdashptshots.md`
- Example output: `docs/nba_api/stats/endpoints_output/teamdashptshots_output.md`
- Required python args: `team_id`
- Python:
  ```python
  from nba_api.stats.endpoints import TeamDashPtShots
  endpoint = TeamDashPtShots(team_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `TeamID` | `team_id` | yes |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `GameSegment` | `game_segment_nullable` | no |
  | `LastNGames` | `last_n_games` | no |
  | `LeagueID` | `league_id` | no |
  | `Location` | `location_nullable` | no |
  | `Month` | `month` | no |
  | `OpponentTeamID` | `opponent_team_id` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `PerMode` | `per_mode_simple` | no |
  | `Period` | `period` | no |
  | `Season` | `season` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_all_star` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `ClosestDefender10ftPlusShooting` (18): `TEAM_ID`, `TEAM_NAME`, `SORT_ORDER`, `G`, `CLOSE_DEF_DIST_RANGE`, `FGA_FREQUENCY`, `FGM`, `FGA`, `FG_PCT`, `EFG_PCT`, `FG2A_FREQUENCY`, `FG2M`, `FG2A`, `FG2_PCT`, `FG3A_FREQUENCY`, `FG3M`, `FG3A`, `FG3_PCT`
  - `ClosestDefenderShooting` (18): `TEAM_ID`, `TEAM_NAME`, `SORT_ORDER`, `G`, `CLOSE_DEF_DIST_RANGE`, `FGA_FREQUENCY`, `FGM`, `FGA`, `FG_PCT`, `EFG_PCT`, `FG2A_FREQUENCY`, `FG2M`, `FG2A`, `FG2_PCT`, `FG3A_FREQUENCY`, `FG3M`, `FG3A`, `FG3_PCT`
  - `DribbleShooting` (18): `TEAM_ID`, `TEAM_NAME`, `SORT_ORDER`, `G`, `DRIBBLE_RANGE`, `FGA_FREQUENCY`, `FGM`, `FGA`, `FG_PCT`, `EFG_PCT`, `FG2A_FREQUENCY`, `FG2M`, `FG2A`, `FG2_PCT`, `FG3A_FREQUENCY`, `FG3M`, `FG3A`, `FG3_PCT`
  - `GeneralShooting` (18): `TEAM_ID`, `TEAM_NAME`, `SORT_ORDER`, `G`, `SHOT_TYPE`, `FGA_FREQUENCY`, `FGM`, `FGA`, `FG_PCT`, `EFG_PCT`, `FG2A_FREQUENCY`, `FG2M`, `FG2A`, `FG2_PCT`, `FG3A_FREQUENCY`, `FG3M`, `FG3A`, `FG3_PCT`
  - `ShotClockShooting` (18): `TEAM_ID`, `TEAM_NAME`, `SORT_ORDER`, `G`, `SHOT_CLOCK_RANGE`, `FGA_FREQUENCY`, `FGM`, `FGA`, `FG_PCT`, `EFG_PCT`, `FG2A_FREQUENCY`, `FG2M`, `FG2A`, `FG2_PCT`, `FG3A_FREQUENCY`, `FG3M`, `FG3A`, `FG3_PCT`
  - `TouchTimeShooting` (18): `TEAM_ID`, `TEAM_NAME`, `SORT_ORDER`, `G`, `TOUCH_TIME_RANGE`, `FGA_FREQUENCY`, `FGM`, `FGA`, `FG_PCT`, `EFG_PCT`, `FG2A_FREQUENCY`, `FG2M`, `FG2A`, `FG2_PCT`, `FG3A_FREQUENCY`, `FG3M`, `FG3A`, `FG3_PCT`

  </details>

### TeamDetails

- HTTP: `GET https://stats.nba.com/stats/teamdetails`
- Repo docs: `docs/nba_api/stats/endpoints/teamdetails.md`
- Example output: `docs/nba_api/stats/endpoints_output/teamdetails_output.md`
- Required python args: `team_id`
- Python:
  ```python
  from nba_api.stats.endpoints import TeamDetails
  endpoint = TeamDetails(team_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `TeamID` | `team_id` | yes |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `TeamAwardsChampionships` (2): `YEARAWARDED`, `OPPOSITETEAM`
  - `TeamAwardsConf` (2): `YEARAWARDED`, `OPPOSITETEAM`
  - `TeamAwardsDiv` (2): `YEARAWARDED`, `OPPOSITETEAM`
  - `TeamBackground` (11): `TEAM_ID`, `ABBREVIATION`, `NICKNAME`, `YEARFOUNDED`, `CITY`, `ARENA`, `ARENACAPACITY`, `OWNER`, `GENERALMANAGER`, `HEADCOACH`, `DLEAGUEAFFILIATION`
  - `TeamHistory` (5): `TEAM_ID`, `CITY`, `NICKNAME`, `YEARFOUNDED`, `YEARACTIVETILL`
  - `TeamHof` (6): `PLAYERID`, `PLAYER`, `POSITION`, `JERSEY`, `SEASONSWITHTEAM`, `YEAR`
  - `TeamRetired` (6): `PLAYERID`, `PLAYER`, `POSITION`, `JERSEY`, `SEASONSWITHTEAM`, `YEAR`
  - `TeamSocialSites` (2): `ACCOUNTTYPE`, `WEBSITE_LINK`

  </details>

### TeamEstimatedMetrics

- HTTP: `GET https://stats.nba.com/stats/teamestimatedmetrics`
- Repo docs: `docs/nba_api/stats/endpoints/teamestimatedmetrics.md`
- Example output: `docs/nba_api/stats/endpoints_output/teamestimatedmetrics_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import TeamEstimatedMetrics
  endpoint = TeamEstimatedMetrics()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `LeagueID` | `league_id` | no |
  | `Season` | `season` | no |
  | `SeasonType` | `season_type` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `TeamEstimatedMetrics` (30): `TEAM_NAME`, `TEAM_ID`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `E_OFF_RATING`, `E_DEF_RATING`, `E_NET_RATING`, `E_PACE`, `E_AST_RATIO`, `E_OREB_PCT`, `E_DREB_PCT`, `E_REB_PCT`, `E_TM_TOV_PCT`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `E_OFF_RATING_RANK`, `E_DEF_RATING_RANK`, `E_NET_RATING_RANK`, `E_AST_RATIO_RANK`, `E_OREB_PCT_RANK`, `E_DREB_PCT_RANK`, `E_REB_PCT_RANK`, `E_TM_TOV_PCT_RANK`, `E_PACE_RANK`

  </details>

### TeamGameLog

- HTTP: `GET https://stats.nba.com/stats/teamgamelog`
- Repo docs: `docs/nba_api/stats/endpoints/teamgamelog.md`
- Example output: `docs/nba_api/stats/endpoints_output/teamgamelog_output.md`
- Required python args: `team_id`
- Python:
  ```python
  from nba_api.stats.endpoints import TeamGameLog
  endpoint = TeamGameLog(team_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `TeamID` | `team_id` | yes |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `LeagueID` | `league_id_nullable` | no |
  | `Season` | `season` | no |
  | `SeasonType` | `season_type_all_star` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `TeamGameLog` (27): `Team_ID`, `Game_ID`, `GAME_DATE`, `MATCHUP`, `WL`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `STL`, `BLK`, `TOV`, `PF`, `PTS`

  </details>

### TeamGameLogs

- HTTP: `GET https://stats.nba.com/stats/teamgamelogs`
- Repo docs: `docs/nba_api/stats/endpoints/teamgamelogs.md`
- Example output: `docs/nba_api/stats/endpoints_output/teamgamelogs_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import TeamGameLogs
  endpoint = TeamGameLogs()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `GameSegment` | `game_segment_nullable` | no |
  | `LastNGames` | `last_n_games_nullable` | no |
  | `LeagueID` | `league_id_nullable` | no |
  | `Location` | `location_nullable` | no |
  | `MeasureType` | `measure_type_player_game_logs_nullable` | no |
  | `Month` | `month_nullable` | no |
  | `OppTeamID` | `opp_team_id_nullable` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `PORound` | `po_round_nullable` | no |
  | `PerMode` | `per_mode_simple_nullable` | no |
  | `Period` | `period_nullable` | no |
  | `PlayerID` | `player_id_nullable` | no |
  | `Season` | `season_nullable` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_nullable` | no |
  | `ShotClockRange` | `shot_clock_range_nullable` | no |
  | `TeamID` | `team_id_nullable` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `TeamGameLogs` (56): `SEASON_YEAR`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_NAME`, `GAME_ID`, `GAME_DATE`, `MATCHUP`, `WL`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`

  </details>

### TeamGameStreakFinder

- HTTP: `GET https://stats.nba.com/stats/teamgamestreakfinder`
- Repo docs: `docs/nba_api/stats/endpoints/teamgamestreakfinder.md`
- Example output: `docs/nba_api/stats/endpoints_output/teamgamestreakfinder_output.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import TeamGameStreakFinder
  endpoint = TeamGameStreakFinder()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `ActiveStreaksOnly` | `active_streaks_only_nullable` | no |
  | `ActiveTeamsOnly` | `active_teams_only_nullable` | no |
  | `BtrOPPAST` | `btr_opp_ast_nullable` | no |
  | `BtrOPPBLK` | `btr_opp_blk_nullable` | no |
  | `BtrOPPDREB` | `btr_opp_dreb_nullable` | no |
  | `BtrOPPFG3A` | `btr_opp_fg3a_nullable` | no |
  | `BtrOPPFG3M` | `btr_opp_fg3m_nullable` | no |
  | `BtrOPPFG3PCT` | `btr_opp_fg3_pct_nullable` | no |
  | `BtrOPPFGA` | `btr_opp_fga_nullable` | no |
  | `BtrOPPFGM` | `btr_opp_fgm_nullable` | no |
  | `BtrOPPFG_PCT` | `btr_opp_fg_pct_nullable` | no |
  | `BtrOPPFTA` | `btr_opp_fta_nullable` | no |
  | `BtrOPPFTM` | `btr_opp_ftm_nullable` | no |
  | `BtrOPPFT_PCT` | `btr_opp_ft_pct_nullable` | no |
  | `BtrOPPOREB` | `btr_opp_oreb_nullable` | no |
  | `BtrOPPPF` | `btr_opp_pf_nullable` | no |
  | `BtrOPPPTS` | `btr_opp_pts_nullable` | no |
  | `BtrOPPPTS2NDCHANCE` | `btr_opp_pts2nd_chance_nullable` | no |
  | `BtrOPPPTSFB` | `btr_opp_pts_fb_nullable` | no |
  | `BtrOPPPTSOFFTOV` | `btr_opp_pts_off_tov_nullable` | no |
  | `BtrOPPPTSPAINT` | `btr_opp_pts_paint_nullable` | no |
  | `BtrOPPREB` | `btr_opp_reb_nullable` | no |
  | `BtrOPPSTL` | `btr_opp_stl_nullable` | no |
  | `BtrOPPTOV` | `btr_opp_tov_nullable` | no |
  | `Conference` | `conference_nullable` | no |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `Division` | `division_simple_nullable` | no |
  | `EqAST` | `eq_ast_nullable` | no |
  | `EqBLK` | `eq_blk_nullable` | no |
  | `EqDD` | `eq_dd_nullable` | no |
  | `EqDREB` | `eq_dreb_nullable` | no |
  | `EqFG3A` | `eq_fg3a_nullable` | no |
  | `EqFG3M` | `eq_fg3m_nullable` | no |
  | `EqFG3_PCT` | `eq_fg3_pct_nullable` | no |
  | `EqFGA` | `eq_fga_nullable` | no |
  | `EqFGM` | `eq_fgm_nullable` | no |
  | `EqFG_PCT` | `eq_fg_pct_nullable` | no |
  | `EqFTA` | `eq_fta_nullable` | no |
  | `EqFTM` | `eq_ftm_nullable` | no |
  | `EqFT_PCT` | `eq_ft_pct_nullable` | no |
  | `EqMINUTES` | `eq_minutes_nullable` | no |
  | `EqOPPPTS2NDCHANCE` | `eq_opp_pts2nd_chance_nullable` | no |
  | `EqOPPPTSFB` | `eq_opp_pts_fb_nullable` | no |
  | `EqOPPPTSOFFTOV` | `eq_opp_pts_off_tov_nullable` | no |
  | `EqOPPPTSPAINT` | `eq_opp_pts_paint_nullable` | no |
  | `EqOREB` | `eq_oreb_nullable` | no |
  | `EqPF` | `eq_pf_nullable` | no |
  | `EqPTS` | `eq_pts_nullable` | no |
  | `EqPTS2NDCHANCE` | `eq_pts2nd_chance_nullable` | no |
  | `EqPTSFB` | `eq_pts_fb_nullable` | no |
  | `EqPTSOFFTOV` | `eq_pts_off_tov_nullable` | no |
  | `EqPTSPAINT` | `eq_pts_paint_nullable` | no |
  | `EqREB` | `eq_reb_nullable` | no |
  | `EqSTL` | `eq_stl_nullable` | no |
  | `EqTD` | `eq_td_nullable` | no |
  | `EqTOV` | `eq_tov_nullable` | no |
  | `GameID` | `game_id_nullable` | no |
  | `GtAST` | `gt_ast_nullable` | no |
  | `GtBLK` | `gt_blk_nullable` | no |
  | `GtDD` | `gt_dd_nullable` | no |
  | `GtDREB` | `gt_dreb_nullable` | no |
  | `GtFG3A` | `gt_fg3a_nullable` | no |
  | `GtFG3M` | `gt_fg3m_nullable` | no |
  | `GtFG3_PCT` | `gt_fg3_pct_nullable` | no |
  | `GtFGA` | `gt_fga_nullable` | no |
  | `GtFGM` | `gt_fgm_nullable` | no |
  | `GtFG_PCT` | `gt_fg_pct_nullable` | no |
  | `GtFTA` | `gt_fta_nullable` | no |
  | `GtFTM` | `gt_ftm_nullable` | no |
  | `GtFT_PCT` | `gt_ft_pct_nullable` | no |
  | `GtMINUTES` | `gt_minutes_nullable` | no |
  | `GtOPPAST` | `gt_opp_ast_nullable` | no |
  | `GtOPPBLK` | `gt_opp_blk_nullable` | no |
  | `GtOPPDREB` | `gt_opp_dreb_nullable` | no |
  | `GtOPPFG3A` | `gt_opp_fg3a_nullable` | no |
  | `GtOPPFG3M` | `gt_opp_fg3m_nullable` | no |
  | `GtOPPFG3PCT` | `gt_opp_fg3_pct_nullable` | no |
  | `GtOPPFGA` | `gt_opp_fga_nullable` | no |
  | `GtOPPFGM` | `gt_opp_fgm_nullable` | no |
  | `GtOPPFG_PCT` | `gt_opp_fg_pct_nullable` | no |
  | `GtOPPFTA` | `gt_opp_fta_nullable` | no |
  | `GtOPPFTM` | `gt_opp_ftm_nullable` | no |
  | `GtOPPFT_PCT` | `gt_opp_ft_pct_nullable` | no |
  | `GtOPPOREB` | `gt_opp_oreb_nullable` | no |
  | `GtOPPPF` | `gt_opp_pf_nullable` | no |
  | `GtOPPPTS` | `gt_opp_pts_nullable` | no |
  | `GtOPPPTS2NDCHANCE` | `gt_opp_pts2nd_chance_nullable` | no |
  | `GtOPPPTSFB` | `gt_opp_pts_fb_nullable` | no |
  | `GtOPPPTSOFFTOV` | `gt_opp_pts_off_tov_nullable` | no |
  | `GtOPPPTSPAINT` | `gt_opp_pts_paint_nullable` | no |
  | `GtOPPREB` | `gt_opp_reb_nullable` | no |
  | `GtOPPSTL` | `gt_opp_stl_nullable` | no |
  | `GtOPPTOV` | `gt_opp_tov_nullable` | no |
  | `GtOREB` | `gt_oreb_nullable` | no |
  | `GtPF` | `gt_pf_nullable` | no |
  | `GtPTS` | `gt_pts_nullable` | no |
  | `GtPTS2NDCHANCE` | `gt_pts2nd_chance_nullable` | no |
  | `GtPTSFB` | `gt_pts_fb_nullable` | no |
  | `GtPTSOFFTOV` | `gt_pts_off_tov_nullable` | no |
  | `GtPTSPAINT` | `gt_pts_paint_nullable` | no |
  | `GtREB` | `gt_reb_nullable` | no |
  | `GtSTL` | `gt_stl_nullable` | no |
  | `GtTD` | `gt_td_nullable` | no |
  | `GtTOV` | `gt_tov_nullable` | no |
  | `LStreak` | `lstreak_nullable` | no |
  | `LeagueID` | `league_id_nullable` | no |
  | `Location` | `location_nullable` | no |
  | `LtAST` | `lt_ast_nullable` | no |
  | `LtBLK` | `lt_blk_nullable` | no |
  | `LtDD` | `lt_dd_nullable` | no |
  | `LtDREB` | `lt_dreb_nullable` | no |
  | `LtFG3A` | `lt_fg3a_nullable` | no |
  | `LtFG3M` | `lt_fg3m_nullable` | no |
  | `LtFG3_PCT` | `lt_fg3_pct_nullable` | no |
  | `LtFGA` | `lt_fga_nullable` | no |
  | `LtFGM` | `lt_fgm_nullable` | no |
  | `LtFG_PCT` | `lt_fg_pct_nullable` | no |
  | `LtFTA` | `lt_fta_nullable` | no |
  | `LtFTM` | `lt_ftm_nullable` | no |
  | `LtFT_PCT` | `lt_ft_pct_nullable` | no |
  | `LtMINUTES` | `lt_minutes_nullable` | no |
  | `LtOPPAST` | `lt_opp_ast_nullable` | no |
  | `LtOPPBLK` | `lt_opp_blk_nullable` | no |
  | `LtOPPDREB` | `lt_opp_dreb_nullable` | no |
  | `LtOPPFG3A` | `lt_opp_fg3a_nullable` | no |
  | `LtOPPFG3M` | `lt_opp_fg3m_nullable` | no |
  | `LtOPPFG3PCT` | `lt_opp_fg3_pct_nullable` | no |
  | `LtOPPFGA` | `lt_opp_fga_nullable` | no |
  | `LtOPPFGM` | `lt_opp_fgm_nullable` | no |
  | `LtOPPFG_PCT` | `lt_opp_fg_pct_nullable` | no |
  | `LtOPPFTA` | `lt_opp_fta_nullable` | no |
  | `LtOPPFTM` | `lt_opp_ftm_nullable` | no |
  | `LtOPPFT_PCT` | `lt_opp_ft_pct_nullable` | no |
  | `LtOPPOREB` | `lt_opp_oreb_nullable` | no |
  | `LtOPPPF` | `lt_opp_pf_nullable` | no |
  | `LtOPPPTS` | `lt_opp_pts_nullable` | no |
  | `LtOPPPTS2NDCHANCE` | `lt_opp_pts2nd_chance_nullable` | no |
  | `LtOPPPTSFB` | `lt_opp_pts_fb_nullable` | no |
  | `LtOPPPTSOFFTOV` | `lt_opp_pts_off_tov_nullable` | no |
  | `LtOPPPTSPAINT` | `lt_opp_pts_paint_nullable` | no |
  | `LtOPPREB` | `lt_opp_reb_nullable` | no |
  | `LtOPPSTL` | `lt_opp_stl_nullable` | no |
  | `LtOPPTOV` | `lt_opp_tov_nullable` | no |
  | `LtOREB` | `lt_oreb_nullable` | no |
  | `LtPF` | `lt_pf_nullable` | no |
  | `LtPTS` | `lt_pts_nullable` | no |
  | `LtPTS2NDCHANCE` | `lt_pts2nd_chance_nullable` | no |
  | `LtPTSFB` | `lt_pts_fb_nullable` | no |
  | `LtPTSOFFTOV` | `lt_pts_off_tov_nullable` | no |
  | `LtPTSPAINT` | `lt_pts_paint_nullable` | no |
  | `LtREB` | `lt_reb_nullable` | no |
  | `LtSTL` | `lt_stl_nullable` | no |
  | `LtTD` | `lt_td_nullable` | no |
  | `LtTOV` | `lt_tov_nullable` | no |
  | `MinGames` | `min_games_nullable` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `PORound` | `po_round_nullable` | no |
  | `Season` | `season_nullable` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_nullable` | no |
  | `TeamID` | `team_id_nullable` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |
  | `VsTeamID` | `vs_team_id_nullable` | no |
  | `WStreak` | `wstreak_nullable` | no |
  | `WrsOPPAST` | `wrs_opp_ast_nullable` | no |
  | `WrsOPPBLK` | `wrs_opp_blk_nullable` | no |
  | `WrsOPPDREB` | `wrs_opp_dreb_nullable` | no |
  | `WrsOPPFG3A` | `wrs_opp_fg3a_nullable` | no |
  | `WrsOPPFG3M` | `wrs_opp_fg3m_nullable` | no |
  | `WrsOPPFG3PCT` | `wrs_opp_fg3_pct_nullable` | no |
  | `WrsOPPFGA` | `wrs_opp_fga_nullable` | no |
  | `WrsOPPFGM` | `wrs_opp_fgm_nullable` | no |
  | `WrsOPPFG_PCT` | `wrs_opp_fg_pct_nullable` | no |
  | `WrsOPPFTA` | `wrs_opp_fta_nullable` | no |
  | `WrsOPPFTM` | `wrs_opp_ftm_nullable` | no |
  | `WrsOPPFT_PCT` | `wrs_opp_ft_pct_nullable` | no |
  | `WrsOPPOREB` | `wrs_opp_oreb_nullable` | no |
  | `WrsOPPPF` | `wrs_opp_pf_nullable` | no |
  | `WrsOPPPTS` | `wrs_opp_pts_nullable` | no |
  | `WrsOPPPTS2NDCHANCE` | `wrs_opp_pts2nd_chance_nullable` | no |
  | `WrsOPPPTSFB` | `wrs_opp_pts_fb_nullable` | no |
  | `WrsOPPPTSOFFTOV` | `wrs_opp_pts_off_tov_nullable` | no |
  | `WrsOPPPTSPAINT` | `wrs_opp_pts_paint_nullable` | no |
  | `WrsOPPREB` | `wrs_opp_reb_nullable` | no |
  | `WrsOPPSTL` | `wrs_opp_stl_nullable` | no |
  | `WrsOPPTOV` | `wrs_opp_tov_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `TeamGameStreakFinderParametersResults` (10): `TEAM_NAME`, `TEAM_ID`, `GAMESTREAK`, `STARTDATE`, `ENDDATE`, `ACTIVESTREAK`, `NUMSEASONS`, `LASTSEASON`, `FIRSTSEASON`, `ABBREVIATION`

  </details>

### TeamHistoricalLeaders

- HTTP: `GET https://stats.nba.com/stats/teamhistoricalleaders`
- Repo docs: `docs/nba_api/stats/endpoints/teamhistoricalleaders.md`
- Example output: `docs/nba_api/stats/endpoints_output/teamhistoricalleaders_output.md`
- Required python args: `team_id`
- Python:
  ```python
  from nba_api.stats.endpoints import TeamHistoricalLeaders
  endpoint = TeamHistoricalLeaders(team_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `TeamID` | `team_id` | yes |
  | `LeagueID` | `league_id` | no |
  | `SeasonID` | `season_id` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `CareerLeadersByTeam` (17): `TEAM_ID`, `PTS`, `PTS_PERSON_ID`, `PTS_PLAYER`, `AST`, `AST_PERSON_ID`, `AST_PLAYER`, `REB`, `REB_PERSON_ID`, `REB_PLAYER`, `BLK`, `BLK_PERSON_ID`, `BLK_PLAYER`, `STL`, `STL_PERSON_ID`, `STL_PLAYER`, `SEASON_YEAR`

  </details>

### TeamInfoCommon

- HTTP: `GET https://stats.nba.com/stats/teaminfocommon`
- Repo docs: `docs/nba_api/stats/endpoints/teaminfocommon.md`
- Example output: `docs/nba_api/stats/endpoints_output/teaminfocommon_output.md`
- Required python args: `team_id`
- Python:
  ```python
  from nba_api.stats.endpoints import TeamInfoCommon
  endpoint = TeamInfoCommon(team_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `TeamID` | `team_id` | yes |
  | `LeagueID` | `league_id` | no |
  | `Season` | `season_nullable` | no |
  | `SeasonType` | `season_type_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `AvailableSeasons` (1): `SEASON_ID`
  - `TeamInfoCommon` (15): `TEAM_ID`, `SEASON_YEAR`, `TEAM_CITY`, `TEAM_NAME`, `TEAM_ABBREVIATION`, `TEAM_CONFERENCE`, `TEAM_DIVISION`, `TEAM_CODE`, `W`, `L`, `PCT`, `CONF_RANK`, `DIV_RANK`, `MIN_YEAR`, `MAX_YEAR`
  - `TeamSeasonRanks` (11): `LEAGUE_ID`, `SEASON_ID`, `TEAM_ID`, `PTS_RANK`, `PTS_PG`, `REB_RANK`, `REB_PG`, `AST_RANK`, `AST_PG`, `OPP_PTS_RANK`, `OPP_PTS_PG`

  </details>

### TeamPlayerDashboard

- HTTP: `GET https://stats.nba.com/stats/teamplayerdashboard`
- Repo docs: `docs/nba_api/stats/endpoints/teamplayerdashboard.md`
- Example output: `docs/nba_api/stats/endpoints_output/teamplayerdashboard_output.md`
- Required python args: `team_id`
- Python:
  ```python
  from nba_api.stats.endpoints import TeamPlayerDashboard
  endpoint = TeamPlayerDashboard(team_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `TeamID` | `team_id` | yes |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `GameSegment` | `game_segment_nullable` | no |
  | `LastNGames` | `last_n_games` | no |
  | `LeagueID` | `league_id_nullable` | no |
  | `Location` | `location_nullable` | no |
  | `MeasureType` | `measure_type_detailed_defense` | no |
  | `Month` | `month` | no |
  | `OpponentTeamID` | `opponent_team_id` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `PORound` | `po_round_nullable` | no |
  | `PaceAdjust` | `pace_adjust` | no |
  | `PerMode` | `per_mode_detailed` | no |
  | `Period` | `period` | no |
  | `PlusMinus` | `plus_minus` | no |
  | `Rank` | `rank` | no |
  | `Season` | `season` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_all_star` | no |
  | `ShotClockRange` | `shot_clock_range_nullable` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `PlayersSeasonTotals` (61): `GROUP_SET`, `PLAYER_ID`, `PLAYER_NAME`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `NBA_FANTASY_PTS`, `DD2`, `TD3`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `NBA_FANTASY_PTS_RANK`, `DD2_RANK`, `TD3_RANK`
  - `TeamOverall` (56): `GROUP_SET`, `TEAM_ID`, `TEAM_NAME`, `GROUP_VALUE`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`

  </details>

### TeamPlayerOnOffDetails

- HTTP: `GET https://stats.nba.com/stats/teamplayeronoffdetails`
- Repo docs: `docs/nba_api/stats/endpoints/teamplayeronoffdetails.md`
- Example output: `docs/nba_api/stats/endpoints_output/teamplayeronoffdetails_output.md`
- Required python args: `team_id`
- Python:
  ```python
  from nba_api.stats.endpoints import TeamPlayerOnOffDetails
  endpoint = TeamPlayerOnOffDetails(team_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `TeamID` | `team_id` | yes |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `GameSegment` | `game_segment_nullable` | no |
  | `LastNGames` | `last_n_games` | no |
  | `LeagueID` | `league_id_nullable` | no |
  | `Location` | `location_nullable` | no |
  | `MeasureType` | `measure_type_detailed_defense` | no |
  | `Month` | `month` | no |
  | `OpponentTeamID` | `opponent_team_id` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `PaceAdjust` | `pace_adjust` | no |
  | `PerMode` | `per_mode_detailed` | no |
  | `Period` | `period` | no |
  | `PlusMinus` | `plus_minus` | no |
  | `Rank` | `rank` | no |
  | `Season` | `season` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_all_star` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `OverallTeamPlayerOnOffDetails` (57): `GROUP_SET`, `GROUP_VALUE`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_NAME`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`
  - `PlayersOffCourtTeamPlayerOnOffDetails` (59): `GROUP_SET`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_NAME`, `VS_PLAYER_ID`, `VS_PLAYER_NAME`, `COURT_STATUS`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`
  - `PlayersOnCourtTeamPlayerOnOffDetails` (59): `GROUP_SET`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_NAME`, `VS_PLAYER_ID`, `VS_PLAYER_NAME`, `COURT_STATUS`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`

  </details>

### TeamPlayerOnOffSummary

- HTTP: `GET https://stats.nba.com/stats/teamplayeronoffsummary`
- Repo docs: `docs/nba_api/stats/endpoints/teamplayeronoffsummary.md`
- Example output: `docs/nba_api/stats/endpoints_output/teamplayeronoffsummary_output.md`
- Required python args: `team_id`
- Python:
  ```python
  from nba_api.stats.endpoints import TeamPlayerOnOffSummary
  endpoint = TeamPlayerOnOffSummary(team_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `TeamID` | `team_id` | yes |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `GameSegment` | `game_segment_nullable` | no |
  | `LastNGames` | `last_n_games` | no |
  | `LeagueID` | `league_id_nullable` | no |
  | `Location` | `location_nullable` | no |
  | `MeasureType` | `measure_type_detailed_defense` | no |
  | `Month` | `month` | no |
  | `OpponentTeamID` | `opponent_team_id` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `PaceAdjust` | `pace_adjust` | no |
  | `PerMode` | `per_mode_detailed` | no |
  | `Period` | `period` | no |
  | `PlusMinus` | `plus_minus` | no |
  | `Rank` | `rank` | no |
  | `Season` | `season` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_all_star` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `OverallTeamPlayerOnOffSummary` (57): `GROUP_SET`, `GROUP_VALUE`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_NAME`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`
  - `PlayersOffCourtTeamPlayerOnOffSummary` (13): `GROUP_SET`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_NAME`, `VS_PLAYER_ID`, `VS_PLAYER_NAME`, `COURT_STATUS`, `GP`, `MIN`, `PLUS_MINUS`, `OFF_RATING`, `DEF_RATING`, `NET_RATING`
  - `PlayersOnCourtTeamPlayerOnOffSummary` (13): `GROUP_SET`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_NAME`, `VS_PLAYER_ID`, `VS_PLAYER_NAME`, `COURT_STATUS`, `GP`, `MIN`, `PLUS_MINUS`, `OFF_RATING`, `DEF_RATING`, `NET_RATING`

  </details>

### TeamVsPlayer

- HTTP: `GET https://stats.nba.com/stats/teamvsplayer`
- Repo docs: `docs/nba_api/stats/endpoints/teamvsplayer.md`
- Required python args: `vs_player_id`, `team_id`
- Python:
  ```python
  from nba_api.stats.endpoints import TeamVsPlayer
  endpoint = TeamVsPlayer(vs_player_id='…', team_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `TeamID` | `team_id` | yes |
  | `VsPlayerID` | `vs_player_id` | yes |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `GameSegment` | `game_segment_nullable` | no |
  | `LastNGames` | `last_n_games` | no |
  | `LeagueID` | `league_id_nullable` | no |
  | `Location` | `location_nullable` | no |
  | `MeasureType` | `measure_type_detailed_defense` | no |
  | `Month` | `month` | no |
  | `OpponentTeamID` | `opponent_team_id` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `PaceAdjust` | `pace_adjust` | no |
  | `PerMode` | `per_mode_detailed` | no |
  | `Period` | `period` | no |
  | `PlayerID` | `player_id_nullable` | no |
  | `PlusMinus` | `plus_minus` | no |
  | `Rank` | `rank` | no |
  | `Season` | `season` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_playoffs` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `OnOffCourt` (61): `GROUP_SET`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_NAME`, `VS_PLAYER_ID`, `VS_PLAYER_NAME`, `COURT_STATUS`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `CFID`, `CFPARAMS`
  - `Overall` (58): `GROUP_SET`, `GROUP_VALUE`, `TEAM_ID`, `TEAM_ABBREVIATION`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `CFID`, `CFPARAMS`
  - `ShotAreaOffCourt` (13): `GROUP_SET`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_NAME`, `VS_PLAYER_ID`, `VS_PLAYER_NAME`, `COURT_STATUS`, `GROUP_VALUE`, `FGM`, `FGA`, `FG_PCT`, `CFID`, `CFPARAMS`
  - `ShotAreaOnCourt` (13): `GROUP_SET`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_NAME`, `VS_PLAYER_ID`, `VS_PLAYER_NAME`, `COURT_STATUS`, `GROUP_VALUE`, `FGM`, `FGA`, `FG_PCT`, `CFID`, `CFPARAMS`
  - `ShotAreaOverall` (10): `GROUP_SET`, `GROUP_VALUE`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_NAME`, `FGM`, `FGA`, `FG_PCT`, `CFID`, `CFPARAMS`
  - `ShotDistanceOffCourt` (13): `GROUP_SET`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_NAME`, `VS_PLAYER_ID`, `VS_PLAYER_NAME`, `COURT_STATUS`, `GROUP_VALUE`, `FGM`, `FGA`, `FG_PCT`, `CFID`, `CFPARAMS`
  - `ShotDistanceOnCourt` (13): `GROUP_SET`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_NAME`, `VS_PLAYER_ID`, `VS_PLAYER_NAME`, `COURT_STATUS`, `GROUP_VALUE`, `FGM`, `FGA`, `FG_PCT`, `CFID`, `CFPARAMS`
  - `ShotDistanceOverall` (10): `GROUP_SET`, `GROUP_VALUE`, `TEAM_ID`, `TEAM_ABBREVIATION`, `TEAM_NAME`, `FGM`, `FGA`, `FG_PCT`, `CFID`, `CFPARAMS`
  - `vsPlayerOverall` (63): `GROUP_SET`, `GROUP_VALUE`, `PLAYER_ID`, `GP`, `W`, `L`, `W_PCT`, `MIN`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `TOV`, `STL`, `BLK`, `BLKA`, `PF`, `PFD`, `PTS`, `PLUS_MINUS`, `NBA_FANTASY_PTS`, `DD2`, `TD3`, `GP_RANK`, `W_RANK`, `L_RANK`, `W_PCT_RANK`, `MIN_RANK`, `FGM_RANK`, `FGA_RANK`, `FG_PCT_RANK`, `FG3M_RANK`, `FG3A_RANK`, `FG3_PCT_RANK`, `FTM_RANK`, `FTA_RANK`, `FT_PCT_RANK`, `OREB_RANK`, `DREB_RANK`, `REB_RANK`, `AST_RANK`, `TOV_RANK`, `STL_RANK`, `BLK_RANK`, `BLKA_RANK`, `PF_RANK`, `PFD_RANK`, `PTS_RANK`, `PLUS_MINUS_RANK`, `NBA_FANTASY_PTS_RANK`, `DD2_RANK`, `TD3_RANK`, `CFID`, `CFPARAMS`

  </details>

### TeamYearByYearStats

- HTTP: `GET https://stats.nba.com/stats/teamyearbyyearstats`
- Repo docs: `docs/nba_api/stats/endpoints/teamyearbyyearstats.md`
- Example output: `docs/nba_api/stats/endpoints_output/teamyearbyyearstats_output.md`
- Required python args: `team_id`
- Python:
  ```python
  from nba_api.stats.endpoints import TeamYearByYearStats
  endpoint = TeamYearByYearStats(team_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `TeamID` | `team_id` | yes |
  | `LeagueID` | `league_id` | no |
  | `PerMode` | `per_mode_simple` | no |
  | `SeasonType` | `season_type_all_star` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `TeamStats` (34): `TEAM_ID`, `TEAM_CITY`, `TEAM_NAME`, `YEAR`, `GP`, `WINS`, `LOSSES`, `WIN_PCT`, `CONF_RANK`, `DIV_RANK`, `PO_WINS`, `PO_LOSSES`, `CONF_COUNT`, `DIV_COUNT`, `NBA_FINALS_APPEARANCE`, `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `PF`, `STL`, `TOV`, `BLK`, `PTS`, `PTS_RANK`

  </details>

### VideoDetails

- HTTP: `GET https://stats.nba.com/stats/videodetails`
- Repo docs: `docs/nba_api/stats/endpoints/videodetails.md`
- Required python args: `team_id`, `player_id`
- Python:
  ```python
  from nba_api.stats.endpoints import VideoDetails
  endpoint = VideoDetails(team_id='…', player_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `PlayerID` | `player_id` | yes |
  | `TeamID` | `team_id` | yes |
  | `AheadBehind` | `ahead_behind_nullable` | no |
  | `ClutchTime` | `clutch_time_nullable` | no |
  | `ContextFilter` | `context_filter_nullable` | no |
  | `ContextMeasure` | `context_measure_detailed` | no |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `EndPeriod` | `end_period_nullable` | no |
  | `EndRange` | `end_range_nullable` | no |
  | `GameID` | `game_id_nullable` | no |
  | `GameSegment` | `game_segment_nullable` | no |
  | `LastNGames` | `last_n_games` | no |
  | `LeagueID` | `league_id_nullable` | no |
  | `Location` | `location_nullable` | no |
  | `Month` | `month` | no |
  | `OpponentTeamID` | `opponent_team_id` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `Period` | `period` | no |
  | `PointDiff` | `point_diff_nullable` | no |
  | `Position` | `position_nullable` | no |
  | `RangeType` | `range_type_nullable` | no |
  | `RookieYear` | `rookie_year_nullable` | no |
  | `Season` | `season` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_all_star` | no |
  | `StartPeriod` | `start_period_nullable` | no |
  | `StartRange` | `start_range_nullable` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |

  </details>
- Response data sets: none documented in source (`expected_data` empty)

### VideoDetailsAsset

- HTTP: `GET https://stats.nba.com/stats/videodetailsasset`
- Repo docs: `docs/nba_api/stats/endpoints/videodetailsasset.md`
- Required python args: `team_id`, `player_id`
- Python:
  ```python
  from nba_api.stats.endpoints import VideoDetailsAsset
  endpoint = VideoDetailsAsset(team_id='…', player_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `PlayerID` | `player_id` | yes |
  | `TeamID` | `team_id` | yes |
  | `AheadBehind` | `ahead_behind_nullable` | no |
  | `ClutchTime` | `clutch_time_nullable` | no |
  | `ContextFilter` | `context_filter_nullable` | no |
  | `ContextMeasure` | `context_measure_detailed` | no |
  | `DateFrom` | `date_from_nullable` | no |
  | `DateTo` | `date_to_nullable` | no |
  | `EndPeriod` | `end_period_nullable` | no |
  | `EndRange` | `end_range_nullable` | no |
  | `GameID` | `game_id_nullable` | no |
  | `GameSegment` | `game_segment_nullable` | no |
  | `LastNGames` | `last_n_games` | no |
  | `LeagueID` | `league_id_nullable` | no |
  | `Location` | `location_nullable` | no |
  | `Month` | `month` | no |
  | `OpponentTeamID` | `opponent_team_id` | no |
  | `Outcome` | `outcome_nullable` | no |
  | `Period` | `period` | no |
  | `PointDiff` | `point_diff_nullable` | no |
  | `Position` | `position_nullable` | no |
  | `RangeType` | `range_type_nullable` | no |
  | `RookieYear` | `rookie_year_nullable` | no |
  | `Season` | `season` | no |
  | `SeasonSegment` | `season_segment_nullable` | no |
  | `SeasonType` | `season_type_all_star` | no |
  | `StartPeriod` | `start_period_nullable` | no |
  | `StartRange` | `start_range_nullable` | no |
  | `VsConference` | `vs_conference_nullable` | no |
  | `VsDivision` | `vs_division_nullable` | no |

  </details>
- Response data sets: none documented in source (`expected_data` empty)

### VideoEvents

- HTTP: `GET https://stats.nba.com/stats/videoevents`
- Repo docs: `docs/nba_api/stats/endpoints/videoevents.md`
- Required python args: `game_id`
- Python:
  ```python
  from nba_api.stats.endpoints import VideoEvents
  endpoint = VideoEvents(game_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `GameID` | `game_id` | yes |
  | `GameEventID` | `game_event_id` | no |

  </details>
- Response data sets: none documented in source (`expected_data` empty)

### VideoEventsAsset

- HTTP: `GET https://stats.nba.com/stats/videoeventsasset`
- Required python args: `game_id`
- Python:
  ```python
  from nba_api.stats.endpoints import VideoEventsAsset
  endpoint = VideoEventsAsset(game_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `GameID` | `game_id` | yes |
  | `GameEventID` | `game_event_id` | no |

  </details>
- Response data sets: none documented in source (`expected_data` empty)

### VideoStatus

- HTTP: `GET https://stats.nba.com/stats/videostatus`
- Repo docs: `docs/nba_api/stats/endpoints/videostatus.md`
- Required python args: none
- Python:
  ```python
  from nba_api.stats.endpoints import VideoStatus
  endpoint = VideoStatus()
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `GameDate` | `game_date` | no |
  | `LeagueID` | `league_id` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `VideoStatus` (14): `GAME_ID`, `GAME_DATE`, `VISITOR_TEAM_ID`, `VISITOR_TEAM_CITY`, `VISITOR_TEAM_NAME`, `VISITOR_TEAM_ABBREVIATION`, `HOME_TEAM_ID`, `HOME_TEAM_CITY`, `HOME_TEAM_NAME`, `HOME_TEAM_ABBREVIATION`, `GAME_STATUS`, `GAME_STATUS_TEXT`, `IS_AVAILABLE`, `PT_XYZ_AVAILABLE`

  </details>

### WinProbabilityPBP

- HTTP: `GET https://stats.nba.com/stats/winprobabilitypbp`
- Repo docs: `docs/nba_api/stats/endpoints/winprobabilitypbp.md`
- Example output: `docs/nba_api/stats/endpoints_output/winprobabilitypbp_output.md`
- Required python args: `game_id`
- Python:
  ```python
  from nba_api.stats.endpoints import WinProbabilityPBP
  endpoint = WinProbabilityPBP(game_id='…')
  raw = endpoint.get_dict()
  ```
- Query parameters:
  <details>
  <summary>Show parameters</summary>

  | API name | Python arg | Required |
  |---|---|---|
  | `GameID` | `game_id` | yes |
  | `RunType` | `run_type` | no |

  </details>
- Response data sets:
  <details>
  <summary>Show data sets + columns</summary>

  - `GameInfo` (8): `GAME_ID`, `GAME_DATE`, `HOME_TEAM_ID`, `HOME_TEAM_ABR`, `HOME_TEAM_PTS`, `VISITOR_TEAM_ID`, `VISITOR_TEAM_ABR`, `VISITOR_TEAM_PTS`
  - `WinProbPBP` (15): `GAME_ID`, `EVENT_NUM`, `HOME_PCT`, `VISITOR_PCT`, `HOME_PTS`, `VISITOR_PTS`, `HOME_SCORE_MARGIN`, `PERIOD`, `SECONDS_REMAINING`, `HOME_POSS_IND`, `HOME_G`, `DESCRIPTION`, `LOCATION`, `PCTIMESTRING`, `ISVISIBLE`

  </details>

### BoxScore

- HTTP: `GET https://cdn.nba.com/static/json/liveData/boxscore/boxscore_{game_id}.json`
- Repo docs: `docs/nba_api/live/endpoints/boxscore.md`
- Required python args: `game_id`
- Python:
  ```python
  from nba_api.live.nba.endpoints import BoxScore
  endpoint = BoxScore(game_id='…')
  payload = endpoint.get_dict()
  ```

### Odds

- HTTP: `GET https://cdn.nba.com/static/json/liveData/odds/odds_todaysGames.json`
- Repo docs: `docs/nba_api/live/endpoints/odds.md`
- Required python args: none
- Python:
  ```python
  from nba_api.live.nba.endpoints import Odds
  endpoint = Odds()
  payload = endpoint.get_dict()
  ```

### PlayByPlay

- HTTP: `GET https://cdn.nba.com/static/json/liveData/playbyplay/playbyplay_{game_id}.json`
- Repo docs: `docs/nba_api/live/endpoints/playbyplay.md`
- Required python args: `game_id`
- Python:
  ```python
  from nba_api.live.nba.endpoints import PlayByPlay
  endpoint = PlayByPlay(game_id='…')
  payload = endpoint.get_dict()
  ```

### ScoreBoard

- HTTP: `GET https://cdn.nba.com/static/json/liveData/scoreboard/todaysScoreboard_00.json`
- Repo docs: `docs/nba_api/live/endpoints/scoreboard.md`
- Required python args: none
- Python:
  ```python
  from nba_api.live.nba.endpoints import ScoreBoard
  endpoint = ScoreBoard()
  payload = endpoint.get_dict()
  ```
