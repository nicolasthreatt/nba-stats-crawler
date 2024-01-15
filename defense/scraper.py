from defense.parser import parse
from defense.tables.columns import defense_dashboard_types
from defense.tables.defense_dashboard import DefensiveDashboard
from selenium import webdriver
from players.tables.player import Player
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.browsertools import load_stat_table_page
from utils.types import TableType


def player(player: Player, season_year: str = '2020-21', season_type: str = 'Regular%20Season'):
    '''
    Produces each player's defense dashboard stats from:
        - https://wwww.nba.com/stats/players/defense-dash-overall/
    '''

    player.addTable('defense_dashboards', DefensiveDashboard())

    # URL Configurations
    name        = player.name.split(' ')[0] + '%20' + player.name.split(' ')[1]
    table_type  = 'players/'
    stat        = 'PLAYER_NAME'

    # Start browser
    browser = webdriver.Chrome()

    # Get Stats and Respective Ranking
    for stat_key, stat_url in defense_dashboard_types.items():

        # Browse to correct stat category
        url = 'https://nba.com/stats/' + table_type  + stat_url + '/?sort=' + stat + '&CF=PLAYER_NAME*E*' + name + '&Season=' + season_year + '&SeasonType=' + season_type
        browser.get(url)
        
        # Scrape stats if table exist
        table = load_stat_table_page(browser)
        if table:
            parse(table.text, stat_key.title(), player=player)

    # Close browser
    browser.quit()


def teams(teams: dict, season_year: str = '2020-21', season_type: str = 'Regular%20Season'):
    '''
    Produces each teams's defense dashboard stats from:
        - https://www.nba.com/stats/teams/defense-dash-overall/
    '''

    # Add stat class to teams
    for team in teams:
        teams[team].addTable('defense_dashboards', DefensiveDashboard())

    # URL Configurations
    table_type  = 'teams/'
    stat        = 'TEAM_NAME'

    # Start browser
    browser = webdriver.Chrome()

    # Get Stats and Respective Ranking
    for stat_key, stat_url in defense_dashboard_types.items():

        # Browse to correct stat category
        url = 'https://nba.com/stats/' + table_type + stat_url + '?sort=' + stat + '&dir=-1' + '&Season=' + season_year + '&SeasonType=' + season_type
        browser.get(url)

        # Scrape stats and get rank if table exist
        table = load_stat_table_page(browser)
        if table:
            parse(table.text, stat_key.title(), teams=teams)

    # Close browser
    browser.quit()
