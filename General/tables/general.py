# general/general.py
from columns import *
from advanced import GeneralAdvanced
from defense import GeneralDefense
from four_factors import GeneralFourFactors
from misc import GeneralMisc
from opponent import GeneralOpponent
from scoring import GeneralScoring
from traditional import GeneralTraditional
from usage import GeneralUsage
from utils.types import TableType


general_tables = {
    'Traditional':  'traditional',
    'Advanced':     'advanced',
    'Misc':         'misc',
    'Scoring':      'scoring',
    'Usage':        'usage',
    'Opponent':     'opponent',
    'Defense':      'defense',
    'Four Factors': 'four-factors',
}


class General(dict):
    def __init__(self, table_type):
        self.games      = int()   # Total Games Played
        self.wins       = int()   # Totals Wins
        self.losses     = int()   # Total Losses
        self.mins       = float() # Minutes

        if table_type == TableType.TEAM.name:
            self.win_p  = float() # Wining Percentage

        init(self, table_type)

    def __getattr__(self, key):
        return self[key]


# Initialize General Stat Types
def init(GeneralClass, table_type):
    for key in general_tables:
        if key.title() == 'Traditional':
            GeneralClass[key.title()] = GeneralTraditional(table_type)
        elif key.title() == 'Advanced':
            GeneralClass[key.title()] = GeneralAdvanced(table_type)
        elif key.title() == 'Misc':
            GeneralClass[key.title()] = GeneralMisc(table_type)
        elif key.title() == 'Scoring':
            GeneralClass[key.title()] = GeneralScoring(table_type)
        elif key.title() == 'Usage':
            if table_type == TableType.PLAYER.name:
                GeneralClass[key.title()] = GeneralUsage(table_type)
        elif key.title() == 'Opponent':
            GeneralClass[key.title()] = GeneralOpponent(table_type)
        elif key.title() == 'Defense':
            GeneralClass[key.title()] = GeneralDefense(table_type)
        elif key.title() == 'Four Factors':
            if table_type == TableType.TEAM.name:
                GeneralClass[key.title()] = GeneralFourFactors(table_type)


# Initialize General Ranks
def create_ranking_columns(GeneralStatClass, table_columns):
    for stat in table_columns:
        if '_NAME' not in stat:
            GeneralStatClass[stat] = int()


# Get General Table
def get_table_type(table_type, stat_key):
    return {
        'Traditional':  traditional_player_stats if table_type == TableType.PLAYER.name else traditional_team_stats,
        'Advanced':     advanced_player_stats    if table_type == TableType.PLAYER.name else advanced_teams_stats,
        'Misc':         misc_player_stats        if table_type == TableType.PLAYER.name else misc_team_stats,
        'Scoring':      scoring_player_stats     if table_type == TableType.PLAYER.name else scoring_team_stats,
        'Usage':        usage_player_stats       if table_type == TableType.PLAYER.name else None,
        'Opponent':     opponent_player_stats    if table_type == TableType.PLAYER.name else opponent_team_stats,
        'Defense':      defensive_player_stats   if table_type == TableType.PLAYER.name else defensive_team_stats,
        'Four Factors': None                     if table_type == TableType.PLAYER.name else four_factor_team_stats,
    }.get(stat_key)
