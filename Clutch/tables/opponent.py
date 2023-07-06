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
