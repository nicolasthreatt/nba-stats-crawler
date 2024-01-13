import itertools
from players.tables.player import Player
from utils.headers import getStatColumnType
from utils.types import TableType

# Get Shooting Stats
def parse(table: str, stat_type: str, player: Player = None, teams: dict = None):

    table_type = TableType.PLAYER.name if player else TableType.TEAM.name
    (table_header_row, table_column_offset) = getStatColumnType('Shooting ' + stat_type, table_type)

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
                    ShootingClass = player

                elif teams:
                    team = info.upper()
                    ShootingClass = teams[team]

            # Extract stats
            elif (index % 2) == 0:

                # Create iterator
                itr = itertools.count(table_column_offset)

                # Split info from table into a list
                data = info.split(' ')
                data = [stat.replace("-", "0") for stat in data]

                if stat_type == '5ft Range':
                    fg_m_lt_5ft         = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_m_lt_5ft = float(fg_m_lt_5ft)

                    fg_a_lt_5ft         = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_a_lt_5ft = float(fg_a_lt_5ft)

                    fg_pct_lt_5ft       = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_pct_lt_5ft = float(fg_pct_lt_5ft)

                    fg_m_5ft_to_9ft     = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_m_5ft_to_9ft = float(fg_m_5ft_to_9ft)

                    fg_a_5ft_to_9ft     = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_a_5ft_to_9ft = float(fg_a_5ft_to_9ft)

                    fg_pct_5ft_to_9ft   = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_pct_5ft_to_9ft = float(fg_pct_5ft_to_9ft)

                    fg_m_10ft_to_14ft   = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_m_10ft_to_14ft = float(fg_m_10ft_to_14ft)

                    fg_a_10ft_to_14ft   = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_a_10ft_to_14ft = float(fg_a_10ft_to_14ft)

                    fg_pct_10ft_to_14ft = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_pct_10ft_to_14ft = float(fg_pct_10ft_to_14ft)

                    fg_m_15ft_to_19ft   = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_m_15ft_to_19ft = float(fg_m_15ft_to_19ft)

                    fg_a_15ft_to_19ft   = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_a_15ft_to_19ft = float(fg_a_15ft_to_19ft)

                    fg_pct_15ft_to_19ft = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_pct_15ft_to_19ft = float(fg_pct_15ft_to_19ft)

                    fg_m_20ft_to_24ft   = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_m_20ft_to_24ft = float(fg_m_20ft_to_24ft)

                    fg_a_20ft_to_24ft   = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_a_20ft_to_24ft = float(fg_a_20ft_to_24ft)

                    fg_pct_20ft_to_24ft = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_pct_20ft_to_24ft = float(fg_pct_20ft_to_24ft)

                    fg_m_25ft_to_29ft   = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_m_25ft_to_29ft = float(fg_m_25ft_to_29ft)

                    fg_a_25ft_to_29ft   = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_a_25ft_to_29ft = float(fg_a_25ft_to_29ft)

                    fg_pct_25ft_to_29ft = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_pct_25ft_to_29ft = float(fg_pct_25ft_to_29ft)

                elif stat_type == '8ft Range':
                    fg_m_lt_8ft           = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_m_lt_8ft = float(fg_m_lt_8ft)

                    fg_a_lt_8ft           = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_a_lt_8ft = float(fg_a_lt_8ft)

                    fg_pct_lt_8ft         = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_pct_lt_8ft = float(fg_pct_lt_8ft)

                    fg_m_8ft_to_16ft      = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_m_8ft_to_16ft = float(fg_m_8ft_to_16ft)

                    fg_a_8ft_to_16ft      = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_a_8ft_to_16ft = float(fg_a_8ft_to_16ft)

                    fg_pct_8ft_to_16ft    = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_pct_8ft_to_16ft = float(fg_pct_8ft_to_16ft)

                    fg_m_16ft_to_24ft     = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_m_16ft_to_24ft = float(fg_m_16ft_to_24ft)

                    fg_a_16ft_to_24ft     = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_a_16ft_to_24ft = float(fg_a_16ft_to_24ft)

                    fg_pct_16ft_to_24ft   = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_pct_16ft_to_24ft = float(fg_pct_16ft_to_24ft)

                    fg_m_24ft_plus        = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_m_24ft_plus = float(fg_m_24ft_plus)

                    fg_a_24ft_plus        = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_a_24ft_plus = float(fg_a_24ft_plus)

                    fg_pct_24ft_plus      = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_pct_24ft_plus = float(fg_pct_24ft_plus)

                    fg_m_backcourt_shot   = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_m_backcourt_shot = float(fg_m_backcourt_shot)

                    fg_a_backcourt_shot   = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_a_backcourt_shot = float(fg_a_backcourt_shot)

                    fg_pct_backcourt_shot = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_pct_backcourt_shot = float(fg_pct_backcourt_shot)

                elif stat_type == 'By Zone':
                    fg_m_restricted_area   = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_m_restricted_area = float(fg_m_restricted_area)

                    fg_a_restricted_area   = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_a_restricted_area = float(fg_a_restricted_area)

                    fg_pct_restricted_area = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_pct_restricted_area = float(fg_pct_restricted_area)

                    fg_m_paint             = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_m_paint = float(fg_m_paint)

                    fg_a_paint             = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_a_paint = float(fg_a_paint)

                    fg_pct_paint           = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_pct_paint = float(fg_pct_paint)

                    fg_m_midrange          = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_m_midrange = float(fg_m_midrange)

                    fg_a_midrange          = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_a_midrange = float(fg_a_midrange)

                    fg_pct_midrange        = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_pct_midrange = float(fg_pct_midrange)

                    fg_m_left_corner_3     = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_m_left_corner_3 = float(fg_m_left_corner_3)

                    fg_a_left_corner_3     = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_a_left_corner_3 = float(fg_a_left_corner_3)

                    fg_pct_left_corner_3   = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_pct_left_corner_3 = float(fg_pct_left_corner_3)

                    fg_m_right_corner_3    = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_m_right_corner_3 = float(fg_m_right_corner_3)

                    fg_a_right_corner_3    = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_a_right_corner_3 = float(fg_a_right_corner_3)

                    fg_pct_right_corner_3  = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_pct_right_corner_3 = float(fg_pct_right_corner_3)

                    fg_m_corner_3    = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_m_corner_3 = float(fg_m_corner_3)

                    fg_a_corner_3    = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_a_corner_3 = float(fg_a_corner_3)

                    fg_pct_corner_3  = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_pct_corner_3 = float(fg_pct_corner_3)

                    fg_m_above_break_3     = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_m_above_break_3 = float(fg_m_above_break_3)

                    fg_a_above_break_3     = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_a_above_break_3 = float(fg_a_above_break_3)

                    fg_pct_above_break_3   = data[next(itr)]
                    ShootingClass.shooting[stat_type].fg_pct_above_break_3 = float(fg_pct_above_break_3)

            index += 1
