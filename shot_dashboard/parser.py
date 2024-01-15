import itertools
from players.tables.player import Player
from utils.browsertools import find_team_name
from utils.headers import getStatColumnType
from utils.types import TableType


# Get Shot Dashboard Stats
def parse(table: str, stat_type: str, player: Player = None, teams: dict = None):

    table_type = TableType.PLAYER.name if player else TableType.TEAM.name
    (table_header_row, table_column_offset) = getStatColumnType('Shot Dashboard', table_type)

    # Parse statistic table
    for row, info in enumerate(table.split('\n')):

        # Throw away header rows
        if row > table_header_row:

            # Get Correct Player/Team
            if player:
                name = info.title()
                player.name = name
                StatClass = player.shot_dashboard

            elif teams:
                team = find_team_name(info)
                info = info.replace(team, '').strip()
                StatClass = teams[team].shot_dashboard

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
