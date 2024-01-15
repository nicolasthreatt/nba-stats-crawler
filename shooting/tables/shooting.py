from shooting.tables.dashboard import ShotDashboard
from shooting.tables.five_ft import Shooting5Ft
from shooting.tables.eight_ft import Shooting8Ft
from shooting.tables.zone import ShootingZone
from utils.filters import distance_range


class Shooting(dict):
    def __init__(self):
        for distance in distance_range.keys():
            if distance == '5ft Range':
                self[distance] = Shooting5Ft()
            elif distance == '8ft Range':
                self[distance] = Shooting8Ft()
            elif distance == 'By Zone':
                self[distance] = ShootingZone()

    def __getattr__(self, key):
        return self[key]
