'''
Steps to setup pyodc:
    - https://docs.microsoft.com/en-us/sql/connect/python/pyodbc/python-sql-driver-pyodbc?view=sql-server-ver15
Connect to Azure SQL Database:
    - https://docs.microsoft.com/en-us/azure/azure-sql/database/connect-query-python?tabs=windows 
Install ODBC Driver:
    -https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/install-microsoft-odbc-driver-sql-server-macos?view=sql-server-ver15
'''

import os
import pyodbc

def connect():

    # Database Credentials
    server   = os.getenv('azureServer')
    database = os.getenv('azureDBPlayer')
    username = os.getenv('azureDBUsername')
    password = os.getenv('azureDBPswd')
    driver   = '{ODBC Driver 17 for SQL Server}'

    # Connect to Database
    cnxn = pyodbc.connect('DRIVER='+driver+';      \
                           SERVER='+server+';      \
                           PORT=1433;              \
                           DATABASE='+database+';  \
                           UID='+username+';       \
                           PWD='+ password)
    return cnxn


def insert_player_data(player):
    cnxn = connect()

    if cnxn:
        print('Database connected...')

        print('Inserting Stats...')
        insert_bio(cnxn, player)
        insert_box_outs(cnxn, player)
        insert_boxscores(cnxn, player)
        insert_clutch(cnxn, player)
        insert_defensive_dashboard(cnxn, player)
        insert_general(cnxn, player)
        insert_hustle(cnxn, player)
        insert_opp_shooting(cnxn, player)
        insert_play_types(cnxn, player)
        insert_shooting(cnxn, player)
        insert_shot_dashboard(cnxn, player)
        insertdata(cnxn, player)

        cnxn.close()
        print('Database connection closed...')
    else:
        exit('Database connection failed...')


def insert_bio(cnxn, player):
    cursor = cnxn.cursor()

    insert_query = '''INSERT INTO [Players].[Bio](Player,
                                                  Team, 
                                                  Age,         Height,     Weight,
                                                  College,     Country,
                                                  DraftYear,   DraftRound, DraftNumber,
                                                  GamesPlayed,
                                                  Pts,         Rebs,       Asts,
                                                  NetRating,
                                                  ORebPct,     DRebPct,
                                                  AstPct,      TsPct,      UsagePct)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
    values = (
              player.name,
              player.team,
              player.age,          player.height,   player.weight,
              player.college,      player.country,
              player.draft_year,   player.draft_rd, player.draft_num,
              player.games_played,
              player.pts,          player.reb,      player.ast,
              player.netrtg,
              player.oreb_pct,     player.dreb_pct,
              player.usage_pct,    player.ts_pct,   player.ast_pct
    )

    cursor.execute(insert_query, values)

    # Commit Inserts
    cnxn.commit()


def insert_box_outs(cnxn, player):
    cursor = cnxn.cursor()

    insert_query = '''INSERT INTO BoxOuts.BoxOuts (Player,
                                                   Boxouts, 
                                                   OffBoxouts,           DefBoxouts,
                                                   TeamRebOnBoxOuts,     PlayerRebOnBoxOuts,
                                                   PctBoxoutsOff,        PctBoxoutsDef,
                                                   PctTeamRebWhenBoxOut, PctPlayerRebWhenBoxOut)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''

    data = player.boxOutStats
    values = (
              player.name,
              data.boxouts,
              data.off_boxouts,              data.def_boxouts
              data.team_reb_on_boxouts,      data.player_reb_on_boxouts,
              data.pct_boxouts_off,          data.pct_boxouts_def,
              data.pct_team_reb_when_boxout, data.pct_player_reb_when_boxout
    )

    cursor.execute(insert_query, values)

    # Commit Inserts
    cnxn.commit()


def insert_boxscores(cnxn, player):
    cursor = cnxn.cursor()

    insert_query = '''INSERT INTO BoxScores.BoxScores(Player, Opponent, GameDate,
                                                      Result, Mins,     Pts,
                                                      FgM,    FgA,      FgPct,
                                                      Fg3M,   Fg3A,     Fg3Pct,
                                                      FtM,    FtA,      FtPct,
                                                      OReb,   DReb,     TReb,
                                                      Ast,    Stl,      Blk,
                                                      Tov,    PF,       PlusMinus)
                      VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,  ?, ?, ?, ?, ?, ?, ?, ?, ?) '''

    for game in player.boxscoreStats.game:
        values = (
                  player.name  game.opponent, game.game_date,
                  game.result, game.mins,     game.pts,
                  game.fg_m,   game.fg_a,     game.fg_pct,
                  game.fg3_m,  game.fg3_a,    game.fg3_pct,
                  game.ft_m,   game.ft_a,     game.ft_pct,
                  game.oreb,   game.dreb,     game.treb,
                  game.ast,    game.stl,      game.blk,
                  game.tov,    game.pf,       game.plusminus
        )

        cursor.execute(insert_query, values)

    # Commit Inserts
    cnxn.commit()


def insert_defensive_dashboard(cnxn, player):
    cursor = cnxn.cursor()

    insert_query = '''INSERT INTO DefensiveDashboard.DefensiveDashboard(Player,
                                                                        Type, Freq,
                                                                        DefendedFgM, DefendedFgA, DefendedFgPct, FgPct,
                                                                        PctPtsDiff)
                      VALUES(?, ?, ?, ?, ?, ?, ?, ?) '''


    for key, data in player.defense_dashboards.items():
        values = (
                  player.name,
                  key, data.freq,
                  data.defended_fg_m, data.defended_fg_a, data.defended_fg_pct,
                  data.fg_pct,        data.pct_pts_diff
        )

        cursor.execute(insert_query, values)

    # Commit Inserts
    cnxn.commit()


