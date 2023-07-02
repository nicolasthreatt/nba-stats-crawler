'''
GENERAL
'''

import itertools
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from utils import browserutils
from utils.headers import getStatColumnType
from utils.Types import TableType
from .TableColumns import *

from pprint import pprint


general_tables = {
    'Traditional':  'traditional',
    'Advanced':     'advanced',
    'Misc':         'misc',
    'Scoring':      'scoring',
    'Usage':        'usage',
    'Opponent':     'opponent',
    'Defense':      'defense',
    'Four Factors': 'four-factors',
}


class General(dict):
    def __init__(self, table_type):
        self.games      = int()   # Total Games Played
        self.wins       = int()   # Totals Wins
        self.losses     = int()   # Total Losses
        self.mins       = float() # Minutes

        if table_type == TableType.TEAM.name:
            self.win_p  = float() # Wining Percentage

        initGeneralStatTypes(self, table_type)

    def __getattr__(self, key):
        return self[key]


class GeneralTraditional:
    def __init__(self, table_type):
        self.pts        = float() # Points
        self.fg_m       = float() # Fields Goals Made
        self.fg_a       = float() # Field Goals Attempted
        self.fg_pct     = float() # Field Goal Percentage
        self.fg3_m      = float() # Three Points Made
        self.fg3_a      = float() # Three Points Attempted
        self.fg3_pct    = float() # Three Point Percentage
        self.ft_m       = float() # Free Throws Made
        self.ft_a       = float() # Free Throws Attempted
        self.ft_pct     = float() # Free Throw Percentage
        self.oreb       = float() # Offensive Rebounds
        self.dreb       = float() # Defensive Rebounds
        self.treb       = float() # Total Rebounds
        self.ast        = float() # Assists
        self.tov        = float() # Turnovers
        self.stl        = float() # Steals
        self.blk        = float() # Blocks
        self.pf_c       = float() # Personal Fouls Commited
        self.plusminus  = float() # Plus Minus
        self.rank_dict  = dict()  # Dictionary to hold each stat rank

        if table_type == TableType.TEAM.name:
            self.blk_a  = float() # Block Attempt
            self.pf_d   = float() # Personal Fouls Drawn
        elif table_type == TableType.PLAYER.name:
            self.fp     = float() # Fantasy Points
            self.dd2    = int()   # Double-Double
            self.td3    = int()   # Triple-Double

        initGeneralStatRanks(self.rank_dict, getGeneralType(table_type, 'Traditional'))


class GeneralAdvanced:
    def __init__(self, table_type):
        self.orating    = float() # Offensive Rating
        self.drating    = float() # Defensive Rating
        self.netrating  = float() # Net Rating
        self.ast_pct    = float() # Assist Percentage
        self.ast_tov    = float() # Assist Turover Ratio
        self.ast_ratio  = float() # Assist Ratio
        self.oreb_pct   = float() # Offensive Rebound Percentage
        self.dreb_pct   = float() # Defensive Rebound Percentage
        self.reb_pct    = float() # Total Rebound Percentage
        self.tov_pct    = float() # Turnover Ratio/Percentage
        self.efg_pct    = float() # Effective Field Goal Percentage
        self.ts_pct     = float() # True Shooting Percentage
        self.pace       = float() # Pace
        self.pie        = float() # Player Impact Estimate (PIE)
        self.rank_dict  = dict()

        if table_type == TableType.PLAYER.name:
            self.usage  = float() # Usage

        initGeneralStatRanks(self.rank_dict, getGeneralType(table_type, 'Advanced'))


class GeneralMisc:
    def __init__(self, table_type):
        self.pts_off_tov        = float() # Points Off Turnover
        self.pts_2nd_chance     = float() # 2nd Chance Points
        self.pts_fastbreak      = float() # Fastbreak Points
        self.pts_in_paint       = float() # Points in the Paint
        self.opp_pts_off_tov    = float() # Opponent Points Off Turnovers
        self.opp_2nd_chance_pts = float() # Opponent 2nd Chance Points
        self.opp_fastbreak_pts  = float() # Opponent Fastbreak Points
        self.opp_pts_in_paint   = float() # Opponent Points In the Paint
        self.rank_dict  = dict()

        if table_type == TableType.PLAYER.name:
            self.blk            = float() # Blocks Per Game
            self.blk_a          = float() # Blocks Attempted Per Game
            self.fouls_c        = float() # Personal Fouls Commited Per Game
            self.fouls_d        = float() # Personal Fouls Drawn Per Game

        initGeneralStatRanks(self.rank_dict, getGeneralType(table_type, 'Misc'))


