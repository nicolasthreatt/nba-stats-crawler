from hustle.parser import parse
from hustle.tables.hustle import Hustle
from players.tables.player import Player
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.types import TableType
from utils.browsertools import load_stat_table_page


# Store Stats to Player
def player(player: Player, season_year: str = '2020-21', season_type: str = 'Regular%20Season'):
    '''
    Produces each player's hustle stats from:
        - https://www.nba.com/stats/players/hustle/
    '''

    # Add stat class to player
    player.addTable('hustle', Hustle())

    # URL Configurations
    name       = player.name.split(' ')[0] + '%20' + player.name.split(' ')[1]
    table_type = 'players/'
    stat_type  = 'hustle'

    # Start browser
    browser = webdriver.Chrome()

    # Browse to correct stat category
    url = 'https://nba.com/stats/' + table_type + stat_type + '/?sort=&CF=PLAYER_NAME*E*' + name + '&Season=' + season_year + '&SeasonType=' + season_type
    browser.get(url)

    # Scrape stats if table exist
    table = load_stat_table_page(browser)
    if table:
        parse(table.text, stat_type.title(), player=player)

    # Close browser
    browser.quit()


# Store Stats to Teams
def teams(teams: dict, season_year: str = '2020-21', season_type: str = 'Regular%20Season'):
    '''
    Produces each team's hustle stats from:
        - https://www.nba.com/stats/teams/hustle/
    '''

    # Add stat class to teams
    for team in teams:
        teams[team].addTable('hustle', Hustle())

    # URl Configurations
    table_type  = 'teams/'
    stat_type   = 'hustle'
    stat        = 'TEAM_NAME'

    # Start browser
    browser = webdriver.Chrome()

    # Browse to correct stat category
    url = 'https://nba.com/stats/' + table_type + stat_type + '?Season=' + season_year + '&SeasonType=' + season_type
    browser.get(url)

    # Scrape stats and get rank if table exist
    table = load_stat_table_page(browser)
    if table:
        parse(table.text, stat_type.title(), teams=teams)

    # Close browser
    browser.quit()
