"""
STAT FILTERS
"""

# Distance Range Stats Types
distance_range = {
    '5ft Range': '',
    '8ft Range': '&DistanceRange=8ft%20Range',
    'By Zone':   '&DistanceRange=By%20Zone',
}

# Shot Range Stat Types
shot_range = {
    'Overall':          '',
    'Catch and Shoot':  '&GeneralRange=Catch%20and%20Shoot',
    'Pull ups':         '&GeneralRange=Pullups',
    'Less Than 10ft':   '&GeneralRange=Less%20Than%2010%20ft',
}

# Shot Clock Range (Secs) Ranges
shot_clock_range = {
    '24-22':              '',
    '22-18 (Very Early)': '&ShotClockRange=22-18%20Very%20Early',
    '18-15 (Early)':      '&ShotClockRange=18-15%20Early',
    '15-7 (Average)':     '&ShotClockRange=15-7%20Average',
    '7-4 (Late)':         '&ShotClockRange=7-4%20Late',
    '4-0 (Very Late)':    '&ShotClockRange=4-0%20Very%20Late',
}

# Number of Dribbles Ranges
dribble_range = {
    '0':   '',
    '1':   '&DribbleRange=1%20Dribble',
    '2':   '&DribbleRange=2%20Dribbles',
    '3-6': '&DribbleRange=3-6%20Dribbles',
    '7+':  '&DribbleRange=7%2B%20Dribbles'
}

# Time (Secs) Touching Ball Ranges
touch_time_range = {
    '0-2': '',
    '2-6': '&DribbleRange=7%2B%20Dribbles',
    '6+':  '&TouchTimeRange=Touch%206%2B%20Seconds',
}

# Closest Defender Distance (Feet) Ranges
closest_defender_distance_range = {
    '0-2 Feet (Very Tight)': '',
    '2-4 Feet (Tight)':      '&CloseDefDistRange=2-4%20Feet%20-%20Tight',
    '4-6 Feet (Open)':       '&CloseDefDistRange=4-6%20Feet%20-%20Open',
    '6+ Feet (Wide Open)':   '&CloseDefDistRange=6%2B%20Feet%20-%20Wide%20Open',
}

# Season Type
season_types = {
    'Preason':        '&SeasonType=Pre%20Season',
    'Regular Season': '&SeasonType=Regular%20Season',
    'Playoffs':       '&SeasonType=Playoffs',
    'All-Star':       '&SeasonType=All%20Star',
}

# Per Mode Types
per_mode_types = {
    'Total':          '&PerMode=Totals',
    'Per Game':       '',
    'Per 100 Poss':   '&PerMode=Per100Possessions',
    'Per 100 Plays':  '&PerMode=Per100Plays',
    'Per 48 Minutes': '&PerMode=Per48',
    'Per 40 Minutes': '&PerMode=Per40',
    'Per 36 Minutes': '&PerMode=Per36',
    'Per 1 Minute':   '&PerMode=PerMinute',
    'Per 1 Poss':     '&PerMode=PerPossession',
    'Per 1 Play':     '&PerMode=PerPlay',
    'Minutes Per':    '&PerMode=MinutesPer',
}

# Offensive or Defensive
type_grouping = {
    'Offensive': '&TypeGrouping=offensive',
    'Defensive': '&TypeGrouping=defensive',
}

# Team Grouping
groupBy = {
    'Conference': '&GroupBy=conf',
    'Division':   '&GroupBy=div'
}
