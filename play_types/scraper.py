
from parser import parse
from selenium import webdriver
from tables.columns import *
from tables.play_types import Playtype
from utils import browserutils
from utils.Player import Player
from utils.Team import Team
from webdriver_manager.chrome import ChromeDriverManager


# Store Stats to Player
def player(player: Player, season_year: str = '2020-21', season_type: str = 'Regular%20Season'):
    '''
    Produces each player's playtype stats from:
        - https://www.nba.com/stats/players/transition/
        - https://www.nba.com/stats/players/isolation/
        - https://www.nba.com/stats/players/ball-handler/
        - https://www.nba.com/stats/players/roll-man/
        - https://www.nba.com/stats/players/playtype-post-up/
        - https://www.nba.com/stats/players/spot-up/
        - https://www.nba.com/stats/players/hand-off/
        - https://www.nba.com/stats/players/cut/
        - https://www.nba.com/stats/players/off-screen/
        - https://www.nba.com/stats/players/putbacks/
        - https://www.nba.com/stats/players/playtype-misc/
    '''

    # Add stat class to player
    player.addTable('playtypes', Playtype())

    # URL Configurations
    name       = player.name.split(' ')[0] + '%20' + player.name.split(' ')[1]
    table_type = 'players/'
    stat       = 'PLAYER_NAME'

    # Start browser
    browser = webdriver.Chrome(ChromeDriverManager().install())

    # Get stats from correct url path
    for playtype_key, playtype_url in playtypes.items():
        for typegroup_key, typegroup_url in type_grouping.items():

            # Browse to correct stat category
            url = 'https://nba.com/stats/' + table_type + playtype_url + '#!?CF=PLAYER_NAME*E*' + name + '&sort=' + stat + '&Season=' + season_year + '&SeasonType=' + season_type + typegroup_url
            browser.get(url)

            # Scrape stats if table exist
            table = browserutils.loadStatTable(browser)
            
            if table is not None:
                parse(table, playtype_key +' (' + typegroup_key.title() + ')', player=player)

    # Close browser
    browser.quit()


# Store Stats to Teams
def teams(teams: Team, season_year: str = '2020-21', season_type: str = 'Regular%20Season'):
    '''
    Produces each player's playtype stats from:
        - https://www.nba.com/stats/teams/transition/
        - https://www.nba.com/stats/teams/isolation/
        - https://www.nba.com/stats/teams/ball-handler/
        - https://www.nba.com/stats/teams/roll-man/
        - https://www.nba.com/stats/teams/playtype-post-up/
        - https://www.nba.com/stats/teams/spot-up/
        - https://www.nba.com/stats/teams/hand-off/
        - https://www.nba.com/stats/teams/cut/
        - https://www.nba.com/stats/teams/off-screen/
        - https://www.nba.com/stats/teams/putbacks/
        - https://www.nba.com/stats/teams/playtype-misc/
    '''

    # Add stat class to teams
    for team in teams:
        teams[team].addTable('playtypes', Playtype())

    # URL Configuration
    table_type = 'teams/'
    stat       = 'TEAM_NAME'

    # Start browser
    browser = webdriver.Chrome(ChromeDriverManager().install())

    # Get stats from correct url path
    for playtype_key, playtype_url in playtypes.items():
        for typegroup_key, typegroup_url in type_grouping.items():

            # Browse to correct stat category
            url = 'https://nba.com/stats/' + table_type + playtype_url + '?sort=' + stat + '&dir=-1' + '&Season=' + season_year + '&SeasonType=' + season_type + typegroup_url
            browser.get(url)

            # Scrape stats if table exist
            table = browserutils.loadStatTable(browser)
            if table is not None:
                parse(table, playtype_key +' (' + typegroup_key.title() + ')', teams=teams)

    # Close browser
    browser.quit()
