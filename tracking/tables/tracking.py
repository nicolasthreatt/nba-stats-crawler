# tracking/tracking.py
from tracking.tables.catch_and_shoot import CatchShoot
from tracking.tables.defensive_impact import DefensiveImpact
from tracking.tables.drives import Drives
from tracking.tables.passing import Passing
from tracking.tables.pull_ups import PullUpShooting
from tracking.tables.rebounds import Rebounding, DefensiveRebounding, OffensiveRebounding
from tracking.tables.shooting_efficiency import ShootingEfficiency
from tracking.tables.speed_distance import SpeedDistance
from tracking.tables.touches import Touches, ElbowTouches, PaintTouches, PostUpTouches
from utils.types import TableType


# TODO: MOVE TO UTILS
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
        for table in tracking_tables:
            if table == 'Drives':
                self[table] = Drives()
            elif table == 'Defensive Impact':
                self[table] = DefensiveImpact()
            elif table == 'Catch-Shoot':
                self[table] = CatchShoot()
            elif table == 'Passing':
                self[table] = Passing()
            elif table == 'Touches':
                self[table] = Touches()
            elif table == 'Pull-Up':
                self[table] = PullUpShooting()
            elif table == 'Rebounding':
                self[table] = Rebounding(table_type)
            elif table == 'Offensive Rebounding':
                self[table] = OffensiveRebounding(table_type)
            elif table == 'Defensive Rebounding':
                self[table] = DefensiveRebounding(table_type)
            elif table == 'Shooting Efficiency':
                self[table] = ShootingEfficiency()
            elif table == 'Speed-Distance':
                self[table] = SpeedDistance()
            elif table == 'Elbow Touch':
                self[table] = ElbowTouches()
            elif table == 'Post Ups':
                self[table] = PostUpTouches()
            elif table == 'Paint Touches':
                self[table] = PaintTouches()

    def __getattr__(self, key):
        return self[key]