def insert_clutch(cnxn, player):
    cursor = cnxn.cursor()

    for key, data in player.clutch.items():

        if key == 'Traditional':
            insert_query = '''INSERT INTO Clutch.Traditional(Player,
                                                             Pts,
                                                             FgM,  FgA,  FgPct,
                                                             Fg3M, Fg3A, Fg3Pct,
                                                             FtM,  FtA,  FtPct,
                                                             OReb, DReb, TReb,
                                                             Ast,  Tov,  Stl,
                                                             Blk, PF_C, 
                                                             FantasyPts, PlusMinus)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            values = (
                      player.name,
                      data.clutch_pts,
                      data.clutch_fg_m,    data.clutch_fg_a,  data.clutch_fg_pct,
                      data.clutch_fg3_m,   data.clutch_fg3_a, data.clutch_fg3_pct,
                      data.clutch_ft_m,    data.clutch_ft_a,  data.clutch_ft_pct,
                      data.clutch_oreb,    data.clutch_dreb,  data.clutch_treb,
                      data.clutch_ast,     data.clutch_tov,   data.clutch_stl,
                      data.clutch_blk,     data.clutch_fouls_c,
                      data.clutch_fp,      data.clutch_plusminus
            )

        elif key == 'Advanced':
            insert_query = '''INSERT INTO Clutch.Advanced(Player,
                                                            OffRating, DefRating,   NetRating,
                                                            AstPct,    AstTovRatio, AstRatio,
                                                            ORebPct,   DRebPct,     RebPct,
                                                            TovRatio,
                                                            EfgPct,    TsPct,       UsagePct,
                                                            Pace,      PIE)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            values = (
                      player.name,
                      data.clutch_orating,   data.clutch_drating,       data.clutch_netrating,
                      data.clutch_ast_pct,   data.clutch_ast_tov_ratio, data.clutch_ast_ratio,
                      data.clutch_oreb_pct,  data.clutch_dreb_pct,      data.clutch_reb_pct,
                      data.clutch_tov_ratio,
                      data.clutch_efg_pct,   data.clutch_ts_pct,        data.clutch_usage_pct,
                      data.clutch_pace,      data.clutch_pie
            )


        elif key == 'Misc':
            insert_query = '''INSERT INTO Clutch.Misc(Player,
                                                      PtsOffTov,       Pts2ndChance,    
                                                      PtsFastBreak,    PtsInPaint,
                                                      OppPtsOffTov,    OppPts2ndChance,
                                                      OppPtsFastBreak, OppPtsInPaint,
                                                      Blk,             BlkA,
                                                      PF_C,            PF_D)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            values = (
                      player.name,
                      data.clutch_pts_off_tov,       data.clutch_pts_2nd_chance,
                      data.clutch_pts_fastbreak,     data.clutch_pts_in_paint,
                      data.clutch_opp_pts_off_tov,   data.clutch_opp_2nd_chance_pts,
                      data.clutch_opp_fastbreak_pts, data.clutch_opp_pts_in_paint,
                      data.clutch_blk,               data.clutch_blk_a,
                      data.clutch_fouls_c,           data.clutch_fouls_d
            )


        elif key == 'Scoring':
            insert_query = '''INSERT INTO Clutch.Scoring(Player,
                                                         PctFgA2Pt,     PctFgA3Pt,
                                                         PctPts2Pt,     PctPtsMid,       PctPts3pt,
                                                         PctPtsFb,      PctPtsFT,        PctPtsOffTov, PctPtsInPaint,
                                                         PctPts2PtsAst, PctPts2PtsUnAst,
                                                         PctPts3PtsAst, PctPts3PtsUnAst,
                                                         PctPtsFgMAst,  PctPtsFgMUnAst)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            values = (
                      player.name,
                      data.clutch_pct_fga_2pt,      data.clutch_pct_fga_3pt,
                      data.clutch_pct_pts_2pt,      data.clutch_pct_pts_mid,       data.clutch_pct_pts_3pt,
                      data.clutch_pct_pts_fb,       data.clutch_pct_pts_ft,        data.clutch_pct_pts_off_tov, data.clutch_pct_pts_in_paint,
                      data.clutch_pct_pts_2pts_ast, data.clutch_pct_pts_2pts_uast,
                      data.clutch_pct_pts_3pts_ast, data.clutch_pct_pts_3pts_uast,
                      data.clutch_pct_pts_fgm_ast,  data.clutch_pct_pts_fgm_uast
            )


        elif key == 'Usage':
            insert_query = '''INSERT INTO Clutch.Usage(Player,
                                                       UsagePct,
                                                       PctOfTeamFgM,  PctOfTeamFgA,
                                                       PctOfTeamFg3M, PctOfTeamFg3A,
                                                       PctOfTeamFtM,  PctOfTeamFtA,
                                                       PctOfTeamOReb, PctOfTeamDReb, PctOfTeamTReb,
                                                       PctOfTeamAst,  PctOfTeamTov,  PctOfTeamStl,
                                                       PctOfTeamBlk,  PctOfTeamBlkA,
                                                       PctOfTeamPF_C, PctOfTeamPF_D,
                                                       PctOfTeamPts)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            values = (
                      player.name,
                      data.clutch_pct_usage,
                      data.clutch_pct_of_team_fg_m,  data.clutch_pct_of_team_fg_a,
                      data.clutch_pct_of_team_fg3_m, data.clutch_pct_of_team_fg3_a,
                      data.clutch_pct_of_team_ft_m,  data.clutch_pct_of_team_ft_a,
                      data.clutch_pct_of_team_oreb,  data.clutch_pct_of_team_dreb,  data.clutch_pct_of_team_treb,
                      data.clutch_pct_of_team_ast,   data.clutch_pct_of_team_tov,   data.clutch_pct_of_team_stl,
                      data.clutch_pct_of_team_blk,   data.clutch_pct_of_team_blk_a,
                      data.clutch_pct_of_team_pf_c,  data.clutch_pct_of_team_pf_d,
                      data.clutch_pct_of_team_pts
            )

        cursor.execute(insert_query, values)

    # Commit Inserts
    cnxn.commit()


def insert_general(cnxn, player):
    cursor = cnxn.cursor()

    for key, data in player.general.items():

        if key == 'Traditional':
            insert_query = '''INSERT INTO General.Traditional(Player,
                                                              Pts,
                                                              FgM,        FgA,  FgPct,
                                                              Fg3M,       Fg3A, Fg3Pct,
                                                              FtM,        FtA,  FtPct,
                                                              OReb,       DReb, TReb,
                                                              Ast,        Tov,  Stl,
                                                              Blk,        PF_C, 
                                                              FantasyPts, DD2, TD3,
                                                              PlusMinus)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            values = (
                      player.name,
                      data.pts,
                      data.fg_m,    data.fg_a,  data.fg_pct,
                      data.fg3_m,   data.fg3_a, data.fg3_pct,
                      data.ft_m,    data.ft_a,  data.ft_pct,
                      data.oreb,    data.dreb,  data.treb,
                      data.ast,     data.tov,   data.stl,
                      data.blk,     data.pf_c,
                      data.fp,      data.dd2,   data.td3,
                      data.plusminus
            )

        elif key == 'Advanced':
            insert_query = '''INSERT INTO General.Advanced(Player,
                                                            OffRating, DefRating,   NetRating,
                                                            AstPct,    AstTovRatio, AstRatio,
                                                            ORebPct,   DRebPct,     RebPct,
                                                            TovPct,
                                                            EfgPct,    TsPct,       UsagePct,
                                                            Pace,      PIE)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            values = (
                      player.name,
                      data.orating,   data.drating,  data.netrating,
                      data.ast_pct,   data.ast_tov,  data.ast_ratio,
                      data.oreb_pct,  data.dreb_pct, data.reb_pct,
                      data.tov_pct,
                      data.efg_pct,   data.ts_pct,   data.usage,
                      data.pace,      data.pie
            )

        elif key == 'Misc':
            insert_query = '''INSERT INTO General.Misc(Player,
                                                        PtsOffTov,       Pts2ndChance,
                                                        PtsFastBreak,    PtsInPaint,
                                                        OppPtsOffTov,    OppPts2ndChance,
                                                        OppPtsFastBreak, OppPtsInPaint,
                                                        Blk,             BlkA,
                                                        PF_C,            PF_D)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            values = (
                      player.name,
                      data.pts_off_tov,       data.pts_2nd_chance,
                      data.pts_fastbreak,     data.pts_in_paint,
                      data.opp_pts_off_tov,   data.opp_2nd_chance_pts,
                      data.opp_fastbreak_pts, data.opp_pts_in_paint,
                      data.blk,               data.blk_a,
                      data.fouls_c,           data.fouls_d
            )

        elif key == 'Scoring':
            insert_query = '''INSERT INTO General.Scoring(Player,
                                                          PctFgA2Pt,     PctFgA3Pt,
                                                          PctPts2Pt,     PctPtsMid,       PctPts3pt,
                                                          PctPtsFb,      PctPtsFT,        PctPtsOffTov, PctPtsInPaint,
                                                          PctPts2PtsAst, PctPts2PtsUnAst,
                                                          PctPts3PtsAst, PctPts3PtsUnAst,
                                                          PctPtsFgMAst,  PctPtsFgMUnAst)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            values = (
                      player.name,
                      data.pct_fga_2pt,      data.pct_fga_3pt,
                      data.pct_pts_2pt,      data.pct_pts_mid,       data.pct_pts_3pt,
                      data.pct_pts_fb,       data.pct_pts_ft,        data.pct_pts_off_tov, data.pct_pts_in_paint,
                      data.pct_pts_2pts_ast, data.pct_pts_2pts_uast,
                      data.pct_pts_3pts_ast, data.pct_pts_3pts_uast,
                      data.pct_pts_fgm_ast,  data.pct_pts_fgm_uast
            )
        
        elif key == 'Usage':
            insert_query = '''INSERT INTO General.Usage(Player,
                                                        UsagePct,
                                                        PctOfTeamFgM,  PctOfTeamFgA,
                                                        PctOfTeamFg3M, PctOfTeamFg3A,
                                                        PctOfTeamFtM,  PctOfTeamFtA,
                                                        PctOfTeamOReb, PctOfTeamDReb, PctOfTeamTReb,
                                                        PctOfTeamAst,  PctOfTeamTov,  PctOfTeamStl,
                                                        PctOfTeamBlk,  PctOfTeamBlkA,
                                                        PctOfTeamPF_C, PctOfTeamPF_D,
                                                        PctOfTeamPts)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            values = (
                      player.name,
                      data.pct_usage,
                      data.pct_of_team_fg_m,  data.pct_of_team_fg_a,
                      data.pct_of_team_fg3_m, data.pct_of_team_fg3_a,
                      data.pct_of_team_ft_m,  data.pct_of_team_ft_a,
                      data.pct_of_team_oreb,  data.pct_of_team_dreb,  data.pct_of_team_treb,
                      data.pct_of_team_ast,   data.pct_of_team_tov,   data.pct_of_team_stl,
                      data.pct_of_team_blk,   data.pct_of_team_blk_a,
                      data.pct_of_team_pf_c,  data.pct_of_team_pf_d,
                      data.pct_of_team_pts
            )

        elif key == 'Opponent':
            insert_query = '''INSERT INTO General.Opponent(Player,
                                                           OppFgM,  OppFgA,  OppFgPct,
                                                           OppFg3M, OppFg3A, OppFg3Pct,
                                                           OppFtM,  OppFtA,  OppFtPct,
                                                           OppOReb, OppDReb, OppTReb,
                                                           OppAst,  OppTov,  OppStl,
                                                           OppBlk,  OppBlkA,
                                                           OppPfC,  OppPfD,
                                                           OppPts,  OppPlusMinus)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            values = (
                      player.name,
                      data.opp_fg_m,  data.opp_fg_a,      data.opp_fg_pct,
                      data.opp_fg3_m, data.opp_fg3_a,     data.opp_fg3_pct,
                      data.opp_ft_m,  data.opp_ft_a,      data.opp_ft_pct,
                      data.opp_oreb,  data.opp_dreb,      data.opp_treb,
                      data.opp_ast,   data.opp_tov,       data.opp_stl,
                      data.opp_blk,   data.opp_blk_a,
                      data.opp_pf,    data.opp_pf_d,
                      data.opp_pts,   data.opp_plusminus
            )

        elif key == 'Defense':
            insert_query = '''INSERT INTO General.Defense(Player,
                                                            DRating,       DReb,           DRebPct,
                                                            Stl,           Blk,
                                                            OppPtsOffTov, OppPts2ndChance, OppPtsFastBreak, OppPtsInPaint,
                                                            PctDReb,      PctStl,          PctBlk,
                                                            DefWS)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            values = (
                      player.name,
                      data.drating,         data.dreb,               data.dreb_pct,
                      data.stl,             data.blk,
                      data.opp_pts_off_tov, data.opp_2nd_chance_pts, data.opp_fb_pts, data.opp_pts_in_paint,
                      data.pct_dreb,        data.pct_stl,            data.pct_blk,
                      data.def_ws
            )

        cursor.execute(insert_query, values)

    # Commit Inserts
    cnxn.commit()


