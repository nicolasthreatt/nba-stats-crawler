class BoxScores:
    """Box Score Class"""
    def __init__(self):
        self.game = list()

    def add_game(self):
        """Add Game to Box Score"""
        self.game.append(BoxScoreStats())


class BoxScoreStats:
    """Box Score Stats Class"""
    def __init__(self):
        self.opponent  = str()   # Opponent
        self.game_date = str()   # Game Date
        self.result     = str()  # Win/Loss
        self.mins      = int()   # Minutes Played
        self.pts       = int()   # Points
        self.fg_m      = int()   # Field Goals Made
        self.fg_a      = int()   # Field Goal Percentage
        self.fg_pct    = float() # Field Goals Attempted
        self.fg3_m     = int()   # 3 Point Field Goals Made
        self.fg3_a     = int()   # 3 Point Field Goals Attempted
        self.fg3_pct   = float() # 3 Point Field Goals Percentage
        self.ft_m      = int()   # Free Throws Made
        self.ft_a      = int()   # Free Throws Attempted
        self.ft_pct    = float() # Free Throw Percentage
        self.oreb      = int()   # Offensive Rebounds
        self.dreb      = int()   # Defensive Rebounds
        self.treb      = int()   # Rebounds
        self.ast       = int()   # Assists
        self.stl       = int()   # Steals
        self.blk       = int()   # Blocks
        self.tov       = int()   # Turnovers
        self.pf        = int()   # Personal Fouls
        self.plusminus = int()   # Plus Minus
