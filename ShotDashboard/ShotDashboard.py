"""
SHOT DASHBOARD
"""

import itertools

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from utils import browserutils
from utils.filters import shot_range, shot_clock_range, dribble_range, touch_time_range, closest_defender_distance_range
from utils.headers import getStatColumnType
from utils.Types import TableType


shot_dashboard_types = {
    'general':             shot_range,                      # General
    'shotclock':           shot_clock_range,                # Shotclock
    'dribbles':            dribble_range,                   # Driblles
    'touch-time':          touch_time_range,                # Touch Time
    'closest-defender':    closest_defender_distance_range, # Closet Defender
    'closest-defender-10': closest_defender_distance_range, # Closet Defender Atleast 10 ft
}


class ShotDashboard(dict):
    def __init__(self, table_type=None):
        initShotDashboardTypes(self)

    def __getattr__(self, key):
        return self[key]


# Shot Dashboard Stats
class ShotDashboardStats:
    def __init__(self):
        self.fg_freq   = float() # Field Goal Frequency
        self.fg_m      = float() # Field Goals Made
        self.fg_a      = float() # Field Goals Attemped
        self.fg_pct    = float() # Field Goal Percentage
        self.eFg_pct   = float() # Effective Field Goal Percentage
        self.fg2_freq  = float() # Two Point Field Goal Frequency
        self.fg2_m     = float() # Two Field Goals Made
        self.fg2_a     = float() # Two Point Field Goals Attemped
        self.fg2_pct   = float() # Two Field Goal Percentage
        self.fg3_freq  = float() # Three Point Field Goal Frequency
        self.fg3_m     = float() # Three Field Goals Made
        self.fg3_a     = float() # Three Field Goals Attemped
        self.fg3_pct   = float() # Three Field Goal Percentage


# Get Shot Dashboard Stats
def initShotDashboardTypes(StatClass):

    for shot_dashboard_key, stat_type_dict in shot_dashboard_types.items():
        for stat_filter_key in stat_type_dict.keys():

            key = shot_dashboard_key.title() + ': ' + stat_filter_key
            StatClass[key] = ShotDashboardStats()


# Store Stats to Player
def scrape_player(player, season_year = '2020-21', season_type = 'Regular%20Season'):
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
    browser = webdriver.Chrome(ChromeDriverManager().install())

    # Get Stats and Respective Ranking
    for shot_dashboard_type, shot_dashboard_stats in shot_dashboard_types.items():
        for stat_key, stat_url in shot_dashboard_stats.items():

            shot_dashboard_key = shot_dashboard_type.title() + ': ' + stat_key

            # Browse to correct stat category
            url = 'https://nba.com/stats/' + table_type + stat_type + shot_dashboard_type + '/?CF=PLAYER_NAME*E*' + name + '&sort=' + stat + '&Season=' + season_year + '&SeasonType=' + season_type + stat_url
            browser.get(url)

            # Scrape stats if table exist
            table = browserutils.loadStatTable(browser)
            if table is not None:
                getShotDashboardStats(table, shot_dashboard_key, player=player)

    browser.quit()



# Store Stats to Teams
def collectTeamStats(teams, season_year = '2020-21', season_type = 'Regular%20Season'):
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
                getShotDashboardStats(table, key, teams=teams)

    # Close browser
    browser.quit()


# Get Shot Dashboard Stats
def getShotDashboardStats(table, stat_type, player=None, teams=None):

    table_type = TableType.PLAYER.name if player is not None else TableType.TEAM.name
    (table_header_row, table_column_offset) = getStatColumnType('Shot Dashboard', table_type)

    # Parse statistic table
    index = 1
    for row, info in enumerate(table.split('\n')):

        # Throw away header rows
        if row > table_header_row:

            # Get Correct Player/Team
            if (index % 2) == 1:

                if player is not None:
                    name = info.title()
                    player.name = name
                    StatClass = player.shot_dashboard

                elif teams is not None:
                    team = info.upper()
                    StatClass = teams[team].shot_dashboard

            # Extract stats
            elif (index % 2) == 0:

                # Create iterator
                itr = itertools.count(table_column_offset)

                # Split info from table into a list
                data = info.split(' ')
                data = [stat.replace("-", "0") for stat in data]

                fg_freq  = data[next(itr)]
                StatClass[stat_type].fg_freq = float(fg_freq.strip('%'))

                fg_m     = data[next(itr)]
                StatClass[stat_type].fg_m = float(fg_m)

                fg_a     = data[next(itr)]
                StatClass[stat_type].fg_a = float(fg_a)

                fg_pct   = data[next(itr)]
                StatClass[stat_type].fg_pct = float(fg_pct)

                eFg_pct  = data[next(itr)]
                StatClass[stat_type].eFg_pct = float(eFg_pct)

                fg2_freq = data[next(itr)]
                StatClass[stat_type].fg2_freq = float(fg2_freq.strip('%'))

                fg2_m    = data[next(itr)]
                StatClass[stat_type].fg2_m = float(fg2_m)

                fg2_a    = data[next(itr)]
                StatClass[stat_type].fg2_a = float(fg2_a)

                fg2_pct  = data[next(itr)]
                StatClass[stat_type].fg2_pct = float(fg2_pct)

                fg3_freq = data[next(itr)]
                StatClass[stat_type].fg3_freq = float(fg3_freq.strip('%'))

                fg3_m    = data[next(itr)]
                StatClass[stat_type].fg3_m = float(fg3_m)

                fg3_a    = data[next(itr)]
                StatClass[stat_type].fg3_a = float(fg3_a)

                fg3_pct  = data[next(itr)]
                StatClass[stat_type].fg3_pct = float(fg3_pct)

            index += 1