def insert_hustle(cnxn, player):
    cursor = cnxn.cursor()

    insert_query = '''INSERT INTO Hustle.Hustle(Player,
                                                ScreenAst, ScreenAstPts,
                                                Deflections,
                                                OLooseBallsRecovered, DLooseBallsRecovered, TLooseBallsRecovered,
                                                PctLooseBallsO, PctLooseBallsD,
                                                ChargesDrawn,
                                                Contested2ptShots, Contested3ptShots, ContestedAllShots)
                      VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) '''

    data = player.hustle
    values = (
              player.name,
              data.screen_ast,              data.screen_ast_pts,
              data.deflections,
              data.o_loose_balls_recovered, data.d_loose_balls_recovered, data.tot_loose_balls_recovered,
              data.pct_loose_ball_o,        data.pct_loose_ball_d,
              data.charges_drawn,
              data.contested_2pt_shots,     data.contested_3pt_shots,      data.contested_all_shots
    )

    cursor.execute(insert_query, values)

    # Commit Inserts
    cnxn.commit()


def insert_opp_shooting(cnxn, player):
    cursor = cnxn.cursor()

    for key, data in player.opponent_shooting.items():

        if key == '5ft Range':
            insert_query = '''INSERT INTO [OpponentShooting].[5ft](Player,
                                                                   FgM_LT_5ft,   FgA_LT_5ft,   FgPct_LT_5ft,
                                                                   FgM_5To9ft,   FgA_5To9ft,   FgPct_5To9ft,
                                                                   FgM_10To14ft, FgA_10To14ft, FgPct_10To14ft,
                                                                   FgM_15To19ft, FgA_15To19ft, FgPct_15To19ft,
                                                                   FgM_20To24ft, FgA_20To24ft, FgPct_20To24ft,
                                                                   FgM_25To29ft, FgA_25To29ft, FgPct_25To29ft)
                            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) '''
            values = (
                      player.name,
                      data.fg_m_lt_5ft,       data.fg_a_lt_5ft,       data.fg_pct_lt_5ft,
                      data.fg_m_5ft_to_9ft,   data.fg_a_5ft_to_9ft,   data.fg_pct_5ft_to_9ft,
                      data.fg_m_10ft_to_14ft, data.fg_a_10ft_to_14ft, data.fg_pct_10ft_to_14ft,
                      data.fg_m_15ft_to_19ft, data.fg_a_15ft_to_19ft, data.fg_pct_15ft_to_19ft,
                      data.fg_m_20ft_to_24ft, data.fg_a_20ft_to_24ft, data.fg_pct_20ft_to_24ft,
                      data.fg_m_25ft_to_29ft, data.fg_a_25ft_to_29ft, data.fg_pct_25ft_to_29ft
            )

        elif key == '8ft Range':
            insert_query = '''INSERT INTO [OpponentShooting].[8ft](Player,
                                                                   FgM_LT_8ft,        FgA_LT_8ft,        FgPct_LT_8ft,
                                                                   FgM_8To16ft,       FgA_8To16ft,       FgPct_8To16ft,
                                                                   FgM_16To24ft,      FgA_16To24ft,      FgPct_16To24ft,
                                                                   FgM_24ft_Plus,     FgA_24ft_Plus,     FgPct_24ft_Plus,
                                                                   FgM_BackcourtShot, FgA_BackcourtShot, FgPct_BackcourtShot)
                            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) '''
            values = (
                      player.name,
                      data.fg_m_lt_8ft,         data.fg_a_lt_8ft,         data.fg_pct_lt_8ft,
                      data.fg_m_8ft_to_16ft,    data.fg_a_8ft_to_16ft,    data.fg_pct_8ft_to_16ft,
                      data.fg_m_16ft_to_24ft,   data.fg_a_16ft_to_24ft,   data.fg_pct_16ft_to_24ft,
                      data.fg_m_24ft_plus,      data.fg_a_24ft_plus,      data.fg_pct_24ft_plus,
                      data.fg_m_backcourt_shot, data.fg_a_backcourt_shot, data.fg_pct_backcourt_shot
            )
        
        elif key == 'By Zone':
            insert_query = '''INSERT INTO [OpponentShooting].[Zone](Player,
                                                                    FgM_RestrictedArea, FgA_RestrictedArea, FgPct_RestrictedArea,
                                                                    FgM_Paint,          FgA_Paint,          FgPct_Paint,
                                                                    FgM_Midrange,       FgA_Midrange,       FgPct_Midrange,
                                                                    FgM_LeftCorner3,    FgA_LeftCorner3,    FgPct_LeftCorner3,
                                                                    FgM_RightCorner3,   FgA_RightCorner3,   FgPct_RightCorner3,
                                                                    FgM_Corner3,        FgA_Corner3,        FgPct_Corner3,
                                                                    FgM_AboveBreak3,    FgA_AboveBreak3,    FgPct_AboveBreak3)
                                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) '''
            values = (
                      player.name,
                      data.fg_m_restricted_area, data.fg_a_restricted_area, data.fg_pct_restricted_area,
                      data.fg_m_paint,           data.fg_a_paint,           data.fg_pct_paint,
                      data.fg_m_midrange,        data.fg_a_midrange,        data.fg_pct_midrange,
                      data.fg_m_left_corner_3,   data.fg_a_left_corner_3,   data.fg_pct_left_corner_3,
                      data.fg_m_right_corner_3,  data.fg_a_right_corner_3,  data.fg_pct_right_corner_3,
                      data.fg_m_corner_3,        data.fg_a_corner_3,        data.fg_pct_corner_3,
                      data.fg_m_above_break_3,   data.fg_a_above_break_3,   data.fg_pct_above_break_3
            )

        cursor.execute(insert_query, values)

    # Commit Inserts
    cnxn.commit()


