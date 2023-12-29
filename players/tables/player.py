class Player:
    def __init__(self):
        self.name         = str()   # Player Name
        self.team         = str()   # Current Team
        self.age          = int()   # Age
        self.height       = str()   # Height
        self.weight       = int()   # Weight
        self.college      = str()   # College
        self.country      = str()   # Country
        self.draft_year   = str()   # Draft Year
        self.draft_rd     = str()   # Draft Round
        self.draft_num    = str()   # Draft Number
        self.games_played = int()   # Games Played
        self.pts          = float() # Points
        self.reb          = float() # Rebounds
        self.ast          = float() # Assists
        self.netrtg       = float() # Net Rating
        self.oreb_pct     = float() # Offensive Rebounding Percentage
        self.dreb_pct     = float() # Defensive Rebound Percent
        self.usage_pct    = float() # Usage Percent
        self.ts_pct       = float() # True Shot Percent
        self.ast_pct      = float() # Assist Percent

    def addTable(self, name, table):
        setattr(self, name, table)
