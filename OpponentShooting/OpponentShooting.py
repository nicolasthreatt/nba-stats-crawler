"""
OPPONENT SHOOTING
"""

import itertools
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from utils import browserutils
from utils.filters import *
from utils.headers import getStatColumnType
from utils.Types import TableType

opponent_shooting_stats_types = {
    'Overall':               'opponent-shooting/',
    'General':               'opponent-shots-general/',
    'Shot Clock':            'opponent-shots-shotclock/',
    'Dribbles':              'opponent-shots-dribbles/',
    'Touch Time':            'opponent-shots-touch-time/',
    'Closest Defender':      'opponent-shots-closest-defender/',
    'Closest Defender 10ft': 'opponent-shots-closest-defender-10/',
}


class OpponentShooting(dict):
    def __init__(self, table_type):
        initOpponentShootingTypes(self, table_type)

    def __getattr__(self, key):
        return self[key]


# Shooting 5Ft Stats
class Shooting5Ft:
    def __init__(self):
        self.fg_m_lt_5ft         = float() # Field Goals Made Less Than 5FT
        self.fg_a_lt_5ft         = float() # Field Goals Attempted Less Than 5FT
        self.fg_pct_lt_5ft       = float() # Field Goals Percentage Less Than 5FT
        self.fg_m_5ft_to_9ft     = float() # Field Goals Made 5ft to 9ft
        self.fg_a_5ft_to_9ft     = float() # Field Goals Attempted 5ft to 9ft
        self.fg_pct_5ft_to_9ft   = float() # Field Goals Percentage 5ft to 9ft
        self.fg_m_10ft_to_14ft   = float() # Field Goals Made 10ft to 14ft
        self.fg_a_10ft_to_14ft   = float() # Field Goals Attempted 10ft to 14ft
        self.fg_pct_10ft_to_14ft = float() # Field Goals Percentage 10ft to 14ft
        self.fg_m_15ft_to_19ft   = float() # Field Goals Made 15ft to 19ft
        self.fg_a_15ft_to_19ft   = float() # Field Goals Attempted 15ft to 19ft
        self.fg_pct_15ft_to_19ft = float() # Field Goals Percentage 15ft to 19ft
        self.fg_m_20ft_to_24ft   = float() # Field Goals Made 20ft to 24ft
        self.fg_a_20ft_to_24ft   = float() # Field Goals Attempted 20ft to 24ft
        self.fg_pct_20ft_to_24ft = float() # Field Goals Percentage 20ft to 24ft
        self.fg_m_25ft_to_29ft   = float() # Field Goals Made 25ft to 29ft
        self.fg_a_25ft_to_29ft   = float() # Field Goals Attempted 25ft to 29ft
        self.fg_pct_25ft_to_29ft = float() # Field Goals Percentage 25ft to 29ft


# Shooting 8Ft Stats
class Shooting8Ft:
    def __init__(self):
        self.fg_m_lt_8ft           = float() # Field Goals Made Less Than 8FT
        self.fg_a_lt_8ft           = float() # Field Goals Attempted Less Than 8FT
        self.fg_pct_lt_8ft         = float() # Field Goals Percentage Less Than 8FT
        self.fg_m_8ft_to_16ft      = float() # Field Goals Made 8ft to 16ft
        self.fg_a_8ft_to_16ft      = float() # Field Goals Attempted 8ft to 16ft
        self.fg_pct_8ft_to_16ft    = float() # Field Goals Percentage 8ft to 16ft
        self.fg_m_16ft_to_24ft     = float() # Field Goals Made 16ft to 24ft
        self.fg_a_16ft_to_24ft     = float() # Field Goals Attempted 16ft to 24ft
        self.fg_pct_16ft_to_24ft   = float() # Field Goals Percentage 16ft to 24ft
        self.fg_m_24ft_plus        = float() # Field Goals Made 24ft Plus
        self.fg_a_24ft_plus        = float() # Field Goals Attempted 24ft Plus
        self.fg_pct_24ft_plus      = float() # Field Goals Percentage 24ft Plus
        self.fg_m_backcourt_shot   = float() # Field Goals Made Backcourt Shot
        self.fg_a_backcourt_shot   = float() # Field Goals Attempted Backcourt Shot
        self.fg_pct_backcourt_shot = float() # Field Goals Percentage Backcourt Shot


