from utils.filters import distance_range
from five_ft import Shooting5Ft
from eight_ft import Shooting8Ft
from zone import ShootingZone


class Shooting(dict):
    def __init__(self):
        init(self)

    def __getattr__(self, key):
        return self[key]


# Initialize Shot Dashboard Stats
def init(ShootingClass):
    for distance in distance_range.keys():
        if distance == '5ft Range':
            ShootingClass[distance] = Shooting5Ft()
        elif distance == '8ft Range':
            ShootingClass[distance] = Shooting8Ft()
        elif distance == 'By Zone':
            ShootingClass[distance] = ShootingZone()

