from itertools import cycle
from players.parser import create_new_player
from players.tables.player import Player
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.browsertools import load_stat_table_page


NBA_STATS_URL = 'https://www.nba.com/stats/players/bio/'


def retrieve_player(name: str, season_year: str = '2020-21', season_type: str = 'Regular%20Season') -> list:
    """
    Retreives NBA player names from the specified URL.

    Returns:
        List[str]: A list of formatted player names.
    """
    player = Player()
    with webdriver.Chrome() as browser:

        browser.get(NBA_STATS_URL + '?sort=&CF=PLAYER_NAME*E*' + name.replace(' ', '%20') + '&Season=' + season_year + '&SeasonType=' + season_type)
        browser = load_stat_table_page(browser)

        headers = browser.find_elements(By.TAG_NAME, 'th')
        rows    = browser.find_elements(By.TAG_NAME, 'td')

        bio = dict()
        for header, row in zip(cycle(headers), rows):
            bio[header.text.strip()] = row.text.strip()
            if len(bio) == len(headers):
                break
        
        player = create_new_player(bio)

    browser.quit()

    return player


def retrieve_all_players(season_year: str = '2020-21', season_type: str = 'Regular%20Season') -> list:
    """
    Retreives NBA player names from the specified URL.

    Returns:
        List[str]: A list of formatted player names.
    """
    players = list()
    with webdriver.Chrome() as browser:
        browser.get(NBA_STATS_URL + '?Season=' + season_year + '&SeasonType=' + season_type)
        browser = load_stat_table_page(browser)

        headers = browser.find_elements(By.TAG_NAME, 'th')
        rows    = browser.find_elements(By.TAG_NAME, 'td')

        bio = dict()
        for header, row in zip(cycle(headers), rows):
            bio[header.text.strip()] = row.text.strip()
            if len(bio) == len(headers):
                players.append(create_new_player(bio))
                bio.clear()

    browser.quit()

    return players
