"""
SHOOTING
"""

import itertools

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from utils import browserutils
from utils.filters import distance_range
from utils.headers import getStatColumnType
from utils.Types import TableType

class Shooting(dict):
    def __init__(self):
        initShootingTypes(self)

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
        self.fg_m_paint             = float() # Field Goals Made In The Paint (Non Restricted Area)
        self.fg_a_paint             = float() # Field Goals Attempted In The Paint (Non Restricted Area)
        self.fg_pct_paint           = float() # Field Goal Percentage In The Paint (Non Restricted Area)
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


# Initialize Shot Dashboard Stats
def initShootingTypes(StatClass):
    for distance in distance_range.keys():

        if distance == '5ft Range':
            StatClass[distance] = Shooting5Ft()
        elif distance == '8ft Range':
            StatClass[distance] = Shooting8Ft()
        elif distance == 'By Zone':
            StatClass[distance] = ShootingZone()


# Store Stats to Player
def scrape_player(player, season_year = '2020-21', season_type = 'Regular%20Season'):
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
            getShootingStats(table, shooting_distance_range_key, player=player)

    # Close browser
    browser.quit()


# Store Stats to Teams
def scrape_teams(teams, season_year = '2020-21', season_type = 'Regular%20Season'):
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
            getShootingStats(table, shooting_distance_range_key, teams=teams)

    # Close browser
    browser.quit()