class ShootingZone:
    def __init__(self):
        self.fg_m_restricted_area   = float() # Field Goals Made Restricted Area
        self.fg_a_restricted_area   = float() # Field Goals Attempted Restricted Area
        self.fg_pct_restricted_area = float() # Field Goal Percentage Restricted Area
        self.fg_m_paint             = float() # Field Goals Made In Paint (Non Restricted Area)
        self.fg_a_paint             = float() # Field Goals Attempted In Paint (Non Restricted Area)
        self.fg_pct_paint           = float() # Field Goal Percentage In Paint (Non Restricted Area)
        self.fg_m_midrange          = float() # Field Goals Made Midrange
        self.fg_a_midrange          = float() # Field Goals Attempted Midrange
        self.fg_pct_midrange        = float() # Field Goal Percentage Midrange
        self.fg_m_left_corner_3     = float() # Field Goals Made Left Corner 3
        self.fg_a_left_corner_3     = float() # Field Goals Attempted Left Corner 3
        self.fg_pct_left_corner_3   = float() # Field Goal Percentage Left Corner 3
        self.fg_m_right_corner_3    = float() # Field Goals Made Right Corner 3
        self.fg_a_right_corner_3    = float() # Field Goals Attempted Right Corner 3
        self.fg_pct_right_corner_3  = float() # Field Goal Percentage Right Corner 3
        self.fg_m_corner_3          = float() # Field Goals Made Corner 3
        self.fg_a_corner_3          = float() # Field Goals Attempted Corner 3
        self.fg_pct_corner_3        = float() # Field Goal Percentage Corner 3
        self.fg_m_above_break_3     = float() # Field Goals Made Above The Break 3
        self.fg_a_above_break_3     = float() # Field Goals Attempted Above The Break 3
        self.fg_pct_above_break_3   = float() # Field Goal Percentage Above The Break 3


# Shot Dashboard Stats
class ShotDashboard:
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


# Get Opponent Shooting Stats
def initOpponentShootingTypes(StatClass, table_type):
    for distance_key in distance_range:
        if distance_key == '5ft Range':
            StatClass[distance_key] = Shooting5Ft()
        elif distance_key == '8ft Range':
            StatClass[distance_key] = Shooting8Ft()
        elif distance_key == 'By Zone':
            StatClass[distance_key] = ShootingZone()

    if table_type == TableType.TEAM.name:
        for shot_type_key in shot_range:
            StatClass[shot_type_key]  = ShotDashboard()

        for shot_clock_key in shot_clock_range:
            StatClass[shot_clock_key] = ShotDashboard()

        for dribbles_key in dribble_range:
            StatClass[dribbles_key]   = ShotDashboard()

        for touch_time_key in touch_time_range:
            StatClass[touch_time_key] = ShotDashboard()

        for closest_defender_distance_key in closest_defender_distance_range:
            StatClass[closest_defender_distance_key] = ShotDashboard()


# Store Stats to Player
def scrape_player(player, season_year = '2020-21', season_type = 'Regular%20Season'):
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
    browser = webdriver.Chrome(ChromeDriverManager().install())

    # Get stats from correct url path
    for distance_range_key, distance_range_url in distance_range.items():

        # Browse to correct stat category
        url = 'https://nba.com/stats/' + table_type + stat_url + '?sort=&CF=PLAYER_NAME*E*' + name + '&Season=' + season_year + '&SeasonType=' + season_type + distance_range_url
        browser.get(url)

        # Scrape stats if table exist
        table = browserutils.loadStatTable(browser)
        if table is not None:
            getOpponentShootingStats(table, distance_range_key, 'Opponent Shooting ' + stat_key + ' ' + distance_range_key, player=player)

    # Close browser
    browser.quit()


