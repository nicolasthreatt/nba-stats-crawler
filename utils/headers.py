"""
TABLE HEADERS
"""

import sys
sys.path.append("..")

from utils.Types import TableType

# Bio Stat Table
BIO_HEADER_COLS                            = 0

# Shooting Table Type Column Offset
BIO_PLAYER_OFFSET                          = 0


# Boxout Stat Table
BOXOUT_PLAYER_COLS                         = 4
BOXOUT_TEAM_COLS                           = 0

# Boxout Team Table Type Column Offset
BOXOUT_PLAYER_OFFSET                       = 4
BOXOUT_TEAM_OFFSET                         = 0


# Boxscore Stat Table
BOX_SCORE_STATS_COLS                       = 0

# Boxscore Team Table Type Column Offset
BOXSCORE_PLAYER_OFFSET                     = 2
BOXSCORE_TEAM_OFFSET                       = 2


# Clutch Stat Tables
CLUTCH_TRADITIONAL_STATS_COLS              = 0
CLUTCH_ADVANCED_STATS_COLS                 = 0
CLUTCH_MISC_STATS_COLS                     = 11
CLUTCH_SCORING_STATS_COLS                  = 29
CLUTCH_USAGE_STATS_COLS                    = 0
CLUTCH_FOUR_FACTOR_STATS_COLS              = 10
CLUTCH_OPPONENT_STATS_COLS                 = 39

# Clutch Team Table Type Column Offset
CLUTCH_TRADITIONAL_PLAYER_OFFSET           = 2
CLUTCH_TRADITIONAL_TEAM_OFFSET             = 0
CLUTCH_ADVANCED_PLAYER_OFFSET              = 6
CLUTCH_ADVANCED_TEAM_OFFSET                = 4
CLUTCH_FOUR_FACTOR_TEAM_OFFSET             = 5
CLUTCH_MISC_PLAYER_OFFSET                  = 6
CLUTCH_MISC_TEAM_OFFSET                    = 4
CLUTCH_SCORING_PLAYER_OFFSET               = 6
CLUTCH_SCORING_TEAM_OFFSET                 = 4
CLUTCH_USAGE_PLAYER_OFFSET                 = 6
CLUTCH_OPPONENT_TEAM_OFFSET                = 4


# Defensive Dashboard Table
DEFENSIVE_DASHBOARD_STATS_COLS             = 0

DEFENSIVE_DASHBOARD_PLAYER_OFFSET          = 5
DEFENSIVE_DASHBOARD_TEAM_OFFSET            = 2


# General Stat Tables
GENERAL_TRADIONAL_STAT_COLS                = 0
GENERAL_ADVANCED_PLAYER_STAT_COLS          = 0
GENERAL_ADVANCED_TEAM_STAT_COLS            = 2
GENERAL_FOUR_FACTOR_STATS_COLS             = 10
GENERAL_MISC_STATS_COLS                    = 11
GENERAL_SCORING_STATS_COLS                 = 29
GENERAL_USAGE_STATS_COLS                   = 0
GENERAL_OPPONENT_STATS_COLS                = 39
GENERAL_DEFENSE_PLAYER_STATS_COLS          = 9
GENERAL_DEFENSE_TEAM_STATS_COLS            = 7

# General Table Type Column Offset
GENERAL_TRADIONAL_PLAYER_OFFSET            = 2
GENERAL_TRADIONAL_TEAM_OFFSET              = 0
GENERAL_ADVANCED_PLAYER_OFFSET             = 6
GENERAL_ADVANCED_TEAM_OFFSET               = 4
GENERAL_FOUR_FACTOR_TEAM_OFFSET            = 5
GENERAL_MISC_PLAYER_OFFSET                 = 6
GENERAL_MISC_TEAM_OFFSET                   = 4
GENERAL_SCORING_PLAYER_OFFSET              = 6
GENERAL_SCORING_TEAM_OFFSET                = 4
GENERAL_USAGE_PLAYER_OFFSET                = 6
GENERAL_OPPONENT_PLAYER_OFFSET             = 5
GENERAL_OPPONENT_TEAM_OFFSET               = 4
GENERAL_DEFENSE_PLAYER_OFFSET              = 6
GENERAL_DEFENSE_TEAM_OFFSET                = 0


