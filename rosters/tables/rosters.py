# Team class to hold each team's roster
class RosterTeam:
    def __init__(self, team, player = None):
        self.team = team
        self.players = []

    def getTeam(self):
        return (self.team)


# Player info class
class RosterPlayer:
    def __init__(self):
        self.name       = str() # Name
        self.number     = int() # Jersey Number
        self.height     = str() # Height
        self.weight     = int() # Weight
        self.position   = str() # Position
        self.birthdate  = str() # Birthdate
        self.age        = int() # Age
        self.experience = str() # Experience
        self.school     = str() # School
