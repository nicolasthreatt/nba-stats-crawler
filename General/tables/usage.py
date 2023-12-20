from general import create_ranking_columns, get_table_type
from utils.Types import TableType


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

            create_ranking_columns(self.rank_dict, get_table_type(table_type, 'Usage')) 