# Hustle Stat Table
HUSTLE_STATS_COLS                          = 11

# Hustle Team Table Type Column Offset
HUSTLE_PLAYER_OFFSET                       = 4
HUSTLE_TEAM_OFFSET                         = 1


# Opponent Shooting Stat Tables
OPPONENT_SHOOTING_OVERALL_STATS_5FT_COLS   = 6
OPPONENT_SHOOTING_OVERALL_STATS_8FT_COLS   = 5
OPPONENT_SHOOTING_OVERALL_STATS_ZONE_COLS  = 4
OPPONENT_SHOOTING_GENERAL_STATS_COLS       = 2
OPPONENT_SHOOTING_SHOT_CLOCK_STATS_COLS    = 2
OPPONENT_SHOOTING_DRIBBLES_STATS_COLS      = 2
OPPONENT_SHOOTING_TOUCH_TIME_STATS_COLS    = 2
OPPONENT_SHOOTING_DEFENDER_STATS_COLS      = 2

# Opponent Shooting Team Table Type Column Offset
OPPONENT_SHOOTING_PLAYER_OFFSET            = 2
OPPONENT_SHOOTING_TEAM_OFFSET              = 2
OPPONENT_SHOOTING_OVERALL_TEAM_OFFSET      = 0


# Playtype Stat Tables
PLAYTYPES_STATS_COLS                       = 5

# Playtyoe Column Offset
PLAYTYPES_PLAYER_COLS_OFFSET               = 2
PLAYTYPES_TEAM_COLS_OFFSET                 = 0


# Shooting Stat Tables
SHOOTING_STATS_5FT_COLS                    = 6
SHOOTING_STATS_8FT_COLS                    = 5
SHOOTING_STATS_ZONE_COLS                   = 4

# Shooting Table Type Column Offset
SHOOTING_STATS_PLAYER_OFFSET               = 2
SHOOTING_STATS_TEAM_OFFSET                 = 0


# Shot Dashboard Stat Table
SHOT_DASHBOARD_COLS                        = 2

# Shooting Table Type Column Offset
SHOT_DASHBOARD_PLAYERS_OFFSET              = 4
SHOT_DASHBOARD_TEAM_OFFSET                 = 2


# Tracking Tables
TRACKING_DRIVES_COLS                       = 0
TRACKING_DEFENSIVE_IMPACT_COLS             = 0
TRACKING_CATCH_SHOOT_COLS                  = 0
TRACKING_PASSING_STATS_COLS                = 9
TRACKING_TOUCHES_STATS_COLS                = 11
TRACKING_PULL_UP_STATS_COLS                = 0
TRACKING_REBOUNDING_PLAYER_COLS            = 7
TRACKING_REBOUNDING_TEAM_COLS              = 6
TRACKING_OREBOUNDING_PLAYER_COLS           = 7
TRACKING_OREBOUNDING_TEAM_COLS             = 6
TRACKING_DREBOUNDING_PLAYER_COLS           = 7
TRACKING_DREBOUNDING_TEAM_COLS             = 6
TRACKING_SHOOTING_EFFICIENCY_COLS          = 12
TRACKING_SPEED_DISTANCE_COLS               = 0
TRACKING_ELBOW_TOUCHES_COLS                = 1
TRACKING_POST_UP_TOUCHES_COLS              = 1
TRACKING_PAINT_TOUCHES_COLS                = 1

