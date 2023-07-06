"""
BOXSCORES

TODO:
    - CURRENTLY ONLY GETS 1ST PAGE OF TABLE; NEED TO GET ALL ROWS
"""

import itertools
from selenium import webdriver
from utils import browserutils
from utils.filters import *
from utils.headers import getStatColumnType
from utils.Player import Player
from utils.Team import Team
from utils.Types import TableType
from webdriver_manager.chrome import ChromeDriverManager


class BoxScores:
    """Box Score Class"""
    def __init__(self):
        self.game = list()

    def add_game(self):
        """Add Game to Box Score"""
        self.game.append(BoxScoreStats())


class BoxScoreStats:
    """Box Score Stats Class"""
    def __init__(self):
        self.opponent  = str()   # Opponent
        self.game_date = str()   # Game Date
        self.result     = str()  # Win/Loss
        self.mins      = int()   # Minutes Played
        self.pts       = int()   # Points
        self.fg_m      = int()   # Field Goals Made
        self.fg_a      = int()   # Field Goal Percentage
        self.fg_pct    = float() # Field Goals Attempted
        self.fg3_m     = int()   # 3 Point Field Goals Made
        self.fg3_a     = int()   # 3 Point Field Goals Attempted
        self.fg3_pct   = float() # 3 Point Field Goals Percentage
        self.ft_m      = int()   # Free Throws Made
        self.ft_a      = int()   # Free Throws Attempted
        self.ft_pct    = float() # Free Throw Percentage
        self.oreb      = int()   # Offensive Rebounds
        self.dreb      = int()   # Defensive Rebounds
        self.treb      = int()   # Rebounds
        self.ast       = int()   # Assists
        self.stl       = int()   # Steals
        self.blk       = int()   # Blocks
        self.tov       = int()   # Turnovers
        self.pf        = int()   # Personal Fouls
        self.plusminus = int()   # Plus Minus


def scrape_player(player: Player, season_year: str = '2020-21', season_type: str = 'Regular%20Season'):
    """
    Produces each player's box scores stats from:
        - https://www.nba.com/stats/players/boxscores/
    """

    # Add stat class to player
    player.addTable('boxscoreStats', BoxScores())

    # URL Configurations
    name       = player.name.split(' ')[0] + '%20' + player.name.split(' ')[1]
    table_type = 'players/'
    stat_type  = 'boxscores'

    # Start browser
    browser = webdriver.Chrome(ChromeDriverManager().install())

    # Browse to correct stat category
    url = 'https://nba.com/stats/' + table_type  + stat_type + '/?sort=&CF=PLAYER_NAME*E*' + name + '&Season=' + season_year + '&SeasonType=' + season_type
    browser.get(url)

    # Scrape stats if table exist
    table = browserutils.loadStatTable(browser)
    parse(table, stat_type.title(), player=player)

    # Close browser
    browser.quit()


def scrape_teams(teams: Team, season_year: str = '2020-21', season_type: str = 'Regular%20Season'):
    """
    Produces each team's box scores stats from:
        - https://www.nba.com/stats/teams/boxscores/

    Args:
        teams (dict): The dictionary of teams
        season_year (str): The season year
        season_type (str): The season type
    """

    # URL Configurations
    table_type = 'teams/'
    stat_type = 'boxscores'

    # Start browser
    browser = webdriver.Chrome(ChromeDriverManager().install())

    # Get each team's box score stats from every game played
    for team in teams:
        teams[team].addTable('boxscoreStats', BoxScores())

        # Browse to correct stat category
        url = 'https://www.nba.com/stats/' + table_type + stat_type + '/?CF=TEAM_NAME*E*' + team.title().replace(' ', '%20') + '&Season=' + season_year + '&SeasonType=' + season_type
        browser.get(url)

        # Scrape stats if table exist
        table = browserutils.loadStatTable(browser)
        if table is not None:
            parse(table, stat_type.title(), team=teams[team])

    # Close browser
    browser.quit()


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
