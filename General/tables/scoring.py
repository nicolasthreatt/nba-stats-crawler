from general import create_ranking_columns, get_table_type
from utils.Types import TableType


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

        create_ranking_columns(self.rank_dict, get_table_type(table_type, 'Scoring'))
