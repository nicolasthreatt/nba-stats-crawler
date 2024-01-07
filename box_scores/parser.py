import itertools
from utils.headers import getStatColumnType
from utils.types import TableType

def parse(table: str, stat_type: str, player = None, team = None):
    """Parses the boxscore stats table and stores the data in the player/team object

    Args:
        table (str): The table containing the boxscore stats
        stat_type (str): The type of stat being parsed
        player (Player): The player object to store the stats
        team (Team): The team object to store the stats
    """

    table_type = TableType.PLAYER.name if player is not None else TableType.TEAM.name
    table_header_row, table_column_offset = getStatColumnType(stat_type, table_type)

    index = 1
    game_number = 1

    # Parse statistic table if it exists
    for row, info in enumerate(table.split('\n')):

        # Throwaway junk lines (column names)
        if row > table_header_row:

            # Get Correct Player
            if ((index % 2) == 1) and (player is not None):

                name = info.title()
                player.name = name
                player.boxscoreStats.add_game()
                StatClass = player.boxscoreStats

            # Extract stats
            if ((index % 2) == 0) or (team is not None):

                if team is not None:
                    # Reset game_number iterator every team
                    if len(team.boxscoreStats.game) == 0:
                        game_number = 1

                    team.boxscoreStats.add_game()
                    StatClass = team.boxscoreStats

                # Split info from table into a list
                data = info.split(' ')

                # Replace missing fields with zeros
                data[:-1] = [stat.replace("-", "0") for stat in data[:-1]]

                # Create iterator
                itr = itertools.count(table_column_offset)

                opponent   = data[next(itr)] + ' ' + data[next(itr)]
                StatClass.game[game_number - 1].opponent = opponent

                game_date  = data[next(itr)]
                StatClass.game[game_number - 1].game_date = game_date

                result     = data[next(itr)]
                StatClass.game[game_number - 1].result = result

                mins       = data[next(itr)]
                StatClass.game[game_number - 1].mins = int(mins)

                pts        = data[next(itr)]
                StatClass.game[game_number - 1].pts = int(pts)

                fg_m       = data[next(itr)]
                StatClass.game[game_number - 1].fg_m = int(fg_m)

                fg_a       = data[next(itr)]
                StatClass.game[game_number - 1].fg_a = int(fg_a)

                fg_pct     = data[next(itr)]
                StatClass.game[game_number - 1].fg_pct = float(fg_pct)

                fg3_m      = data[next(itr)]
                StatClass.game[game_number - 1].fg3_m = int(fg3_m)

                fg3_a      = data[next(itr)]
                StatClass.game[game_number - 1].fg3_a = int(fg3_a)

                fg3_pct    = data[next(itr)]
                StatClass.game[game_number - 1].fg3_pct = float(fg3_pct.replace("-", "0"))

                ft_m       = data[next(itr)]
                StatClass.game[game_number - 1].ft_m = int(ft_m)

                ft_a       = data[next(itr)]
                StatClass.game[game_number - 1].ft_a = int(ft_a)

                ft_pct     = data[next(itr)]
                StatClass.game[game_number - 1].ft_pct = float(ft_pct.replace("-", "0"))

                oreb       = data[next(itr)]
                StatClass.game[game_number - 1].oreb = int(oreb)

                dreb       = data[next(itr)]
                StatClass.game[game_number - 1].dreb = int(dreb)

                treb       = data[next(itr)]
                StatClass.game[game_number - 1].treb = int(treb)

                ast        = data[next(itr)]
                StatClass.game[game_number - 1].ast = int(ast)

                stl        = data[next(itr)]
                StatClass.game[game_number - 1].stl = int(stl)

                blk        = data[next(itr)]
                StatClass.game[game_number - 1].blk = int(blk)

                tov        = data[next(itr)]
                StatClass.game[game_number - 1].tov = int(tov)

                pf         = data[next(itr)]
                StatClass.game[game_number - 1].pf = int(pf)

                plus_minus = data[next(itr)]
                StatClass.game[game_number - 1].plus_minus = int(plus_minus)

                # Increment Game Count
                game_number += 1

            index += 1
