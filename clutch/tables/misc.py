# Misc Stats
class ClutchMisc:
    def __init__(self, table_type):
        self.clutch_pts_off_tov        = float() # Points Off Turnover
        self.clutch_pts_2nd_chance     = float() # 2nd Chance Points
        self.clutch_pts_fastbreak      = float() # Fastbreak Points
        self.clutch_pts_in_paint       = float() # Points in the Paint
        self.clutch_opp_pts_off_tov    = float() # Opponent Points Off Turnovers
        self.clutch_opp_2nd_chance_pts = float() # Opponent 2nd Chance Points
        self.clutch_opp_fastbreak_pts  = float() # Opponent Fastbreak Points
        self.clutch_opp_pts_in_paint   = float() # Opponent Points In the Paint

        if table_type == TableType.PLAYER.name:
            self.clutch_blk            = float() # Blocks
            self.clutch_blk_a          = float() # Blocks Attempted
            self.clutch_fouls_c        = float() # Personal Fouls Commited Per Game
            self.clutch_fouls_d        = float() # Personal Fouls Drawn Per Game

        self.statrank_dict             = dict()  # Dictionary to hold each team's stat rank
