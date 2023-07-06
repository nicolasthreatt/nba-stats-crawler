# Tradional Stats
class ClutchTradional:
    def __init__(self, table_type=None):
        self.clutch_pts       = float() # Points
        self.clutch_fg_m      = float() # Field Goals Made
        self.clutch_fg_a      = float() # Field Goals Attempted
        self.clutch_fg_pct    = float() # Field Goals Percentage
        self.clutch_fg3_m     = float() # Three Points Made
        self.clutch_fg3_a     = float() # Three Points Attempted
        self.clutch_fg3_pct   = float() # Three Point Percentage
        self.clutch_ft_m      = float() # Free Throws Made
        self.clutch_ft_a      = float() # Free Throws Attempted
        self.clutch_ft_pct    = float() # Free Throw Percentage
        self.clutch_oreb      = float() # Offensive Rebounds
        self.clutch_dreb      = float() # Defensive Rebounds
        self.clutch_treb      = float() # Total Rebounds
        self.clutch_ast       = float() # Assist
        self.clutch_tov       = float() # Turnovers
        self.clutch_stl       = float() # Steals
        self.clutch_blk       = float() # Blocks
        self.clutch_fouls_c   = float() # Personal Fouls Commited
        self.clutch_plusminus = float() # Plus Minus
        self.statrank_dict    = dict()  # Dictionary to hold each team's stat rank

        if table_type == TableType.PLAYER.name:
            self.clutch_fp    = float() # Fantasy Points

        if table_type == TableType.TEAM.name:
            self.clutch_blk_a   = float() # Block Attempts
            self.clutch_fouls_d = float() # Personal Fouls Drawn
