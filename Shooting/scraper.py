from parser import parse
from selenium import webdriver
from tables.shooting import Shooting
from utils import browserutils
from utils.Player import Player
from utils.Team import Team
from utils.Types import TableType
from webdriver_manager.chrome import ChromeDriverManager


# Store Stats to Player
def player(player: Player, season_year: str = '2020-21', season_type: str = 'Regular%20Season'):
    '''
    Produces each player's shooting stats from:
        - https://wwww.nba.com/stats/players/shooting/
    '''

    # Add stat class to player
    player.addTable('shooting', Shooting())

    # URL Configurations
    name       = player.name.split(' ')[0] + '%20' + player.name.split(' ')[1]
    table_type = 'players/'
    stat_type  = 'shooting'
    stat       = 'PLAYER_NAME'

    # Start browser
    browser = webdriver.Chrome(ChromeDriverManager().install())

    # Get stats from correct url path
    for shooting_distance_range_key, shooting_distance_range_url in distance_range.items():

        # Browse to correct stat category
        url = 'https://nba.com/stats/' + table_type + stat_type + '/?sort=' + stat + '&CF=PLAYER_NAME*E*' + name + '&Season=' + season_year + '&SeasonType=' + season_type + shooting_distance_range_url
        browser.get(url)
        
        # Scrape stats if table exist
        table = browserutils.loadStatTable(browser)
        if table is not None:
            parse(table, shooting_distance_range_key, player=player)

    # Close browser
    browser.quit()


# Store Stats to Teams
def teams(teams: Team, season_year: str = '2020-21', season_type: str = 'Regular%20Season'):
    '''
    Produces each teams's shooting stats from:
        - https://www.nba.com/stats/teams/shooting/
    '''

    # Add stat class to teams
    for team in teams:
        teams[team].addTable('shooting', Shooting())

    # URL Configurations
    table_type = 'teams/'
    stat_type  = 'shooting'

    # Start browser
    browser = webdriver.Chrome(ChromeDriverManager().install())

    for shooting_distance_range_key, shooting_distance_range_url in distance_range.items():

        # Browse to correct stat category
        url = 'https://nba.com/stats/' + table_type + stat_type  + '/?' + '&Season=' + season_year + '&SeasonType=' + season_type + shooting_distance_range_url
        browser.get(url)

        # Scrape stats if table exist
        table = browserutils.loadStatTable(browser)
        if table is not None:
            parse(table, shooting_distance_range_key, teams=teams)

    # Close browser
    browser.quit()

