from utils.filters import *
from utils.Types import TableType


opponent_shooting_stats_types = {
    'Overall':               'opponent-shooting/',
    'General':               'opponent-shots-general/',
    'Shot Clock':            'opponent-shots-shotclock/',
    'Dribbles':              'opponent-shots-dribbles/',
    'Touch Time':            'opponent-shots-touch-time/',
    'Closest Defender':      'opponent-shots-closest-defender/',
    'Closest Defender 10ft': 'opponent-shots-closest-defender-10/',
}


class OpponentShooting(dict):
    def __init__(self, table_type):
        init(self, table_type)

    def __getattr__(self, key):
        return self[key]


# Get Opponent Shooting Stats
def init(ShootingClass, table_type):
    for distance_key in distance_range:
        if distance_key == '5ft Range':
            ShootingClass[distance_key] = Shooting5Ft()
        elif distance_key == '8ft Range':
            ShootingClass[distance_key] = Shooting8Ft()
        elif distance_key == 'By Zone':
            ShootingClass[distance_key] = ShootingZone()

    if table_type == TableType.TEAM.name:
        for shot_type_key in shot_range:
            ShootingClass[shot_type_key]  = ShotDashboard()
        for shot_clock_key in shot_clock_range:
            ShootingClass[shot_clock_key] = ShotDashboard()
        for dribbles_key in dribble_range:
            ShootingClass[dribbles_key]   = ShotDashboard()
        for touch_time_key in touch_time_range:
            ShootingClass[touch_time_key] = ShotDashboard()
        for closest_defender_distance_key in closest_defender_distance_range:
            ShootingClass[closest_defender_distance_key] = ShotDashboard()
