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

