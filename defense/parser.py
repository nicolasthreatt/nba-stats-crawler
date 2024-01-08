
import itertools
from players.tables.player import Player
from utils.headers import getStatColumnType
from utils.types import TableType


# Collect Defensive Dashboard Stats
def parse(table: str, stat_type: str, player: Player = None, teams: dict = None):
    """Parses the defensive dashbaord stats table and stores the data in the player/team object

    Args:
        table (str): nba.com/stats table containing the stats
        stat_type (str): type of stat being parsed
        player (Player): player object to store the stats
        team (dict): team object to store the stats
    """

    table_type = TableType.PLAYER.name if player is not None else TableType.TEAM.name
    (table_header_row, table_column_offset) = getStatColumnType('Defensive Dashboard', table_type)

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

                freq            = data[next(itr)]
                StatClass.defense_dashboards[stat_key].freq = float(freq.strip('%'))

                defended_fg_m   = data[next(itr)]
                StatClass.defense_dashboards[stat_key].defended_fg_m = float(defended_fg_m)

                defended_fg_a   = data[next(itr)]
                StatClass.defense_dashboards[stat_key].defended_fg_a = float(defended_fg_a)

                defended_fg_pct = data[next(itr)]
                StatClass.defense_dashboards[stat_key].defended_fg_pct = float(defended_fg_pct)

                fg_pct          = data[next(itr)]
                StatClass.defense_dashboards[stat_key].fg_pct = float(fg_pct)

                pct_pts_diff    = data[next(itr)]
                StatClass.defense_dashboards[stat_key].pct_pts_diff = float(pct_pts_diff)

            index += 1
