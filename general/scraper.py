from general.parser import parse
from general.tables.general import General
from general.helpers import stats_urls_tables
from players.tables.player import Player
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.browsertools import load_stat_table_page
from utils.types import TableType


# Store Stats to Player
def player(player: Player, season_year: str = '2020-21', season_type: str = 'Regular%20Season'):
    '''
    Produces each player's general stats from:
        - https://www.nba.com/stats/players/traditional/
        - https://www.nba.com/stats/players/advanced/
        - https://www.nba.com/stats/players/misc/
        - https://www.nba.com/stats/players/scoring/
        - https://www.nba.com/stats/players/usage/
        - https://www.nba.com/stats/players/opponent/
        - https://www.nba.com/stats/players/defense/
    '''

    # Add stat class to player
    player.addTable('general', General(TableType.PLAYER.name))

    # URL Configurations
    name       = player.name.split(' ')[0] + '%20' + player.name.split(' ')[1]
    table_type = 'players/'
    stat       = 'PLAYER_NAME'

    # Start browser
    browser = webdriver.Chrome()

    # Get stats from correct url path
    for stat_key, stat_url in stats_urls_tables.items():
        if stat_key != 'Four Factors':
            # Browse to correct stat category
            url = 'https://nba.com/stats/' + table_type + stat_url + '/#!?CF=PLAYER_NAME*E*' + name + '&sort=' + stat + '&Season=' + season_year + '&SeasonType=' + season_type
            browser.get(url)

            # Scrape stats if table exists
            table = load_stat_table_page(browser)
            if table.text:
                parse(table.text, stat_key.title(), player=player)

    # Close browser
    browser.quit()


# Store Stats to Teams
def teams(teams: dict, season_year: str = '2020-21', season_type: str = 'Regular%20Season'):
    '''
    Produces each team's general stats from:
        - https://nba.com/stats/teams/traditional/
        - https://nba.com/stats/teams/advanced/
        - https://nba.com/stats/teams/four-factors/
        - https://nba.com/stats/teams/misc/
        - https://nba.com/stats/teams/scoring/
        - https://nba.com/stats/teams/opponent/
        - https://nba.com/stats/teams/defense/
    '''

    # Add stat class to teams
    for team in teams:
        teams[team].addTable('general', General(TableType.TEAM.name))

    # URL Configurations
    table_type  = 'teams/'
    stat        = 'TEAM_NAME'

    # Start browser
    browser = webdriver.Chrome()

    for stat_key, stat_url in stats_urls_tables.items():

        if stat_key != 'Usage':
            # Browse to correct stat category
            url = 'https://nba.com/stats/' + table_type  + stat_url + '?sort=' + stat + '&dir=-1' + '&Season=' + season_year + '&SeasonType=' + season_type
            browser.get(url)

            table = load_stat_table_page(browser)
            if table.text:
                parse(table.text, stat_key.title(), teams=teams)

    # Close browser
    browser.quit()

