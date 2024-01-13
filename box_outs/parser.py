import itertools
from players.tables.player import Player
from utils.headers import getStatColumnType
from utils.types import TableType


# Collect Box Out Stats
def parse(table: str, stat_key: str, player: Player = None, teams: dict = None):
    """
    Parses box out stats from nba stats table and adds them to player/team object

    Args:
        table (str): table from https://www.nba.com/stats/players/box-outs/
        stat_key (str): key for stat
        player (Player): player object
        teams (dict): teams dictionary
    """

    table_type = TableType.PLAYER.name if player else TableType.TEAM.name
    table_header_row, table_column_offset = getStatColumnType(stat_key, table_type)

    # Parse statistic table
    for row, info in enumerate(table.split('\n')):

        # Throw away header
        if row > table_header_row:

            # Get Correct Player/Team
            if (row % 2) == 1:
                if player:
                    player.name = info.title()
                    StatClass = player.boxOutStats
                elif teams:
                    team = info.upper()

                    StatClass = teams[team].boxOutStats

            # Extract stats
            if (row % 2) == 0:

                # Create iterator
                itr = itertools.count(table_column_offset)

                # Split info from table into a list
                data = info.split(' ')
                data = [item.replace("-", "0") for item in data]

                if teams: next(itr) # Skip Minutes Column (Need to edit TableHeader.py)

                boxouts = data[next(itr)]
                StatClass.boxouts = float(boxouts)

                off_boxouts = data[next(itr)]
                StatClass.off_boxouts = float(off_boxouts)

                def_boxouts = data[next(itr)]
                StatClass.def_boxouts = float(def_boxouts)

                if player:
                    team_reb_on_boxouts = data[next(itr)]
                    StatClass.team_reb_on_boxouts = float(team_reb_on_boxouts)

                    player_reb_on_boxouts = data[next(itr)]
                    StatClass.player_reb_on_boxouts = float(player_reb_on_boxouts)

                pct_boxouts_off = data[next(itr)]
                StatClass.pct_boxouts_off = float(pct_boxouts_off)

                pct_boxouts_def = data[next(itr)]
                StatClass.pct_boxouts_def = float(pct_boxouts_def)

                if player:
                    pct_team_reb_when_boxout = data[next(itr)]
                    StatClass.pct_team_reb_when_boxout = float(pct_team_reb_when_boxout)

                    pct_player_reb_when_boxout = data[next(itr)]
                    StatClass.pct_player_reb_when_boxout = float(pct_player_reb_when_boxout)
