from shooting.tables.dashboard import ShotDashboard
from shooting.tables.five_ft import Shooting5Ft
from shooting.tables.eight_ft import Shooting8Ft
from shooting.tables.zone import ShootingZone
from utils.filters import *
from utils.types import TableType


# TODO: MOVE TO UTILS
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
        for distance_key in distance_range:
            if distance_key == '5ft Range':
                self[distance_key] = Shooting5Ft()
            elif distance_key == '8ft Range':
                self[distance_key] = Shooting8Ft()
            elif distance_key == 'By Zone':
                self[distance_key] = ShootingZone()

        if table_type == TableType.TEAM.name:
            for shot_type_key in shot_range:
                self[shot_type_key]  = ShotDashboard()
            for shot_clock_key in shot_clock_range:
                self[shot_clock_key] = ShotDashboard()
            for dribbles_key in dribble_range:
                self[dribbles_key]   = ShotDashboard()
            for touch_time_key in touch_time_range:
                self[touch_time_key] = ShotDashboard()
            for closest_defender_distance_key in closest_defender_distance_range:
                self[closest_defender_distance_key] = ShotDashboard()

    def __getattr__(self, key):
        return self[key]
