"""
BOX OUTS
"""

import itertools
from selenium import webdriver
from utils import browserutils
from utils.headers import getStatColumnType
from utils.Player import Player
from utils.Types import TableType
from webdriver_manager.chrome import ChromeDriverManager


boxout_stats = [
    'TEAM_NAME',
    'BOX_OUTS',
    'OFF_BOXOUTS',
    'DEF_BOXOUTS',
    'PCT_BOX_OUTS_OFF',
    'PCT_BOX_OUTS_DEF',
]

class BoxOuts:
    """Box Out Class"""
    def __init__(self, table_type):
        self.boxouts                         = float() # Box Outs
        self.off_boxouts                     = float() # Offensive Box Outs
        self.def_boxouts                     = float() # Defensive Box Outs
        self.pct_boxouts_off                 = float() # Percentage of Box Outs Offense
        self.pct_boxouts_def                 = float() # Percentage of Box Outs Defense

        if table_type == TableType.PLAYER.name:
            self.team_reb_on_boxouts         = float() # Teams Number of Rebounds on Box Outs
            self.player_reb_on_boxouts       = float() # Player Number of Rebounds on Box Outs
            self.pct_team_reb_when_boxout    = float() # Percentage of Team Rebounds when Box Out
            self.pct_player_reb_when_boxout  = float() # Percentage of Player Rebounds when Box Out


def scrape_player(player: Player, season_year: str = '2020-21', season_type: str = 'Regular%20Season'):
    """
    Produces each player's box out stats from:
        - https://www.nba.com/stats/players/box-outs/
    """

    # Add stat class to player
    player.addTable('boxOutStats', BoxOuts(TableType.PLAYER.name))

    # URL Configurations
    name        = player.name.split(' ')[0] + '%20' + player.name.split(' ')[1]
    table_type  = 'players/'
    stat_type   = 'box-outs'

    # Start browser
    browser = webdriver.Chrome(ChromeDriverManager().install())

    url = 'https://nba.com/stats/' + table_type + stat_type + '/?sort=&CF=PLAYER_NAME*E*' + name + '&Season=' + season_year + '&SeasonType=' + season_type
    browser.get(url)

    # Scrape stats if table exist
    table = browserutils.loadStatTable(browser)
    parse(table, stat_type.title(), player=player)

    # Close browser
    browser.quit()


def scrape_teams(teams: str, season_year: str = '2020-21', season_type: str = 'Regular%20Season'):
    """
    Produces each teams's box out stats from:
        - https://www.stats.nba.com/teams/box-outs/
    
    Args:
        teams (dict): teams dictionary
        season_year (str): season year
        season_type (str): season type
    """

        # Add stat class to teams
    for team in teams:
        teams[team].addTable('boxOutStats', BoxOuts(TableType.TEAM.name))

    # URL Configurations
    table_type  = 'teams/'
    stat_type   = 'box-outs'
    stat        = 'TEAM_NAME'

    # Start browser
    browser = webdriver.Chrome(ChromeDriverManager().install())

    # Browse to correct stat category
    url = 'https://nba.com/stats/' + table_type + stat_type + '/?sort=' + stat + '&dir=-1' + '&Season=' + season_year + season_type
    browser.get(url)

    # Scrape stats if table exist
    table = browserutils.loadStatTable(browser)
    if table is not None:
        parse(table, stat_type.title(), teams=teams)

    # Close browser
    browser.quit()


# Collect Box Out Stats
def parse(table: str, stat_key: str, player = None, teams = None):
    """
    Parses box out stats from nba stats table and adds them to player/team object

    Args:
        table (str): table from https://www.nba.com/stats/players/box-outs/
        stat_key (str): key for stat
        player (Player): player object
        teams (dict): teams dictionary
    """

    table_type = TableType.PLAYER.name if player is not None else TableType.TEAM.name
    table_header_row, table_column_offset = getStatColumnType(stat_key, table_type)

    # Parse statistic table
    for row, info in enumerate(table.split('\n')):

        # Throw away header
        if row > table_header_row:

            # Get Correct Player/Team
            if (row % 2) == 1:
                if player is not None:
                    player.name = info.title()
                    StatClass = player.boxOutStats
                elif teams is not None:
                    team = info.upper()

                    StatClass = teams[team].boxOutStats

            # Extract stats
            if (row % 2) == 0:

                # Create iterator
                itr = itertools.count(table_column_offset)

                # Split info from table into a list
                data = info.split(' ')
                data = [item.replace("-", "0") for item in data]

                if teams is not None: next(itr) # Skip Minutes Column (Need to edit TableHeader.py)

                boxouts = data[next(itr)]
                StatClass.boxouts = float(boxouts)

                off_boxouts = data[next(itr)]
                StatClass.off_boxouts = float(off_boxouts)

                def_boxouts = data[next(itr)]
                StatClass.def_boxouts = float(def_boxouts)

                if player is not None:
                    team_reb_on_boxouts = data[next(itr)]
                    StatClass.team_reb_on_boxouts = float(team_reb_on_boxouts)

                    player_reb_on_boxouts = data[next(itr)]
                    StatClass.player_reb_on_boxouts = float(player_reb_on_boxouts)

                pct_boxouts_off = data[next(itr)]
                StatClass.pct_boxouts_off = float(pct_boxouts_off)

                pct_boxouts_def = data[next(itr)]
                StatClass.pct_boxouts_def = float(pct_boxouts_def)

                if player is not None:
                    pct_team_reb_when_boxout = data[next(itr)]
                    StatClass.pct_team_reb_when_boxout = float(pct_team_reb_when_boxout)

                    pct_player_reb_when_boxout = data[next(itr)]
                    StatClass.pct_player_reb_when_boxout = float(pct_player_reb_when_boxout)
