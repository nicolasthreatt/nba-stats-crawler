# tracking/tracking.py
from catch_and_shoot import CatchShoot
from defensive_impact import DefensiveImpact
from drives import Drives
from passing import Passing
from pull_ups import PullUpShooting
from rebounds import Rebounding, DefensiveRebounding, OffensiveRebounding
from shooting_efficiency import ShootingEfficiency
from speed_distance import SpeedDistance
from touches import Touches, ElbowTouches, PaintTouches, PostUpTouches
from utils.types import TableType


tracking_tables = {
    'Drives':               'drives/',
    'Defensive Impact':     'defensive-impact/',
    'Catch-Shoot':          'catch-shoot/',
    'Passing':              'passing/',
    'Touches':              'touches/',
    'Pull-Up':              'pullup/',
    'Rebounding':           'rebounding/',
    'Offensive Rebounding': 'offensive-rebounding/',
    'Defensive Rebounding': 'defensive-rebounding/',
    'Shooting Efficiency':  'shooting-efficiency/',
    'Speed-Distance':       'speed-distance/',
    'Elbow Touch':          'elbow-touch/',
    'Post Ups':             'tracking-post-ups/',
    'Paint Touches':        'paint-touch/',
}


class Tracking(dict):
    def __init__(self, table_type):
        init(self, table_type)

    def __getattr__(self, key):
        return self[key]


# Get Tracking Stats Classes
def init(TrackingClass, table_type):
    for table in tracking_tables:
        if table == 'Drives':
            TrackingClass[table] = Drives()
        elif table == 'Defensive Impact':
            TrackingClass[table] = DefensiveImpact()
        elif table == 'Catch-Shoot':
            TrackingClass[table] = CatchShoot()
        elif table == 'Passing':
            TrackingClass[table] = Passing()
        elif table == 'Touches':
            TrackingClass[table] = Touches()
        elif table == 'Pull-Up':
            TrackingClass[table] = PullUpShooting()
        elif table == 'Rebounding':
            TrackingClass[table] = Rebounding(table_type)
        elif table == 'Offensive Rebounding':
            TrackingClass[table] = OffensiveRebounding(table_type)
        elif table == 'Defensive Rebounding':
            TrackingClass[table] = DefensiveRebounding(table_type)
        elif table == 'Shooting Efficiency':
            TrackingClass[table] = ShootingEfficiency()
        elif table == 'Speed-Distance':
            TrackingClass[table] = SpeedDistance()
        elif table == 'Elbow Touch':
            TrackingClass[table] = ElbowTouches()
        elif table == 'Post Ups':
            TrackingClass[table] = PostUpTouches()
        elif table == 'Paint Touches':
            TrackingClass[table] = PaintTouches()
