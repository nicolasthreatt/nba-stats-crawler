"""
CLUTCH
"""

import itertools
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from utils import browserutils
from utils.headers import getStatColumnType
from utils.Types import TableType
from .TableColumn import *


clutch_stats_tables = {
    'Traditional':  'clutch-traditional/',
    'Advanced':     'clutch-advanced/',
    'Misc':         'clutch-misc/',
    'Scoring':      'clutch-scoring/',
    'Usage':        'clutch-usage/',
    'Four Factors': 'clutch-four-factors',
    'Opponent':     'clutch-opponent/',
}


class Clutch(dict):
    def __init__(self, table_type):
        self.clutch_games          = int()   # Total Games Played
        self.clutch_wins           = int()   # Totals Wins
        self.clutch_losses         = int()   # Total Loses
        self.clutch_mins           = float() # Minutes
        self.statrank_dict         = dict()  # Dictionary to hold each team's stat rank

        if table_type == TableType.TEAM.name:
            self.clutch_win_pct    = float() # Win Percentage

        initClutchStatTypes(self, table_type)

    def __getattr__(self, key):
        return self[key]


# Tradional Stats
class ClutchTradional:
    def __init__(self, table_type=None):
        self.clutch_pts       = float() # Points
        self.clutch_fg_m      = float() # Field Goals Made
        self.clutch_fg_a      = float() # Field Goals Attempted
        self.clutch_fg_pct    = float() # Field Goals Percentage
        self.clutch_fg3_m     = float() # Three Points Made
        self.clutch_fg3_a     = float() # Three Points Attempted
        self.clutch_fg3_pct   = float() # Three Point Percentage
        self.clutch_ft_m      = float() # Free Throws Made
        self.clutch_ft_a      = float() # Free Throws Attempted
        self.clutch_ft_pct    = float() # Free Throw Percentage
        self.clutch_oreb      = float() # Offensive Rebounds
        self.clutch_dreb      = float() # Defensive Rebounds
        self.clutch_treb      = float() # Total Rebounds
        self.clutch_ast       = float() # Assist
        self.clutch_tov       = float() # Turnovers
        self.clutch_stl       = float() # Steals
        self.clutch_blk       = float() # Blocks
        self.clutch_fouls_c   = float() # Personal Fouls Commited
        self.clutch_plusminus = float() # Plus Minus
        self.statrank_dict    = dict()  # Dictionary to hold each team's stat rank

        if table_type == TableType.PLAYER.name:
            self.clutch_fp    = float() # Fantasy Points

        if table_type == TableType.TEAM.name:
            self.clutch_blk_a   = float() # Block Attempts
            self.clutch_fouls_d = float() # Personal Fouls Drawn


# Advanced Stats
class ClutchAdvanced:
    def __init__(self, table_type):
        self.clutch_orating       = float() # Offensive Rating
        self.clutch_drating       = float() # Defensive Rating
        self.clutch_netrating     = float() # Net Rating
        self.clutch_ast_pct       = float() # Assist Percentage
        self.clutch_ast_tov_ratio = float() # Assist Turover Ratio
        self.clutch_ast_ratio     = float() # Assist Ratio
        self.clutch_oreb_pct      = float() # Offensive Rebound Percentage
        self.clutch_dreb_pct      = float() # Defensive Rebound Percentage
        self.clutch_reb_pct       = float() # Total Rebound Percentage
        self.clutch_tov_ratio     = float() # Turnover Ratio
        self.clutch_efg_pct       = float() # Effective Field Goal Percentage
        self.clutch_ts_pct        = float() # True Shooting Percentage
        self.clutch_pace          = float() # Pace
        self.clutch_pie           = float() # Player Impact Estimate (PIE)
        self.statrank_dict        = dict()  # Dictionary to hold each team's stat rank

        if table_type == TableType.PLAYER.name:
            self.clutch_usage_pct = float() # Usage


class ClutchFourFactors:
    def __init__(self, table_type):
        if table_type == TableType.TEAM.name:
            self.clutch_efg_pct      = float() # Effective Field Goal Percentage
            self.clutch_fta_rate     = float() # Free Throw Attempt Rate
            self.clutch_tov_pct      = float() # Turnover Percentage
            self.clutch_oreb_pct     = float() # Offensive Rebound Percentage
            self.clutch_opp_efg_pct  = float() # Opponent's Effective Field Goal Percentage
            self.clutch_opp_fta_rate = float() # Opponent's Free Throw Attempted Rate
            self.clutch_opp_tov_pct  = float() # Opponent's Turnover Percentage
            self.clutch_opp_oreb_pct = float() # Opponent's Offensive Rebound Rate
            self.statrank_dict       = dict()  # Dictionary to hold each team's stat rank