class GeneralScoring:
    def __init__(self, table_type):
        self.pct_fga_2pt       = float() # Percent of Field Goals Attempted (2 Pointers)
        self.pct_fga_3pt       = float() # Percent of Field Goals Attempted (3 Pointers)
        self.pct_pts_2pt       = float() # Percent of Points (2 Pointers)
        self.pct_pts_mid       = float() # Percent of Points (Mid-Range)
        self.pct_pts_3pt       = float() # Percent of Points (3 Pointers)
        self.pct_pts_fb        = float() # Percent of Points (Fast Break Points)
        self.pct_pts_ft        = float() # Percent of Points (Free Throw Points)
        self.pct_pts_off_tov   = float() # Percent of Points (Off Turnovers)
        self.pct_pts_in_paint  = float() # Percent of Points (Points in Paint)
        self.pct_pts_2pts_ast  = float() # Percent of 2 Point Field Goals Made Assisted
        self.pct_pts_2pts_uast = float() # Percent of 2 Point Field Goals Made Unassisted
        self.pct_pts_3pts_ast  = float() # Percent of 3 Point Field Goals Made Assisted
        self.pct_pts_3pts_uast = float() # Percent of 3 Point Field Goals Made Unassisted
        self.pct_pts_fgm_ast   = float() # Percent of Total Field Goals Made Assisted
        self.pct_pts_fgm_uast  = float() # Percent of Total Field Goals Made Unassisted
        self.rank_dict         = dict()  # Dictionary to hold each stat rank

        initGeneralStatRanks(self.rank_dict, getGeneralType(table_type, 'Scoring'))


class GeneralUsage:
    def __init__(self, table_type):
        if table_type == TableType.PLAYER.name:
            self.pct_usage         = float() # Usage Percent
            self.pct_of_team_fg_m  = float() # Percent of Team's Field Goals Made
            self.pct_of_team_fg_a  = float() # Percent of Team's Field Goals Attempted
            self.pct_of_team_fg3_m = float() # Percent of Team's 3PT Field Goals Made
            self.pct_of_team_fg3_a = float() # Percent of Team's 3PT Field Goals Attempted
            self.pct_of_team_ft_m  = float() # Percent of Team's Free Throws Made
            self.pct_of_team_ft_a  = float() # Percent of Team's Free Throws Attempted
            self.pct_of_team_oreb  = float() # Percent of Team's Offensive Rebounds
            self.pct_of_team_dreb  = float() # Percent of Team's Defensive Rebounds
            self.pct_of_team_treb  = float() # Percent of Team's Total Rebounds
            self.pct_of_team_ast   = float() # Percent of Team's Assists
            self.pct_of_team_tov   = float() # Percent of Team's Turnovers
            self.pct_of_team_stl   = float() # Percent of Team's Steals
            self.pct_of_team_blk   = float() # Percent of Team's Blocks
            self.pct_of_team_blk_a = float() # Percent of Team's Blocked Field Goal Attempts
            self.pct_of_team_pf_c  = float() # Percent of Team's Personal Fouls Committed
            self.pct_of_team_pf_d  = float() # Percent of Team's Personal Fouls Drawn
            self.pct_of_team_pts   = float() # Percent of Team's Points
            self.rank_dict         = dict()  # Dictionary to hold each stat rank

            initGeneralStatRanks(self.rank_dict, getGeneralType(table_type, 'Usage')) 


