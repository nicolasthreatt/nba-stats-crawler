from utils.Types import TableType

class Rebounding:
    def __init__(self, table_type):
        self.rebs                 = float() # Rebounds
        self.contested_rebs       = float() # Contested Rebounds
        self.contested_rebs_pct   = float() # Contested Rebound Percentage
        self.reb_chances          = float() # Rebound Chance
        self.reb_chances_pct      = float() # Rebound Chance Percentage
        self.deferred_reb_chances = float() # Deferred Rebound Chances
        self.adj_reb_chance_pct   = float() # Adjusted Rebound Chance Percentage

        if table_type == TableType.PLAYER.name:
            self.avg_reb_dist     = float() # Average Rebound Distance


class OffensiveRebounding:
    def __init__(self, table_type):
        self.orebs                 = float() # Offensive Rebounds
        self.contested_orebs       = float() # Contested Offensive Rebounds
        self.contested_orebs_pct   = float() # Contested Offensive Rebound Percentage
        self.oreb_chances          = float() # Offensive Rebound Chance
        self.oreb_chances_pct      = float() # Offensive Rebound Chance Percentage
        self.deferred_oreb_chances = float() # Deferred Offensive Rebound Chances
        self.adj_oreb_chance_pct   = float() # Adjusted Offensive Rebound Chance Percentage

        if table_type == TableType.PLAYER.name:
            self.avg_oreb_dist     = float() # Average Offensive Rebound Distance


class DefensiveRebounding:
    def __init__(self, table_type):
        self.drebs                 = float() # Defensive Rebounds
        self.contested_drebs       = float() # Contested Defensive Rebounds
        self.contested_drebs_pct   = float() # Contested Defensive Rebound Percentage
        self.dreb_chances          = float() # Defensive Rebound Chance
        self.dreb_chances_pct      = float() # Defensive Rebound Chance Percentage
        self.deferred_dreb_chances = float() # Deferred Defensive Rebound Chances
        self.adj_dreb_chance_pct   = float() # Adjusted Defensive Rebound Chance Percentage

        if table_type == TableType.PLAYER.name:
            self.avg_dreb_dist     = float() # Average Defensive Rebound Distance