# Misc Stats
class ClutchMisc:
    def __init__(self, table_type):
        self.clutch_pts_off_tov        = float() # Points Off Turnover
        self.clutch_pts_2nd_chance     = float() # 2nd Chance Points
        self.clutch_pts_fastbreak      = float() # Fastbreak Points
        self.clutch_pts_in_paint       = float() # Points in the Paint
        self.clutch_opp_pts_off_tov    = float() # Opponent Points Off Turnovers
        self.clutch_opp_2nd_chance_pts = float() # Opponent 2nd Chance Points
        self.clutch_opp_fastbreak_pts  = float() # Opponent Fastbreak Points
        self.clutch_opp_pts_in_paint   = float() # Opponent Points In the Paint

        if table_type == TableType.PLAYER.name:
            self.clutch_blk            = float() # Blocks
            self.clutch_blk_a          = float() # Blocks Attempted
            self.clutch_fouls_c        = float() # Personal Fouls Commited Per Game
            self.clutch_fouls_d        = float() # Personal Fouls Drawn Per Game

        self.statrank_dict             = dict()  # Dictionary to hold each team's stat rank


# Scoring Stats
class ClutchScoring:
    def __init__(self, table_type):
        self.clutch_pct_fga_2pt       = float() # Percent of Field Goals Attempted (2 Pointers)
        self.clutch_pct_fga_3pt       = float() # Percent of Field Goals Attempted (3 Pointers)
        self.clutch_pct_pts_2pt       = float() # Percent of Points (2 Pointers)
        self.clutch_pct_pts_mid       = float() # Percent of Points (Mid-Range)
        self.clutch_pct_pts_3pt       = float() # Percent of Points (3 Pointers)
        self.clutch_pct_pts_fb        = float() # Percent of Points (Fast Break Points)
        self.clutch_pct_pts_ft        = float() # Percent of Points (Free Throw Points)
        self.clutch_pct_pts_off_tov   = float() # Percent of Points (Off Turnovers)
        self.clutch_pct_pts_in_paint  = float() # Percent of Points (Points in Paint)
        self.clutch_pct_pts_2pts_ast  = float() # Percent of 2 Point Field Goals Made Assisted
        self.clutch_pct_pts_2pts_uast = float() # Percent of 2 Point Field Goals Made Unassisted
        self.clutch_pct_pts_3pts_ast  = float() # Percent of 3 Point Field Goals Made Assisted
        self.clutch_pct_pts_3pts_uast = float() # Percent of 3 Point Field Goals Made Unassisted
        self.clutch_pct_pts_fgm_ast   = float() # Percent of Total Field Goals Made Assisted
        self.clutch_pct_pts_fgm_uast  = float() # Percent of Total Field Goals Made Unassisted
        self.statrank_dict            = dict()  # Dictionary to hold each team's stat rank


# Usage Stats
class ClutchUsage:
    def __init__(self, table_type):
        self.clutch_pct_usage         = float() # Usage Percent
        self.clutch_pct_of_team_fg_m  = float() # Percent of Team's Field Goals Made
        self.clutch_pct_of_team_fg_a  = float() # Percent of Team's Field Goals Attempted
        self.clutch_pct_of_team_fg3_m = float() # Percent of Team's 3PT Field Goals Made
        self.clutch_pct_of_team_fg3_a = float() # Percent of Team's 3PT Field Goals Attempted
        self.clutch_pct_of_team_ft_m  = float() # Percent of Team's Free Throws Made
        self.clutch_pct_of_team_ft_a  = float() # Percent of Team's Free Throws Attempted
        self.clutch_pct_of_team_oreb  = float() # Percent of Team's Offensive Rebounds
        self.clutch_pct_of_team_dreb  = float() # Percent of Team's Defensive Rebounds
        self.clutch_pct_of_team_treb  = float() # Percent of Team's Total Rebounds
        self.clutch_pct_of_team_ast   = float() # Percent of Team's Assists
        self.clutch_pct_of_team_tov   = float() # Percent of Team's Turnovers
        self.clutch_pct_of_team_stl   = float() # Percent of Team's Steals
        self.clutch_pct_of_team_blk   = float() # Percent of Team's Blocks
        self.clutch_pct_of_team_blk_a = float() # Percent of Team's Blocked Field Goal Attempts
        self.clutch_pct_of_team_pf_c  = float() # Percent of Team's Personal Fouls Committed
        self.clutch_pct_of_team_pf_d  = float() # Percent of Team's Personal Fouls Drawn
        self.clutch_pct_of_team_pts   = float() # Percent of Team's Points
        self.statrank_dict            = dict()  # Dictionary to hold each team's stat rank