class GeneralOpponent:
    def __init__(self, table_type):
        self.opp_fg_m       = float() # Opponent's Field Goals Made
        self.opp_fg_a       = float() # Opponent's Field Goals Attempted
        self.opp_fg_pct     = float() # Opponent's Field Goals Percentage
        self.opp_fg3_m      = float() # Opponent's Three Points Made
        self.opp_fg3_a      = float() # Opponent's Three Points Attempted
        self.opp_fg3_pct    = float() # Opponent's Three Point Percentage
        self.opp_ft_m       = float() # Opponent's Free Throws Made
        self.opp_ft_a       = float() # Opponent's Free Throws Attempted
        self.opp_ft_pct     = float() # Opponent's Free Throw Percentage
        self.opp_oreb       = float() # Opponent's Offensive Rebounds
        self.opp_dreb       = float() # Opponent's Defensive Rebounds
        self.opp_treb       = float() # Opponent's Total Rebounds
        self.opp_ast        = float() # Opponent's Assists
        self.opp_tov        = float() # Opponent's Turnovers
        self.opp_stl        = float() # Opponent's Steals
        self.opp_blk        = float() # Opponent's Blocks
        self.opp_blk_a      = float() # Opponent's Blocked Field Goal Attempts
        self.opp_pf         = float() # Opponent's Personal Fouls
        self.opp_pf_d       = float() # Opponent's Personal Fouls Drawn
        self.opp_pts        = float() # Opponent's Points
        self.opp_plusminus  = float() # Opponent's Plus Minus
        self.rank_dict      = dict()  # Dictionary to hold each stat rank

        initGeneralStatRanks(self.rank_dict, getGeneralType(table_type, 'Opponent')) 


class GeneralDefense:
    def __init__(self, table_type):
        self.drating            = float() # Defensive Rating
        self.dreb               = float() # Defensive Rebounds
        self.dreb_pct           = float() # Defensive Rebound Percentage
        self.stl                = float() # Steals
        self.blk                = float() # Blocks
        self.opp_pts_off_tov    = float() # Opponent Points Off Turnovers
        self.opp_2nd_chance_pts = float() # Opponent 2nd Chance Points
        self.opp_fb_pts         = float() # Opponent Fast Break Points
        self.opp_pts_in_paint   = float() # Opponent Points in the Paint
        self.rank_dict          = dict()  # Dictionary to hold each stat rank

        if table_type == TableType.PLAYER.name:
            self.pct_dreb       = float() # Percent of Team's Defensive Rebounds
            self.pct_stl        = float() # Percent of Team's Steal's
            self.pct_blk        = float() # Percent of Team's Blocks
            self.def_ws         = float() # Defensive Win Shares

        initGeneralStatRanks(self.rank_dict, getGeneralType(table_type, 'Defense'))


class GeneralFourFactors:
    def __init__(self, table_type):
        if table_type == TableType.TEAM.name:
            self.efg_pct        = float() # Effective Field Goal Percentage
            self.fta_rate       = float() # Free Throw Attempt Rate
            self.tov_pct        = float() # Turnover Percentage
            self.oreb_pct       = float() # Offensive Rebound Percentage
            self.opp_efg_pct    = float() # Opponent's Effective Field Goal Percentage
            self.opp_fta_rate   = float() # Opponent's Free Throw Attempted Rate
            self.opp_tov_pct    = float() # Opponent's Turnover Percentage
            self.opp_oreb_pct   = float() # Opponent's Offensive Rebound Rate
            self.rank_dict      = dict()  # Dictionary to hold each stat rank

            initGeneralStatRanks(self.rank_dict, getGeneralType(table_type, 'Four Factors')) 


# Initialize General Stat Types
def initGeneralStatTypes(StatClass, table_type):

    for key in general_tables:

        if key.title() == 'Traditional':
            StatClass[key.title()] = GeneralTraditional(table_type)

        elif key.title() == 'Advanced':
            StatClass[key.title()] = GeneralAdvanced(table_type)

        elif key.title() == 'Misc':
            StatClass[key.title()] = GeneralMisc(table_type)

        elif key.title() == 'Scoring':
            StatClass[key.title()] = GeneralScoring(table_type)

        elif key.title() == 'Usage':
            if table_type == TableType.PLAYER.name:
                StatClass[key.title()] = GeneralUsage(table_type)

        elif key.title() == 'Opponent':
            StatClass[key.title()] = GeneralOpponent(table_type)

        elif key.title() == 'Defense':
            StatClass[key.title()] = GeneralDefense(table_type)

        elif key.title() == 'Four Factors':
            if table_type == TableType.TEAM.name:
                StatClass[key.title()] = GeneralFourFactors(table_type)


# Initialize General Ranks
def initGeneralStatRanks(statrank_dict, table_stats):
    for stat in table_stats:
        if '_NAME' not in stat:
            statrank_dict[stat] = int()


