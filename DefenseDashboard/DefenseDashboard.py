'''
DEFENSE DASHBOARD
'''

import itertools
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from utils import browserutils
from utils.headers import getStatColumnType
from utils.Types import TableType
from .TableColumns import *


defense_dashboard_types = {
    'Overall':           'defense-dash-overall',
    '3 Pointer':         'defense-dash-3pt',
    '2 Pointer':         'defense-dash-2pt',
    'Less than 6ft':     'defense-dash-lt6',
    'Less than 10ft':    'defense-dash-lt10',
    'Greater than 15ft': 'defense-dash-gt15',
}


class DefensiveDashboard(dict):
    def __init__(self):
        initDefensiveDashboardStatTypes(self)

    def __getattr__(self, key):
        return self[key]


# Defensive Dashboard Stats
class DefensiveDashboardStats:
    def __init__(self):
        self.freq            = float() # Frequency
        self.defended_fg_m   = float() # Defended Field Goals Made
        self.defended_fg_a   = float() # Defended Field Goals Attempted
        self.defended_fg_pct = float() # Defended Field Goal Percentage
        self.fg_pct          = float() # Field Goal Percentage
        self.pct_pts_diff    = float() # Percentage Points Different


# Initialize Defense Dashboard Stat Types
def initDefensiveDashboardStatTypes(StatClass):
    for key in defense_dashboard_types:
        StatClass[key.title()] = DefensiveDashboardStats()


# Store Stats to Player
def scrape_player(player, season_year = '2020-21', season_type = 'Regular%20Season'):
    '''
    Produces each player's defense dashboard stats from:
        - https://wwww.nba.com/stats/players/defense-dash-overall/
    '''

    player.addTable('defense_dashboards', DefensiveDashboard())

    # URL Configurations
    name        = player.name.split(' ')[0] + '%20' + player.name.split(' ')[1]
    table_type  = 'players/'
    stat        = 'PLAYER_NAME'

    # Start browser
    browser = webdriver.Chrome(ChromeDriverManager().install())

    # Get Stats and Respective Ranking
    for stat_key, stat_url in defense_dashboard_types.items():

        # Browse to correct stat category
        url = 'https://nba.com/stats/' + table_type  + stat_url + '/?sort=' + stat + '&CF=PLAYER_NAME*E*' + name + '&Season=' + season_year + '&SeasonType=' + season_type
        browser.get(url)
        
        # Scrape stats if table exist
        table = browserutils.loadStatTable(browser)
        if table is not None:
            getDefensiveDashboardStats(table, stat_key.title(), player=player)

    # Close browser
    browser.quit()



# Store Stats to Teams
def scrape_teams(teams, season_year = '2020-21', season_type = 'Regular%20Season'):
    '''
    Produces each teams's defense dashboard stats from:
        - https://www.nba.com/stats/teams/defense-dash-overall/
    '''

    # Add stat class to teams
    for team in teams:
        teams[team].addTable('defense_dashboards', DefensiveDashboard())

    # URL Configurations
    table_type  = 'teams/'
    stat        = 'TEAM_NAME'

    # Start browser
    browser = webdriver.Chrome(ChromeDriverManager().install())

    # Get Stats and Respective Ranking
    for stat_key, stat_url in defense_dashboard_types.items():

        # Browse to correct stat category
        url = 'https://nba.com/stats/' + table_type + stat_url + '?sort=' + stat + '&dir=-1' + '&Season=' + season_year + '&SeasonType=' + season_type
        browser.get(url)

        # Scrape stats and get rank if table exist
        table = browserutils.loadStatTable(browser)
        if table is not None:
            getDefensiveDashboardStats(table, stat_key.title(), teams=teams)

    # Close browser
    browser.quit()


# Collect Defensive Dashboard Stats
def getDefensiveDashboardStats(table, stat_key, player=None, teams=None):

    table_type = TableType.PLAYER.name if player is not None else TableType.TEAM.name
    (table_header_row, table_column_offset) = getStatColumnType('Defensive Dashboard', table_type)

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

                # Parse and store stats
                data = info.split(' ')

                freq            = data[next(itr)]
                StatClass.defense_dashboards[stat_key].freq = float(freq.strip('%'))

                defended_fg_m   = data[next(itr)]
                StatClass.defense_dashboards[stat_key].defended_fg_m = float(defended_fg_m)

                defended_fg_a   = data[next(itr)]
                StatClass.defense_dashboards[stat_key].defended_fg_a = float(defended_fg_a)

                defended_fg_pct = data[next(itr)]
                StatClass.defense_dashboards[stat_key].defended_fg_pct = float(defended_fg_pct)

                fg_pct          = data[next(itr)]
                StatClass.defense_dashboards[stat_key].fg_pct = float(fg_pct)

                pct_pts_diff    = data[next(itr)]
                StatClass.defense_dashboards[stat_key].pct_pts_diff = float(pct_pts_diff)

            index += 1


def getDefensiveDashboardType(table_type, stat_key):
    return {
        'Overall':           None if table_type == TableType.PLAYER.name else dd_overall_team_stats,
        '3 Pointer':         None if table_type == TableType.PLAYER.name else dd_fg3pt_team_stats,
        '2 Pointer':         None if table_type == TableType.PLAYER.name else dd_fg2pt_team_stats,
        'Less than 6ft':     None if table_type == TableType.PLAYER.name else dd_lt_6ft_team_stats,
        'Less than 10ft':    None if table_type == TableType.PLAYER.name else dd_lt_10ft_team_stats,
        'Greater than 15ft': None if table_type == TableType.PLAYER.name else dd_gt_15ft_team_stats,
    }.get(stat_key)
