"""
BOX OUTS
"""
from utils.types import TableType


class BoxOuts:
    """Box Out Class"""
    def __init__(self, table_type):
        self.boxouts                         = float() # Box Outs
        self.off_boxouts                     = float() # Offensive Box Outs
        self.def_boxouts                     = float() # Defensive Box Outs
        self.pct_boxouts_off                 = float() # Percentage of Box Outs Offense
        self.pct_boxouts_def                 = float() # Percentage of Box Outs Defense

        if table_type == TableType.PLAYER.name:
            self.team_reb_on_boxouts         = float() # Teams Number of Rebounds on Box Outs
            self.player_reb_on_boxouts       = float() # Player Number of Rebounds on Box Outs
            self.pct_team_reb_when_boxout    = float() # Percentage of Team Rebounds when Box Out
            self.pct_player_reb_when_boxout  = float() # Percentage of Player Rebounds when Box Out

