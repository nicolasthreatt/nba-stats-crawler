from general import create_ranking_columns, get_table_type
from utils.Types import TableType


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

        create_ranking_columns(self.rank_dict, get_table_type(table_type, 'Defense'))
