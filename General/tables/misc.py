from general import create_ranking_columns, get_table_type
from utils.Types import TableType


class GeneralMisc:
    def __init__(self, table_type):
        self.pts_off_tov        = float() # Points Off Turnover
        self.pts_2nd_chance     = float() # 2nd Chance Points
        self.pts_fastbreak      = float() # Fastbreak Points
        self.pts_in_paint       = float() # Points in the Paint
        self.opp_pts_off_tov    = float() # Opponent Points Off Turnovers
        self.opp_2nd_chance_pts = float() # Opponent 2nd Chance Points
        self.opp_fastbreak_pts  = float() # Opponent Fastbreak Points
        self.opp_pts_in_paint   = float() # Opponent Points In the Paint
        self.rank_dict  = dict()

        if table_type == TableType.PLAYER.name:
            self.blk            = float() # Blocks Per Game
            self.blk_a          = float() # Blocks Attempted Per Game
            self.fouls_c        = float() # Personal Fouls Commited Per Game
            self.fouls_d        = float() # Personal Fouls Drawn Per Game

        create_ranking_columns(self.rank_dict, get_table_type(table_type, 'Misc'))