# Store Stats to Teams
def collectTeamStats(teams, season_year = '2020-21', season_type = 'Regular%20Season'):
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
    browser = webdriver.Chrome(ChromeDriverManager().install())

    for stat_key, stat_url in opponent_shooting_stats_types.items():

        if stat_key == 'Overall':
            for  distance_range_key, distance_range_url in distance_range.items():
                browsePage(browser, teams, stat_url, distance_range_url, distance_range_key, stat_key)

        elif stat_key == 'General':
            for  shot_range_key, shot_range_url in shot_range.items():
                browsePage(browser, teams, stat_url, shot_range_url, shot_range_key, stat_key)

        elif stat_key == 'Shot Clock':
            for  shot_clock_range_key, shot_clock_range_url in shot_clock_range.items():
                browsePage(browser, teams, stat_url, shot_clock_range_url, shot_clock_range_key, stat_key)

        elif stat_key == 'Dribbles':
            for  dribble_range_key, dribble_range_url in dribble_range.items():
                browsePage(browser, teams, stat_url, dribble_range_url, dribble_range_key, stat_key)

        elif stat_key == 'Touch Time':
            for  touch_time_key, touch_time_url in touch_time_range.items():
                browsePage(browser, teams, stat_url, touch_time_url, touch_time_key, stat_key)

        elif stat_key in ('Closest Defender', 'Closest Defender 10ft'):
            for  closest_defender_key, closest_defender_url in closest_defender_distance_range.items():
                browsePage(browser, teams, stat_url, closest_defender_url, closest_defender_key, stat_key)

    # Close browser
    browser.quit()


def browsePage(browser, teams, table_url, stat_url, stat_type, stat_key, season_year = '2019-20', season_type = 'Regular%20Season'):

    # URL Configurations
    table_type  = 'teams/'
    stat        = 'TEAM_NAME'

    # Browse to correct stat category
    url = 'https://nba.com/stats/' + table_type + table_url + '?'+ stat_url+ '&Season=' + season_year + '&SeasonType=' + season_type + '&sort=' + stat
    browser.get(url)

    # Scrape stats if table exist
    table = browserutils.loadStatTable(browser)
    if table is not None:
        if stat_key == "Overall":
            getOpponentShootingStats(table, stat_type, 'Opponent Shooting ' + stat_key + ' ' + stat_type, teams=teams)
        else:
            getOpponentShootingStats(table, stat_type, 'Opponent Shooting ' + stat_key, teams=teams)


