import general.helpers as helpers
from utils.types import TableType


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

            four_factors_table_type = helpers.get_table_type(table_type, 'Four Factors')
            helpers.create_ranking_columns(self.rank_dict, four_factors_table_type)