# Store Stats to Player
def scrape_player(player, season_year = '2020-21', season_type = 'Regular%20Season'):
    '''
    Produces each player's general stats from:
        - https://www.nba.com/stats/players/traditional/
        - https://www.nba.com/stats/players/advanced/
        - https://www.nba.com/stats/players/misc/
        - https://www.nba.com/stats/players/scoring/
        - https://www.nba.com/stats/players/usage/
        - https://www.nba.com/stats/players/opponent/
        - https://www.nba.com/stats/players/defense/
    '''

    # Add stat class to player
    player.addTable('general', General(TableType.PLAYER.name))

    # URL Configurations
    name       = player.name.split(' ')[0] + '%20' + player.name.split(' ')[1]
    table_type = 'players/'
    stat       = 'PLAYER_NAME'

    # Start browser
    browser = webdriver.Chrome(ChromeDriverManager().install())

    # Get stats from correct url path
    for stat_key, stat_url in general_tables.items():

        if stat_key != 'Four Factors':

            # Browse to correct stat category
            url = 'https://nba.com/stats/' + table_type + stat_url + '/#!?CF=PLAYER_NAME*E*' + name + '&sort=' + stat + '&Season=' + season_year + '&SeasonType=' + season_type
            browser.get(url)

            # Scrape stats if table exists
            table = browserutils.loadStatTable(browser)
            if table is not None:
                getGenerlStats(table, stat_key.title(), player=player)

    # Close browser
    browser.quit()


# Store Stats to Teams
def scrape_teams(teams, season_year = '2020-21', season_type = 'Regular%20Season'):
    '''
    Produces each team's general stats from:
        - https://nba.com/stats/teams/traditional/
        - https://nba.com/stats/teams/advanced/
        - https://nba.com/stats/teams/four-factors/
        - https://nba.com/stats/teams/misc/
        - https://nba.com/stats/teams/scoring/
        - https://nba.com/stats/teams/opponent/
        - https://nba.com/stats/teams/defense/
    '''

    # Add stat class to teams
    for team in teams:
        teams[team].addTable('general', General(TableType.TEAM.name))

    # URL Configurations
    table_type  = 'teams/'
    stat        = 'TEAM_NAME'

    # Start browser
    browser = webdriver.Chrome(ChromeDriverManager().install())

    for stat_key, stat_url in general_tables.items():

        if stat_key != 'Usage':

            # Browse to correct stat category
            url = 'https://nba.com/stats/' + table_type  + stat_url + '?sort=' + stat + '&dir=-1' + '&Season=' + season_year + '&SeasonType=' + season_type
            browser.get(url)

            table = browserutils.loadStatTable(browser)
            if table is not None:
                getGenerlStats(table, stat_key.title(), teams=teams)
        
        # if stat_key == 'Traditional' or stat_key == 'Advanced':
        #     for stat, data in teams[team].general.items():
        #         print()
        #         print()
        #         if stat == 'Traditional' or stat == 'Advanced':
        #             # for 
        #             # print(stat, ": ", vars(your_object))
        #             pprint(vars(your_object))

    # Close browser
    browser.quit()