def insert_play_types(cnxn, player):
    cursor = cnxn.cursor()

    insert_query = '''INSERT INTO Playtypes.Playtypes(Player,
                                                      Playtype, Poss, Freq,
                                                      PPP, Pts,
                                                      FgM, FgA, FgPct, eFgPct,
                                                      FtFreq, TovFreq, SfFreq, And1Freq, ScoreFreq,
                                                      Percentile)
                      VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) '''

    for key, data in player.playtypes.items():
        values = (
                  player.name,
                  key,             data.poss,     data.freq,
                  data.ppp,        data.pts,
                  data.fg_m,       data.fg_a,     data.fg_pct,  data.efg_pct,
                  data.ft_freq,    data.tov_freq, data.sf_freq, data.and1_freq, data.score_freq,
                  data.percentile
        )

        cursor.execute(insert_query, values)

    # Commit Inserts
    cnxn.commit()


def insert_shooting(cnxn, player):
    cursor = cnxn.cursor()

    for key, data in player.shooting.items():

        if key == '5ft Range':
            insert_query = '''INSERT INTO [Shooting].[5ft](Player,
                                                           FgM_LT_5ft,   FgA_LT_5ft,   FgPct_LT_5ft,
                                                           FgM_5To9ft,   FgA_5To9ft,   FgPct_5To9ft,
                                                           FgM_10To14ft, FgA_10To14ft, FgPct_10To14ft,
                                                           FgM_15To19ft, FgA_15To19ft, FgPct_15To19ft,
                                                           FgM_20To24ft, FgA_20To24ft, FgPct_20To24ft,
                                                           FgM_25To29ft, FgA_25To29ft, FgPct_25To29ft)
                                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) '''
            values = (
                      player.name,
                      data.fg_m_lt_5ft,       data.fg_a_lt_5ft,       data.fg_pct_lt_5ft,
                      data.fg_m_5ft_to_9ft,   data.fg_a_5ft_to_9ft,   data.fg_pct_5ft_to_9ft,
                      data.fg_m_10ft_to_14ft, data.fg_a_10ft_to_14ft, data.fg_pct_10ft_to_14ft,
                      data.fg_m_15ft_to_19ft, data.fg_a_15ft_to_19ft, data.fg_pct_15ft_to_19ft,
                      data.fg_m_20ft_to_24ft, data.fg_a_20ft_to_24ft, data.fg_pct_20ft_to_24ft,
                      data.fg_m_25ft_to_29ft, data.fg_a_25ft_to_29ft, data.fg_pct_25ft_to_29ft
            )


        elif key == '8ft Range':
            insert_query = '''INSERT INTO [Shooting].[8ft](Player,
                                                           FgM_LT_8ft,        FgA_LT_8ft,        FgPct_LT_8ft,
                                                           FgM_8To16ft,       FgA_8To16ft,       FgPct_8To16ft,
                                                           FgM_16To24ft,      FgA_16To24ft,      FgPct_16To24ft,
                                                           FgM_24ft_Plus,     FgA_24ft_Plus,     FgPct_24ft_Plus,
                                                           FgM_BackcourtShot, FgA_BackcourtShot, FgPct_BackcourtShot)
                                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) '''
            values = (
                      player.name,
                      data.fg_m_lt_8ft,         data.fg_a_lt_8ft,         data.fg_pct_lt_8ft,
                      data.fg_m_8ft_to_16ft,    data.fg_a_8ft_to_16ft,    data.fg_pct_8ft_to_16ft,
                      data.fg_m_16ft_to_24ft,   data.fg_a_16ft_to_24ft,   data.fg_pct_16ft_to_24ft,
                      data.fg_m_24ft_plus,      data.fg_a_24ft_plus,      data.fg_pct_24ft_plus,
                      data.fg_m_backcourt_shot, data.fg_a_backcourt_shot, data.fg_pct_backcourt_shot
            )

        elif key == 'By Zone':
            insert_query = '''INSERT INTO [Shooting].[Zone](Player,
                                                            FgM_RestrictedArea, FgA_RestrictedArea, FgPct_RestrictedArea,
                                                            FgM_Paint,          FgA_Paint,          FgPct_Paint,
                                                            FgM_Midrange,       FgA_Midrange,       FgPct_Midrange,
                                                            FgM_LeftCorner3,    FgA_LeftCorner3,    FgPct_LeftCorner3,
                                                            FgM_RightCorner3,   FgA_RightCorner3,   FgPct_RightCorner3,
                                                            FgM_Corner3,        FgA_Corner3,        FgPct_Corner3,
                                                            FgM_AboveBreak3,    FgA_AboveBreak3,    FgPct_AboveBreak3)
                                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) '''
            values = (
                      player.name,
                      data.fg_m_restricted_area, data.fg_a_restricted_area, data.fg_pct_restricted_area,
                      data.fg_m_paint,           data.fg_a_paint,           data.fg_pct_paint,
                      data.fg_m_midrange,        data.fg_a_midrange,        data.fg_pct_midrange,
                      data.fg_m_left_corner_3,   data.fg_a_left_corner_3,   data.fg_pct_left_corner_3,
                      data.fg_m_right_corner_3,  data.fg_a_right_corner_3,  data.fg_pct_right_corner_3,
                      data.fg_m_corner_3,        data.fg_a_corner_3,        data.fg_pct_corner_3,
                      data.fg_m_above_break_3,   data.fg_a_above_break_3,   data.fg_pct_above_break_3
            )

        cursor.execute(insert_query, values)

    # Commit Inserts
    cnxn.commit()


