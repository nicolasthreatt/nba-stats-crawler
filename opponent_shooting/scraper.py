from opponent_shooting.parser import parse
from selenium import webdriver
from opponent_shooting.tables.opponent_shooting import OpponentShooting
from opponent_shooting.tables.opponent_shooting import opponent_shooting_stats_types
from players.tables.player import Player
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.browsertools import load_stat_table_page
from utils.filters import *
from utils.types import TableType


# Store Stats to Player
def player(player: Player, season_year: str = '2020-21', season_type: str = 'Regular%20Season'):
    '''
    Produces each player's opponent shooting stats from:
        - https://www.nba.com/stats/players/opponent-shooting/
    '''

    # Add stat class to player
    player.addTable('opponent_shooting', OpponentShooting(TableType.PLAYER.name))

    # URL Configurations
    name       = player.name.split(' ')[0] + '%20' + player.name.split(' ')[1]
    table_type = 'players/'
    stat_key   = list(opponent_shooting_stats_types.keys())[0] 
    stat_url   = list(opponent_shooting_stats_types.values())[0] 

    # Start browser
    browser = webdriver.Chrome()

    # Get stats from correct url path
    for distance_range_key, distance_range_url in distance_range.items():

        # Browse to correct stat category
        url = 'https://nba.com/stats/' + table_type + stat_url + '?sort=&CF=PLAYER_NAME*E*' + name + '&Season=' + season_year + '&SeasonType=' + season_type + distance_range_url
        browser.get(url)

        # Scrape stats if table exist
        table = load_stat_table_page(browser)
        if table:
            parse(table.text, 'Opponent Shooting ' + stat_key + ' ' + distance_range_key, player=player)

    # Close browser
    browser.quit()


# Store Stats to Teams
def teams(teams: dict, season_year: str = '2020-21', season_type: str = 'Regular%20Season'):
    '''
    Produces each team's opponent shooting stats from:
        - https://www.nba.com/stats/teams/opponent-shooting/
        - https://www.nba.com/stats/teams/opponent-shots-general/
        - https://www.nba.com/stats/teams/opponent-shooting-shotclock/
        - https://www.nba.com/stats/teams/opponent-shooting-dribbles/
        - https://www.nba.com/stats/teams/opponent-shooting-touch-time/
        - https://www.nba.com/stats/teams/opponent-shooting-closest-defender/
        - https://www.nba.com/stats/teams/opponent-shooting-closest-defender-10/
    '''

    # Add stat class to teams
    for team in teams:
        teams[team].addTable('opponent_shooting', OpponentShooting(TableType.TEAM.name))

    # Start browser
    browser = webdriver.Chrome()

    for stat_key, stat_url in opponent_shooting_stats_types.items():

        if stat_key == 'Overall':
            for  distance_range_key, distance_range_url in distance_range.items():
                browse_page(browser, teams, stat_url, distance_range_url, distance_range_key, stat_key)

        elif stat_key == 'General':
            for  shot_range_key, shot_range_url in shot_range.items():
                browse_page(browser, teams, stat_url, shot_range_url, shot_range_key, stat_key)

        elif stat_key == 'Shot Clock':
            for  shot_clock_range_key, shot_clock_range_url in shot_clock_range.items():
                browse_page(browser, teams, stat_url, shot_clock_range_url, shot_clock_range_key, stat_key)

        elif stat_key == 'Dribbles':
            for  dribble_range_key, dribble_range_url in dribble_range.items():
                browse_page(browser, teams, stat_url, dribble_range_url, dribble_range_key, stat_key)

        elif stat_key == 'Touch Time':
            for  touch_time_key, touch_time_url in touch_time_range.items():
                browse_page(browser, teams, stat_url, touch_time_url, touch_time_key, stat_key)

        elif stat_key in ('Closest Defender', 'Closest Defender 10ft'):
            for  closest_defender_key, closest_defender_url in closest_defender_distance_range.items():
                browse_page(browser, teams, stat_url, closest_defender_url, closest_defender_key, stat_key)

    # Close browser
    browser.quit()


def browse_page(browser, teams, table_url, stat_url, stat_type, stat_key, season_year = '2019-20', season_type = 'Regular%20Season'):

    # URL Configurations
    table_type  = 'teams/'
    stat        = 'TEAM_NAME'

    # Browse to correct stat category
    url = 'https://nba.com/stats/' + table_type + table_url + '?'+ stat_url+ '&Season=' + season_year + '&SeasonType=' + season_type + '&sort=' + stat
    browser.get(url)

    # Scrape stats if table exist
    table = load_stat_table_page(browser)
    if table:
        parse(table.text, stat_key, stat_type, teams=teams)
