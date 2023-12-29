from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from utils import browserutils

NBA_STATS_URL = 'https://www.nba.com/stats/players/list/'


def get_players() -> list:
    """
    Fetches NBA player names from the specified URL.

    Returns:
        List[str]: A list of formatted player names.
    """
    with webdriver.Chrome(ChromeDriverManager().install()) as browser:
        browser.get(NBA_STATS_URL)
        players_unformatted = browserutils.load_players_list(browser)
    
    players = format(players_unformatted)
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