def insert_shot_dashboard(cnxn, player):
    cursor = cnxn.cursor()

    insert_query = '''INSERT INTO ShotDashboard.ShotDashboard(Player,
                                                              Type,
                                                              FgFreq,  FgM,  FgA,  FgPct, eFgPct,
                                                              Fg2Freq, Fg2M, Fg2A, Fg2Pct,
                                                              Fg3Freq, Fg3M, Fg3A, Fg3Pct)
                      VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) '''


    for key, data in player.shot_dashboard.items():
        values = (
                  player.name,
                  key,
                  data.fg_freq,  data.fg_m,  data.fg_a,  data.fg_pct, data.eFg_pct,
                  data.fg2_freq, data.fg2_m, data.fg2_a, data.fg2_pct,
                  data.fg3_freq, data.fg3_m, data.fg3_a, data.fg3_pct
        )

        cursor.execute(insert_query, values)

    # Commit Inserts
    cnxn.commit()


def insert_tracking(cnxn, player):
    cursor = cnxn.cursor()

    for key, data in player.tracking.items():

        if key == 'Drives':
            insert_query = '''INSERT INTO [Tracking].[Drives](Player,
                                                              Drives,
                                                              FgM,    FgA,      FgPct,
                                                              FtM,    FtA,      FtPct,
                                                              Pts,    PctPts,
                                                              Passes, PctPasses,
                                                              Ast,    PctAst,
                                                              Tov,    PctTov,
                                                              Pf,     PctPf)
                                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) '''
            values = (
                      player.name,
                      data.drives,
                      data.drive_fg_m,    data.drive_fg_a,      data.drive_fg_pct,
                      data.drive_ft_m,    data.drive_ft_a,      data.drive_ft_pct,
                      data.drive_pts,     data.drive_pct_pts,
                      data.drive_passes,  data.drive_pct_passes,
                      data.drive_ast,     data.drive_pct_ast,
                      data.drive_tov,     data.drive_pct_tov,
                      data.drive_pf,      data.drive_pct_pf
            )

        elif key == 'Defensive Impact':
            insert_query = '''INSERT INTO [Tracking].[DefensiveImpact](Player,
                                                                       Stl,         Blk,         DReb,
                                                                       DefendedFgM, DefendedFgA, DefendedFgPct)
                                VALUES(?, ?, ?, ?, ?, ?, ?) '''
            values = (
                      player.name,
                      data.stl,           data.blk,           data.dreb, 
                      data.defended_fg_m, data.defended_fg_a, data.defended_fg_pct
            )

        elif key == 'Catch-Shoot':
            insert_query = '''INSERT INTO [Tracking].[CatchShoot](Player,
                                                                  Pts,
                                                                  FgM,  FgA,  FgPct,
                                                                  Fg3M, Fg3A, Fg3Pct,
                                                                  eFgPct)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            values = (
                      player.name,
                      data.catch_shoot_pts,
                      data.catch_shoot_fg_m,    data.catch_shoot_fg_a,  data.catch_shoot_fg_pct,
                      data.catch_shoot_fg3_m,   data.catch_shoot_fg3_a, data.catch_shoot_fg3_pct,
                      data.catch_shoot_efg_pct
            )

        elif key == 'Pull-Up':
            insert_query = '''INSERT INTO [Tracking].[PullUpShooting](Player,
                                                                      Pts,
                                                                      FgM,  FgA,  FgPct,
                                                                      Fg3M, Fg3A, Fg3Pct,
                                                                      eFgPct)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            values = (
                      player.name,
                      data.pull_up_shooting_pts,
                      data.pull_up_shooting_fg_m,    data.pull_up_shooting_fg_a,  data.pull_up_shooting_fg_pct,
                      data.pull_up_shooting_fg3_m,   data.pull_up_shooting_fg3_a, data.pull_up_shooting_fg3_pct,
                      data.pull_up_shooting_efg_pct
            )

        elif key == 'Passing':
            insert_query = '''INSERT INTO [Tracking].[Passing](Player,
                                                               PassesMaded,    PassesReceived,
                                                               Ast,            SecondaryAst,   PotentialAst,
                                                               AstPtsCreated,
                                                               AstAdjusted,    AstPassRatio,   AstPassRatioAdjusted)
                                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?) '''
            values = (
                      player.name,
                      data.passes_made,     data.passes_received,
                      data.ast,             data.secondary_ast,   data.potential_ast,
                      data.ast_pts_created,
                      data.ast_adjusted,
                      data.ast_to_pass_pct,
                      data.ast_to_pass_pct_adjusted
            )

        elif key == 'Touches':
            insert_query = '''INSERT INTO [Tracking].[Touches](Player,
                                                               Pts,
                                                               Touches,          FrontCourtTouches,
                                                               TimeOfPoss,       AvgSecPerTouch,    AvgDribblePerTouch,
                                                               PtsPerTouch,
                                                               ElbowTouches,     PostTouches,       PaintTouches,
                                                               PtsPerElbowTouch, PtsPerPostTouch,   PtsPerPaintTouch)
                                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) '''
            values = (
                      player.name,
                      data.pts,
                      data.touches,             data.front_cout_touches,
                      data.time_of_poss,        data.avg_sec_per_touch,  data.avg_dribble_per_touch,
                      data.pts_per_touch,
                      data.elbow_touches,       data.post_touches,       data.paint_touches,
                      data.pts_per_elbow_touch, data.pts_per_post_touch, data.pts_per_paint_touch
            )

        elif key == 'Rebounding':
            insert_query = '''INSERT INTO [Tracking].[Rebounding](Player,
                                                                  Rebs,
                                                                  ContestedReb,       ContestedRebPct,
                                                                  RebChances,         RebChancesPct,
                                                                  DeferredRebChances, AdjRebChancePct,
                                                                  AvgRebDistanceFeet)
                                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?) '''
            values = (
                      player.name,
                      data.rebs,
                      data.contested_rebs,        data.contested_rebs_pct,
                      data.reb_chances,           data.reb_chances_pct,
                      data.deferred_reb_chances,  data.adj_reb_chance_pct,
                      data.avg_reb_dist
            )

        elif key == 'Offensive Rebounding':
            insert_query = '''INSERT INTO [Tracking].[OffensiveRebounding](Player,
                                                                           ORebs,
                                                                           ContestedOReb,       ContestedORebPct,
                                                                           ORebChances,         ORebChancesPct,
                                                                           DeferredORebChances, AdjORebChancePct,
                                                                           AvgORebDistanceFeet)
                                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?) '''
            values = (
                      player.name,
                      data.orebs,
                      data.contested_orebs,        data.contested_orebs_pct,
                      data.oreb_chances,           data.oreb_chances_pct,
                      data.deferred_oreb_chances,  data.adj_oreb_chance_pct,
                      data.avg_oreb_dist
            )

        elif key == 'Defensive Rebounding':
            insert_query = '''INSERT INTO [Tracking].[DefensiveRebounding](Player,
                                                                           DRebs,
                                                                           ContestedDReb,       ContestedDRebPct,
                                                                           DRebChances,         DRebChancesPct,
                                                                           DeferredDRebChances, AdjDRebChancePct,
                                                                           AvgDRebDistanceFeet)
                                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?) '''
            values = (player.name,
                      data.drebs,
                      data.contested_drebs,        data.contested_drebs_pct,
                      data.dreb_chances,           data.dreb_chances_pct,
                      data.deferred_dreb_chances,  data.adj_dreb_chance_pct,
                      data.avg_dreb_dist
            )

        elif key == 'Shooting Efficiency':
            insert_query = '''INSERT INTO [Tracking].[ShootingEfficiency](Player,
                                                                          Pts,
                                                                          DrivePts,          DriveFgPct,
                                                                          CatchShootPts,     CatchShootFgPct,
                                                                          PullUpShootingPts, PullUpShootingFgPct,
                                                                          PaintTouchPts,     PaintTouchFgPct,
                                                                          PostTouchPts,      PostTouchFgPct,
                                                                          ElbowTouchPts,     ElbowTouchFgPct,
                                                                          eFgPct)
                                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) '''
            values = (
                      player.name,
                      data.pts,
                      data.drive_pts,            data.drive_fg_pct,
                      data.catch_shoot_pts,      data.catch_shoot_fg_pct,
                      data.pull_up_shooting_pts, data.pull_up_shooting_fg_pct,
                      data.paint_touch_pts,      data.paint_touch_fg_pct,
                      data.post_touch_pts,       data.post_touch_fg_pct,
                      data.elbow_touch_pts,      data.elbow_touch_fg_pct,
                      data.efg_pct
            )

        elif key == 'Speed-Distance':
            insert_query = '''INSERT INTO [Tracking].[SpeedDistance](Player,
                                                                     DistFeet,     DistMiles,
                                                                     DistMilesOff, DistMilesDef,
                                                                     AvgSpeed,     AvgSpeedOff, AvgSpeedDef)
                                VALUES(?, ?, ?, ?, ?, ?, ?, ?) '''
            values = (player.name,                                                                         \
                      data.dist_feet,      data.dist_miles,                                \
                      data.dist_miles_off, data.dist_miles_def,                            \
                      data.avg_speed,      data.avg_speed_off, data.avg_speed_def)

        elif key == 'Elbow Touch':
            insert_query = '''INSERT INTO [Tracking].[ElbowTouches](Player,
                                                                    Touches, ElbowTouches,
                                                                    FgM,     FgA,          FgPct,
                                                                    FtM,     FtA,          FtPct,
                                                                    Pts,     PctPts,
                                                                    Passes,  PctPasses,
                                                                    Ast,     PctAst,
                                                                    Tov,     PctTov,
                                                                    Pf,      PctPf)
                                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) '''
            values = (
                      player.name,
                      data.touches,             data.elbow_touches,
                      data.elbow_touch_fg_m,    data.elbow_touch_fg_a,      data.elbow_touch_fg_pct,
                      data.elbow_touch_ft_m,    data.elbow_touch_ft_a,      data.elbow_touch_ft_pct,
                      data.elbow_touch_pts,     data.elbow_touch_pct_pts,
                      data.elbow_touch_passes,  data.elbow_touch_pct_passes,
                      data.elbow_touch_ast,     data.elbow_touch_pct_ast,
                      data.elbow_touch_tov,     data.elbow_touch_pct_tov, 
                      data.elbow_touch_pf,      data.elbow_touch_pct_p
            )

        elif key == 'Post Ups':
            insert_query = '''INSERT INTO [Tracking].[PostUpTouches](Player,
                                                                     Touches, PostUpTouches,
                                                                     FgM,     FgA,           FgPct,
                                                                     FtM,     FtA,           FtPct,
                                                                     Pts,     PctPts,
                                                                     Passes,  PctPasses,
                                                                     Ast,     PctAst,
                                                                     Tov,     PctTov,
                                                                     Pf,      PctPf)
                                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) '''
            values = (
                      player.name,
                      data.touches,               data.post_up_touches,
                      data.post_up_touch_fg_m,    data.post_up_touch_fg_a,      data.post_up_touch_fg_pct,
                      data.post_up_touch_ft_m,    data.post_up_touch_ft_a,      data.post_up_touch_ft_pct,
                      data.post_up_touch_pts,     data.post_up_touch_pct_pts,
                      data.post_up_touch_passes,  data.post_up_touch_pct_passes,
                      data.post_up_touch_ast,     data.post_up_touch_pct_ast,
                      data.post_up_touch_tov,     data.post_up_touch_pct_tov,
                      data.post_up_touch_pf,      data.post_up_touch_pct_p
            )

        elif key == 'Paint Touches':
            insert_query = '''INSERT INTO [Tracking].[PaintTouches](Player,
                                                                    Touches, PaintTouches,
                                                                    FgM,     FgA,           FgPct,
                                                                    FtM,     FtA,           FtPct,
                                                                    Pts,     PctPts,
                                                                    Passes,  PctPasses,
                                                                    Ast,     PctAst,
                                                                    Tov,     PctTov,
                                                                    Pf,      PctPf)
                                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) '''
            values = (
                      player.name,
                      data.touches,             data.paint_touches,
                      data.paint_touch_fg_m,    data.paint_touch_fg_a,      data.paint_touch_fg_pct,
                      data.paint_touch_ft_m,    data.paint_touch_ft_a,      data.paint_touch_ft_pct,
                      data.paint_touch_pts,     data.paint_touch_pct_pts,
                      data.paint_touch_passes,  data.paint_touch_pct_passes,
                      data.paint_touch_ast,     data.paint_touch_pct_ast,
                      data.paint_touch_tov,     data.paint_touch_pct_tov,
                      data.paint_touch_pf,      data.paint_touch_pct_pf
            )
    
        cursor.execute(insert_query, values)

    # Commit Inserts
    cnxn.commit()
