"""
TODO:
    - CURRENTLY ONLY GETS 1ST PAGE OF TABLE; NEED TO GET ALL ROWS
"""
from box_scores.parser import parse
from box_scores.tables.box_scores import BoxScores
from players.tables.player import Player
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.browsertools import load_stat_table_page


def player(player: Player, season_year: str = '2020-21', season_type: str = 'Regular%20Season'):
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
    browser = webdriver.Chrome()

    # Browse to correct stat category
    url = 'https://nba.com/stats/' + table_type  + stat_type + '/?CF=PLAYER_NAME*E*' + name + '&Season=' + season_year + '&SeasonType=' + season_type
    browser.get(url)

    # Scrape stats if table exist
    table = load_stat_table_page(browser)
    if table:
        parse(table.text, stat_type.title(), player=player)

    # Close browser
    browser.quit()


def teams(teams: dict, season_year: str = '2020-21', season_type: str = 'Regular%20Season'):
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
    browser = webdriver.Chrome()

    # Get each team's box score stats from every game played
    for team in teams:
        teams[team].addTable('boxscoreStats', BoxScores())

        # Browse to correct stat category
        url = 'https://www.nba.com/stats/' + table_type + stat_type + '/?CF=TEAM_NAME*E*' + team.title().replace(' ', '%20') + '&Season=' + season_year + '&SeasonType=' + season_type
        browser.get(url)

        # Scrape stats if table exist
        table = load_stat_table_page(browser)
        if table:
            parse(table.text, stat_type.title(), team=teams[team])

    # Close browser
    browser.quit()
