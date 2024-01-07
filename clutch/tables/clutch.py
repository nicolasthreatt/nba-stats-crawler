# clutch/clutch.py
from clutch.tables.columns import *
from clutch.tables.advanced import ClutchAdvanced
from clutch.tables.four_factors import ClutchFourFactors
from clutch.tables.misc import ClutchMisc
from clutch.tables.opponent import ClutchOpponent
from clutch.tables.scoring import ClutchScoring
from clutch.tables.traditional import ClutchTradional
from clutch.tables.usage import ClutchUsage
from utils.types import TableType


clutch_stats_tables = {
    'Traditional':  'clutch-traditional/',
    'Advanced':     'clutch-advanced/',
    'Misc':         'clutch-misc/',
    'Scoring':      'clutch-scoring/',
    'Usage':        'clutch-usage/',
    'Four Factors': 'clutch-four-factors',
    'Opponent':     'clutch-opponent/',
}


class Clutch(dict):
    def __init__(self, table_type):
        self.clutch_games          = int()   # Total Games Played
        self.clutch_wins           = int()   # Totals Wins
        self.clutch_losses         = int()   # Total Loses
        self.clutch_mins           = float() # Minutes
        self.statrank_dict         = dict()  # Dictionary to hold each team's stat rank

        if table_type == TableType.TEAM.name:
            self.clutch_win_pct    = float() # Win Percentage

        self.create_tables(self, table_type)

    def __getattr__(self, key):
        return self[key]

    def create_tables(self, ClutchClass: dict, table_type: TableType):  # TODO: SEE if CluchClass can be removed
        """Create a dictionary of for each clutch stat table.
        This can be done for the `Clutch` class is represented as a dictionary.

        Args:
            ClutchClass (Clutch): Clutch class
            table_type (str): Table type (player/team)
        """
        for clutch_stat_table in clutch_stats_tables:
            if clutch_stat_table == 'Traditional':
                ClutchClass[clutch_stat_table] = ClutchTradional(table_type)
            elif clutch_stat_table == 'Advanced':
                ClutchClass[clutch_stat_table] = ClutchAdvanced(table_type)
            elif clutch_stat_table == 'Misc':
                ClutchClass[clutch_stat_table] = ClutchMisc(table_type)
            elif clutch_stat_table == 'Scoring':
                ClutchClass[clutch_stat_table] = ClutchScoring(table_type)
            elif clutch_stat_table == 'Usage':
                if(table_type == TableType.PLAYER.name):
                    ClutchClass[clutch_stat_table] = ClutchUsage(table_type)
            elif clutch_stat_table == 'Four Factors':
                if(table_type == TableType.TEAM.name):
                    ClutchClass[clutch_stat_table] = ClutchFourFactors(table_type)
            elif clutch_stat_table == 'Opponent':
                if(table_type == TableType.TEAM.name):
                    ClutchClass[clutch_stat_table] = ClutchOpponent(table_type)
            else:
                raise ValueError('Clutch Stat Type: ' + clutch_stat_table + ' not found.')