class ClutchOpponent:
    def __init__(self, table_type):
        self.clutch_opp_fg_m      = float() # Opponent's Field Goals Made
        self.clutch_opp_fg_a      = float() # Opponent's Field Goals Attempted
        self.clutch_opp_fg_pct    = float() # Opponent's Field Goals Percentage
        self.clutch_opp_fg3_m     = float() # Opponent's Three Points Made
        self.clutch_opp_fg3_a     = float() # Opponent's Three Points Attempted
        self.clutch_opp_fg3_pct   = float() # Opponent's Three Point Percentage
        self.clutch_opp_ft_m      = float() # Opponent's Free Throws Made
        self.clutch_opp_ft_a      = float() # Opponent's Free Throws Attempted
        self.clutch_opp_ft_pct    = float() # Opponent's Free Throw Percentage
        self.clutch_opp_oreb      = float() # Opponent's Offensive Rebounds
        self.clutch_opp_dreb      = float() # Opponent's Defensive Rebounds
        self.clutch_opp_treb      = float() # Opponent's Total Rebounds
        self.clutch_opp_ast       = float() # Opponent's Assists Per Game
        self.clutch_opp_tov       = float() # Opponent's Turnovers Per Game
        self.clutch_opp_stl       = float() # Opponent's Steals Per Game
        self.clutch_opp_blk       = float() # Opponent's Blocks Per Game
        self.clutch_opp_blk_a     = float() # Opponent's Blocked Field Goal Attempts
        self.clutch_opp_pf        = float() # Opponent's Personal Fouls
        self.clutch_opp_pf_d      = float() # Opponent's Personal Fouls Drawn
        self.clutch_opp_pts       = float() # Opponent's Points
        self.clutch_opp_plusminus = float() # Opponent's Plus Minus
        self.statrank_dict        = dict()  # Dictionary to hold each team's stat rank


# Initialize Clutch Stat Types
def initClutchStatTypes(StatClass, table_type):

    for clutch_stat_table in clutch_stats_tables:

        if clutch_stat_table == 'Traditional':
            StatClass[clutch_stat_table] = ClutchTradional(table_type)

        elif clutch_stat_table == 'Advanced':
            StatClass[clutch_stat_table] = ClutchAdvanced(table_type)

        elif clutch_stat_table == 'Misc':
            StatClass[clutch_stat_table] = ClutchMisc(table_type)

        elif clutch_stat_table == 'Scoring':
            StatClass[clutch_stat_table] = ClutchScoring(table_type)

        elif clutch_stat_table == 'Usage':
            if(table_type == TableType.PLAYER.name):
                StatClass[clutch_stat_table] = ClutchUsage(table_type)

        elif clutch_stat_table == 'Four Factors':
            if(table_type == TableType.TEAM.name):
                StatClass[clutch_stat_table] = ClutchFourFactors(table_type)

        elif clutch_stat_table == 'Opponent':
            if(table_type == TableType.TEAM.name):
                StatClass[clutch_stat_table] = ClutchOpponent(table_type)


def scrape_player(player, season_year = '2020-21', season_type = 'Regular%20Season'):
    '''
    Produces each player's clutch stats from:
        - https://www.nba.com/stats/players/clutch-traditional/
        - https://www.nba.com/stats/players/clutch-advanced/
        - https://www.nba.com/stats/players/clutch-misc/
        - https://www.nba.com/stats/players/clutch-scoring/
        - https://www.nba.com/stats/players/clutch-usage/
    '''

    # Add stat class to player
    player.addTable('clutch', Clutch(TableType.PLAYER.name))

    # URL Configurations
    name       = player.name.split(' ')[0] + '%20' + player.name.split(' ')[1]
    table_type = 'players/'
    per_mode   = 'Totals'
    stat       = 'PLAYER_NAME'

    # Start browser
    browser = webdriver.Chrome(ChromeDriverManager().install())

    # Get stats from correct url path
    for stat_key, stat_url in clutch_stats_tables.items():

        if not stat_key in ('Four Factors', 'Opponent'):

            # Browse to correct stat category
            url = 'https://nba.com/stats/' + table_type  + stat_url + '/?sort=' + stat + '&CF=PLAYER_NAME*E*' + name + '&Season=' + season_year + '&SeasonType=' + season_type + '&PerMode=' + per_mode
            browser.get(url)

            # Scrape stats if table exists
            table = browserutils.loadStatTable(browser)
            if table is not None:
                getClutchStats(table, stat_key, player=player)

    # Close browser
    browser.quit()