# Collect General Stats
def getGenerlStats(table, stat_key, player=None, teams=None):

    table_type = TableType.PLAYER.name if player is not None else TableType.TEAM.name
    (table_header_row, table_column_offset) = getStatColumnType('General ' + stat_key, table_type)

    # Parse statistic table
    index = 1
    for row, info in enumerate(table.split('\n')):

        # Throwaway junk lines (column names)
        if row > table_header_row:

            # Get Correct Class
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

                if stat_key == 'Traditional':
                    games      = data[next(itr)]
                    StatClass.games = int(games)

                    wins       = data[next(itr)]
                    StatClass.wins = int(wins)

                    losses      = data[next(itr)]
                    StatClass.losses = int(losses)

                    mins       = data[next(itr)]
                    StatClass.mins = float(mins)

                    if teams is not None:
                        win_p = data[next(itr)]
                        StatClass.win_p = float(win_p)

                    pts        = data[next(itr)]
                    StatClass.general[stat_key].pts = float(pts)

                    fg_m       = data[next(itr)]
                    StatClass.general[stat_key].fg_m = float(fg_m)

                    fg_a       = data[next(itr)]
                    StatClass.general[stat_key].fg_a = float(fg_a)

                    fg_pct       = data[next(itr)]
                    StatClass.general[stat_key].fg_pct = float(fg_pct)

                    fg3_m      = data[next(itr)]
                    StatClass.general[stat_key].fg3_m = float(fg3_m)

                    fg3_a      = data[next(itr)]
                    StatClass.general[stat_key].fg3_a = float(fg3_a)

                    fg3_pct    = data[next(itr)]
                    StatClass.general[stat_key].fg3_pct = float(fg3_pct)

                    ft_m       = data[next(itr)]
                    StatClass.general[stat_key].ft_m = float(ft_m)

                    ft_a       = data[next(itr)]
                    StatClass.general[stat_key].ft_a = float(ft_a)

                    ft_pct       = data[next(itr)]
                    StatClass.general[stat_key].ft_pct = float(ft_pct)

                    oreb       = data[next(itr)]
                    StatClass.general[stat_key].oreb = float(oreb)

                    dreb       = data[next(itr)]
                    StatClass.general[stat_key].dreb = float(dreb)

                    treb       = data[next(itr)]
                    StatClass.general[stat_key].treb = float(treb)

                    ast        = data[next(itr)]
                    StatClass.general[stat_key].ast = float(ast)

                    tov        = data[next(itr)]
                    StatClass.general[stat_key].tov = float(tov)

                    stl        = data[next(itr)]
                    StatClass.general[stat_key].stl = float(stl)

                    blk        = data[next(itr)]
                    StatClass.general[stat_key].blk = float(blk)

                    if teams is not None:
                        blk_a = data[next(itr)]
                        StatClass.general[stat_key].blk_a = float(blk_a)

                    pf_c      = data[next(itr)]
                    StatClass.general[stat_key].pf_c = float(pf_c)

                    if teams is not None:
                        pf_d = data[next(itr)]
                        StatClass.general[stat_key].pf_d = float(pf_d)

                    if player is not None:
                        fp         = data[next(itr)]
                        StatClass.general[stat_key].fp = float(fp)

                        dd2        = data[next(itr)]
                        StatClass.general[stat_key].dd2 = float(dd2)

                        td3        = data[next(itr)]
                        StatClass.general[stat_key].td3 = float(td3)

                    plusminus = data[next(itr)]
                    StatClass.general[stat_key].plusminus = float(plusminus)

                elif stat_key == 'Advanced':
                    orating = data[next(itr)]
                    StatClass.general[stat_key].orating = float(orating)

                    drating = data[next(itr)]
                    StatClass.general[stat_key].drating = float(drating)

                    netrating = data[next(itr)]
                    StatClass.general[stat_key].netrating = float(netrating)

                    ast_pct = data[next(itr)]
                    StatClass.general[stat_key].ast_pct = float(ast_pct)

                    ast_tov = data[next(itr)]
                    StatClass.general[stat_key].ast_tov = float(ast_tov)

                    ast_ratio = data[next(itr)]
                    StatClass.general[stat_key].ast_ratio = float(ast_ratio)

                    oreb_pct = data[next(itr)]
                    StatClass.general[stat_key].oreb_pct = float(oreb_pct)

                    dreb_pct = data[next(itr)]
                    StatClass.general[stat_key].dreb_pct = float(dreb_pct)

                    reb_pct = data[next(itr)]
                    StatClass.general[stat_key].reb_pct = float(reb_pct)

                    tov_pct = data[next(itr)]
                    StatClass.general[stat_key].tov_pct = float(tov_pct)

                    efg_pct = data[next(itr)]
                    StatClass.general[stat_key].efg_pct = float(efg_pct)

                    if player is not None:
                        usage = data[next(itr)]
                        StatClass.general[stat_key].usage = float(usage)

                    ts_pct = data[next(itr)]
                    StatClass.general[stat_key].ts_pct = float(ts_pct)

                    pace = data[next(itr)]
                    StatClass.general[stat_key].pace = float(pace)

                    pie = data[next(itr)]
                    StatClass.general[stat_key].pie = float(pie)

                elif stat_key == 'Misc':
                    pts_off_tov = data[next(itr)]
                    StatClass.general[stat_key].pts_off_tov = float(pts_off_tov)

                    pts_2nd_chance = data[next(itr)]
                    StatClass.general[stat_key].pts_2nd_chance = float(pts_2nd_chance)

                    pts_fastbreak = data[next(itr)]
                    StatClass.general[stat_key].pts_fastbreak = float(pts_fastbreak)

                    pts_in_paint = data[next(itr)]
                    StatClass.general[stat_key].pts_in_paint = float(pts_in_paint)

                    opp_pts_off_tov = data[next(itr)]
                    StatClass.general[stat_key].opp_pts_off_tov = float(opp_pts_off_tov)

                    opp_2nd_chance_pts = data[next(itr)]
                    StatClass.general[stat_key].opp_2nd_chance_pts = float(opp_2nd_chance_pts)

                    opp_fastbreak_pts = data[next(itr)]
                    StatClass.general[stat_key].opp_fastbreak_pts = float(opp_fastbreak_pts)

                    opp_pts_in_paint = data[next(itr)]
                    StatClass.general[stat_key].opp_pts_in_paint = float(opp_pts_in_paint)

                    if player is not None:
                        blk = data[next(itr)]
                        StatClass.general[stat_key].blk = float(blk)

                        blk_a = data[next(itr)]
                        StatClass.general[stat_key].blk_a = float(blk_a)

                        fouls_c = data[next(itr)]
                        StatClass.general[stat_key].fouls_c = float(fouls_c)

                        fouls_d = data[next(itr)]
                        StatClass.general[stat_key].fouls_d = float(fouls_d)

                elif stat_key == 'Scoring':
                    pct_fga_2pt       = data[next(itr)]
                    StatClass.general[stat_key].pct_fga_2pt = float(pct_fga_2pt)

                    pct_fga_3pt       = data[next(itr)]
                    StatClass.general[stat_key].pct_fga_3pt = float(pct_fga_3pt)

                    pct_pts_2pt       = data[next(itr)]
                    StatClass.general[stat_key].pct_pts_2pt = float(pct_pts_2pt)

                    pct_pts_mid       = data[next(itr)]
                    StatClass.general[stat_key].pct_pts_mid = float(pct_pts_mid)

                    pct_pts_3pt       = data[next(itr)]
                    StatClass.general[stat_key].pct_pts_3pt = float(pct_pts_3pt)

                    pct_pts_fb        = data[next(itr)]
                    StatClass.general[stat_key].pct_pts_fb = float(pct_pts_fb)

                    pct_pts_ft        = data[next(itr)]
                    StatClass.general[stat_key].pct_pts_ft = float(pct_pts_ft)

                    pct_pts_off_tov   = data[next(itr)]
                    StatClass.general[stat_key].pct_pts_off_tov = float(pct_pts_off_tov)

                    pct_pts_in_paint  = data[next(itr)]
                    StatClass.general[stat_key].pct_pts_in_paint = float(pct_pts_in_paint)

                    pct_pts_2pts_ast  = data[next(itr)]
                    StatClass.general[stat_key].pct_pts_2pts_ast = float(pct_pts_2pts_ast)

                    pct_pts_2pts_uast = data[next(itr)]
                    StatClass.general[stat_key].pct_pts_2pts_uast = float(pct_pts_2pts_uast)

                    pct_pts_3pts_ast  = data[next(itr)]
                    StatClass.general[stat_key].pct_pts_3pts_ast = float(pct_pts_3pts_ast)

                    pct_pts_3pts_uast = data[next(itr)]
                    StatClass.general[stat_key].pct_pts_3pts_uast = float(pct_pts_3pts_uast)

                    pct_pts_fgm_ast   = data[next(itr)]
                    StatClass.general[stat_key].p_pts_fgm_ast = float(pct_pts_fgm_ast)

                    pct_pts_fgm_uast  = data[next(itr)]
                    StatClass.general[stat_key].pct_pts_fgm_uast = float(pct_pts_fgm_uast)

                elif stat_key == 'Usage':
                    pct_usage         = data[next(itr)]
                    StatClass.general[stat_key].pct_usage = float(pct_usage)

                    pct_of_team_fg_m  = data[next(itr)]
                    StatClass.general[stat_key].pct_of_team_fg_m = float(pct_of_team_fg_m)

                    pct_of_team_fg_a  = data[next(itr)]
                    StatClass.general[stat_key].pct_of_team_fg_a = float(pct_of_team_fg_a)

                    pct_of_team_fg3_m = data[next(itr)]
                    StatClass.general[stat_key].pct_of_team_fg3_m = float(pct_of_team_fg3_m)

                    pct_of_team_fg3_a = data[next(itr)]
                    StatClass.general[stat_key].pct_of_team_fg3_a = float(pct_of_team_fg3_a)

                    pct_of_team_ft_m   = data[next(itr)]
                    StatClass.general[stat_key].pct_of_team_ft_m = float(pct_of_team_ft_m)

                    pct_of_team_ft_a  = data[next(itr)]
                    StatClass.general[stat_key].pct_of_team_ft_a = float(pct_of_team_ft_a)

                    pct_of_team_oreb  = data[next(itr)]
                    StatClass.general[stat_key].pct_of_team_oreb = float(pct_of_team_oreb)

                    pct_of_team_dreb  = data[next(itr)]
                    StatClass.general[stat_key].pct_of_team_dreb = float(pct_of_team_dreb)

                    pct_of_team_treb  = data[next(itr)]
                    StatClass.general[stat_key].pct_of_team_treb = float(pct_of_team_treb)

                    pct_of_team_ast   = data[next(itr)]
                    StatClass.general[stat_key].pct_of_team_ast = float(pct_of_team_ast)

                    pct_of_team_tov   = data[next(itr)]
                    StatClass.general[stat_key].pct_of_team_tov = float(pct_of_team_tov)

                    pct_of_team_stl   = data[next(itr)]
                    StatClass.general[stat_key].pct_of_team_stl = float(pct_of_team_stl)

                    pct_of_team_blk   = data[next(itr)]
                    StatClass.general[stat_key].pct_of_team_blk = float(pct_of_team_blk)

                    pct_of_team_blk_a = data[next(itr)]
                    StatClass.general[stat_key].pct_of_team_blk_a = float(pct_of_team_blk_a)

                    pct_of_team_pf_c  = data[next(itr)]
                    StatClass.general[stat_key].pct_of_team_pf_c = float(pct_of_team_pf_c)

                    pct_of_team_pf_d  = data[next(itr)]
                    StatClass.general[stat_key].pct_of_team_pf_d = float(pct_of_team_pf_d)

                    pct_of_team_pts   = data[next(itr)]
                    StatClass.general[stat_key].pct_of_team_pts = float(pct_of_team_pts)

                elif stat_key == 'Opponent':
                    opp_fg_m     = data[next(itr)]
                    StatClass.general[stat_key].opp_fg_m = float(opp_fg_m)

                    opp_fg_a     = data[next(itr)]
                    StatClass.general[stat_key].opp_fg_a = float(opp_fg_a)

                    opp_fg_pct     = data[next(itr)]
                    StatClass.general[stat_key].opp_fg_pct = float(opp_fg_pct)

                    opp_fg3_a    = data[next(itr)]
                    StatClass.general[stat_key].opp_fg3_a = float(opp_fg3_a)

                    opp_fg3_pct    = data[next(itr)]
                    StatClass.general[stat_key].opp_fg3_pct = float(opp_fg3_pct)

                    opp_ft_m     = data[next(itr)]
                    StatClass.general[stat_key].opp_ft_m = float(opp_ft_m)

                    opp_ft_a     = data[next(itr)]
                    StatClass.general[stat_key].opp_ft_a = float(opp_ft_a)

                    opp_ft_p     = data[next(itr)]
                    StatClass.general[stat_key].opp_ft_p = float(opp_ft_p)

                    opp_oreb     = data[next(itr)]
                    StatClass.general[stat_key].opp_oreb = float(opp_oreb)

                    opp_dreb     = data[next(itr)]
                    StatClass.general[stat_key].opp_dreb = float(opp_dreb)

                    opp_treb     = data[next(itr)]
                    StatClass.general[stat_key].opp_treb = float(opp_treb)

                    opp_ast      = data[next(itr)]
                    StatClass.general[stat_key].opp_ast = float(opp_ast)

                    opp_tov      = data[next(itr)]
                    StatClass.general[stat_key].opp_tov = float(opp_tov)

                    opp_stl      = data[next(itr)]
                    StatClass.general[stat_key].opp_stl = float(opp_stl)

                    opp_blk      = data[next(itr)]
                    StatClass.general[stat_key].opp_blk = float(opp_blk)

                    opp_blk_a    = data[next(itr)]
                    StatClass.general[stat_key].opp_blk_a = float(opp_blk_a)

                    opp_pf       = data[next(itr)]
                    StatClass.general[stat_key].opp_pf = float(opp_pf)

                    opp_pf_d     = data[next(itr)]
                    StatClass.general[stat_key].opp_pf_d = float(opp_pf_d)

                    opp_pts      = data[next(itr)]
                    StatClass.general[stat_key].opp_pts = float(opp_pts)

                    opp_plusminus = data[next(itr)]
                    StatClass.general[stat_key].opp_plusminus = float(opp_plusminus)

                elif stat_key == 'Defense':
                    drating            = data[next(itr)]
                    StatClass.general[stat_key].drating = float(drating)

                    dreb               = data[next(itr)]
                    StatClass.general[stat_key].dreb = float(dreb)

                    dreb_pct           = data[next(itr)]
                    StatClass.general[stat_key].dreb_pct = float(dreb_pct)

                    if player is not None:
                        pct_dreb       = data[next(itr)]
                        StatClass.general[stat_key].pct_dreb = float(pct_dreb)

                    stl                = data[next(itr)]
                    StatClass.general[stat_key].stl = float(stl)

                    if player is not None:
                        pct_stl        = data[next(itr)]
                        StatClass.general[stat_key].pct_stl = float(pct_stl)

                    blk                = data[next(itr)]
                    StatClass.general[stat_key].blk = float(blk)

                    if player is not None:
                        pct_blk        = data[next(itr)]
                        StatClass.general[stat_key].pct_blk = float(pct_blk)

                    opp_pts_off_tov    = data[next(itr)]
                    StatClass.general[stat_key].opp_pts_off_tov = float(opp_pts_off_tov)

                    opp_2nd_chance_pts = data[next(itr)]
                    StatClass.general[stat_key].opp_2nd_chance_pts = float(opp_2nd_chance_pts)

                    opp_fb_pts         = data[next(itr)]
                    StatClass.general[stat_key].opp_fb_pts = float(opp_fb_pts)

                    opp_pts_in_paint   = data[next(itr)]
                    StatClass.general[stat_key].opp_pts_in_paint = float(opp_pts_in_paint)

                    if player is not None:
                        def_ws         = data[next(itr)]
                        StatClass.general[stat_key].def_ws = float(def_ws)

                elif stat_key == 'Four Factors':
                    efg_pct      = data[next(itr)]
                    StatClass.general[stat_key].efg_pct = float(efg_pct)

                    fta_rate     = data[next(itr)]
                    StatClass.general[stat_key].fta_rate = float(fta_rate)

                    tov_pct      = data[next(itr)]
                    StatClass.general[stat_key].tov_pct = float(tov_pct)

                    oreb_pct     = data[next(itr)]
                    StatClass.general[stat_key].oreb_pct = float(oreb_pct)

                    opp_efg_pct  = data[next(itr)]
                    StatClass.general[stat_key].opp_efg_pct = float(opp_efg_pct)

                    opp_fta_rate = data[next(itr)]
                    StatClass.general[stat_key].opp_fta_rate = float(opp_fta_rate)

                    opp_tov_pct  = data[next(itr)]
                    StatClass.general[stat_key].opp_tov_pct = float(opp_tov_pct)

                    opp_oreb_pct = data[next(itr)]
                    StatClass.general[stat_key].opp_oreb_pct = float(opp_oreb_pct)

            index += 1


