from utils.filters import (
    shot_range,
    shot_clock_range,
    dribble_range,
    touch_time_range,
    closest_defender_distance_range
)


# TODO: MOVE TO UTILS
shot_dashboard_types = {
    'general':             shot_range,                      # General
    'shotclock':           shot_clock_range,                # Shotclock
    'dribbles':            dribble_range,                   # Driblles
    'touch-time':          touch_time_range,                # Touch Time
    'closest-defender':    closest_defender_distance_range, # Closet Defender
    'closest-defender-10': closest_defender_distance_range, # Closet Defender Atleast 10 ft
}


class ShotDashboard(dict):
    def __init__(self, table_type=None):
        for shot_dashboard_key, stat_type_dict in shot_dashboard_types.items():
            for stat_filter_key in stat_type_dict.keys():
                key = shot_dashboard_key.title() + ': ' + stat_filter_key
                self[key] = ShotDashboardStats()

    def __getattr__(self, key):
        return self[key]


# Shot Dashboard Stats
class ShotDashboardStats:
    def __init__(self):
        self.fg_freq   = float() # Field Goal Frequency
        self.fg_m      = float() # Field Goals Made
        self.fg_a      = float() # Field Goals Attemped
        self.fg_pct    = float() # Field Goal Percentage
        self.eFg_pct   = float() # Effective Field Goal Percentage
        self.fg2_freq  = float() # Two Point Field Goal Frequency
        self.fg2_m     = float() # Two Field Goals Made
        self.fg2_a     = float() # Two Point Field Goals Attemped
        self.fg2_pct   = float() # Two Field Goal Percentage
        self.fg3_freq  = float() # Three Point Field Goal Frequency
        self.fg3_m     = float() # Three Field Goals Made
        self.fg3_a     = float() # Three Field Goals Attemped
        self.fg3_pct   = float() # Three Field Goal Percentage
