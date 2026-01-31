from nba_api.stats.endpoints import ScoreboardV3, BoxScoreTraditionalV3

# sb_endpoint = ScoreboardV3(game_date='2025-06-22')
# sb_data = sb_endpoint.get_dict()
# print(f"Scoreboard Data: {sb_data}")

bx_endpoint = BoxScoreTraditionalV3(game_id='0042400407')
bx_data = bx_endpoint.get_dict()
print(f"Box Score Data: {bx_data}") 