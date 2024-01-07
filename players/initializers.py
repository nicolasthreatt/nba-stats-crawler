from selenium import webdriver
from players.tables.player import Player
from players.parser import parse
from utils import browsertools


# Browse to correct player info page
def player(fname: str, lname: str, season_year: str = '2020-21', season_type: str = 'Regular%20Season'):
    # Create player object
    player = Player()

    # URL Configurations
    name        = fname + '%20' + lname
    table_type  = 'players/'
    stat_url    = 'bio/'

    # Start browser
    browser = webdriver.Chrome()

    # Browse to correct stat category
    url = 'https://nba.com/stats/' + table_type + stat_url + '?sort=&CF=PLAYER_NAME*E*' + name + '&Season=' + season_year + '&SeasonType=' + season_type
    browser.get(url)

    # Scrape stats
    player_bio_table = browsertools.loadPlayerInfo(browser, mode="bios") # TODO: MOVE TO CRAWLER.PY
    if player_bio_table is not None:
        print('Initializing player...\n')
        parse(player_bio_table, player)
        print('Player initialized...\n')

    # Close browser
    browser.quit()

    # Return initialized player
    return player


# Browse to correct player info page
def players(players_names: list, season_year: str = '2019-20', season_type: str = 'Regular%20Season'):
    # URL Configurations
    table_type  = 'players/'
    stat_url    = 'bio/'

    # Start browser
    browser = webdriver.Chrome(ChromeDriverManager().install())

    print('Initializing players...')
    players = list()
    for player_name in players_names:

        # Create player object
        player = Player()

        # Browse to correct stat category
        url = 'https://stats.nba.com/' + table_type + stat_url + '?sort=&CF=PLAYER_NAME*E*' + player_name + '&Season=' + season_year + '&SeasonType=' + season_type
        browser.get(url)

        # Scrape stats if table exist
        table = browserutils.loadPlayerInfo(browser)
        if bool(table):
            parse(table, player)
            players.append(player)

    # Close browser
    browser.quit()
    print('Players initialized...')

    # Return initialized player
    return players
