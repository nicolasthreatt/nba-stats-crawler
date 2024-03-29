import itertools
from players.tables.player import Player
from utils.browsertools import find_team_name
from utils.headers import getStatColumnType
from utils.types import TableType


# Collect Stats
def parse(table: str, stat_type: str, player: Player = None, teams: dict = None):

    table_type = TableType.PLAYER.name if player else TableType.TEAM.name
    table_header_row, table_column_offset = getStatColumnType('Playtype', table_type)

    # Parse statistic table if it exists
    for row, info in enumerate(table.split('\n')):

        # Throw away header rows
        if row > table_header_row:

            # Get Correct Player
            if player:
                name = info.title()
                player.name = name
                StatClass = player
            elif teams:
                team = find_team_name(info)
                info = info.replace(team, '').strip()
                StatClass = teams[team]

            # Create iterator
            itr = itertools.count(table_column_offset)

            # Split info from table into a list
            data = info.split(' ')
            data = [stat.replace("-", "0") for stat in data]

            # Collect Stats
            poss       = data[next(itr)]
            StatClass.playtypes[stat_type].poss = float(poss)

            freq       = data[next(itr)]
            StatClass.playtypes[stat_type].freq = float(freq.strip('%'))

            ppp        = data[next(itr)]
            StatClass.playtypes[stat_type].ppp = float(ppp)

            pts        = data[next(itr)]
            StatClass.playtypes[stat_type].pts = float(pts)

            fg_m       = data[next(itr)]
            StatClass.playtypes[stat_type].fg_m = float(fg_m)

            fg_a       = data[next(itr)]
            StatClass.playtypes[stat_type].fg_a = float(fg_a)

            fg_pct     = data[next(itr)]
            StatClass.playtypes[stat_type].fg_pct = float(fg_pct.strip('%'))

            efg_pct    = data[next(itr)]
            StatClass.playtypes[stat_type].efg_pct = float(efg_pct.strip('%'))

            ft_freq    = data[next(itr)]
            StatClass.playtypes[stat_type].ft_freq = float(ft_freq.strip('%'))

            tov_freq   = data[next(itr)]
            StatClass.playtypes[stat_type].tov_freq = float(tov_freq.strip('%'))

            sf_freq    = data[next(itr)]
            StatClass.playtypes[stat_type].sf_freq = float(sf_freq.strip('%'))

            and1_freq  = data[next(itr)]
            StatClass.playtypes[stat_type].and1_freq = float(and1_freq.strip('%'))

            score_freq = data[next(itr)]
            StatClass.playtypes[stat_type].score_freq = float(score_freq.strip('%'))

            percentile = data[next(itr)]
            StatClass.playtypes[stat_type].percentile = float(percentile)