# Collect General Stat Rank
def getGeneralRank(table, stat_key, stat, player=None, teams=None):

    for row, info in enumerate(table.split('\n')):

        # Throwaway header row
        if row > 0:

            # Extract Rank
            if (row % 2) == 1:
                rank = int(info)

                if player is not None:
                    player.general[stat_key].rank_dict[stat] = rank

            elif (row % 2) == 0:
                if teams is not None:
                    team = info.upper()
                    teams[team].general[stat_key].rank_dict[stat] = rank


# Get General Table
def getGeneralType(table_type, stat_key):
    return {
        'Traditional':  traditional_player_stats if table_type == TableType.PLAYER.name else traditional_team_stats,
        'Advanced':     advanced_player_stats    if table_type == TableType.PLAYER.name else advanced_teams_stats,
        'Misc':         misc_player_stats        if table_type == TableType.PLAYER.name else misc_team_stats,
        'Scoring':      scoring_player_stats     if table_type == TableType.PLAYER.name else scoring_team_stats,
        'Usage':        usage_player_stats       if table_type == TableType.PLAYER.name else None,
        'Opponent':     opponent_player_stats    if table_type == TableType.PLAYER.name else opponent_team_stats,
        'Defense':      defensive_player_stats   if table_type == TableType.PLAYER.name else defensive_team_stats,
        'Four Factors': None                     if table_type == TableType.PLAYER.name else four_factor_team_stats,
    }.get(stat_key)
