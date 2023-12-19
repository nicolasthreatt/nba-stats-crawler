# clutch/tables/columns.py

clutch_stats = [
    'GP',
    'W',
    'L',
    'W_PCT',
    'MIN',
]

clutch_traditional_player = [ 
    'PLAYER_NAME',
    'PTS',
    'FGM',
    'FGA',
    'FG3M',
    'FG3A',
    'FTM',
    'FTA',
    'OREB',
    'DREB',
    'REB',
    'AST',
    'TOV',
    'STL',
    'BLK',
    'NBA_FANTASY_PTS',
    'PLUS_MINUS',
]

clutch_traditional_team = [ 
    'TEAM_NAME',
    'PTS',
    'FGM',
    'FGA',
    'FG_PCT',
    'FG3M',
    'FG3A',
    'FG3_PCT',
    'FTM',
    'FTA',
    'FT_PCT',
    'OREB',
    'DREB',
    'REB',
    'AST',
    'TOV',
    'STL',
    'BLK',
    'BLKA',
    'PF',
    'PFD',
    'PLUS_MINUS',
]

clutch_advanced_player = [ 
    'PLAYER_NAME',
    'OFF_RATING',
    'DEF_RATING',
    'NET_RATING',
    'AST_PCT',
    'AST_TO',
    'AST_RATIO',
    'OREB_PCT',
    'DREB_PCT',
    'REB_PCT',
    'TM_TOV_PCT',
    'EFG_PCT',
    'TS_PCT',
    'PACE',
    'PIE',
]

clutch_advanced_team = [ 
    'TEAM_NAME',
    'OFF_RATING',
    'DEF_RATING',
    'NET_RATING',
    'AST_PCT',
    'AST_TO',
    'AST_RATIO',
    'OREB_PCT',
    'DREB_PCT',
    'REB_PCT',
    'TM_TOV_PCT',
    'EFG_PCT',
    'TS_PCT',
    'PACE',
    'PIE',
]

clutch_four_factors_team = [ 
    'TEAM_NAME',
    'EFG_PCT',
    'FTA_RATE',
    'TM_TOV_PCT',
    'OREB_PCT',
    'OPP_EFG_PCT',
    'OPP_FTA_RATE',
    'OPP_TOV_PCT',
    'OPP_OREB_PCT',
]

clutch_misc_player = [ 
    'PLAYER_NAME',
    'PTS_OFF_TOV',
    'PTS_2ND_CHANCE',
    'PTS_FB',
    'PTS_PAINT',
    'OPP_PTS_OFF_TOV',
    'OPP_PTS_2ND_CHANCE',
    'OPP_PTS_FB',
    'OPP_PTS_PAINT',
    'BLK',
    'BLKA',
    'PF',
    'PFD',
]

clutch_misc_team = [ 
    'TEAM_NAME',
    'PTS_OFF_TOV',
    'PTS_2ND_CHANCE',
    'PTS_FB',
    'PTS_PAINT',
    'OPP_PTS_OFF_TOV',
    'OPP_PTS_2ND_CHANCE',
    'OPP_PTS_FB',
    'OPP_PTS_PAINT',
]

clutch_scoring_player = [ 
    'PLAYER_NAME',
    'PCT_FGA_2PT',
    'PCT_FGA_3PT',
    'PCT_FGA_3PT',
    'PCT_PTS_2PT',
    'PCT_PTS_2PT_MR',
    'PCT_PTS_3PT',
    'PCT_PTS_FB',
    'PCT_PTS_FT',
    'PCT_PTS_OFF_TOV',
    'PCT_PTS_PAINT',
    'PCT_AST_2PM',
    'PCT_UAST_2PM',
    'PCT_AST_3PM',
    'PCT_UAST_3PM',
    'PCT_AST_FGM',
    'PCT_UAST_FGM',
]

clutch_scoring_team = [ 
    'TEAM_NAME',
    'PCT_FGA_2PT',
    'PCT_FGA_3PT',
    'PCT_FGA_3PT',
    'PCT_PTS_2PT',
    'PCT_PTS_2PT_MR',
    'PCT_PTS_3PT',
    'PCT_PTS_FB',
    'PCT_PTS_FT',
    'PCT_PTS_OFF_TOV',
    'PCT_PTS_PAINT',
    'PCT_AST_2PM',
    'PCT_UAST_2PM',
    'PCT_AST_3PM',
    'PCT_UAST_3PM',
    'PCT_AST_FGM',
    'PCT_UAST_FGM',
]

clutch_usage_player = [ 
    'PLAYER_NAME',
    'USG_PCT',
    'PCT_FGM',
    'PCT_FGA',
    'PCT_FG3M',
    'PCT_FG3A',
    'PCT_FTM',
    'PCT_FTA',
    'PCT_OREB',
    'PCT_DREB',
    'PCT_REB',
    'PCT_AST',
    'PCT_TOV',
    'PCT_STL',
    'PCT_BLK',
    'PCT_BLKA',
    'PCT_PF',
    'PCT_PFD',
    'PCT_PTS',
]

clutch_opponent_team = [ 
    'TEAM_NAME',
    'OPP_FGM',
    'OPP_FGA',
    'OPP_FG_PCT',
    'OPP_FG3M',
    'OPP_FG3A',
    'OPP_FG3_PCT',
    'OPP_FTM',
    'OPP_FTA',
    'OPP_FT_PCT',
    'OPP_OREB',
    'OPP_DREB',
    'OPP_REB',
    'OPP_AST',
    'OPP_TOV',
    'OPP_STL',
    'OPP_BLK',
    'OPP_BLKA',
    'OPP_PF',
    # 'OPP_PFD',
    'OPP_PTS',
    'PLUS_MINUS',
]