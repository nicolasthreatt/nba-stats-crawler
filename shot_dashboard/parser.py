import itertools
from utils.headers import getStatColumnType
from utils.Player import Player
from utils.Team import Team
from utils.types import TableType

# Get Shot Dashboard Stats
def parse(table: str, stat_type: str, player: Player = None, team: Team = None):

    table_type = TableType.PLAYER.name if player is not None else TableType.TEAM.name
    (table_header_row, table_column_offset) = getStatColumnType('Shot Dashboard', table_type)

    # Parse statistic table
    index = 1
    for row, info in enumerate(table.split('\n')):

        # Throw away header rows
        if row > table_header_row:

            # Get Correct Player/Team
            if (index % 2) == 1:

                if player is not None:
                    name = info.title()
                    player.name = name
                    StatClass = player.shot_dashboard

                elif teams is not None:
                    team = info.upper()
                    StatClass = teams[team].shot_dashboard

            # Extract stats
            elif (index % 2) == 0:

                # Create iterator
                itr = itertools.count(table_column_offset)

                # Split info from table into a list
                data = info.split(' ')
                data = [stat.replace("-", "0") for stat in data]

                fg_freq  = data[next(itr)]
                StatClass[stat_type].fg_freq = float(fg_freq.strip('%'))

                fg_m     = data[next(itr)]
                StatClass[stat_type].fg_m = float(fg_m)

                fg_a     = data[next(itr)]
                StatClass[stat_type].fg_a = float(fg_a)

                fg_pct   = data[next(itr)]
                StatClass[stat_type].fg_pct = float(fg_pct)

                eFg_pct  = data[next(itr)]
                StatClass[stat_type].eFg_pct = float(eFg_pct)

                fg2_freq = data[next(itr)]
                StatClass[stat_type].fg2_freq = float(fg2_freq.strip('%'))

                fg2_m    = data[next(itr)]
                StatClass[stat_type].fg2_m = float(fg2_m)

                fg2_a    = data[next(itr)]
                StatClass[stat_type].fg2_a = float(fg2_a)

                fg2_pct  = data[next(itr)]
                StatClass[stat_type].fg2_pct = float(fg2_pct)

                fg3_freq = data[next(itr)]
                StatClass[stat_type].fg3_freq = float(fg3_freq.strip('%'))

                fg3_m    = data[next(itr)]
                StatClass[stat_type].fg3_m = float(fg3_m)

                fg3_a    = data[next(itr)]
                StatClass[stat_type].fg3_a = float(fg3_a)

                fg3_pct  = data[next(itr)]
                StatClass[stat_type].fg3_pct = float(fg3_pct)

            index += 1
