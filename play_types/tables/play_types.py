from utils.filters import type_grouping  # TODO: Add offensive and defensive advanced filter


playtypes = {
    'Transition':   'transition/',       # Transition
    'Isolation':    'isolation/',        # Iso
    'Ball Handler': 'ball-handler/',     # Pick & Role Ball Handler
    'Roll Man':     'roll-man/',         # Pick & Roll Roll Man
    'Post-Up':      'playtype-post-up/', # Post Up
    'Spot-Up':      'spot-up/',          # Spot Up
    'Hand-Off':     'hand-off/',         # Handoff
    'Cut':          'cut/',              # Cut
    'Off-Screen':   'off-screen/',       # Off Screen
    'Putbacks':     'putbacks/',         # Put Backs
    'Misc':         'playtype-misc/',    # Misc
}


class Playtype(dict):
    def __init__(self):
        init(self)

    def __getattr__(self, key):
        return self[key]


# Stat info class
class PlaytypeStats:
    def __init__(self):
        self.poss       = float() # Possessions
        self.freq       = float() # Frequency
        self.ppp        = float() # Points Per Possession
        self.pts        = float() # Points
        self.fg_m       = float() # Fields Goals Made
        self.fg_a       = float() # Field Goals Attempted
        self.fg_pct     = float() # Field Goal Percentage
        self.efg_pct    = float() # Effective Field Goal Percentage
        self.ft_freq    = float() # Free Throw Frequency
        self.tov_freq   = float() # Turnover Frequency
        self.sf_freq    = float() # Shooting Foul Frequency
        self.and1_freq  = float() # And1 Frequency
        self.score_freq = float() # Scoring Frequency
        self.percentile = float() # Percentile


def init(PlayTypeClass: Playtype):
    for playtype in playtypes:
        for typegroup_key in type_grouping:
            key = playtype + ' (' + typegroup_key.title() + ')'
            PlayTypeClass[key] = PlaytypeStats()
