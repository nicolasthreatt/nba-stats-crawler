# general/general.py
import general.helpers as helpers
from utils.types import TableType


class General(dict):
    def __init__(self, table_type):
        self.games      = int()   # Total Games Played
        self.wins       = int()   # Totals Wins
        self.losses     = int()   # Total Losses
        self.mins       = float() # Minutes

        if table_type == TableType.TEAM.name:
            self.win_p  = float() # Wining Percentage

        helpers.init(self, table_type)

    def __getattr__(self, key):
        return self[key]
