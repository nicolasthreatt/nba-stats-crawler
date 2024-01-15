from box_outs.parser import parse
from box_outs.tables.box_outs import BoxOuts
from players.tables.player import Player
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.browsertools import load_stat_table_page
from utils.types import TableType


def player(player: Player, season_year: str = '2020-21', season_type: str = 'Regular%20Season'):
    """
    Produces each player's box out stats from:
        - https://www.nba.com/stats/players/box-outs/
    """

    # Add stat class to player
    player.addTable('boxOutStats', BoxOuts(TableType.PLAYER.name))

    # URL Configurations
    name        = player.name.split(' ')[0] + '%20' + player.name.split(' ')[1]
    table_type  = 'players/'
    stat_type   = 'box-outs'

    # Start browser
    browser = webdriver.Chrome()

    url = 'https://nba.com/stats/' + table_type + stat_type + '/?sort=&CF=PLAYER_NAME*E*' + name + '&Season=' + season_year + '&SeasonType=' + season_type
    browser.get(url)

    # Scrape stats if table exist
    table = load_stat_table_page(browser)
    if table:
        parse(table.text, stat_type.title(), player=player)

    # Close browser
    browser.quit()


def teams(teams: dict, season_year: str = '2020-21', season_type: str = 'Regular+Season'):
    """
    Produces each teams's box out stats from:
        - https://www.stats.nba.com/teams/box-outs/
    
    Args:
        teams (dict): teams dictionary
        season_year (str): season year
        season_type (str): season type
    """

    # Add stat class to teams
    for team in teams:
        teams[team].addTable('boxOutStats', BoxOuts(TableType.TEAM.name))

    # URL Configurations
    table_type  = 'teams/'
    stat_type   = 'box-outs'
    stat        = 'TEAM_NAME'

    # Start browser
    browser = webdriver.Chrome()

    # Browse to correct stat category
    url = 'https://nba.com/stats/' + table_type + stat_type + '/?sort=' + stat + '&dir=-1' + '&Season=' + season_year + '&SeasonType=' + season_type
    browser.get(url)

    # Scrape stats if table exist
    table = browser.find_element(By.CLASS_NAME, "Crom_table__p1iZz")
    if table:
        parse(table.text, stat_type.title(), teams=teams)

    # Close browser
    browser.quit()
