from selenium import webdriver
from selenium.webdriver.common.by import By
from utils import browserutils

NBA_STATS_URL = 'https://www.nba.com/players/'


def get_all_players() -> list:
    """
    Fetches NBA player names from the specified URL.

    Returns:
        List[str]: A list of formatted player names.
    """
    with webdriver.Chrome() as browser:
        browser.get(NBA_STATS_URL)

        # TODO: WAIT FOR PAGE TO FINISH LOADING
        players = [player.text.replace("\n", " ") for player in browser.find_elements(By.CLASS_NAME, "RosterRow_playerName__G28lg")]

    return players


def format(players_unformatted: list) -> list:
    """
    Formats the unformatted player names.

    Args:
        players_unformatted (List[str]): List of unformatted player names.

    Returns:
        List[str]: List of formatted player names.
    """
    formatted_players = []

    for player_unformatted in players_unformatted:
        last_name, first_name = player_unformatted.text.split(',')
        formatted_players.append(f"{first_name.strip()} {last_name}")

    return formatted_players
