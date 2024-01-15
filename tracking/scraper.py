from players.tables.player import Player
from selenium import webdriver
from selenium.webdriver.common.by import By
from tracking.parser import parse
from tracking.tables.tracking import Tracking, tracking_tables
from utils.browsertools import load_stat_table_page
from utils.types import TableType


# Store Stats to Player
def player(player: Player, season_year: str = '2020-21', season_type: str = 'Regular%20Season'):
    '''
    Produces each player's tracking stats from:
        - https://www.nba.com/stats/players/drives/
        - https://www.nba.com/stats/players/defensive-impact/
        - https://www.nba.com/stats/players/catch-shoot/
        - https://www.nba.com/stats/players/passing/
        - https://www.nba.com/stats/players/touches/
        - https://www.nba.com/stats/players/pullup/
        - https://www.nba.com/stats/players/rebounding/
        - https://www.nba.com/stats/players/offensive-rebounding/
        - https://www.nba.com/stats/players/defensive-rebounding/
        - https://www.nba.com/stats/players/shooting-efficiency/
        - https://www.nba.com/stats/players/speed-distance/
        - https://www.nba.com/stats/players/elbow-touch/
        - https://www.nba.com/stats/players/tracking-post-ups/
        - https://www.nba.com/stats/players/paint-touch/
    '''

    # Add stat class to player
    player.addTable('tracking', Tracking(TableType.PLAYER.name))

    # URL Configurations
    name       = player.name.split(' ')[0] + '%20' + player.name.split(' ')[1]
    table_type = 'players/'
    stat       = 'PLAYER_NAME'

    # Start browser
    browser = webdriver.Chrome()

    # Get stats from correct url path
    for stat_key, stat_url in tracking_tables.items():

        # Browse to correct stat category
        url = 'https://nba.com/stats/' + table_type + stat_url + '/?CF=PLAYER_NAME*E*' + name + '&sort=' + stat + '&Season=' + season_year + '&SeasonType=' + season_type
        browser.get(url)

        # Scrape stats if table exist
        table = load_stat_table_page(browser)
        if table:
            parse(table.text, stat_key, player=player)

    # Close browser
    browser.quit()


# Store Stats to Teams
def teams(teams: dict, season_year: str = '2020-21', season_type: str = 'Regular%20Season'):
    '''
    Produces each team's tracking stats from:
        - https://nba.com/stats/teams/drives/
        - https://nba.com/stats/teams/defensive-impact/
        - https://nba.com/stats/teams/catch-shoot/
        - https://nba.com/stats/teams/passing/
        - https://nba.com/stats/teams/touches/
        - https://nba.com/stats/teams/pullup/
        - https://nba.com/stats/teams/rebounding/
        - https://nba.com/stats/teams/offensive-rebounding/
        - https://nba.com/stats/teams/defensive-rebounding/
        - https://nba.com/stats/teams/shooting-efficiency/
        - https://nba.com/stats/teams/speed-distance/
        - https://nba.com/stats/teams/elbow-touch/
        - https://nba.com/stats/teams/tracking-post-ups/
        - https://nba.com/stats/teams/paint-touch/
    '''

    # Add stat class to teams
    for team in teams:
        teams[team].addTable('tracking', Tracking(TableType.TEAM.name))

    # URL Configurations
    table_type = 'teams/'
    stat       = 'TEAM_NAME'

    # Start browser
    browser = webdriver.Chrome()

    for stat_key, stat_url in tracking_tables.items():

        # Browse to correct stat category
        url = 'https://nba.com/stats/' + table_type + stat_url + '?sort=' + stat + '&dir=-1' + '&Season=' + season_year + '&SeasonType=' + season_type
        browser.get(url)

        # Scrape stats if table exist
        table = load_stat_table_page(browser)
        if table:
            parse(table.text, stat_key, teams=teams)

    # Close browser
    browser.quit()
