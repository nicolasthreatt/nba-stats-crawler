from general import create_ranking_columns, get_table_type
from utils.Types import TableType


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

        create_ranking_columns(self.rank_dict, get_table_type(table_type, 'Opponent')) 