# Tracking Column Offsets
TRACKING_DRIVES_PLAYER_OFFSET              = 5
TRACKING_DRIVES_TEAM_OFFSET                = 4
TRACKING_DEFENSIVE_PLAYER_OFFSET           = 5
TRACKING_DEFENSIVE_TEAM_OFFSET             = 4
TRACKING_CATCH_SHOOT_PLAYER_OFFSET         = 3
TRACKING_CATCH_SHOOT_TEAM_OFFSET           = 2
TRACKING_PASSING_PLAYER_OFFSET             = 5
TRACKING_PASSING_TEAM_OFFSET               = 4
TRACKING_TOUCHES_PLAYER_OFFSET             = 5
TRACKING_TOUCHES_TEAM_OFFSET               = 4
TRACKING_PULL_UP_PLAYER_OFFSET             = 5
TRACKING_PULL_UP_TEAM_OFFSET               = 4
TRACKING_REBOUNDING_PLAYER_OFFSET          = 5
TRACKING_REBOUNDING_TEAM_OFFSET            = 4
TRACKING_OREBOUNDING_PLAYER_OFFSET         = 5
TRACKING_OREBOUNDING_TEAM_OFFSET           = 4
TRACKING_DREBOUNDING_PLAYER_OFFSET         = 5
TRACKING_DREBOUNDING_TEAM_OFFSET           = 4
TRACKING_SHOOTING_EFFICIENCY_PLAYER_OFFSET = 5
TRACKING_SHOOTING_EFFICIENCY_TEAM_OFFSET   = 4
TRACKING_SPEED_DISTANCE_PLAYER_OFFSET      = 5
TRACKING_SPEED_DISTANCE_TEAM_OFFSET        = 4
TRACKING_ELBOW_TOUCHES_PLAYER_OFFSET       = 5
TRACKING_ELBOW_TOUCHES_TEAM_OFFSET         = 4
TRACKING_POST_UP_TOUCHES_PLAYER_OFFSET     = 5
TRACKING_POST_UP_TOUCHES_TEAM_OFFSET       = 4
TRACKING_PAINT_TOUCHES_PLAYER_OFFSET       = 5
TRACKING_PAINT_TOUCHES_TEAM_OFFSET         = 4


