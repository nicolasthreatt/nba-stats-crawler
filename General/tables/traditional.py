import general.helpers as helpers
from utils.types import TableType

class GeneralTraditional:
    def __init__(self, table_type):
        self.pts        = float() # Points
        self.fg_m       = float() # Fields Goals Made
        self.fg_a       = float() # Field Goals Attempted
        self.fg_pct     = float() # Field Goal Percentage
        self.fg3_m      = float() # Three Points Made
        self.fg3_a      = float() # Three Points Attempted
        self.fg3_pct    = float() # Three Point Percentage
        self.ft_m       = float() # Free Throws Made
        self.ft_a       = float() # Free Throws Attempted
        self.ft_pct     = float() # Free Throw Percentage
        self.oreb       = float() # Offensive Rebounds
        self.dreb       = float() # Defensive Rebounds
        self.treb       = float() # Total Rebounds
        self.ast        = float() # Assists
        self.tov        = float() # Turnovers
        self.stl        = float() # Steals
        self.blk        = float() # Blocks
        self.pf_c       = float() # Personal Fouls Commited
        self.plusminus  = float() # Plus Minus
        self.rank_dict  = dict()  # Dictionary to hold each stat rank

        if table_type == TableType.TEAM.name:
            self.blk_a  = float() # Block Attempt
            self.pf_d   = float() # Personal Fouls Drawn
        elif table_type == TableType.PLAYER.name:
            self.fp     = float() # Fantasy Points
            self.dd2    = int()   # Double-Double
            self.td3    = int()   # Triple-Double

        traditional_table_type = helpers.get_table_type(table_type, 'Traditional')
        helpers.create_ranking_columns(self.rank_dict, traditional_table_type)
