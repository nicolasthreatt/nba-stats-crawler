'''
STAT COLUMNS
'''

traditional_player_stats = [ 
    'PLAYER_NAME',
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
    'PF',
    'NBA_FANTASY_PTS',
    'DD2',
    'TD3',
    'PLUS_MINUS'
]

traditional_team_stats = [ 
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
    'PLUS_MINUS'
]

advanced_player_stats = [ 
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
    'USG_PCT',
    'PACE',
    'PIE',
]

advanced_teams_stats = [ 
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

misc_player_stats = [
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

misc_team_stats = [
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

scoring_player_stats = [
    'PLAYER_NAME',
    'PCT_FGA_2PT',
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
    'PCT_UAST_FGM'
]

scoring_team_stats = [
    'TEAM_NAME',
    'PCT_FGA_2PT',
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
    'PCT_UAST_FGM'
]

usage_player_stats = [
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

opponent_player_stats = [
    'VS_PLAYER_NAME',
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
    'OPP_PFD',
    'OPP_PTS',
    'PLUS_MINUS'
]

opponent_team_stats = [
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
    'OPP_PFD',
    'OPP_PTS',
    'PLUS_MINUS'
]

defensive_player_stats = [
    'PLAYER_NAME',
    'DEF_RATING',
    'DREB',
    'DREB_PCT',
    'PCT_DREB',
    'STL',
    'PCT_STL',
    'BLK',
    'PCT_BLK',
    'OPP_PTS_OFF_TOV',
    'OPP_PTS_2ND_CHANCE',
    'OPP_PTS_FB',
    'OPP_PTS_PAINT',
    'DEF_WS'
]

defensive_team_stats = [
    'TEAM_NAME',
    'DEF_RATING',
    'DREB',
    'DREB_PCT',
    'STL',
    'BLK',
    'OPP_PTS_OFF_TOV',
    'OPP_PTS_2ND_CHANCE',
    'OPP_PTS_FB',
    'OPP_PTS_PAINT',
]

four_factor_team_stats = [
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