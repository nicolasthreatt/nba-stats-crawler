
import itertools
from utils.headers import getStatColumnType
from players.tables.player import Player
from teams.tables.team import Team
from utils.types import TableType


def parse(table: str, stat_type: str, player: Player = None, teams: dict = None):
    """Parses the clutch stats table and stores the data in the player/team object

    Args:
        table (str): nba.com/stats table containing the stats
        stat_type (str): type of stat being parsed
        player (Player): player object to store the stats
        teams (Team): team object to store the stats
    """

    # Get correct table type
    table_type = TableType.PLAYER.name if player else TableType.TEAM.name
    table_header_row, table_column_offset = getStatColumnType('Clutch ' + stat_type, table_type)

    # Parse statistic table
    index = 1
    for row, info in enumerate(table.split('\n')):

        # Throwaway junk lines (column names)
        if row > table_header_row:

            # Get Correct Player/Team
            if (index % 2) == 1:

                if player:
                    name = info.title()
                    player.name = name
                    StatClass = player.clutch

                elif teams:
                    team = info.upper()

                    StatClass = teams[team].clutch

            # Extract stats
            elif (index % 2) == 0:

                # Create iterator
                itr = itertools.count(table_column_offset)
                
                # Split info from table into a list
                data  = info.split(' ')

                if stat_type == 'Traditional':
                    clutch_games     = data[next(itr)]
                    StatClass.clutch_games = int(clutch_games)

                    clutch_wins      = data[next(itr)]
                    StatClass.clutch_wins = int(clutch_wins)

                    clutch_losses    = data[next(itr)]
                    StatClass.clutch_losses = int(clutch_losses)

                    if teams:
                        clutch_win_pct    = data[next(itr)]
                        StatClass.clutch_win_pct = float(clutch_win_pct)

                    clutch_mins      = data[next(itr)]
                    StatClass.clutch_mins = float(clutch_mins)

                    clutch_pts       = data[next(itr)]
                    StatClass[stat_type].clutch_pts = float(clutch_pts)

                    clutch_fg_m      = data[next(itr)]
                    StatClass[stat_type].clutch_fg_m = float(clutch_fg_m)

                    clutch_fg_a      = data[next(itr)]
                    StatClass[stat_type].clutch_fg_a = float(clutch_fg_a)

                    clutch_fg_pct    = data[next(itr)]
                    StatClass[stat_type].clutch_fg_pct = float(clutch_fg_pct)

                    clutch_fg3_m     = data[next(itr)]
                    StatClass[stat_type].clutch_fg3_m = float(clutch_fg3_m)

                    clutch_fg3_a     = data[next(itr)]
                    StatClass[stat_type].clutch_fg3_a = float(clutch_fg3_a)

                    clutch_fg3_pct   = data[next(itr)]
                    StatClass[stat_type].clutch_fg3_pct = float(clutch_fg3_pct)

                    clutch_ft_m      = data[next(itr)]
                    StatClass[stat_type].clutch_ft_m = float(clutch_ft_m)

                    clutch_ft_a      = data[next(itr)]
                    StatClass[stat_type].clutch_ft_a = float(clutch_ft_a)

                    clutch_ft_pct    = data[next(itr)]
                    StatClass[stat_type].clutch_ft_pct = float(clutch_ft_pct)

                    clutch_oreb      = data[next(itr)]
                    StatClass[stat_type].clutch_oreb = float(clutch_oreb)

                    clutch_dreb      = data[next(itr)]
                    StatClass[stat_type].clutch_dreb = float(clutch_dreb)

                    clutch_treb      = data[next(itr)]
                    StatClass[stat_type].clutch_treb = float(clutch_treb)

                    clutch_ast       = data[next(itr)]
                    StatClass[stat_type].clutch_ast = float(clutch_ast)

                    clutch_tov       = data[next(itr)]
                    StatClass[stat_type].clutch_tov = float(clutch_tov)

                    clutch_stl       = data[next(itr)]
                    StatClass[stat_type].clutch_stl = float(clutch_stl)

                    clutch_blk       = data[next(itr)]
                    StatClass[stat_type].clutch_blk = float(clutch_blk)

                    if teams:
                        clutch_blk_a = data[next(itr)]
                        StatClass[stat_type].clutch_blk = float(clutch_blk_a)

                    clutch_fouls_c   = data[next(itr)]
                    StatClass[stat_type].clutch_fouls_c = float(clutch_fouls_c)

                    if player:
                        clutch_fp    = data[next(itr)]
                        StatClass[stat_type].clutch_fp = float(clutch_fp)

                    if teams:
                        clutch_fouls_d = data[next(itr)]
                        StatClass[stat_type].clutch_fouls_d = float(clutch_fouls_d)

                    if player:
                        clutch_plusminus = data[next(itr) + 2]  # Skip DD and TD Columns for Player

                    if teams:
                        clutch_plusminus = data[next(itr)]

                    StatClass[stat_type].clutch_plusminus = float(clutch_plusminus)

                elif stat_type == 'Advanced':
                    clutch_orating       = data[next(itr)]
                    StatClass[stat_type].clutch_orating = float(clutch_orating)

                    clutch_drating       = data[next(itr)]
                    StatClass[stat_type].clutch_drating = float(clutch_drating)

                    clutch_netrating     = data[next(itr)]
                    StatClass[stat_type].clutch_netrating = float(clutch_netrating)

                    clutch_ast_pct       = data[next(itr)]
                    StatClass[stat_type].clutch_ast_pct = float(clutch_ast_pct)

                    clutch_ast_tov_ratio = data[next(itr)]
                    StatClass[stat_type].clutch_ast_tov_ratio = float(clutch_ast_tov_ratio)

                    clutch_ast_ratio     = data[next(itr)]
                    StatClass[stat_type].clutch_ast_ratio = float(clutch_ast_ratio)

                    clutch_oreb_pct      = data[next(itr)]
                    StatClass[stat_type].clutch_oreb_pct = float(clutch_oreb_pct)

                    clutch_dreb_pct      = data[next(itr)]
                    StatClass[stat_type].clutch_dreb_pct = float(clutch_dreb_pct)

                    clutch_reb_pct       = data[next(itr)]
                    StatClass[stat_type].clutch_reb_pct = float(clutch_reb_pct)

                    clutch_tov_ratio     = data[next(itr)]
                    StatClass[stat_type].clutch_tov_ratio = float(clutch_tov_ratio)

                    clutch_efg_pct       = data[next(itr)]
                    StatClass[stat_type].clutch_efg_pct = float(clutch_efg_pct)

                    clutch_ts_pct        = data[next(itr)]
                    StatClass[stat_type].clutch_ts_pct = float(clutch_ts_pct)

                    if player:
                        clutch_usage     = data[next(itr)]
                        StatClass[stat_type].clutch_usage = float(clutch_usage)

                    clutch_pace          = data[next(itr)]
                    StatClass[stat_type].clutch_pace = float(clutch_pace)

                    clutch_pie           = data[next(itr)]
                    StatClass[stat_type].clutch_pie = float(clutch_pie)

                elif stat_type == 'Misc':
                    clutch_pts_off_tov        = data[next(itr)]
                    StatClass[stat_type].clutch_pts_off_tov = float(clutch_pts_off_tov)

                    clutch_pts_2nd_chance     = data[next(itr)]
                    StatClass[stat_type].clutch_pts_2nd_chance = float(clutch_pts_2nd_chance)

                    clutch_pts_fastbreak      = data[next(itr)]
                    StatClass[stat_type].clutch_pts_fastbreak = float(clutch_pts_fastbreak)

                    clutch_pts_in_paint       = data[next(itr)]
                    StatClass[stat_type].clutch_pts_in_paint = float(clutch_pts_in_paint)

                    clutch_opp_pts_off_tov    = data[next(itr)]
                    StatClass[stat_type].clutch_opp_pts_off_tov = float(clutch_opp_pts_off_tov)

                    clutch_opp_2nd_chance_pts = data[next(itr)]
                    StatClass[stat_type].clutch_opp_2nd_chance_pts = float(clutch_opp_2nd_chance_pts)

                    clutch_opp_fastbreak_pts  = data[next(itr)]
                    StatClass[stat_type].clutch_opp_fastbreak_pts = float(clutch_opp_fastbreak_pts)

                    clutch_opp_pts_in_paint   = data[next(itr)]
                    StatClass[stat_type].clutch_opp_pts_in_paint = float(clutch_opp_pts_in_paint)

                    if player:
                        clutch_blk            = data[next(itr)]
                        StatClass[stat_type].clutch_blk = float(clutch_blk)

                        clutch_blk_a          = data[next(itr)]
                        StatClass[stat_type].clutch_blk_a = float(clutch_blk_a)

                        clutch_fouls_c        = data[next(itr)]
                        StatClass[stat_type].clutch_fouls_c = float(clutch_fouls_c)

                        clutch_fouls_d        = data[next(itr)]
                        StatClass[stat_type].clutch_fouls_d = float(clutch_fouls_d)

                elif stat_type == 'Scoring':
                    clutch_pct_fga_2pt       = data[next(itr)]
                    StatClass[stat_type].clutch_pct_fga_2pt = float(clutch_pct_fga_2pt)

                    clutch_pct_fga_3pt       = data[next(itr)]
                    StatClass[stat_type].clutch_pct_fga_3pt = float(clutch_pct_fga_3pt)

                    clutch_pct_pts_2pt       = data[next(itr)]
                    StatClass[stat_type].clutch_pct_pts_2pt = float(clutch_pct_pts_2pt)

                    clutch_pct_pts_mid       = data[next(itr)]
                    StatClass[stat_type].clutch_pct_pts_mid = float(clutch_pct_pts_mid)

                    clutch_pct_pts_3pt       = data[next(itr)]
                    StatClass[stat_type].clutch_pct_pts_3pt = float(clutch_pct_pts_3pt)

                    clutch_pct_pts_fb        = data[next(itr)]
                    StatClass[stat_type].clutch_pct_pts_fb = float(clutch_pct_pts_fb)

                    clutch_pct_pts_ft        = data[next(itr)]
                    StatClass[stat_type].clutch_pct_pts_ft = float(clutch_pct_pts_ft)

                    clutch_pct_pts_off_tov   = data[next(itr)]
                    StatClass[stat_type].clutch_pct_pts_off_tov = float(clutch_pct_pts_off_tov)

                    clutch_pct_pts_in_paint  = data[next(itr)]
                    StatClass[stat_type].clutch_pct_pts_in_paint = float(clutch_pct_pts_in_paint)

                    clutch_pct_pts_2pts_ast  = data[next(itr)]
                    StatClass[stat_type].clutch_pct_pts_2pts_ast = float(clutch_pct_pts_2pts_ast)

                    clutch_pct_pts_2pts_uast = data[next(itr)]
                    StatClass[stat_type].clutch_pct_pts_2pts_uast = float(clutch_pct_pts_2pts_uast)

                    clutch_pct_pts_3pts_ast  = data[next(itr)]
                    StatClass[stat_type].clutch_pct_pts_3pts_ast = float(clutch_pct_pts_3pts_ast)

                    clutch_pct_pts_3pts_uast = data[next(itr)]
                    StatClass[stat_type].clutch_pct_pts_3pts_uast = float(clutch_pct_pts_3pts_uast)

                    clutch_pct_pts_fgm_ast   = data[next(itr)]
                    StatClass[stat_type].clutch_pct_pts_fgm_ast = float(clutch_pct_pts_fgm_ast)

                    clutch_pct_pts_fgm_uast  = data[next(itr)]
                    StatClass[stat_type].clutch_pct_pts_fgm_uast = float(clutch_pct_pts_fgm_uast)

                elif stat_type == 'Usage':
                    clutch_pct_usage         = data[next(itr)]
                    StatClass[stat_type].clutch_pct_usage = float(clutch_pct_usage)

                    clutch_pct_of_team_fg_m  = data[next(itr)]
                    StatClass[stat_type].clutch_pct_of_team_fg_m = float(clutch_pct_of_team_fg_m)

                    clutch_pct_of_team_fg_a  = data[next(itr)]
                    StatClass[stat_type].clutch_pct_of_team_fg_a = float(clutch_pct_of_team_fg_a)

                    clutch_pct_of_team_fg3_m = data[next(itr)]
                    StatClass[stat_type].clutch_pct_of_team_fg3_m = float(clutch_pct_of_team_fg3_m)

                    clutch_pct_of_team_fg3_a = data[next(itr)]
                    StatClass[stat_type].clutch_pct_of_team_fg3_a = float(clutch_pct_of_team_fg3_a)

                    clutch_pct_of_team_ft_m  = data[next(itr)]
                    StatClass[stat_type].clutch_pct_of_team_ft_m = float(clutch_pct_of_team_ft_m)

                    clutch_pct_of_team_ft_a  = data[next(itr)]
                    StatClass[stat_type].clutch_pct_of_team_ft_a = float(clutch_pct_of_team_ft_a)

                    clutch_pct_of_team_oreb  = data[next(itr)]
                    StatClass[stat_type].clutch_pct_of_team_oreb = float(clutch_pct_of_team_oreb)

                    clutch_pct_of_team_dreb  = data[next(itr)]
                    StatClass[stat_type].clutch_pct_of_team_dreb = float(clutch_pct_of_team_dreb)

                    clutch_pct_of_team_treb  = data[next(itr)]
                    StatClass[stat_type].clutch_pct_of_team_treb = float(clutch_pct_of_team_treb)

                    clutch_pct_of_team_ast   = data[next(itr)]
                    StatClass[stat_type].clutch_pct_of_team_ast = float(clutch_pct_of_team_ast)

                    clutch_pct_of_team_tov   = data[next(itr)]
                    StatClass[stat_type].clutch_pct_of_team_tov = float(clutch_pct_of_team_tov)

                    clutch_pct_of_team_stl   = data[next(itr)]
                    StatClass[stat_type].clutch_pct_of_team_stl = float(clutch_pct_of_team_stl)

                    clutch_pct_of_team_blk   = data[next(itr)]
                    StatClass[stat_type].clutch_pct_of_team_blk = float(clutch_pct_of_team_blk)

                    clutch_pct_of_team_blk_a = data[next(itr)]
                    StatClass[stat_type].clutch_pct_of_team_blk_a = float(clutch_pct_of_team_blk_a)

                    clutch_pct_of_team_pf_c  = data[next(itr)]
                    StatClass[stat_type].clutch_pct_of_team_pf_c = float(clutch_pct_of_team_pf_c)

                    clutch_pct_of_team_pf_d  = data[next(itr)]
                    StatClass[stat_type].clutch_pct_of_team_pf_d = float(clutch_pct_of_team_pf_d)

                    clutch_pct_of_team_pts   = data[next(itr)]
                    StatClass[stat_type].clutch_pct_of_team_pts = float(clutch_pct_of_team_pts)

                elif stat_type == 'Four Factors':
                    clutch_efg_pct      = data[next(itr)]
                    StatClass[stat_type].clutch_efg_pct = float(clutch_efg_pct)

                    clutch_fta_rate     = data[next(itr)]
                    StatClass[stat_type].clutch_fta_rate = float(clutch_fta_rate)

                    clutch_tov_pct      = data[next(itr)]
                    StatClass[stat_type].clutch_tov_pct = float(clutch_tov_pct)

                    clutch_oreb_pct     = data[next(itr)]
                    StatClass[stat_type].clutch_oreb_pct = float(clutch_oreb_pct)

                    clutch_opp_efg_pct  = data[next(itr)]
                    StatClass[stat_type].clutch_opp_efg_pct = float(clutch_opp_efg_pct)

                    clutch_opp_fta_rate = data[next(itr)]
                    StatClass[stat_type].clutch_opp_fta_rate = float(clutch_opp_fta_rate)

                    clutch_opp_tov_pct  = data[next(itr)]
                    StatClass[stat_type].clutch_opp_tov_pct = float(clutch_opp_tov_pct)

                    clutch_opp_oreb_pct = data[next(itr)]
                    StatClass[stat_type].clutch_opp_oreb_pct = float(clutch_opp_oreb_pct)

                elif stat_type == 'Opponent':
                    clutch_opp_fg_m      = data[next(itr)]
                    StatClass[stat_type].clutch_opp_fg_m = float(clutch_opp_fg_m)

                    clutch_opp_fg_a      = data[next(itr)]
                    StatClass[stat_type].clutch_opp_fg_a = float(clutch_opp_fg_a)

                    clutch_opp_fg_pct    = data[next(itr)]
                    StatClass[stat_type].clutch_opp_fg_pct = float(clutch_opp_fg_pct)

                    clutch_opp_fg3_a     = data[next(itr)]
                    StatClass[stat_type].clutch_opp_fg3_a = float(clutch_opp_fg3_a)

                    clutch_opp_fg3_pct   = data[next(itr)]
                    StatClass[stat_type].clutch_opp_fg3_pct = float(clutch_opp_fg3_pct)

                    clutch_opp_ft_m      = data[next(itr)]
                    StatClass[stat_type].clutch_opp_ft_m = float(clutch_opp_ft_m)

                    clutch_opp_ft_a      = data[next(itr)]
                    StatClass[stat_type].clutch_opp_ft_a = float(clutch_opp_ft_a)

                    clutch_opp_ft_pct    = data[next(itr)]
                    StatClass[stat_type].clutch_opp_ft_pct = float(clutch_opp_ft_pct)

                    clutch_opp_oreb      = data[next(itr)]
                    StatClass[stat_type].clutch_opp_oreb = float(clutch_opp_oreb)

                    clutch_opp_dreb      = data[next(itr)]
                    StatClass[stat_type].clutch_opp_dreb = float(clutch_opp_dreb)

                    clutch_opp_treb      = data[next(itr)]
                    StatClass[stat_type].clutch_opp_treb = float(clutch_opp_treb)

                    clutch_opp_ast       = data[next(itr)]
                    StatClass[stat_type].clutch_opp_ast = float(clutch_opp_ast)

                    clutch_opp_tov       = data[next(itr)]
                    StatClass[stat_type].clutch_opp_tov = float(clutch_opp_tov)

                    clutch_opp_stl       = data[next(itr)]
                    StatClass[stat_type].clutch_opp_stl = float(clutch_opp_stl)

                    clutch_opp_blk       = data[next(itr)]
                    StatClass[stat_type].clutch_opp_blk = float(clutch_opp_blk)

                    clutch_opp_blk_a     = data[next(itr)]
                    StatClass[stat_type].clutch_opp_blk_a = float(clutch_opp_blk_a)

                    clutch_opp_pf        = data[next(itr)]
                    StatClass[stat_type].clutch_opp_pf = float(clutch_opp_pf)

                    clutch_opp_pf_d      = data[next(itr)]
                    StatClass[stat_type].clutch_opp_pf_d = float(clutch_opp_pf_d)

                    clutch_opp_pts       = data[next(itr)]
                    StatClass[stat_type].clutch_opp_pts = float(clutch_opp_pts)

                    clutch_opp_plusminus = data[next(itr)]
                    StatClass[stat_type].clutch_opp_plusminus = float(clutch_opp_plusminus)

            index += 1
