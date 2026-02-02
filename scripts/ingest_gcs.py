import argparse
import json
from datetime import datetime
from google.cloud import storage
from nba_api.stats.endpoints import BoxScoreTraditionalV3, ScoreboardV3

client = storage.Client()
bucket = client.bucket('nba-stats-9070')

def fetch_scoreboard(game_date):
    """
    Fetches the NBA scoreboard for a given date.

    Parameters:
    game_date (str): The date for which to fetch the scoreboard in 'YYYY-MM-DD' format.

    Returns:
    dict: The scoreboard data.
    """
    scoreboard = ScoreboardV3(game_date=game_date)

    return scoreboard.get_dict()

def extract_game_ids(data):
    """
    Extracts game IDs from the NBA scoreboard for a given date.
    Parameters:
    date_str (str): The date for which to extract game IDs in 'YYYY-MM-DD' format.

    Returns:
    list: A list of game IDs.
    """

    games = data.get('scoreboard', {}).get('games', [])
    games_ids = [game.get('gameId') for game in games]

    return games_ids

def fetch_box_score(game_id):
    """
    Fetches the box score for a given game ID.

    Parameters:
    game_id (str): The game ID for which to fetch the box score.

    Returns:
    dict: The box score data.
    """
    box_score = BoxScoreTraditionalV3(game_id=game_id)

    return box_score.get_dict()

def upload_to_gcs(data, gcs_path):
    """
    Uploads data to Google Cloud Storage.

    Parameters:
    data (dict): The data to upload.
    gcs_path (str): The GCS path where the data should be uploaded.
    """
    blob = bucket.blob(gcs_path)
    blob.upload_from_string(json.dumps(data, indent=2),
    content_type='application/json')

def main():
    """
    Main function to ingest NBA scoreboard and box score data for a given date.
    """

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--date', type=str, help='Date in YYYY-MM-DD format', required=True)
    args = arg_parser.parse_args()
    date_str = args.date

    run_id = datetime.now().strftime('%Y%m%d_%H%M%S')

    scoreboard_path = f'raw/nba/scoreboard/dt={date_str}/run_id={run_id}/scoreboard.json'
    scoreboard_data = fetch_scoreboard(date_str)
    upload_to_gcs(scoreboard_data, scoreboard_path)

    game_ids = extract_game_ids(scoreboard_data)

    for game_id in game_ids:
        boxscore_path = f"raw/nba/boxscore/dt={date_str}/game_id={game_id}/run_id={run_id}/boxscore.json"
        box_score_data = fetch_box_score(game_id)
        upload_to_gcs(box_score_data, boxscore_path)
            
if __name__ == "__main__":
    main()