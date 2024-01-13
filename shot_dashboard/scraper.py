from players.tables.player import Player
from selenium import webdriver
from selenium.webdriver.common.by import By
from shot_dashboard.parser import parse
from shot_dashboard.tables.shot_dashboard import ShotDashboard
from shot_dashboard.tables.shot_dashboard import shot_dashboard_types
from utils.browsertools import load_stat_table_page
from utils.types import TableType


# Store Stats to Player
def player(player: Player, season_year: str = '2020-21', season_type: str = 'Regular%20Season'):
    '''
    Produces each player's shot dashboard stats from:
        - https://www.nba.com/stats/players/shots-general/
        - https://www.nba.com/stats/players/shots-shotclock/
        - https://www.nba.com/stats/players/shots-dribbles/
        - https://www.nba.com/stats/players/shots-touch-time/
        - https://www.nba.com/stats/players/shots-closest-defender/
        - https://www.nba.com/stats/players/shots-closest-defender-10/
    '''

    # Add stat class to player
    player.addTable('shot_dashboard', ShotDashboard())

    # URL Configurations
    name       = player.name.split(' ')[0] + '%20' + player.name.split(' ')[1]
    table_type = 'players/'
    stat_type  = 'shots-'
    stat       = 'PLAYER_NAME'

    # Start browser
    browser = webdriver.Chrome()

    # Get Stats and Respective Ranking
    for shot_dashboard_type, shot_dashboard_stats in shot_dashboard_types.items():
        for stat_key, stat_url in shot_dashboard_stats.items():

            shot_dashboard_key = shot_dashboard_type.title() + ': ' + stat_key

            # Browse to correct stat category
            url = 'https://nba.com/stats/' + table_type + stat_type + shot_dashboard_type + '/?CF=PLAYER_NAME*E*' + name + '&sort=' + stat + '&Season=' + season_year + '&SeasonType=' + season_type + stat_url
            browser.get(url)

            # Scrape stats if table exist
            table = load_stat_table_page(browser)
            if table.text:
                parse(table.text, shot_dashboard_key, player=player)

    browser.quit()



# Store Stats to Teams
def teams(teams: dict, season_year: str = '2020-21', season_type: str = 'Regular%20Season'):
    '''
    Produces each player's shot dashboard stats from:
        - https://www.nba.com/stats/teams/shots-general/
        - https://www.nba.com/stats/teams/shots-shotclock/
        - https://www.nba.com/stats/teams/shots-dribbles/
        - https://www.nba.com/stats/teams/shots-touch-time/
        - https://www.nba.com/stats/teams/shots-closest-defender/
        - https://www.nba.com/stats/teams/shots-closest-defender-10/
    '''

    # Add stat class to teams
    for team in teams:
        teams[team].addTable('shot_dashboard', ShotDashboard())

    # URL Configurations
    table_type = 'teams/'
    stat_type   = 'shots-'

    # Start browser
    browser = webdriver.Chrome(ChromeDriverManager().install())

    # Get Stats and Respective Ranking
    for shot_dashboard_key, stat_filters_dict in shot_dashboard_types.items():
        for stat_key, stat_url in stat_filters_dict.items():

            key = shot_dashboard_key.title() + ': ' + stat_key

            # Browse to correct stat category
            url = 'https://nba.com/stats/' + table_type + stat_type + shot_dashboard_key + '/?' + '&Season=' + season_year + '&SeasonType=' + season_type + stat_url
            browser.get(url)

            # Scrape stats if table exist
            table = browserutils.loadStatTable(browser)
            if table is not None:
                parse(table, key, teams=teams)

    # Close browser
    browser.quit()
