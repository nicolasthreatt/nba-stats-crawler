import itertools
from players.tables.player import Player
from utils.browsertools import find_team_name
from utils.headers import getStatColumnType
from utils.types import TableType


# Collect Stats
def parse(table: str, stat_type: str, player: Player = None, teams: dict = None):
    """Parses the clutch stats table and stores the data in the player/team object

    Args:
        table (str): nba.com/stats table containing the stats
        stat_type (str): type of stat being parsed
        player (Player): player object to store the stats
        teams (dict): team object to store the stats
    """

    table_type = TableType.PLAYER.name if player else TableType.TEAM.name
    (table_header_row, table_column_offset) = getStatColumnType(stat_type, table_type)

    # Parse statistic table
    for row, info in enumerate(table.split('\n')):

        # Throw away header rows
        if row > table_header_row:

            # Get Correct Player/Team
            if player:
                name = info.title()
                player.name = name
                StatClass = player.hustle
            elif teams:
                team = find_team_name(info)
                info = info.replace(team, '').strip()
                StatClass = teams[team].hustle

            # Create iterator
            itr = itertools.count(table_column_offset)

            # Split info from table into a list
            data = info.split(' ')
            data = [item.replace("-", "0") for item in data]

            screen_ast = data[next(itr)]
            StatClass.screen_ast = float(screen_ast)

            screen_ast_pts = data[next(itr)]
            StatClass.screen_ast_pts = float(screen_ast_pts)

            deflections = data[next(itr)]
            StatClass.deflections = float(deflections)

            o_loose_balls_recovered = data[next(itr)]
            StatClass.o_loose_balls_recovered = float(o_loose_balls_recovered)

            d_loose_balls_recovered = data[next(itr)]
            StatClass.d_loose_balls_recovered = float(d_loose_balls_recovered)

            tot_loose_balls_recovered = data[next(itr)]
            StatClass.tot_loose_balls_recovered = float(tot_loose_balls_recovered)

            pct_loose_ball_o = data[next(itr)]
            StatClass.pct_loose_ball_o = float(pct_loose_ball_o)

            pct_loose_ball_d = data[next(itr)]
            StatClass.pct_loose_ball_d = float(pct_loose_ball_d)

            charges_drawn = data[next(itr)]
            StatClass.charges_drawn = float(charges_drawn)

            contested_2pt_shots = data[next(itr)]
            StatClass.contested_2pt_shots = float(contested_2pt_shots)

            contested_3pt_shots = data[next(itr)]
            StatClass.contested_3pt_shots = float(contested_3pt_shots)

            contested_all_shots = data[next(itr)]
            StatClass.contested_all_shots = float(contested_all_shots)
