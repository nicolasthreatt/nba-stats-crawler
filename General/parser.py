import itertools
from utils.headers import getStatColumnType
from utils.Player import Player
from utils.Team import Team
from utils.types import TableType


def parse(table: str, stat_type: str, player: Player = None, team: Team = None):

    table_type = TableType.PLAYER.name if player is not None else TableType.TEAM.name
    (table_header_row, table_column_offset) = getStatColumnType('General ' + stat_key, table_type)

    # Parse statistic table
    index = 1
    for row, info in enumerate(table.split('\n')):

        # Throwaway junk lines (column names)
        if row > table_header_row:

            # Get Correct Class
            if (index % 2) == 1:

                if player is not None:
                    name = info.title()
                    player.name = name
                    StatClass = player

                elif teams is not None:
                    team = info.upper()
                    StatClass = teams[team]

            # Extract stats
            elif (index % 2) == 0:

                # Create iterator
                itr = itertools.count(table_column_offset)

                # Parse and store stats
                data = info.split(' ')

                if stat_key == 'Traditional':
                    games      = data[next(itr)]
                    StatClass.games = int(games)

                    wins       = data[next(itr)]
                    StatClass.wins = int(wins)

                    losses      = data[next(itr)]
                    StatClass.losses = int(losses)

                    mins       = data[next(itr)]
                    StatClass.mins = float(mins)

                    if teams is not None:
                        win_p = data[next(itr)]
                        StatClass.win_p = float(win_p)

                    pts        = data[next(itr)]
                    StatClass.general[stat_key].pts = float(pts)

                    fg_m       = data[next(itr)]
                    StatClass.general[stat_key].fg_m = float(fg_m)

                    fg_a       = data[next(itr)]
                    StatClass.general[stat_key].fg_a = float(fg_a)

                    fg_pct       = data[next(itr)]
                    StatClass.general[stat_key].fg_pct = float(fg_pct)

                    fg3_m      = data[next(itr)]
                    StatClass.general[stat_key].fg3_m = float(fg3_m)

                    fg3_a      = data[next(itr)]
                    StatClass.general[stat_key].fg3_a = float(fg3_a)

                    fg3_pct    = data[next(itr)]
                    StatClass.general[stat_key].fg3_pct = float(fg3_pct)

                    ft_m       = data[next(itr)]
                    StatClass.general[stat_key].ft_m = float(ft_m)

                    ft_a       = data[next(itr)]
                    StatClass.general[stat_key].ft_a = float(ft_a)

                    ft_pct       = data[next(itr)]
                    StatClass.general[stat_key].ft_pct = float(ft_pct)

                    oreb       = data[next(itr)]
                    StatClass.general[stat_key].oreb = float(oreb)

                    dreb       = data[next(itr)]
                    StatClass.general[stat_key].dreb = float(dreb)

                    treb       = data[next(itr)]
                    StatClass.general[stat_key].treb = float(treb)

                    ast        = data[next(itr)]
                    StatClass.general[stat_key].ast = float(ast)

                    tov        = data[next(itr)]
                    StatClass.general[stat_key].tov = float(tov)

                    stl        = data[next(itr)]
                    StatClass.general[stat_key].stl = float(stl)

                    blk        = data[next(itr)]
                    StatClass.general[stat_key].blk = float(blk)

                    if teams is not None:
                        blk_a = data[next(itr)]
                        StatClass.general[stat_key].blk_a = float(blk_a)

                    pf_c      = data[next(itr)]
                    StatClass.general[stat_key].pf_c = float(pf_c)

                    if teams is not None:
                        pf_d = data[next(itr)]
                        StatClass.general[stat_key].pf_d = float(pf_d)

                    if player is not None:
                        fp         = data[next(itr)]
                        StatClass.general[stat_key].fp = float(fp)

                        dd2        = data[next(itr)]
                        StatClass.general[stat_key].dd2 = float(dd2)

                        td3        = data[next(itr)]
                        StatClass.general[stat_key].td3 = float(td3)

                    plusminus = data[next(itr)]
                    StatClass.general[stat_key].plusminus = float(plusminus)

                elif stat_key == 'Advanced':
                    orating = data[next(itr)]
                    StatClass.general[stat_key].orating = float(orating)

                    drating = data[next(itr)]
                    StatClass.general[stat_key].drating = float(drating)

                    netrating = data[next(itr)]
                    StatClass.general[stat_key].netrating = float(netrating)

                    ast_pct = data[next(itr)]
                    StatClass.general[stat_key].ast_pct = float(ast_pct)

                    ast_tov = data[next(itr)]
                    StatClass.general[stat_key].ast_tov = float(ast_tov)

                    ast_ratio = data[next(itr)]
                    StatClass.general[stat_key].ast_ratio = float(ast_ratio)

                    oreb_pct = data[next(itr)]
                    StatClass.general[stat_key].oreb_pct = float(oreb_pct)

                    dreb_pct = data[next(itr)]
                    StatClass.general[stat_key].dreb_pct = float(dreb_pct)

                    reb_pct = data[next(itr)]
                    StatClass.general[stat_key].reb_pct = float(reb_pct)

                    tov_pct = data[next(itr)]
                    StatClass.general[stat_key].tov_pct = float(tov_pct)

                    efg_pct = data[next(itr)]
                    StatClass.general[stat_key].efg_pct = float(efg_pct)

                    if player is not None:
                        usage = data[next(itr)]
                        StatClass.general[stat_key].usage = float(usage)

                    ts_pct = data[next(itr)]
                    StatClass.general[stat_key].ts_pct = float(ts_pct)

                    pace = data[next(itr)]
                    StatClass.general[stat_key].pace = float(pace)

                    pie = data[next(itr)]
                    StatClass.general[stat_key].pie = float(pie)

                elif stat_key == 'Misc':
                    pts_off_tov = data[next(itr)]
                    StatClass.general[stat_key].pts_off_tov = float(pts_off_tov)

                    pts_2nd_chance = data[next(itr)]
                    StatClass.general[stat_key].pts_2nd_chance = float(pts_2nd_chance)

                    pts_fastbreak = data[next(itr)]
                    StatClass.general[stat_key].pts_fastbreak = float(pts_fastbreak)

                    pts_in_paint = data[next(itr)]
                    StatClass.general[stat_key].pts_in_paint = float(pts_in_paint)

                    opp_pts_off_tov = data[next(itr)]
                    StatClass.general[stat_key].opp_pts_off_tov = float(opp_pts_off_tov)

                    opp_2nd_chance_pts = data[next(itr)]
                    StatClass.general[stat_key].opp_2nd_chance_pts = float(opp_2nd_chance_pts)

                    opp_fastbreak_pts = data[next(itr)]
                    StatClass.general[stat_key].opp_fastbreak_pts = float(opp_fastbreak_pts)

                    opp_pts_in_paint = data[next(itr)]
                    StatClass.general[stat_key].opp_pts_in_paint = float(opp_pts_in_paint)

                    if player is not None:
                        blk = data[next(itr)]
                        StatClass.general[stat_key].blk = float(blk)

                        blk_a = data[next(itr)]
                        StatClass.general[stat_key].blk_a = float(blk_a)

                        fouls_c = data[next(itr)]
                        StatClass.general[stat_key].fouls_c = float(fouls_c)

                        fouls_d = data[next(itr)]
                        StatClass.general[stat_key].fouls_d = float(fouls_d)

                elif stat_key == 'Scoring':
                    pct_fga_2pt       = data[next(itr)]
                    StatClass.general[stat_key].pct_fga_2pt = float(pct_fga_2pt)

                    pct_fga_3pt       = data[next(itr)]
                    StatClass.general[stat_key].pct_fga_3pt = float(pct_fga_3pt)

                    pct_pts_2pt       = data[next(itr)]
                    StatClass.general[stat_key].pct_pts_2pt = float(pct_pts_2pt)

                    pct_pts_mid       = data[next(itr)]
                    StatClass.general[stat_key].pct_pts_mid = float(pct_pts_mid)

                    pct_pts_3pt       = data[next(itr)]
                    StatClass.general[stat_key].pct_pts_3pt = float(pct_pts_3pt)

                    pct_pts_fb        = data[next(itr)]
                    StatClass.general[stat_key].pct_pts_fb = float(pct_pts_fb)

                    pct_pts_ft        = data[next(itr)]
                    StatClass.general[stat_key].pct_pts_ft = float(pct_pts_ft)

                    pct_pts_off_tov   = data[next(itr)]
                    StatClass.general[stat_key].pct_pts_off_tov = float(pct_pts_off_tov)

                    pct_pts_in_paint  = data[next(itr)]
                    StatClass.general[stat_key].pct_pts_in_paint = float(pct_pts_in_paint)

                    pct_pts_2pts_ast  = data[next(itr)]
                    StatClass.general[stat_key].pct_pts_2pts_ast = float(pct_pts_2pts_ast)

                    pct_pts_2pts_uast = data[next(itr)]
                    StatClass.general[stat_key].pct_pts_2pts_uast = float(pct_pts_2pts_uast)

                    pct_pts_3pts_ast  = data[next(itr)]
                    StatClass.general[stat_key].pct_pts_3pts_ast = float(pct_pts_3pts_ast)

                    pct_pts_3pts_uast = data[next(itr)]
                    StatClass.general[stat_key].pct_pts_3pts_uast = float(pct_pts_3pts_uast)

                    pct_pts_fgm_ast   = data[next(itr)]
                    StatClass.general[stat_key].p_pts_fgm_ast = float(pct_pts_fgm_ast)

                    pct_pts_fgm_uast  = data[next(itr)]
                    StatClass.general[stat_key].pct_pts_fgm_uast = float(pct_pts_fgm_uast)

                elif stat_key == 'Usage':
                    pct_usage         = data[next(itr)]
                    StatClass.general[stat_key].pct_usage = float(pct_usage)

                    pct_of_team_fg_m  = data[next(itr)]
                    StatClass.general[stat_key].pct_of_team_fg_m = float(pct_of_team_fg_m)

                    pct_of_team_fg_a  = data[next(itr)]
                    StatClass.general[stat_key].pct_of_team_fg_a = float(pct_of_team_fg_a)

                    pct_of_team_fg3_m = data[next(itr)]
                    StatClass.general[stat_key].pct_of_team_fg3_m = float(pct_of_team_fg3_m)

                    pct_of_team_fg3_a = data[next(itr)]
                    StatClass.general[stat_key].pct_of_team_fg3_a = float(pct_of_team_fg3_a)

                    pct_of_team_ft_m   = data[next(itr)]
                    StatClass.general[stat_key].pct_of_team_ft_m = float(pct_of_team_ft_m)

                    pct_of_team_ft_a  = data[next(itr)]
                    StatClass.general[stat_key].pct_of_team_ft_a = float(pct_of_team_ft_a)

                    pct_of_team_oreb  = data[next(itr)]
                    StatClass.general[stat_key].pct_of_team_oreb = float(pct_of_team_oreb)

                    pct_of_team_dreb  = data[next(itr)]
                    StatClass.general[stat_key].pct_of_team_dreb = float(pct_of_team_dreb)

                    pct_of_team_treb  = data[next(itr)]
                    StatClass.general[stat_key].pct_of_team_treb = float(pct_of_team_treb)

                    pct_of_team_ast   = data[next(itr)]
                    StatClass.general[stat_key].pct_of_team_ast = float(pct_of_team_ast)

                    pct_of_team_tov   = data[next(itr)]
                    StatClass.general[stat_key].pct_of_team_tov = float(pct_of_team_tov)

                    pct_of_team_stl   = data[next(itr)]
                    StatClass.general[stat_key].pct_of_team_stl = float(pct_of_team_stl)

                    pct_of_team_blk   = data[next(itr)]
                    StatClass.general[stat_key].pct_of_team_blk = float(pct_of_team_blk)

                    pct_of_team_blk_a = data[next(itr)]
                    StatClass.general[stat_key].pct_of_team_blk_a = float(pct_of_team_blk_a)

                    pct_of_team_pf_c  = data[next(itr)]
                    StatClass.general[stat_key].pct_of_team_pf_c = float(pct_of_team_pf_c)

                    pct_of_team_pf_d  = data[next(itr)]
                    StatClass.general[stat_key].pct_of_team_pf_d = float(pct_of_team_pf_d)

                    pct_of_team_pts   = data[next(itr)]
                    StatClass.general[stat_key].pct_of_team_pts = float(pct_of_team_pts)

                elif stat_key == 'Opponent':
                    opp_fg_m     = data[next(itr)]
                    StatClass.general[stat_key].opp_fg_m = float(opp_fg_m)

                    opp_fg_a     = data[next(itr)]
                    StatClass.general[stat_key].opp_fg_a = float(opp_fg_a)

                    opp_fg_pct     = data[next(itr)]
                    StatClass.general[stat_key].opp_fg_pct = float(opp_fg_pct)

                    opp_fg3_a    = data[next(itr)]
                    StatClass.general[stat_key].opp_fg3_a = float(opp_fg3_a)

                    opp_fg3_pct    = data[next(itr)]
                    StatClass.general[stat_key].opp_fg3_pct = float(opp_fg3_pct)

                    opp_ft_m     = data[next(itr)]
                    StatClass.general[stat_key].opp_ft_m = float(opp_ft_m)

                    opp_ft_a     = data[next(itr)]
                    StatClass.general[stat_key].opp_ft_a = float(opp_ft_a)

                    opp_ft_p     = data[next(itr)]
                    StatClass.general[stat_key].opp_ft_p = float(opp_ft_p)

                    opp_oreb     = data[next(itr)]
                    StatClass.general[stat_key].opp_oreb = float(opp_oreb)

                    opp_dreb     = data[next(itr)]
                    StatClass.general[stat_key].opp_dreb = float(opp_dreb)

                    opp_treb     = data[next(itr)]
                    StatClass.general[stat_key].opp_treb = float(opp_treb)

                    opp_ast      = data[next(itr)]
                    StatClass.general[stat_key].opp_ast = float(opp_ast)

                    opp_tov      = data[next(itr)]
                    StatClass.general[stat_key].opp_tov = float(opp_tov)

                    opp_stl      = data[next(itr)]
                    StatClass.general[stat_key].opp_stl = float(opp_stl)

                    opp_blk      = data[next(itr)]
                    StatClass.general[stat_key].opp_blk = float(opp_blk)

                    opp_blk_a    = data[next(itr)]
                    StatClass.general[stat_key].opp_blk_a = float(opp_blk_a)

                    opp_pf       = data[next(itr)]
                    StatClass.general[stat_key].opp_pf = float(opp_pf)

                    opp_pf_d     = data[next(itr)]
                    StatClass.general[stat_key].opp_pf_d = float(opp_pf_d)

                    opp_pts      = data[next(itr)]
                    StatClass.general[stat_key].opp_pts = float(opp_pts)

                    opp_plusminus = data[next(itr)]
                    StatClass.general[stat_key].opp_plusminus = float(opp_plusminus)

                elif stat_key == 'Defense':
                    drating            = data[next(itr)]
                    StatClass.general[stat_key].drating = float(drating)

                    dreb               = data[next(itr)]
                    StatClass.general[stat_key].dreb = float(dreb)

                    dreb_pct           = data[next(itr)]
                    StatClass.general[stat_key].dreb_pct = float(dreb_pct)

                    if player is not None:
                        pct_dreb       = data[next(itr)]
                        StatClass.general[stat_key].pct_dreb = float(pct_dreb)

                    stl                = data[next(itr)]
                    StatClass.general[stat_key].stl = float(stl)

                    if player is not None:
                        pct_stl        = data[next(itr)]
                        StatClass.general[stat_key].pct_stl = float(pct_stl)

                    blk                = data[next(itr)]
                    StatClass.general[stat_key].blk = float(blk)

                    if player is not None:
                        pct_blk        = data[next(itr)]
                        StatClass.general[stat_key].pct_blk = float(pct_blk)

                    opp_pts_off_tov    = data[next(itr)]
                    StatClass.general[stat_key].opp_pts_off_tov = float(opp_pts_off_tov)

                    opp_2nd_chance_pts = data[next(itr)]
                    StatClass.general[stat_key].opp_2nd_chance_pts = float(opp_2nd_chance_pts)

                    opp_fb_pts         = data[next(itr)]
                    StatClass.general[stat_key].opp_fb_pts = float(opp_fb_pts)

                    opp_pts_in_paint   = data[next(itr)]
                    StatClass.general[stat_key].opp_pts_in_paint = float(opp_pts_in_paint)

                    if player is not None:
                        def_ws         = data[next(itr)]
                        StatClass.general[stat_key].def_ws = float(def_ws)

                elif stat_key == 'Four Factors':
                    efg_pct      = data[next(itr)]
                    StatClass.general[stat_key].efg_pct = float(efg_pct)

                    fta_rate     = data[next(itr)]
                    StatClass.general[stat_key].fta_rate = float(fta_rate)

                    tov_pct      = data[next(itr)]
                    StatClass.general[stat_key].tov_pct = float(tov_pct)

                    oreb_pct     = data[next(itr)]
                    StatClass.general[stat_key].oreb_pct = float(oreb_pct)

                    opp_efg_pct  = data[next(itr)]
                    StatClass.general[stat_key].opp_efg_pct = float(opp_efg_pct)

                    opp_fta_rate = data[next(itr)]
                    StatClass.general[stat_key].opp_fta_rate = float(opp_fta_rate)

                    opp_tov_pct  = data[next(itr)]
                    StatClass.general[stat_key].opp_tov_pct = float(opp_tov_pct)

                    opp_oreb_pct = data[next(itr)]
                    StatClass.general[stat_key].opp_oreb_pct = float(opp_oreb_pct)

            index += 1