def getShootingStats(table, stat_type, player=None, teams=None):

    table_type = TableType.PLAYER.name if player is not None else TableType.TEAM.name
    (table_header_row, table_column_offset) = getStatColumnType('Shooting ' + stat_type, table_type)

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
                    StatClass = player

                elif teams is not None:
                    team = info.upper()
                    StatClass = teams[team]

            # Extract stats
            elif (index % 2) == 0:

                # Create iterator
                itr = itertools.count(table_column_offset)

                # Split info from table into a list
                data = info.split(' ')
                data = [stat.replace("-", "0") for stat in data]

                if stat_type == '5ft Range':
                    fg_m_lt_5ft         = data[next(itr)]
                    StatClass.shooting[stat_type].fg_m_lt_5ft = float(fg_m_lt_5ft)

                    fg_a_lt_5ft         = data[next(itr)]
                    StatClass.shooting[stat_type].fg_a_lt_5ft = float(fg_a_lt_5ft)

                    fg_pct_lt_5ft       = data[next(itr)]
                    StatClass.shooting[stat_type].fg_pct_lt_5ft = float(fg_pct_lt_5ft)

                    fg_m_5ft_to_9ft     = data[next(itr)]
                    StatClass.shooting[stat_type].fg_m_5ft_to_9ft = float(fg_m_5ft_to_9ft)

                    fg_a_5ft_to_9ft     = data[next(itr)]
                    StatClass.shooting[stat_type].fg_a_5ft_to_9ft = float(fg_a_5ft_to_9ft)

                    fg_pct_5ft_to_9ft   = data[next(itr)]
                    StatClass.shooting[stat_type].fg_pct_5ft_to_9ft = float(fg_pct_5ft_to_9ft)

                    fg_m_10ft_to_14ft   = data[next(itr)]
                    StatClass.shooting[stat_type].fg_m_10ft_to_14ft = float(fg_m_10ft_to_14ft)

                    fg_a_10ft_to_14ft   = data[next(itr)]
                    StatClass.shooting[stat_type].fg_a_10ft_to_14ft = float(fg_a_10ft_to_14ft)

                    fg_pct_10ft_to_14ft = data[next(itr)]
                    StatClass.shooting[stat_type].fg_pct_10ft_to_14ft = float(fg_pct_10ft_to_14ft)

                    fg_m_15ft_to_19ft   = data[next(itr)]
                    StatClass.shooting[stat_type].fg_m_15ft_to_19ft = float(fg_m_15ft_to_19ft)

                    fg_a_15ft_to_19ft   = data[next(itr)]
                    StatClass.shooting[stat_type].fg_a_15ft_to_19ft = float(fg_a_15ft_to_19ft)

                    fg_pct_15ft_to_19ft = data[next(itr)]
                    StatClass.shooting[stat_type].fg_pct_15ft_to_19ft = float(fg_pct_15ft_to_19ft)

                    fg_m_20ft_to_24ft   = data[next(itr)]
                    StatClass.shooting[stat_type].fg_m_20ft_to_24ft = float(fg_m_20ft_to_24ft)

                    fg_a_20ft_to_24ft   = data[next(itr)]
                    StatClass.shooting[stat_type].fg_a_20ft_to_24ft = float(fg_a_20ft_to_24ft)

                    fg_pct_20ft_to_24ft = data[next(itr)]
                    StatClass.shooting[stat_type].fg_pct_20ft_to_24ft = float(fg_pct_20ft_to_24ft)

                    fg_m_25ft_to_29ft   = data[next(itr)]
                    StatClass.shooting[stat_type].fg_m_25ft_to_29ft = float(fg_m_25ft_to_29ft)

                    fg_a_25ft_to_29ft   = data[next(itr)]
                    StatClass.shooting[stat_type].fg_a_25ft_to_29ft = float(fg_a_25ft_to_29ft)

                    fg_pct_25ft_to_29ft = data[next(itr)]
                    StatClass.shooting[stat_type].fg_pct_25ft_to_29ft = float(fg_pct_25ft_to_29ft)

                elif stat_type == '8ft Range':
                    fg_m_lt_8ft           = data[next(itr)]
                    StatClass.shooting[stat_type].fg_m_lt_8ft = float(fg_m_lt_8ft)

                    fg_a_lt_8ft           = data[next(itr)]
                    StatClass.shooting[stat_type].fg_a_lt_8ft = float(fg_a_lt_8ft)

                    fg_pct_lt_8ft         = data[next(itr)]
                    StatClass.shooting[stat_type].fg_pct_lt_8ft = float(fg_pct_lt_8ft)

                    fg_m_8ft_to_16ft      = data[next(itr)]
                    StatClass.shooting[stat_type].fg_m_8ft_to_16ft = float(fg_m_8ft_to_16ft)

                    fg_a_8ft_to_16ft      = data[next(itr)]
                    StatClass.shooting[stat_type].fg_a_8ft_to_16ft = float(fg_a_8ft_to_16ft)

                    fg_pct_8ft_to_16ft    = data[next(itr)]
                    StatClass.shooting[stat_type].fg_pct_8ft_to_16ft = float(fg_pct_8ft_to_16ft)

                    fg_m_16ft_to_24ft     = data[next(itr)]
                    StatClass.shooting[stat_type].fg_m_16ft_to_24ft = float(fg_m_16ft_to_24ft)

                    fg_a_16ft_to_24ft     = data[next(itr)]
                    StatClass.shooting[stat_type].fg_a_16ft_to_24ft = float(fg_a_16ft_to_24ft)

                    fg_pct_16ft_to_24ft   = data[next(itr)]
                    StatClass.shooting[stat_type].fg_pct_16ft_to_24ft = float(fg_pct_16ft_to_24ft)

                    fg_m_24ft_plus        = data[next(itr)]
                    StatClass.shooting[stat_type].fg_m_24ft_plus = float(fg_m_24ft_plus)

                    fg_a_24ft_plus        = data[next(itr)]
                    StatClass.shooting[stat_type].fg_a_24ft_plus = float(fg_a_24ft_plus)

                    fg_pct_24ft_plus      = data[next(itr)]
                    StatClass.shooting[stat_type].fg_pct_24ft_plus = float(fg_pct_24ft_plus)

                    fg_m_backcourt_shot   = data[next(itr)]
                    StatClass.shooting[stat_type].fg_m_backcourt_shot = float(fg_m_backcourt_shot)

                    fg_a_backcourt_shot   = data[next(itr)]
                    StatClass.shooting[stat_type].fg_a_backcourt_shot = float(fg_a_backcourt_shot)

                    fg_pct_backcourt_shot = data[next(itr)]
                    StatClass.shooting[stat_type].fg_pct_backcourt_shot = float(fg_pct_backcourt_shot)

                elif stat_type == 'By Zone':
                    fg_m_restricted_area   = data[next(itr)]
                    StatClass.shooting[stat_type].fg_m_restricted_area = float(fg_m_restricted_area)

                    fg_a_restricted_area   = data[next(itr)]
                    StatClass.shooting[stat_type].fg_a_restricted_area = float(fg_a_restricted_area)

                    fg_pct_restricted_area = data[next(itr)]
                    StatClass.shooting[stat_type].fg_pct_restricted_area = float(fg_pct_restricted_area)

                    fg_m_paint             = data[next(itr)]
                    StatClass.shooting[stat_type].fg_m_paint = float(fg_m_paint)

                    fg_a_paint             = data[next(itr)]
                    StatClass.shooting[stat_type].fg_a_paint = float(fg_a_paint)

                    fg_pct_paint           = data[next(itr)]
                    StatClass.shooting[stat_type].fg_pct_paint = float(fg_pct_paint)

                    fg_m_midrange          = data[next(itr)]
                    StatClass.shooting[stat_type].fg_m_midrange = float(fg_m_midrange)

                    fg_a_midrange          = data[next(itr)]
                    StatClass.shooting[stat_type].fg_a_midrange = float(fg_a_midrange)

                    fg_pct_midrange        = data[next(itr)]
                    StatClass.shooting[stat_type].fg_pct_midrange = float(fg_pct_midrange)

                    fg_m_left_corner_3     = data[next(itr)]
                    StatClass.shooting[stat_type].fg_m_left_corner_3 = float(fg_m_left_corner_3)

                    fg_a_left_corner_3     = data[next(itr)]
                    StatClass.shooting[stat_type].fg_a_left_corner_3 = float(fg_a_left_corner_3)

                    fg_pct_left_corner_3   = data[next(itr)]
                    StatClass.shooting[stat_type].fg_pct_left_corner_3 = float(fg_pct_left_corner_3)

                    fg_m_right_corner_3    = data[next(itr)]
                    StatClass.shooting[stat_type].fg_m_right_corner_3 = float(fg_m_right_corner_3)

                    fg_a_right_corner_3    = data[next(itr)]
                    StatClass.shooting[stat_type].fg_a_right_corner_3 = float(fg_a_right_corner_3)

                    fg_pct_right_corner_3  = data[next(itr)]
                    StatClass.shooting[stat_type].fg_pct_right_corner_3 = float(fg_pct_right_corner_3)

                    fg_m_corner_3    = data[next(itr)]
                    StatClass.shooting[stat_type].fg_m_corner_3 = float(fg_m_corner_3)

                    fg_a_corner_3    = data[next(itr)]
                    StatClass.shooting[stat_type].fg_a_corner_3 = float(fg_a_corner_3)

                    fg_pct_corner_3  = data[next(itr)]
                    StatClass.shooting[stat_type].fg_pct_corner_3 = float(fg_pct_corner_3)

                    fg_m_above_break_3     = data[next(itr)]
                    StatClass.shooting[stat_type].fg_m_above_break_3 = float(fg_m_above_break_3)

                    fg_a_above_break_3     = data[next(itr)]
                    StatClass.shooting[stat_type].fg_a_above_break_3 = float(fg_a_above_break_3)

                    fg_pct_above_break_3   = data[next(itr)]
                    StatClass.shooting[stat_type].fg_pct_above_break_3 = float(fg_pct_above_break_3)

            index += 1
