import itertools
from utils.headers import getStatColumnType
from utils.Player import Player
from utils.Team import Team
from utils.types import TableType


def parse(table: str, stat_type: str, player: Player = None, team: Team = None):

    table_type = TableType.PLAYER.name if player is not None else TableType.TEAM.name
    (table_header_row, table_column_offset) = getStatColumnType('Tracking ' + stat_key, table_type)

    # Parse statistic table
    index = 1
    for row, info in enumerate(table.split('\n')):

        # Throwaway junk lines (column names)
        if row > table_header_row:

            # Get Correct Player/Team
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
                data = [stat.replace("-", "0") for stat in data]

                if stat_key == 'Drives':
                    drives           = data[next(itr)]
                    StatClass.tracking[stat_key].drives = float(drives)

                    drive_fg_m       = data[next(itr)]
                    StatClass.tracking[stat_key].drive_fg_m = float(drive_fg_m)

                    drive_fg_a       = data[next(itr)]
                    StatClass.tracking[stat_key].drive_fg_a = float(drive_fg_a)

                    drive_fg_pct     = data[next(itr)]
                    StatClass.tracking[stat_key].drive_fg_pct = float(drive_fg_pct)

                    drive_ft_m       = data[next(itr)]
                    StatClass.tracking[stat_key].drive_ft_m = float(drive_ft_m)

                    drive_ft_a       = data[next(itr)]
                    StatClass.tracking[stat_key].drive_ft_a = float(drive_ft_a)

                    drive_ft_pct     = data[next(itr)]
                    StatClass.tracking[stat_key].drive_ft_pct = float(drive_ft_pct)

                    drive_pts        = data[next(itr)]
                    StatClass.tracking[stat_key].drive_pts = float(drive_pts)

                    drive_pct_pts    = data[next(itr)]
                    StatClass.tracking[stat_key].drive_pct_pts = float(drive_pct_pts)

                    drive_passes     = data[next(itr)]
                    StatClass.tracking[stat_key].drive_passes = float(drive_passes)

                    drive_pct_passes = data[next(itr)]
                    StatClass.tracking[stat_key].drive_pct_passes = float(drive_pct_passes)

                    drive_ast        = data[next(itr)]
                    StatClass.tracking[stat_key].drive_ast = float(drive_ast)

                    drive_pct_ast    = data[next(itr)]
                    StatClass.tracking[stat_key].drive_pct_ast = float(drive_pct_ast)

                    drive_tov        = data[next(itr)]
                    StatClass.tracking[stat_key].drive_tov = float(drive_tov)

                    drive_pct_tov    = data[next(itr)]
                    StatClass.tracking[stat_key].drive_pct_tov = float(drive_pct_tov)

                    drive_pf         = data[next(itr)]
                    StatClass.tracking[stat_key].drive_pf = float(drive_pf)

                    drive_pct_pf     = data[next(itr)]
                    StatClass.tracking[stat_key].drive_pct_pf = float(drive_pct_pf)

                elif stat_key == 'Defensive Impact':
                    stl             = data[next(itr)]
                    StatClass.tracking[stat_key].stl = float(stl)

                    blk             = data[next(itr)]
                    StatClass.tracking[stat_key].blk = float(blk)

                    dreb            = data[next(itr)]
                    StatClass.tracking[stat_key].dreb = float(dreb)

                    defended_fg_m   = data[next(itr)]
                    StatClass.tracking[stat_key].defended_fg_m = float(defended_fg_m)

                    defended_fg_a   = data[next(itr)]
                    StatClass.tracking[stat_key].defended_fg_a = float(defended_fg_a)

                    defended_fg_pct = data[next(itr)]
                    StatClass.tracking[stat_key].defended_fg_pct = float(defended_fg_pct)

                elif stat_key == 'Catch-Shoot':
                    catch_shoot_pts   = data[next(itr)]
                    StatClass.tracking[stat_key].catch_shoot_pts = float(catch_shoot_pts)

                    catch_shoot_fg_m  = data[next(itr)]
                    StatClass.tracking[stat_key].catch_shoot_fg_m = float(catch_shoot_fg_m)

                    catch_shoot_fg_a  = data[next(itr)]
                    StatClass.tracking[stat_key].catch_shoot_fg_a = float(catch_shoot_fg_a)

                    catch_shoot_fg_pct  = data[next(itr)]
                    StatClass.tracking[stat_key].catch_shoot_fg_pct = float(catch_shoot_fg_pct)

                    catch_shoot_fg3_m = data[next(itr)]
                    StatClass.tracking[stat_key].catch_shoot_fg3_m = float(catch_shoot_fg3_m)

                    catch_shoot_fg3_a = data[next(itr)]
                    StatClass.tracking[stat_key].catch_shoot_fg3_a = float(catch_shoot_fg3_a)

                    catch_shoot_fg3_pct = data[next(itr)]
                    StatClass.tracking[stat_key].catch_shoot_fg3_pct = float(catch_shoot_fg3_pct)

                    catch_shoot_efg_pct = data[next(itr)]
                    StatClass.tracking[stat_key].catch_shoot_efg_pct = float(catch_shoot_efg_pct)

                elif stat_key == 'Passing':
                    passes_made              = data[next(itr)]
                    StatClass.tracking[stat_key].passes_made = float(passes_made)

                    passes_received          = data[next(itr)]
                    StatClass.tracking[stat_key].passes_received = float(passes_received)

                    ast                      = data[next(itr)]
                    StatClass.tracking[stat_key].ast = float(ast)

                    secondary_ast            = data[next(itr)]
                    StatClass.tracking[stat_key].secondary_ast = float(secondary_ast)

                    potential_ast            = data[next(itr)]
                    StatClass.tracking[stat_key].potential_ast = float(potential_ast)

                    ast_pts_created          = data[next(itr)]
                    StatClass.tracking[stat_key].ast_pts_created = float(ast_pts_created)

                    ast_adjusted             = data[next(itr)]
                    StatClass.tracking[stat_key].ast_adjusted = float(ast_adjusted)

                    ast_to_pass_pct          = data[next(itr)]
                    StatClass.tracking[stat_key].ast_to_pass_pct = float(ast_to_pass_pct)

                    ast_to_pass_pct_adjusted = data[next(itr)]
                    StatClass.tracking[stat_key].ast_to_pass_pct_adjusted = float(ast_to_pass_pct_adjusted)

                elif stat_key == 'Touches':
                    pts                   = data[next(itr)]
                    StatClass.tracking[stat_key].pts = float(pts)

                    touches               = data[next(itr)]
                    StatClass.tracking[stat_key].touches = float(touches)

                    front_cout_touches    = data[next(itr)]
                    StatClass.tracking[stat_key].front_cout_touches = float(front_cout_touches)

                    time_of_poss          = data[next(itr)]
                    StatClass.tracking[stat_key].time_of_poss = float(time_of_poss)

                    avg_sec_per_touch     = data[next(itr)]
                    StatClass.tracking[stat_key].avg_sec_per_touch = float(avg_sec_per_touch)

                    avg_dribble_per_touch = data[next(itr)]
                    StatClass.tracking[stat_key].avg_dribble_per_touch = float(avg_dribble_per_touch)

                    pts_per_touch         = data[next(itr)]
                    StatClass.tracking[stat_key].pts_per_touch = float(pts_per_touch)

                    elbow_touches         = data[next(itr)]
                    StatClass.tracking[stat_key].elbow_touches = float(elbow_touches)

                    post_touches          = data[next(itr)]
                    StatClass.tracking[stat_key].post_touches = float(post_touches)

                    paint_touches         = data[next(itr)]
                    StatClass.tracking[stat_key].paint_touches = float(paint_touches)

                    pts_per_elbow_touch   = data[next(itr)]
                    StatClass.tracking[stat_key].pts_per_elbow_touch = float(pts_per_elbow_touch)

                    pts_per_post_touch    = data[next(itr)]
                    StatClass.tracking[stat_key].pts_per_post_touch = float(pts_per_post_touch)

                    pts_per_paint_touch   = data[next(itr)]
                    StatClass.tracking[stat_key].pts_per_paint_touch = float(pts_per_paint_touch)

                elif stat_key == 'Pull-Up':
                    pull_up_shooting_pts     = data[next(itr)]
                    StatClass.tracking[stat_key].pull_up_shooting_pts = float(pull_up_shooting_pts)

                    pull_up_shooting_fg_m    = data[next(itr)]
                    StatClass.tracking[stat_key].pull_up_shooting_fg_m = float(pull_up_shooting_fg_m)

                    pull_up_shooting_fg_a    = data[next(itr)]
                    StatClass.tracking[stat_key].pull_up_shooting_fg_a = float(pull_up_shooting_fg_a)

                    pull_up_shooting_fg_pct  = data[next(itr)]
                    StatClass.tracking[stat_key].pull_up_shooting_fg_pct = float(pull_up_shooting_fg_pct)

                    pull_up_shooting_fg3_m   = data[next(itr)]
                    StatClass.tracking[stat_key].pull_up_shooting_fg3_m = float(pull_up_shooting_fg3_m)

                    pull_up_shooting_fg3_a   = data[next(itr)]
                    StatClass.tracking[stat_key].pull_up_shooting_fg3_a = float(pull_up_shooting_fg3_a)

                    pull_up_shooting_fg3_pct = data[next(itr)]
                    StatClass.tracking[stat_key].pull_up_shooting_fg3_pct = float(pull_up_shooting_fg3_pct)

                    pull_up_shooting_efg_pct = data[next(itr)]
                    StatClass.tracking[stat_key].pull_up_shooting_efg_pct = float(pull_up_shooting_efg_pct)

                elif stat_key == 'Rebounding':
                    rebs                 = data[next(itr)]
                    StatClass.tracking[stat_key].rebs = float(rebs)

                    contested_rebs       = data[next(itr)]
                    StatClass.tracking[stat_key].contested_rebs = float(contested_rebs)

                    contested_rebs_pct   = data[next(itr)]
                    StatClass.tracking[stat_key].contested_rebs_pct = float(contested_rebs_pct)

                    reb_chances          = data[next(itr)]
                    StatClass.tracking[stat_key].reb_chances = float(reb_chances)

                    reb_chances_pct      = data[next(itr)]
                    StatClass.tracking[stat_key].reb_chances_pct = float(reb_chances_pct)

                    deferred_reb_chances = data[next(itr)]
                    StatClass.tracking[stat_key].deferred_reb_chances = float(deferred_reb_chances)

                    adj_reb_chance_pct   = data[next(itr)]
                    StatClass.tracking[stat_key].adj_reb_chance_pct = float(adj_reb_chance_pct)

                    if player is not None:
                        avg_reb_dist     = data[next(itr)]
                        StatClass.tracking[stat_key].avg_reb_dist = float(avg_reb_dist)

                elif stat_key == 'Offensive Rebounding':
                    orebs                 = data[next(itr)]
                    StatClass.tracking[stat_key].orebs = float(orebs)

                    contested_orebs       = data[next(itr)]
                    StatClass.tracking[stat_key].contested_orebs = float(contested_orebs)

                    contested_orebs_pct   = data[next(itr)]
                    StatClass.tracking[stat_key].contested_orebs_pct = float(contested_orebs_pct)

                    oreb_chances          = data[next(itr)]
                    StatClass.tracking[stat_key].oreb_chances = float(oreb_chances)

                    oreb_chances_pct      = data[next(itr)]
                    StatClass.tracking[stat_key].oreb_chances_pct = float(oreb_chances_pct)

                    deferred_oreb_chances = data[next(itr)]
                    StatClass.tracking[stat_key].deferred_oreb_chances = float(deferred_oreb_chances)

                    adj_oreb_chance_pct   = data[next(itr)]
                    StatClass.tracking[stat_key].adj_oreb_chance_pct = float(adj_oreb_chance_pct)

                    if player:
                        avg_oreb_dist     = data[next(itr)]
                        StatClass.tracking[stat_key].avg_oreb_dist = float(avg_oreb_dist)

                elif stat_key == 'Defensive Rebounding':
                    drebs                 = data[next(itr)]
                    StatClass.tracking[stat_key].drebs = float(drebs)

                    contested_drebs       = data[next(itr)]
                    StatClass.tracking[stat_key].contested_drebs = float(contested_drebs)

                    contested_drebs_pct   = data[next(itr)]
                    StatClass.tracking[stat_key].contested_drebs_pct = float(contested_drebs_pct)

                    dreb_chances          = data[next(itr)]
                    StatClass.tracking[stat_key].dreb_chances = float(dreb_chances)

                    dreb_chances_pct      = data[next(itr)]
                    StatClass.tracking[stat_key].dreb_chances_pct = float(dreb_chances_pct)

                    deferred_dreb_chances = data[next(itr)]
                    StatClass.tracking[stat_key].deferred_dreb_chances = float(deferred_dreb_chances)

                    adj_dreb_chance_pct   = data[next(itr)]
                    StatClass.tracking[stat_key].adj_dreb_chance_pct = float(adj_dreb_chance_pct)

                    if player is not None:
                        avg_dreb_dist     = data[next(itr)]
                        StatClass.tracking[stat_key].avg_dreb_dist = float(avg_dreb_dist)

                elif stat_key == 'Shooting Efficiency':
                    pts                     = data[next(itr)]
                    StatClass.tracking[stat_key].pts = float(pts)

                    drive_pts               = data[next(itr)]
                    StatClass.tracking[stat_key].drive_pts = float(drive_pts)

                    drive_fg_pct            = data[next(itr)]
                    StatClass.tracking[stat_key].drive_fg_pct = float(drive_fg_pct)

                    catch_shoot_pts         = data[next(itr)]
                    StatClass.tracking[stat_key].catch_shoot_pts = float(catch_shoot_pts)

                    catch_shoot_fg_pct      = data[next(itr)]
                    StatClass.tracking[stat_key].catch_shoot_fg_pct = float(catch_shoot_fg_pct)

                    pull_up_shooting_pts    = data[next(itr)]
                    StatClass.tracking[stat_key].pull_up_shooting_pts = float(pull_up_shooting_pts)

                    pull_up_shooting_fg_pct = data[next(itr)]
                    StatClass.tracking[stat_key].pull_up_shooting_fg_pct = float(pull_up_shooting_fg_pct)

                    paint_touch_pts         = data[next(itr)]
                    StatClass.tracking[stat_key].paint_touch_pts = float(paint_touch_pts)

                    paint_touch_fg_pct      = data[next(itr)]
                    StatClass.tracking[stat_key].paint_touch_fg_pct = float(paint_touch_fg_pct)

                    post_touch_pts          = data[next(itr)]
                    StatClass.tracking[stat_key].post_touch_pts = float(post_touch_pts)

                    post_touch_fg_pct       = data[next(itr)]
                    StatClass.tracking[stat_key].post_touch_fg_pct = float(post_touch_fg_pct)

                    elbow_touch_pts         = data[next(itr)]
                    StatClass.tracking[stat_key].elbow_touch_pts = float(elbow_touch_pts)

                    elbow_touch_fg_pct      = data[next(itr)]
                    StatClass.tracking[stat_key].elbow_touch_fg_pct = float(elbow_touch_fg_pct)

                    efg_pct                 = data[next(itr)]
                    StatClass.tracking[stat_key].efg_pct = float(efg_pct)

                elif stat_key == 'Speed-Distance':
                    dist_feet      = data[next(itr)]
                    StatClass.tracking[stat_key].dist_feet = float(dist_feet)

                    dist_miles     = data[next(itr)]
                    StatClass.tracking[stat_key].dist_miles = float(dist_miles)

                    dist_miles_off = data[next(itr)]
                    StatClass.tracking[stat_key].dist_miles_off = float(dist_miles_off)

                    dist_miles_def = data[next(itr)]
                    StatClass.tracking[stat_key].dist_miles_def = float(dist_miles_def)

                    avg_speed      = data[next(itr)]
                    StatClass.tracking[stat_key].avg_speed = float(avg_speed)

                    avg_speed_off  = data[next(itr)]
                    StatClass.tracking[stat_key].avg_speed_off = float(avg_speed_off)

                    avg_speed_def  = data[next(itr)]
                    StatClass.tracking[stat_key].avg_speed_def = float(avg_speed_def)

                elif stat_key == 'Elbow Touch':
                    touches                = data[next(itr)]
                    StatClass.tracking[stat_key].touches = float(touches)

                    elbow_touches          = data[next(itr)]
                    StatClass.tracking[stat_key].elbow_touches = float(elbow_touches)

                    elbow_touch_fg_m       = data[next(itr)]
                    StatClass.tracking[stat_key].elbow_touch_fg_m = float(elbow_touch_fg_m)

                    elbow_touch_fg_a       = data[next(itr)]
                    StatClass.tracking[stat_key].elbow_touch_fg_a = float(elbow_touch_fg_a)

                    elbow_touch_fg_pct     = data[next(itr)]
                    StatClass.tracking[stat_key].elbow_touch_fg_pct = float(elbow_touch_fg_pct)

                    elbow_touch_ft_m       = data[next(itr)]
                    StatClass.tracking[stat_key].elbow_touch_ft_m = float(elbow_touch_ft_m)

                    elbow_touch_ft_a       = data[next(itr)]
                    StatClass.tracking[stat_key].elbow_touch_ft_a = float(elbow_touch_ft_a)

                    elbow_touch_ft_pct     = data[next(itr)]
                    StatClass.tracking[stat_key].elbow_touch_ft_pct = float(elbow_touch_ft_pct)

                    elbow_touch_pts        = data[next(itr)]
                    StatClass.tracking[stat_key].elbow_touch_pts = float(elbow_touch_pts)

                    elbow_touch_pct_pts    = data[next(itr)]
                    StatClass.tracking[stat_key].elbow_touch_pct_pts = float(elbow_touch_pct_pts)

                    elbow_touch_passes     = data[next(itr)]
                    StatClass.tracking[stat_key].elbow_touch_passes = float(elbow_touch_passes)

                    elbow_touch_pct_passes = data[next(itr)]
                    StatClass.tracking[stat_key].elbow_touch_pct_passes = float(elbow_touch_pct_passes)

                    elbow_touch_ast        = data[next(itr)]
                    StatClass.tracking[stat_key].elbow_touch_ast = float(elbow_touch_ast)

                    elbow_touch_pct_ast    = data[next(itr)]
                    StatClass.tracking[stat_key].elbow_touch_pct_ast = float(elbow_touch_pct_ast)

                    elbow_touch_tov        = data[next(itr)]
                    StatClass.tracking[stat_key].elbow_touch_tov = float(elbow_touch_tov)

                    elbow_touch_pct_tov    = data[next(itr)]
                    StatClass.tracking[stat_key].elbow_touch_pct_tov = float(elbow_touch_pct_tov)

                    elbow_touch_pf         = data[next(itr)]
                    StatClass.tracking[stat_key].elbow_touch_pf = float(elbow_touch_pf)

                    elbow_touch_pct_pf     = data[next(itr)]
                    StatClass.tracking[stat_key].elbow_touch_pct_pf = float(elbow_touch_pct_pf)

                elif stat_key == 'Post Ups':
                    touches                 = data[next(itr)]
                    StatClass.tracking[stat_key].touches = float(touches)

                    post_up_touches          = data[next(itr)]
                    StatClass.tracking[stat_key].post_up_touches = float(post_up_touches)

                    post_up_touch_fg_m       = data[next(itr)]
                    StatClass.tracking[stat_key].post_up_touch_fg_m = float(post_up_touch_fg_m)

                    post_up_touch_fg_a       = data[next(itr)]
                    StatClass.tracking[stat_key].post_up_touch_fg_a = float(post_up_touch_fg_a)

                    post_up_touch_fg_pct     = data[next(itr)]
                    StatClass.tracking[stat_key].post_up_touch_fg_pct = float(post_up_touch_fg_pct)

                    post_up_touch_ft_m       = data[next(itr)]
                    StatClass.tracking[stat_key].post_up_touch_ft_m = float(post_up_touch_ft_m)

                    post_up_touch_ft_a       = data[next(itr)]
                    StatClass.tracking[stat_key].post_up_touch_ft_a = float(post_up_touch_ft_a)

                    post_up_touch_ft_pct     = data[next(itr)]
                    StatClass.tracking[stat_key].post_up_touch_ft_pct = float(post_up_touch_ft_pct)

                    post_up_touch_pts        = data[next(itr)]
                    StatClass.tracking[stat_key].post_up_touch_pts = float(post_up_touch_pts)

                    post_up_touch_pct_pts    = data[next(itr)]
                    StatClass.tracking[stat_key].post_up_touch_pct_pts = float(post_up_touch_pct_pts)

                    post_up_touch_passes     = data[next(itr)]
                    StatClass.tracking[stat_key].post_up_touch_passes = float(post_up_touch_passes)

                    post_up_touch_pct_passes = data[next(itr)]
                    StatClass.tracking[stat_key].post_up_touch_pct_passes = float(post_up_touch_pct_passes)

                    post_up_touch_ast        = data[next(itr)]
                    StatClass.tracking[stat_key].post_up_touch_ast = float(post_up_touch_ast)

                    post_up_touch_pct_ast    = data[next(itr)]
                    StatClass.tracking[stat_key].post_up_touch_pct_ast = float(post_up_touch_pct_ast)

                    post_up_touch_tov        = data[next(itr)]
                    StatClass.tracking[stat_key].post_up_touch_tov = float(post_up_touch_tov)

                    post_up_touch_pct_tov    = data[next(itr)]
                    StatClass.tracking[stat_key].post_up_touch_pct_tov = float(post_up_touch_pct_tov)

                    post_up_touch_pf         = data[next(itr)]
                    StatClass.tracking[stat_key].post_up_touch_pf = float(post_up_touch_pf)

                    post_up_touch_pct_pf     = data[next(itr)]
                    StatClass.tracking[stat_key].post_up_touch_pct_pf = float(post_up_touch_pct_pf)

                elif stat_key == 'Paint Touches':
                    touches                = data[next(itr)]
                    StatClass.tracking[stat_key].touches = float(touches)

                    paint_touches          = data[next(itr)]
                    StatClass.tracking[stat_key].paint_touches = float(paint_touches)

                    paint_touch_fg_m       = data[next(itr)]
                    StatClass.tracking[stat_key].paint_touch_fg_m = float(paint_touch_fg_m)

                    paint_touch_fg_a       = data[next(itr)]
                    StatClass.tracking[stat_key].paint_touch_fg_a = float(paint_touch_fg_a)

                    paint_touch_fg_pct     = data[next(itr)]
                    StatClass.tracking[stat_key].paint_touch_fg_pct = float(paint_touch_fg_pct)

                    paint_touch_ft_m       = data[next(itr)]
                    StatClass.tracking[stat_key].paint_touch_ft_m = float(paint_touch_ft_m)

                    paint_touch_ft_a       = data[next(itr)]
                    StatClass.tracking[stat_key].paint_touch_ft_a = float(paint_touch_ft_a)

                    paint_touch_ft_pct     = data[next(itr)]
                    StatClass.tracking[stat_key].paint_touch_ft_pct = float(paint_touch_ft_pct)

                    paint_touch_pts        = data[next(itr)]
                    StatClass.tracking[stat_key].paint_touch_pts = float(paint_touch_pts)

                    paint_touch_pct_pts    = data[next(itr)]
                    StatClass.tracking[stat_key].paint_touch_pct_pts = float(paint_touch_pct_pts)

                    paint_touch_passes     = data[next(itr)]
                    StatClass.tracking[stat_key].paint_touch_passes = float(paint_touch_passes)

                    paint_touch_pct_passes = data[next(itr)]
                    StatClass.tracking[stat_key].paint_touch_pct_passes = float(paint_touch_pct_passes)

                    paint_touch_ast        = data[next(itr)]
                    StatClass.tracking[stat_key].paint_touch_ast = float(paint_touch_ast)

                    paint_touch_pct_ast    = data[next(itr)]
                    StatClass.tracking[stat_key].paint_touch_pct_ast = float(paint_touch_pct_ast)

                    paint_touch_tov        = data[next(itr)]
                    StatClass.tracking[stat_key].paint_touch_tov = float(paint_touch_tov)

                    paint_touch_pct_tov    = data[next(itr)]
                    StatClass.tracking[stat_key].paint_touch_pct_tov = float(paint_touch_pct_tov)

                    paint_touch_pf         = data[next(itr)]
                    StatClass.tracking[stat_key].paint_touch_pf = float(paint_touch_pf)

                    paint_touch_pct_pf     = data[next(itr)]
                    StatClass.tracking[stat_key].paint_touch_pct_pf = float(paint_touch_pct_pf)

            index += 1
