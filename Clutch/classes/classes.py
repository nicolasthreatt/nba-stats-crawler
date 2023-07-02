"""
Classes for Clutch STats
"""


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