def getStatColumnType(stat_key, table_type):
    return {
        #      KEY                                                              TUPLE
        'Box-Outs':                                (BOXOUT_PLAYER_COLS                         if table_type == TableType.PLAYER.name else BOXOUT_TEAM_COLS, \
                                                    BOXOUT_PLAYER_OFFSET                       if table_type == TableType.PLAYER.name else BOXOUT_TEAM_OFFSET),

        'Boxscores':                               (BOX_SCORE_STATS_COLS, \
                                                    BOXSCORE_PLAYER_OFFSET                     if table_type == TableType.PLAYER.name else BOXSCORE_TEAM_OFFSET),

        'Clutch Traditional':                      (CLUTCH_TRADITIONAL_STATS_COLS, \
                                                    CLUTCH_TRADITIONAL_PLAYER_OFFSET           if table_type == TableType.PLAYER.name else CLUTCH_TRADITIONAL_TEAM_OFFSET), 

        'Clutch Advanced':                         (CLUTCH_ADVANCED_STATS_COLS, \
                                                    CLUTCH_ADVANCED_PLAYER_OFFSET              if table_type == TableType.PLAYER.name else CLUTCH_ADVANCED_TEAM_OFFSET),

        'Clutch Four Factors':                     (CLUTCH_FOUR_FACTOR_STATS_COLS, \
                                                    CLUTCH_FOUR_FACTOR_TEAM_OFFSET),

        'Clutch Misc':                             (CLUTCH_MISC_STATS_COLS, \
                                                    CLUTCH_MISC_PLAYER_OFFSET                  if table_type == TableType.PLAYER.name else CLUTCH_MISC_TEAM_OFFSET),

        'Clutch Scoring':                          (CLUTCH_SCORING_STATS_COLS, \
                                                    CLUTCH_SCORING_PLAYER_OFFSET               if table_type == TableType.PLAYER.name else CLUTCH_SCORING_TEAM_OFFSET),

        'Clutch Usage':                            (CLUTCH_USAGE_STATS_COLS, \
                                                    CLUTCH_USAGE_PLAYER_OFFSET),

        'Clutch Opponent':                         (CLUTCH_OPPONENT_STATS_COLS, \
                                                    CLUTCH_OPPONENT_TEAM_OFFSET),

        'Defensive Dashboard':                     (DEFENSIVE_DASHBOARD_STATS_COLS, \
                                                    DEFENSIVE_DASHBOARD_PLAYER_OFFSET          if table_type == TableType.PLAYER.name else DEFENSIVE_DASHBOARD_TEAM_OFFSET),

        'General Traditional':                     (GENERAL_TRADIONAL_STAT_COLS, \
                                                    GENERAL_TRADIONAL_PLAYER_OFFSET            if table_type == TableType.PLAYER.name else GENERAL_TRADIONAL_TEAM_OFFSET),

        'General Advanced':                        (GENERAL_ADVANCED_PLAYER_STAT_COLS          if table_type == TableType.PLAYER.name else GENERAL_ADVANCED_TEAM_STAT_COLS, \
                                                    GENERAL_ADVANCED_PLAYER_OFFSET             if table_type == TableType.PLAYER.name else GENERAL_ADVANCED_TEAM_OFFSET),

        'General Four Factors':                    (GENERAL_FOUR_FACTOR_STATS_COLS, \
                                                    GENERAL_FOUR_FACTOR_TEAM_OFFSET),

        'General Misc':                            (GENERAL_MISC_STATS_COLS, \
                                                    GENERAL_MISC_PLAYER_OFFSET                 if table_type == TableType.PLAYER.name else GENERAL_MISC_TEAM_OFFSET),

        'General Scoring':                         (GENERAL_SCORING_STATS_COLS, \
                                                    GENERAL_SCORING_PLAYER_OFFSET              if table_type == TableType.PLAYER.name else GENERAL_SCORING_TEAM_OFFSET),

        'General Usage':                           (GENERAL_USAGE_STATS_COLS, \
                                                    GENERAL_USAGE_PLAYER_OFFSET),

        'General Opponent':                        (GENERAL_OPPONENT_STATS_COLS, \
                                                    GENERAL_OPPONENT_PLAYER_OFFSET             if table_type == TableType.PLAYER.name else GENERAL_OPPONENT_TEAM_OFFSET),

        'General Defense':                         (GENERAL_DEFENSE_PLAYER_STATS_COLS          if table_type == TableType.PLAYER.name else GENERAL_DEFENSE_TEAM_STATS_COLS, \
                                                    GENERAL_DEFENSE_PLAYER_OFFSET              if table_type == TableType.PLAYER.name else GENERAL_DEFENSE_TEAM_OFFSET),

        'Hustle':                                  (HUSTLE_STATS_COLS, \
                                                    HUSTLE_PLAYER_OFFSET                       if table_type == TableType.PLAYER.name else HUSTLE_TEAM_OFFSET),

        'Opponent Shooting Overall 5ft Range':     (OPPONENT_SHOOTING_OVERALL_STATS_5FT_COLS, \
                                                    OPPONENT_SHOOTING_PLAYER_OFFSET            if table_type == TableType.PLAYER.name else OPPONENT_SHOOTING_OVERALL_TEAM_OFFSET),

        'Opponent Shooting Overall 8ft Range':     (OPPONENT_SHOOTING_OVERALL_STATS_8FT_COLS, \
                                                    OPPONENT_SHOOTING_PLAYER_OFFSET            if table_type == TableType.PLAYER.name else OPPONENT_SHOOTING_OVERALL_TEAM_OFFSET),

        'Opponent Shooting Overall By Zone':       (OPPONENT_SHOOTING_OVERALL_STATS_ZONE_COLS, \
                                                    OPPONENT_SHOOTING_PLAYER_OFFSET            if table_type == TableType.PLAYER.name else OPPONENT_SHOOTING_OVERALL_TEAM_OFFSET),

        'Opponent Shooting General':               (OPPONENT_SHOOTING_GENERAL_STATS_COLS, \
                                                    OPPONENT_SHOOTING_PLAYER_OFFSET            if table_type == TableType.PLAYER.name else OPPONENT_SHOOTING_TEAM_OFFSET),

        'Opponent Shooting Shot Clock':            (OPPONENT_SHOOTING_SHOT_CLOCK_STATS_COLS, \
                                                    OPPONENT_SHOOTING_PLAYER_OFFSET            if table_type == TableType.PLAYER.name else OPPONENT_SHOOTING_TEAM_OFFSET),

        'Opponent Shooting Dribbles':              (OPPONENT_SHOOTING_DRIBBLES_STATS_COLS, \
                                                    OPPONENT_SHOOTING_PLAYER_OFFSET            if table_type == TableType.PLAYER.name else OPPONENT_SHOOTING_TEAM_OFFSET),

        'Opponent Shooting Touch Time':            (OPPONENT_SHOOTING_TOUCH_TIME_STATS_COLS, \
                                                    OPPONENT_SHOOTING_PLAYER_OFFSET            if table_type == TableType.PLAYER.name else OPPONENT_SHOOTING_TEAM_OFFSET),

        'Opponent Shooting Closest Defender':      (OPPONENT_SHOOTING_DEFENDER_STATS_COLS, \
                                                    OPPONENT_SHOOTING_PLAYER_OFFSET            if table_type == TableType.PLAYER.name else OPPONENT_SHOOTING_TEAM_OFFSET),

        'Opponent Shooting Closest Defender 10ft': (OPPONENT_SHOOTING_DEFENDER_STATS_COLS, \
                                                    OPPONENT_SHOOTING_PLAYER_OFFSET            if table_type == TableType.PLAYER.name else OPPONENT_SHOOTING_TEAM_OFFSET),

        'Playtype':                                (PLAYTYPES_STATS_COLS, \
                                                    PLAYTYPES_PLAYER_COLS_OFFSET               if table_type == TableType.PLAYER.name else PLAYTYPES_TEAM_COLS_OFFSET),

        'Shooting 5ft Range':                      (SHOOTING_STATS_5FT_COLS,  \
                                                    SHOOTING_STATS_PLAYER_OFFSET               if table_type == TableType.PLAYER.name else SHOOTING_STATS_TEAM_OFFSET),

        'Shooting 8ft Range':                      (SHOOTING_STATS_8FT_COLS,  \
                                                    SHOOTING_STATS_PLAYER_OFFSET               if table_type == TableType.PLAYER.name else SHOOTING_STATS_TEAM_OFFSET),

        'Shooting By Zone':                        (SHOOTING_STATS_ZONE_COLS, \
                                                    SHOOTING_STATS_PLAYER_OFFSET               if table_type == TableType.PLAYER.name else SHOOTING_STATS_TEAM_OFFSET),

        'Shot Dashboard':                          (SHOT_DASHBOARD_COLS, \
                                                    SHOT_DASHBOARD_PLAYERS_OFFSET              if table_type == TableType.PLAYER.name else SHOT_DASHBOARD_TEAM_OFFSET),

        'Tracking Drives':                         (TRACKING_DRIVES_COLS, \
                                                    TRACKING_DRIVES_PLAYER_OFFSET              if table_type == TableType.PLAYER.name else TRACKING_DRIVES_TEAM_OFFSET),

        'Tracking Defensive Impact':               (TRACKING_DEFENSIVE_IMPACT_COLS, \
                                                    TRACKING_DEFENSIVE_PLAYER_OFFSET           if table_type == TableType.PLAYER.name else TRACKING_DEFENSIVE_TEAM_OFFSET),

        'Tracking Catch-Shoot':                    (TRACKING_CATCH_SHOOT_COLS, \
                                                    TRACKING_CATCH_SHOOT_PLAYER_OFFSET         if table_type == TableType.PLAYER.name else TRACKING_CATCH_SHOOT_TEAM_OFFSET),

        'Tracking Passing':                        (TRACKING_PASSING_STATS_COLS, \
                                                    TRACKING_PASSING_PLAYER_OFFSET             if table_type == TableType.PLAYER.name else TRACKING_PASSING_TEAM_OFFSET),

        'Tracking Touches':                        (TRACKING_TOUCHES_STATS_COLS, \
                                                    TRACKING_TOUCHES_PLAYER_OFFSET             if table_type == TableType.PLAYER.name else TRACKING_TOUCHES_TEAM_OFFSET),

        'Tracking Pull-Up':                        (TRACKING_PULL_UP_STATS_COLS, \
                                                    TRACKING_PULL_UP_PLAYER_OFFSET             if table_type == TableType.PLAYER.name else TRACKING_PULL_UP_TEAM_OFFSET),

        'Tracking Rebounding':                     (TRACKING_REBOUNDING_PLAYER_COLS            if table_type == TableType.PLAYER.name else TRACKING_REBOUNDING_TEAM_COLS, \
                                                    TRACKING_REBOUNDING_PLAYER_OFFSET          if table_type == TableType.PLAYER.name else TRACKING_REBOUNDING_TEAM_OFFSET),

        'Tracking Offensive Rebounding':           (TRACKING_OREBOUNDING_PLAYER_COLS           if table_type == TableType.PLAYER.name else TRACKING_OREBOUNDING_TEAM_COLS, \
                                                    TRACKING_OREBOUNDING_PLAYER_OFFSET         if table_type == TableType.PLAYER.name else TRACKING_OREBOUNDING_TEAM_OFFSET),

        'Tracking Defensive Rebounding':           (TRACKING_DREBOUNDING_PLAYER_COLS           if table_type == TableType.PLAYER.name else TRACKING_DREBOUNDING_TEAM_COLS, \
                                                    TRACKING_DREBOUNDING_PLAYER_OFFSET         if table_type == TableType.PLAYER.name else TRACKING_DREBOUNDING_TEAM_OFFSET),

        'Tracking Shooting Efficiency':            (TRACKING_SHOOTING_EFFICIENCY_COLS, \
                                                    TRACKING_SHOOTING_EFFICIENCY_PLAYER_OFFSET if table_type == TableType.PLAYER.name else TRACKING_SHOOTING_EFFICIENCY_TEAM_OFFSET),

        'Tracking Speed-Distance':                 (TRACKING_SPEED_DISTANCE_COLS, \
                                                    TRACKING_SPEED_DISTANCE_PLAYER_OFFSET      if table_type == TableType.PLAYER.name else TRACKING_SPEED_DISTANCE_TEAM_OFFSET),

        'Tracking Elbow Touch':                    (TRACKING_ELBOW_TOUCHES_COLS, \
                                                    TRACKING_ELBOW_TOUCHES_PLAYER_OFFSET       if table_type == TableType.PLAYER.name else TRACKING_ELBOW_TOUCHES_TEAM_OFFSET),

        'Tracking Post Ups':                       (TRACKING_POST_UP_TOUCHES_COLS, \
                                                    TRACKING_POST_UP_TOUCHES_PLAYER_OFFSET     if table_type == TableType.PLAYER.name else TRACKING_POST_UP_TOUCHES_TEAM_OFFSET),

        'Tracking Paint Touches':                  (TRACKING_PAINT_TOUCHES_COLS, \
                                                    TRACKING_PAINT_TOUCHES_PLAYER_OFFSET       if table_type == TableType.PLAYER.name else TRACKING_PAINT_TOUCHES_TEAM_OFFSET),

    }.get(stat_key)
