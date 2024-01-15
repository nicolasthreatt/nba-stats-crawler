
from utils.types import TableType


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