# Collect Stats
def getOpponentShootingStats(table, stat_type, stat_key, player=None, teams=None):

    table_type = TableType.PLAYER.name if player is not None else TableType.TEAM.name
    (table_header_row, table_column_offset) = getStatColumnType(stat_key, table_type)

    # Parse statistic table
    index = 1

    for row, info in enumerate(table.split('\n')):

        # Throwaway junk lines (column names)
        if row > table_header_row:

            # Get Correct Player/Team
            if (index % 2) == 1:

                if player is not None:
                    name = info.title()
                    player.name = name
                    StatClass = player.opponent_shooting

                elif teams is not None:
                    team = info.upper()
                    StatClass = teams[team].opponent_shooting

            # Extract stats
            elif (index % 2) == 0:

                # Create iterator
                itr = itertools.count(table_column_offset)

                # Split info from table into a list
                data = info.split(' ')
                data = [stat.replace("-", "0") for stat in data]

                if stat_type == '5ft Range':
                    fg_m_lt_5ft         = data[next(itr)]
                    StatClass[stat_type].fg_m_lt_5ft = float(fg_m_lt_5ft)

                    fg_a_lt_5ft         = data[next(itr)]
                    StatClass[stat_type].fg_a_lt_5ft = float(fg_a_lt_5ft)

                    fg_pct_lt_5ft       = data[next(itr)]
                    StatClass[stat_type].fg_pct_lt_5ft = float(fg_pct_lt_5ft)

                    fg_m_5ft_to_9ft     = data[next(itr)]
                    StatClass[stat_type].fg_m_5ft_to_9ft = float(fg_m_5ft_to_9ft)

                    fg_a_5ft_to_9ft     = data[next(itr)]
                    StatClass[stat_type].fg_a_5ft_to_9ft = float(fg_a_5ft_to_9ft)

                    fg_pct_5ft_to_9ft   = data[next(itr)]
                    StatClass[stat_type].fg_pct_5ft_to_9ft = float(fg_pct_5ft_to_9ft)

                    fg_m_10ft_to_14ft   = data[next(itr)]
                    StatClass[stat_type].fg_m_10ft_to_14ft = float(fg_m_10ft_to_14ft)

                    fg_a_10ft_to_14ft   = data[next(itr)]
                    StatClass[stat_type].fg_a_10ft_to_14ft = float(fg_a_10ft_to_14ft)

                    fg_pct_10ft_to_14ft = data[next(itr)]
                    StatClass[stat_type].fg_pct_10ft_to_14ft = float(fg_pct_10ft_to_14ft)

                    fg_m_15ft_to_19ft   = data[next(itr)]
                    StatClass[stat_type].fg_m_15ft_to_19ft = float(fg_m_15ft_to_19ft)

                    fg_a_15ft_to_19ft   = data[next(itr)]
                    StatClass[stat_type].fg_a_15ft_to_19ft = float(fg_a_15ft_to_19ft)

                    fg_pct_15ft_to_19ft = data[next(itr)]
                    StatClass[stat_type].fg_pct_15ft_to_19ft = float(fg_pct_15ft_to_19ft)

                    fg_m_20ft_to_24ft   = data[next(itr)]
                    StatClass[stat_type].fg_m_20ft_to_24ft = float(fg_m_20ft_to_24ft)

                    fg_a_20ft_to_24ft   = data[next(itr)]
                    StatClass[stat_type].fg_a_20ft_to_24ft = float(fg_a_20ft_to_24ft)

                    fg_pct_20ft_to_24ft = data[next(itr)]
                    StatClass[stat_type].fg_pct_20ft_to_24ft = float(fg_pct_20ft_to_24ft)

                    fg_m_25ft_to_29ft   = data[next(itr)]
                    StatClass[stat_type].fg_m_25ft_to_29ft = float(fg_m_25ft_to_29ft)

                    fg_a_25ft_to_29ft   = data[next(itr)]
                    StatClass[stat_type].fg_a_25ft_to_29ft = float(fg_a_25ft_to_29ft)

                    fg_pct_25ft_to_29ft = data[next(itr)]
                    StatClass[stat_type].fg_pct_25ft_to_29ft = float(fg_pct_25ft_to_29ft)

                elif stat_type == '8ft Range':
                    fg_m_lt_8ft           = data[next(itr)]
                    StatClass[stat_type].fg_m_lt_8ft = float(fg_m_lt_8ft)

                    fg_a_lt_8ft           = data[next(itr)]
                    StatClass[stat_type].fg_a_lt_8ft = float(fg_a_lt_8ft)

                    fg_pct_lt_8ft         = data[next(itr)]
                    StatClass[stat_type].fg_pct_lt_8ft = float(fg_pct_lt_8ft)

                    fg_m_8ft_to_16ft      = data[next(itr)]
                    StatClass[stat_type].fg_m_8ft_to_16ft = float(fg_m_8ft_to_16ft)

                    fg_a_8ft_to_16ft      = data[next(itr)]
                    StatClass[stat_type].fg_a_8ft_to_16ft = float(fg_a_8ft_to_16ft)

                    fg_pct_8ft_to_16ft    = data[next(itr)]
                    StatClass[stat_type].fg_pct_8ft_to_16ft = float(fg_pct_8ft_to_16ft)

                    fg_m_16ft_to_24ft     = data[next(itr)]
                    StatClass[stat_type].fg_m_16ft_to_24ft = float(fg_m_16ft_to_24ft)

                    fg_a_16ft_to_24ft     = data[next(itr)]
                    StatClass[stat_type].fg_a_16ft_to_24ft = float(fg_a_16ft_to_24ft)

                    fg_pct_16ft_to_24ft   = data[next(itr)]
                    StatClass[stat_type].fg_pct_16ft_to_24ft = float(fg_pct_16ft_to_24ft)

                    fg_m_24ft_plus        = data[next(itr)]
                    StatClass[stat_type].fg_m_24ft_plus = float(fg_m_24ft_plus)

                    fg_a_24ft_plus        = data[next(itr)]
                    StatClass[stat_type].fg_a_24ft_plus = float(fg_a_24ft_plus)

                    fg_pct_24ft_plus      = data[next(itr)]
                    StatClass[stat_type].fg_pct_24ft_plus = float(fg_pct_24ft_plus)

                    fg_m_backcourt_shot   = data[next(itr)]
                    StatClass[stat_type].fg_m_backcourt_shot = float(fg_m_backcourt_shot)

                    fg_a_backcourt_shot   = data[next(itr)]
                    StatClass[stat_type].fg_a_backcourt_shot = float(fg_a_backcourt_shot)

                    fg_pct_backcourt_shot = data[next(itr)]
                    StatClass[stat_type].fg_pct_backcourt_shot = float(fg_pct_backcourt_shot)

                elif stat_type == 'By Zone':
                    fg_m_restricted_area   = data[next(itr)]
                    StatClass[stat_type].fg_m_restricted_area = float(fg_m_restricted_area)

                    fg_a_restricted_area   = data[next(itr)]
                    StatClass[stat_type].fg_a_restricted_area = float(fg_a_restricted_area)

                    fg_pct_restricted_area = data[next(itr)]
                    StatClass[stat_type].fg_pct_restricted_area = float(fg_pct_restricted_area)

                    fg_m_paint             = data[next(itr)]
                    StatClass[stat_type].fg_m_paint = float(fg_m_paint)

                    fg_a_paint             = data[next(itr)]
                    StatClass[stat_type].fg_a_paint = float(fg_a_paint)

                    fg_pct_paint           = data[next(itr)]
                    StatClass[stat_type].fg_pct_paint = float(fg_pct_paint)

                    fg_m_midrange          = data[next(itr)]
                    StatClass[stat_type].fg_m_midrange = float(fg_m_midrange)

                    fg_a_midrange          = data[next(itr)]
                    StatClass[stat_type].fg_a_midrange = float(fg_a_midrange)

                    fg_pct_midrange        = data[next(itr)]
                    StatClass[stat_type].fg_pct_midrange = float(fg_pct_midrange)

                    fg_m_left_corner_3     = data[next(itr)]
                    StatClass[stat_type].fg_m_left_corner_3 = float(fg_m_left_corner_3)

                    fg_a_left_corner_3     = data[next(itr)]
                    StatClass[stat_type].fg_a_left_corner_3 = float(fg_a_left_corner_3)

                    fg_pct_left_corner_3   = data[next(itr)]
                    StatClass[stat_type].fg_pct_left_corner_3 = float(fg_pct_left_corner_3)

                    fg_m_right_corner_3    = data[next(itr)]
                    StatClass[stat_type].fg_m_right_corner_3 = float(fg_m_right_corner_3)

                    fg_a_right_corner_3    = data[next(itr)]
                    StatClass[stat_type].fg_a_right_corner_3 = float(fg_a_right_corner_3)

                    fg_pct_right_corner_3  = data[next(itr)]
                    StatClass[stat_type].fg_pct_right_corner_3 = float(fg_pct_right_corner_3)

                    fg_m_corner_3    = data[next(itr)]
                    StatClass[stat_type].fg_m_corner_3 = float(fg_m_corner_3)

                    fg_a_corner_3    = data[next(itr)]
                    StatClass[stat_type].fg_a_corner_3 = float(fg_a_corner_3)

                    fg_pct_corner_3  = data[next(itr)]
                    StatClass[stat_type].fg_pct_corner_3 = float(fg_pct_corner_3)

                    fg_m_above_break_3     = data[next(itr)]
                    StatClass[stat_type].fg_m_above_break_3 = float(fg_m_above_break_3)

                    fg_a_above_break_3     = data[next(itr)]
                    StatClass[stat_type].fg_a_above_break_3 = float(fg_a_above_break_3)

                    fg_pct_above_break_3   = data[next(itr)]
                    StatClass[stat_type].fg_pct_above_break_3 = float(fg_pct_above_break_3)

                else:
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
