class Team:
    def __init__(self):
        self.overall         = {'W': int(), 'L': int()} # Overall Record
        self.win_pct         = float()                  # Winning Percentage
        self.games_back      = float()                  # Games Back
        self.conference_rank = int()                    # Conference Ranking
        self.conference      = {'W': int(), 'L': int()} # Conference Record
        self.division_rank   = int()                    # Dvision Ranking
        self.division        = {'W': int(), 'L': int()} # Dvision Record
        self.home            = {'W': int(), 'L': int()} # Home Record
        self.road            = {'W': int(), 'L': int()} # Road Record
        self.ot              = {'W': int(), 'L': int()} # OT Record
        self.last10          = {'W': int(), 'L': int()} # Last 10 Games Record
        self.streak          = str()                    # Current Streak

    def addTable(self, name, table):
        setattr(self, name, table)