def collectTeamStats(teams, season_year = '2020-21', season_type = 'Regular%20Season'):
    '''
    Produces each team's clutch stats from:
        - https://www.nba.com/stats/teams/clutch-traditional/
        - https://www.nba.com/stats/teams/clutch-advanced/
        - https://www.nba.com/stats/teams/clutch-misc/
        - https://www.nba.com/stats/teams/clutch-scoring/
        - https://www.nba.com/stats/teams/clutch-four-factors/
        - https://www.nba.com/stats/teams/clutch-usage/
    '''

    # Add stat class to teams
    for team in teams:
        teams[team].addTable('clutch', Clutch(TableType.TEAM.name))

    # URL Configurations
    table_type = 'teams/'
    per_mode   = 'Totals'
    stat       = 'TEAM_NAME'

    # Start browser
    browser = webdriver.Chrome(ChromeDriverManager().install())

    # Get Stats and Respective Ranking
    for stat_key, stat_url in clutch_stats_tables.items():

        if stat_key != 'Usage':

            # Browse to correct stat category
            url = 'https://www.nba.com/stats/' + table_type  + stat_url + '?sort=' + stat + '&dir=-1' + '&Season=' + season_year + '&SeasonType=' + season_type + '&PerMode=' + per_mode
            browser.get(url)

            table = browserutils.loadStatTable(browser)
            if table is not None:
                getClutchStats(table, stat_key, teams=teams)

    # Close browser
    browser.quit()


