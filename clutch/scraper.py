from clutch.parser import parse
from clutch.tables.columns import *
from clutch.tables.clutch import Clutch, clutch_stats_tables
from players.tables.player import Player
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.types import TableType
from utils.browsertools import load_stat_table_page


def player(player: Player, season_year: str = '2020-21', season_type: str = 'Regular%20Season'):
    """Produces each player's clutch stats from:
        - https://www.nba.com/stats/players/clutch-traditional/
        - https://www.nba.com/stats/players/clutch-advanced/
        - https://www.nba.com/stats/players/clutch-misc/
        - https://www.nba.com/stats/players/clutch-scoring/
        - https://www.nba.com/stats/players/clutch-usage/
    """

    # Add stat class to player
    player.addTable('clutch', Clutch(TableType.PLAYER.name))

    # URL Configurations
    name       = player.name.split(' ')[0] + '%20' + player.name.split(' ')[1]
    table_type = 'players/'
    per_mode   = 'Totals'
    stat       = 'PLAYER_NAME'

    # Start browser
    browser = webdriver.Chrome()

    # Get stats from correct url path
    for stat_key, stat_url in clutch_stats_tables.items():

        if not stat_key in ('Four Factors', 'Opponent'):

            # Browse to correct stat category
            url = f'https://nba.com/stats/{table_type}{stat_url}/?sort={stat}&CF=PLAYER_NAME*E*{name}&Season={season_year}&SeasonType={season_type}&PerMode={per_mode}'
            browser.get(url)

            # Scrape stats if table exists
            table = load_stat_table_page(browser)
            if table.text:
                parse(table.text, stat_key, player=player)

    # Close browser
    browser.quit()


def teams(teams: dict, season_year: str = '2020-21', season_type: str = 'Regular%20Season'):
    """Produces each team's clutch stats from:
        - https://www.nba.com/stats/teams/clutch-traditional/
        - https://www.nba.com/stats/teams/clutch-advanced/
        - https://www.nba.com/stats/teams/clutch-misc/
        - https://www.nba.com/stats/teams/clutch-scoring/
        - https://www.nba.com/stats/teams/clutch-four-factors/
        - https://www.nba.com/stats/teams/clutch-usage/
    """

    # Add stat class to teams
    for team in teams:
        teams[team].addTable('clutch', Clutch(TableType.TEAM.name))

    # URL Configurations
    table_type = 'teams/'
    per_mode   = 'Totals'
    stat       = 'TEAM_NAME'

    # Start browser
    browser = webdriver.Chrome(ChromeDriverManager().install())

    # Get Stats and Respective Ranking
    for stat_key, stat_url in clutch_stats_tables.items():

        if stat_key != 'Usage':

            # Browse to correct stat category
            url = f'https://nba.com/stats/{table_type}{stat_url}/?sort={stat}&dir=-1&Season={season_year}&SeasonType={season_type}&PerMode={per_mode}'
            browser.get(url)

            table = browserutils.loadStatTable(browser)
            if table:
                parse(table, stat_key, teams=teams)

    # Close browser
    browser.quit()