from defense.tables.columns import *


class DefensiveDashboard(dict):
    def __init__(self):
        initDefensiveDashboardStatTypes(self)

    def __getattr__(self, key):
        return self[key]


# Defensive Dashboard Stats
class DefensiveDashboardStats:
    def __init__(self):
        self.freq            = float() # Frequency
        self.defended_fg_m   = float() # Defended Field Goals Made
        self.defended_fg_a   = float() # Defended Field Goals Attempted
        self.defended_fg_pct = float() # Defended Field Goal Percentage
        self.fg_pct          = float() # Field Goal Percentage
        self.pct_pts_diff    = float() # Percentage Points Different


# Initialize Defense Dashboard Stat Types
def initDefensiveDashboardStatTypes(StatClass):
    for key in defense_dashboard_types:
        StatClass[key.title()] = DefensiveDashboardStats()