# Collect Clutch Stats
def getClutchStats(table, stat_key, player=None, teams=None):

    table_type = TableType.PLAYER.name if player is not None else TableType.TEAM.name
    (table_header_row, table_column_offset) = getStatColumnType('Clutch ' + stat_key, table_type)

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
                    StatClass = player.clutch

                elif teams is not None:
                    team = info.upper()

                    StatClass = teams[team].clutch

            # Extract stats
            elif (index % 2) == 0:

                # Create iterator
                itr = itertools.count(table_column_offset)
                
                # Split info from table into a list
                data  = info.split(' ')

                if stat_key == 'Traditional':
                    clutch_games     = data[next(itr)]
                    StatClass.clutch_games = int(clutch_games)

                    clutch_wins      = data[next(itr)]
                    StatClass.clutch_wins = int(clutch_wins)

                    clutch_losses    = data[next(itr)]
                    StatClass.clutch_losses = int(clutch_losses)

                    if teams is not None:
                        clutch_win_pct    = data[next(itr)]
                        StatClass.clutch_win_pct = float(clutch_win_pct)

                    clutch_mins      = data[next(itr)]
                    StatClass.clutch_mins = float(clutch_mins)

                    clutch_pts       = data[next(itr)]
                    StatClass[stat_key].clutch_pts = float(clutch_pts)

                    clutch_fg_m      = data[next(itr)]
                    StatClass[stat_key].clutch_fg_m = float(clutch_fg_m)

                    clutch_fg_a      = data[next(itr)]
                    StatClass[stat_key].clutch_fg_a = float(clutch_fg_a)

                    clutch_fg_pct    = data[next(itr)]
                    StatClass[stat_key].clutch_fg_pct = float(clutch_fg_pct)

                    clutch_fg3_m     = data[next(itr)]
                    StatClass[stat_key].clutch_fg3_m = float(clutch_fg3_m)

                    clutch_fg3_a     = data[next(itr)]
                    StatClass[stat_key].clutch_fg3_a = float(clutch_fg3_a)

                    clutch_fg3_pct   = data[next(itr)]
                    StatClass[stat_key].clutch_fg3_pct = float(clutch_fg3_pct)

                    clutch_ft_m      = data[next(itr)]
                    StatClass[stat_key].clutch_ft_m = float(clutch_ft_m)

                    clutch_ft_a      = data[next(itr)]
                    StatClass[stat_key].clutch_ft_a = float(clutch_ft_a)

                    clutch_ft_pct    = data[next(itr)]
                    StatClass[stat_key].clutch_ft_pct = float(clutch_ft_pct)

                    clutch_oreb      = data[next(itr)]
                    StatClass[stat_key].clutch_oreb = float(clutch_oreb)

                    clutch_dreb      = data[next(itr)]
                    StatClass[stat_key].clutch_dreb = float(clutch_dreb)

                    clutch_treb      = data[next(itr)]
                    StatClass[stat_key].clutch_treb = float(clutch_treb)

                    clutch_ast       = data[next(itr)]
                    StatClass[stat_key].clutch_ast = float(clutch_ast)

                    clutch_tov       = data[next(itr)]
                    StatClass[stat_key].clutch_tov = float(clutch_tov)

                    clutch_stl       = data[next(itr)]
                    StatClass[stat_key].clutch_stl = float(clutch_stl)

                    clutch_blk       = data[next(itr)]
                    StatClass[stat_key].clutch_blk = float(clutch_blk)

                    if teams is not None:
                        clutch_blk_a = data[next(itr)]
                        StatClass[stat_key].clutch_blk = float(clutch_blk_a)

                    clutch_fouls_c   = data[next(itr)]
                    StatClass[stat_key].clutch_fouls_c = float(clutch_fouls_c)

                    if player is not None:
                        clutch_fp    = data[next(itr)]
                        StatClass[stat_key].clutch_fp = float(clutch_fp)
                    elif teams is not None:
                        clutch_fouls_d = data[next(itr)]
                        StatClass[stat_key].clutch_fouls_d = float(clutch_fouls_d)

                    if player is not None:
                        clutch_plusminus = data[next(itr) + 2]  # Skip DD and TD Columns for Player
                    elif teams is not None:
                        clutch_plusminus = data[next(itr)]

                    StatClass[stat_key].clutch_plusminus = float(clutch_plusminus)

                elif stat_key == 'Advanced':

                    clutch_orating       = data[next(itr)]
                    StatClass[stat_key].clutch_orating = float(clutch_orating)

                    clutch_drating       = data[next(itr)]
                    StatClass[stat_key].clutch_drating = float(clutch_drating)

                    clutch_netrating     = data[next(itr)]
                    StatClass[stat_key].clutch_netrating = float(clutch_netrating)

                    clutch_ast_pct       = data[next(itr)]
                    StatClass[stat_key].clutch_ast_pct = float(clutch_ast_pct)

                    clutch_ast_tov_ratio = data[next(itr)]
                    StatClass[stat_key].clutch_ast_tov_ratio = float(clutch_ast_tov_ratio)

                    clutch_ast_ratio     = data[next(itr)]
                    StatClass[stat_key].clutch_ast_ratio = float(clutch_ast_ratio)

                    clutch_oreb_pct      = data[next(itr)]
                    StatClass[stat_key].clutch_oreb_pct = float(clutch_oreb_pct)

                    clutch_dreb_pct      = data[next(itr)]
                    StatClass[stat_key].clutch_dreb_pct = float(clutch_dreb_pct)

                    clutch_reb_pct       = data[next(itr)]
                    StatClass[stat_key].clutch_reb_pct = float(clutch_reb_pct)

                    clutch_tov_ratio     = data[next(itr)]
                    StatClass[stat_key].clutch_tov_ratio = float(clutch_tov_ratio)

                    clutch_efg_pct       = data[next(itr)]
                    StatClass[stat_key].clutch_efg_pct = float(clutch_efg_pct)

                    clutch_ts_pct        = data[next(itr)]
                    StatClass[stat_key].clutch_ts_pct = float(clutch_ts_pct)

                    if player is not None:
                        clutch_usage     = data[next(itr)]
                        StatClass[stat_key].clutch_usage = float(clutch_usage)

                    clutch_pace          = data[next(itr)]
                    StatClass[stat_key].clutch_pace = float(clutch_pace)

                    clutch_pie           = data[next(itr)]
                    StatClass[stat_key].clutch_pie = float(clutch_pie)

                elif stat_key == 'Misc':

                    clutch_pts_off_tov        = data[next(itr)]
                    StatClass[stat_key].clutch_pts_off_tov = float(clutch_pts_off_tov)

                    clutch_pts_2nd_chance     = data[next(itr)]
                    StatClass[stat_key].clutch_pts_2nd_chance = float(clutch_pts_2nd_chance)

                    clutch_pts_fastbreak      = data[next(itr)]
                    StatClass[stat_key].clutch_pts_fastbreak = float(clutch_pts_fastbreak)

                    clutch_pts_in_paint       = data[next(itr)]
                    StatClass[stat_key].clutch_pts_in_paint = float(clutch_pts_in_paint)

                    clutch_opp_pts_off_tov    = data[next(itr)]
                    StatClass[stat_key].clutch_opp_pts_off_tov = float(clutch_opp_pts_off_tov)

                    clutch_opp_2nd_chance_pts = data[next(itr)]
                    StatClass[stat_key].clutch_opp_2nd_chance_pts = float(clutch_opp_2nd_chance_pts)

                    clutch_opp_fastbreak_pts  = data[next(itr)]
                    StatClass[stat_key].clutch_opp_fastbreak_pts = float(clutch_opp_fastbreak_pts)

                    clutch_opp_pts_in_paint   = data[next(itr)]
                    StatClass[stat_key].clutch_opp_pts_in_paint = float(clutch_opp_pts_in_paint)

                    if player is not None:
                        clutch_blk                = data[next(itr)]
                        StatClass[stat_key].clutch_blk = float(clutch_blk)

                        clutch_blk_a              = data[next(itr)]
                        StatClass[stat_key].clutch_blk_a = float(clutch_blk_a)

                        clutch_fouls_c            = data[next(itr)]
                        StatClass[stat_key].clutch_fouls_c = float(clutch_fouls_c)

                        clutch_fouls_d            = data[next(itr)]
                        StatClass[stat_key].clutch_fouls_d = float(clutch_fouls_d)

                elif stat_key == 'Scoring':

                    clutch_pct_fga_2pt       = data[next(itr)]
                    StatClass[stat_key].clutch_pct_fga_2pt = float(clutch_pct_fga_2pt)

                    clutch_pct_fga_3pt       = data[next(itr)]
                    StatClass[stat_key].clutch_pct_fga_3pt = float(clutch_pct_fga_3pt)

                    clutch_pct_pts_2pt       = data[next(itr)]
                    StatClass[stat_key].clutch_pct_pts_2pt = float(clutch_pct_pts_2pt)

                    clutch_pct_pts_mid       = data[next(itr)]
                    StatClass[stat_key].clutch_pct_pts_mid = float(clutch_pct_pts_mid)

                    clutch_pct_pts_3pt       = data[next(itr)]
                    StatClass[stat_key].clutch_pct_pts_3pt = float(clutch_pct_pts_3pt)

                    clutch_pct_pts_fb        = data[next(itr)]
                    StatClass[stat_key].clutch_pct_pts_fb = float(clutch_pct_pts_fb)

                    clutch_pct_pts_ft        = data[next(itr)]
                    StatClass[stat_key].clutch_pct_pts_ft = float(clutch_pct_pts_ft)

                    clutch_pct_pts_off_tov   = data[next(itr)]
                    StatClass[stat_key].clutch_pct_pts_off_tov = float(clutch_pct_pts_off_tov)

                    clutch_pct_pts_in_paint  = data[next(itr)]
                    StatClass[stat_key].clutch_pct_pts_in_paint = float(clutch_pct_pts_in_paint)

                    clutch_pct_pts_2pts_ast  = data[next(itr)]
                    StatClass[stat_key].clutch_pct_pts_2pts_ast = float(clutch_pct_pts_2pts_ast)

                    clutch_pct_pts_2pts_uast = data[next(itr)]
                    StatClass[stat_key].clutch_pct_pts_2pts_uast = float(clutch_pct_pts_2pts_uast)

                    clutch_pct_pts_3pts_ast  = data[next(itr)]
                    StatClass[stat_key].clutch_pct_pts_3pts_ast = float(clutch_pct_pts_3pts_ast)

                    clutch_pct_pts_3pts_uast = data[next(itr)]
                    StatClass[stat_key].clutch_pct_pts_3pts_uast = float(clutch_pct_pts_3pts_uast)

                    clutch_pct_pts_fgm_ast   = data[next(itr)]
                    StatClass[stat_key].clutch_pct_pts_fgm_ast = float(clutch_pct_pts_fgm_ast)

                    clutch_pct_pts_fgm_uast  = data[next(itr)]
                    StatClass[stat_key].clutch_pct_pts_fgm_uast = float(clutch_pct_pts_fgm_uast)

                elif stat_key == 'Usage':

                    clutch_pct_usage         = data[next(itr)]
                    StatClass[stat_key].clutch_pct_usage = float(clutch_pct_usage)

                    clutch_pct_of_team_fg_m  = data[next(itr)]
                    StatClass[stat_key].clutch_pct_of_team_fg_m = float(clutch_pct_of_team_fg_m)

                    clutch_pct_of_team_fg_a  = data[next(itr)]
                    StatClass[stat_key].clutch_pct_of_team_fg_a = float(clutch_pct_of_team_fg_a)

                    clutch_pct_of_team_fg3_m = data[next(itr)]
                    StatClass[stat_key].clutch_pct_of_team_fg3_m = float(clutch_pct_of_team_fg3_m)

                    clutch_pct_of_team_fg3_a = data[next(itr)]
                    StatClass[stat_key].clutch_pct_of_team_fg3_a = float(clutch_pct_of_team_fg3_a)

                    clutch_pct_of_team_ft_m  = data[next(itr)]
                    StatClass[stat_key].clutch_pct_of_team_ft_m = float(clutch_pct_of_team_ft_m)

                    clutch_pct_of_team_ft_a  = data[next(itr)]
                    StatClass[stat_key].clutch_pct_of_team_ft_a = float(clutch_pct_of_team_ft_a)

                    clutch_pct_of_team_oreb  = data[next(itr)]
                    StatClass[stat_key].clutch_pct_of_team_oreb = float(clutch_pct_of_team_oreb)

                    clutch_pct_of_team_dreb  = data[next(itr)]
                    StatClass[stat_key].clutch_pct_of_team_dreb = float(clutch_pct_of_team_dreb)

                    clutch_pct_of_team_treb  = data[next(itr)]
                    StatClass[stat_key].clutch_pct_of_team_treb = float(clutch_pct_of_team_treb)

                    clutch_pct_of_team_ast   = data[next(itr)]
                    StatClass[stat_key].clutch_pct_of_team_ast = float(clutch_pct_of_team_ast)

                    clutch_pct_of_team_tov   = data[next(itr)]
                    StatClass[stat_key].clutch_pct_of_team_tov = float(clutch_pct_of_team_tov)

                    clutch_pct_of_team_stl   = data[next(itr)]
                    StatClass[stat_key].clutch_pct_of_team_stl = float(clutch_pct_of_team_stl)

                    clutch_pct_of_team_blk   = data[next(itr)]
                    StatClass[stat_key].clutch_pct_of_team_blk = float(clutch_pct_of_team_blk)

                    clutch_pct_of_team_blk_a = data[next(itr)]
                    StatClass[stat_key].clutch_pct_of_team_blk_a = float(clutch_pct_of_team_blk_a)

                    clutch_pct_of_team_pf_c  = data[next(itr)]
                    StatClass[stat_key].clutch_pct_of_team_pf_c = float(clutch_pct_of_team_pf_c)

                    clutch_pct_of_team_pf_d  = data[next(itr)]
                    StatClass[stat_key].clutch_pct_of_team_pf_d = float(clutch_pct_of_team_pf_d)

                    clutch_pct_of_team_pts   = data[next(itr)]
                    StatClass[stat_key].clutch_pct_of_team_pts = float(clutch_pct_of_team_pts)

                elif stat_key == 'Four Factors':

                    clutch_efg_pct      = data[next(itr)]
                    StatClass[stat_key].clutch_efg_pct = float(clutch_efg_pct)

                    clutch_fta_rate     = data[next(itr)]
                    StatClass[stat_key].clutch_fta_rate = float(clutch_fta_rate)

                    clutch_tov_pct      = data[next(itr)]
                    StatClass[stat_key].clutch_tov_pct = float(clutch_tov_pct)

                    clutch_oreb_pct     = data[next(itr)]
                    StatClass[stat_key].clutch_oreb_pct = float(clutch_oreb_pct)

                    clutch_opp_efg_pct  = data[next(itr)]
                    StatClass[stat_key].clutch_opp_efg_pct = float(clutch_opp_efg_pct)

                    clutch_opp_fta_rate = data[next(itr)]
                    StatClass[stat_key].clutch_opp_fta_rate = float(clutch_opp_fta_rate)

                    clutch_opp_tov_pct  = data[next(itr)]
                    StatClass[stat_key].clutch_opp_tov_pct = float(clutch_opp_tov_pct)

                    clutch_opp_oreb_pct = data[next(itr)]
                    StatClass[stat_key].clutch_opp_oreb_pct = float(clutch_opp_oreb_pct)

                elif stat_key == 'Opponent':

                    clutch_opp_fg_m      = data[next(itr)]
                    StatClass[stat_key].clutch_opp_fg_m = float(clutch_opp_fg_m)

                    clutch_opp_fg_a      = data[next(itr)]
                    StatClass[stat_key].clutch_opp_fg_a = float(clutch_opp_fg_a)

                    clutch_opp_fg_pct    = data[next(itr)]
                    StatClass[stat_key].clutch_opp_fg_pct = float(clutch_opp_fg_pct)

                    clutch_opp_fg3_a     = data[next(itr)]
                    StatClass[stat_key].clutch_opp_fg3_a = float(clutch_opp_fg3_a)

                    clutch_opp_fg3_pct   = data[next(itr)]
                    StatClass[stat_key].clutch_opp_fg3_pct = float(clutch_opp_fg3_pct)

                    clutch_opp_ft_m      = data[next(itr)]
                    StatClass[stat_key].clutch_opp_ft_m = float(clutch_opp_ft_m)

                    clutch_opp_ft_a      = data[next(itr)]
                    StatClass[stat_key].clutch_opp_ft_a = float(clutch_opp_ft_a)

                    clutch_opp_ft_pct    = data[next(itr)]
                    StatClass[stat_key].clutch_opp_ft_pct = float(clutch_opp_ft_pct)

                    clutch_opp_oreb      = data[next(itr)]
                    StatClass[stat_key].clutch_opp_oreb = float(clutch_opp_oreb)

                    clutch_opp_dreb      = data[next(itr)]
                    StatClass[stat_key].clutch_opp_dreb = float(clutch_opp_dreb)

                    clutch_opp_treb      = data[next(itr)]
                    StatClass[stat_key].clutch_opp_treb = float(clutch_opp_treb)

                    clutch_opp_ast       = data[next(itr)]
                    StatClass[stat_key].clutch_opp_ast = float(clutch_opp_ast)

                    clutch_opp_tov       = data[next(itr)]
                    StatClass[stat_key].clutch_opp_tov = float(clutch_opp_tov)

                    clutch_opp_stl       = data[next(itr)]
                    StatClass[stat_key].clutch_opp_stl = float(clutch_opp_stl)

                    clutch_opp_blk       = data[next(itr)]
                    StatClass[stat_key].clutch_opp_blk = float(clutch_opp_blk)

                    clutch_opp_blk_a     = data[next(itr)]
                    StatClass[stat_key].clutch_opp_blk_a = float(clutch_opp_blk_a)

                    clutch_opp_pf        = data[next(itr)]
                    StatClass[stat_key].clutch_opp_pf = float(clutch_opp_pf)

                    clutch_opp_pf_d      = data[next(itr)]
                    StatClass[stat_key].clutch_opp_pf_d = float(clutch_opp_pf_d)

                    clutch_opp_pts       = data[next(itr)]
                    StatClass[stat_key].clutch_opp_pts = float(clutch_opp_pts)

                    clutch_opp_plusminus = data[next(itr)]
                    StatClass[stat_key].clutch_opp_plusminus = float(clutch_opp_plusminus)

            index += 1


def getClutchType(table_type, stat_key):
    return {
        'Traditional':  clutch_traditional_player if table_type == TableType.PLAYER.name else clutch_traditional_team,
        'Advanced':     clutch_advanced_player    if table_type == TableType.PLAYER.name else clutch_advanced_team,
        'Misc':         clutch_misc_player        if table_type == TableType.PLAYER.name else clutch_misc_team,
        'Scoring':      clutch_scoring_player     if table_type == TableType.PLAYER.name else clutch_scoring_team,
        'Usage':        clutch_usage_player       if table_type == TableType.PLAYER.name else None,
        'Opponent':     None                      if table_type == TableType.PLAYER.name else clutch_opponent_team,
        'Four Factors': None                      if table_type == TableType.PLAYER.name else clutch_four_factors_team,
    }.get(stat_key)
