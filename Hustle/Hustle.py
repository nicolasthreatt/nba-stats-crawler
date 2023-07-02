"""
HUSTLE
"""

import itertools
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from utils import browserutils
from utils.headers import getStatColumnType
from utils.Types import TableType


class Hustle:
    def __init__(self):
        self.screen_ast                = float() # Screen Assists
        self.screen_ast_pts            = float() # Points From Screen Assists
        self.deflections               = float() # Deflections
        self.o_loose_balls_recovered   = float() # Offensive Loose Balls Recovered
        self.d_loose_balls_recovered   = float() # Defensive Loose Balls Recovered
        self.tot_loose_balls_recovered = float() # Total Loose Balls Recovered
        self.pct_loose_ball_o          = float() # Percentage of Loose Balls Recovered Offensively
        self.pct_loose_ball_d          = float() # Percentage of Loose Balls Recovered Defensively
        self.charges_drawn             = float() # Charges Drawn
        self.contested_2pt_shots       = float() # Contested 2Pt Shots
        self.contested_3pt_shots       = float() # Contested 3Pt Shots
        self.contested_all_shots       = float() # Contested All Shots


# Store Stats to Player
def scrape_player(player, season_year = '2020-21', season_type = 'Regular%20Season'):
    '''
    Produces each player's hustle stats from:
        - https://www.nba.com/stats/players/hustle/
    '''

    # Add stat class to player
    player.addTable('hustle', Hustle())

    # URL Configurations
    name       = player.name.split(' ')[0] + '%20' + player.name.split(' ')[1]
    table_type = 'players/'
    stat_type  = 'hustle'

    # Start browser
    browser = webdriver.Chrome(ChromeDriverManager().install())

    # Browse to correct stat category
    url = 'https://nba.com/stats/' + table_type + stat_type + '/?sort=&CF=PLAYER_NAME*E*' + name + '&Season=' + season_year + '&SeasonType=' + season_type
    browser.get(url)

    # Scrape stats if table exist
    table = browserutils.loadStatTable(browser)
    if table is not None:
        getHustleStats(table, stat_type.title(), player=player)

    # Close browser
    browser.quit()


# Store Stats to Teams
def scrape_teams(teams, season_year = '2020-21', season_type = 'Regular%20Season'):
    '''
    Produces each team's hustle stats from:
        - https://www.nba.com/stats/teams/hustle/
    '''

    # Add stat class to teams
    for team in teams:
        teams[team].addTable('hustle', Hustle())

    # URl Configurations
    table_type  = 'teams/'
    stat_type   = 'hustle'
    stat        = 'TEAM_NAME'

    # Start browser
    browser = webdriver.Chrome(ChromeDriverManager().install())

    # Browse to correct stat category
    url = 'https://nba.com/stats/' + table_type + stat_type + '/?sort=' + stat + '&dir=-1' + '&Season=' + season_year + '&SeasonType=' + season_type
    browser.get(url)

    # Scrape stats and get rank if table exist
    table = browserutils.loadStatTable(browser)
    if table is not None:
        getHustleStats(table, stat_type.title(), teams=teams)

    # Close browser
    browser.quit()


# Collect Stats
def getHustleStats(table, stat_key, player=None, teams=None):

    table_type = TableType.PLAYER.name if player is not None else TableType.TEAM.name
    (table_header_row, table_column_offset) = getStatColumnType(stat_key, table_type)

    # Parse statistic table
    index = 1
    for row, info in enumerate(table.split('\n')):

        # Throw away header rows
        if row > table_header_row:

            # Get Info
            if (index % 2) == 1:

                if player is not None:
                    name = info.title()
                    player.name = name
                    StatClass = player.hustle

                elif teams is not None:
                    team = info.upper()
                    StatClass = teams[team].hustle

            # Extract stats
            elif (index % 2) == 0:

                # Split info from table into a list
                data = info.split(' ')
                data = [item.replace("-", "0") for item in data]

                # Create iterator
                itr = itertools.count(table_column_offset)

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

            index += 1
