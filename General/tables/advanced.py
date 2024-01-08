import general.helpers as helpers
from utils.types import TableType


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

        advanced_table_type = helpers.get_table_type(table_type, 'Traditional')
        helpers.create_ranking_columns(self.rank_dict, advanced_table_type)
