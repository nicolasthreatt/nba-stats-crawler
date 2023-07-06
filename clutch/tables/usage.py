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
