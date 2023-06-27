"""
PLAYER
"""

import itertools
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from utils import browserutils


class Player:
    def __init__(self):
        self.name         = str()   # Player Name
        self.team         = str()   # Current Team
        self.age          = int()   # Age
        self.height       = str()   # Height
        self.weight       = int()   # Weight
        self.college      = str()   # College
        self.country      = str()   # Country
        self.draft_year   = str()   # Draft Year
        self.draft_rd     = str()   # Draft Round
        self.draft_num    = str()   # Draft Number
        self.games_played = int()   # Games Played
        self.pts          = float() # Points
        self.reb          = float() # Rebounds
        self.ast          = float() # Assists
        self.netrtg       = float() # Net Rating
        self.oreb_pct     = float() # Offensive Rebounding Percentage
        self.dreb_pct     = float() # Defensive Rebound Percent
        self.usage_pct    = float() # Usage Percent
        self.ts_pct       = float() # True Shot Percent
        self.ast_pct      = float() # Assist Percent

    def addTable(self, name, table):
        setattr(self, name, table)


# Browse to correct player info page
def initialize_player(fname, lname, season_year = '2020-21', season_type = 'Regular%20Season'):

    # Create player object
    player_obj = Player()

    # URL Configurations
    name        = fname + '%20' + lname
    table_type  = 'players/'
    stat_url    = 'bio/'

    # Start browser
    browser = webdriver.Chrome(ChromeDriverManager().install())

    # Browse to correct stat category
    url = 'https://nba.com/stats/' + table_type + stat_url + '?sort=&CF=PLAYER_NAME*E*' + name + '&Season=' + season_year + '&SeasonType=' + season_type
    browser.get(url)
    browserutils.loadTeamPage(browser, locator="//*[@class='nba-stat-table__overflow']")

    # Scrape stats
    player_bio_table = browser.find_element_by_class_name("nba-stat-table__overflow")
    player_bio_table = browserutils.loadPlayerInfo(player_bio_table, mode="bios")
    if player_bio_table is not None:
        print('Initializing player...\n')
        get_bio_info(player_bio_table, player_obj)
        print('Player initialized...\n')

    # Close browser
    browser.quit()

    # Return initialized player
    return player_obj

# Browse to correct player info page
def initialize_players(playersNames, season_year = '2019-20', season_type = 'Regular%20Season'):

    # URL Configurations
    table_type  = 'players/'
    stat_url    = 'bio/'

    # Start browser
    browser = webdriver.Chrome(ChromeDriverManager().install())

    print('Initializing players...')
    players = list()
    for player in playersNames:

        # Create player object
        player_obj = Player()

        # Browse to correct stat category
        url = 'https://stats.nba.com/' + table_type + stat_url + '?sort=&CF=PLAYER_NAME*E*' + player + '&Season=' + season_year + '&SeasonType=' + season_type
        browser.get(url)

        # Scrape stats if table exist
        table = browserutils.loadPlayerInfo(browser)
        if bool(table):
            get_bio_info(table, player_obj)
            players.append(player_obj)

    # Close browser
    browser.quit()

    print('Players initialized...')

    # Return initialized player
    return players


# Initialize Player with Biographical Information
def get_bio_info(table, player_obj):

    name         = table['PLAYER']
    player_obj.name = str(name)

    team         = table['TEAM']
    player_obj.team = str(team)

    age          = table['AGE']
    player_obj.age = int(age)

    height       = table['HEIGHT']
    player_obj.height = str(height)

    weight       = table['WEIGHT']
    player_obj.weight = int(weight)

    college      = table['COLLEGE']
    player_obj.college = str(college)

    country      = table['COUNTRY']
    player_obj.country = str(country)

    draft_year   = table['DRAFT YEAR']
    player_obj.draft_year = str(draft_year)

    draft_rd     = table['DRAFT ROUND']
    player_obj.draft_rd = str(draft_rd)

    draft_num    = table['DRAFT NUMBER']
    player_obj.draft_num = str(draft_num)

    games_played = table['GP']
    player_obj.games_played = int(games_played)

    pts          = table['PTS']
    player_obj.pts = float(pts)

    reb          = table['REB']
    player_obj.reb = float(reb)

    ast          = table['AST']
    player_obj.ast = float(ast)

    netrtg       = table['NETRTG']
    player_obj.netrtg = float(netrtg)

    oreb_pct     = table['OREB%'].strip('%')
    player_obj.oreb_pct = float(oreb_pct)

    dreb_pct     = table['DREB%'].strip('%')
    player_obj.dreb_pct = float(dreb_pct)

    usage_pct    = table['USG%'].strip('%')
    player_obj.usage_pct = float(usage_pct)

    ts_pct       = table['TS%'].strip('%')
    player_obj.ts_pct = float(ts_pct)

    ast_pct      = table['AST%'].strip('%')
    player_obj.ast_pct = float(ast_pct)


def get_players():

    url = 'https://www.nba.com/stats/players/list/'

    # Start browser
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(url)

    playersUnformatted = browserutils.loadPlayersList(browser)

    players = format_names(playersUnformatted)

    # Close browser
    browser.quit()

    return players


def format_names(playersUnformatted):

    players = list()
    for playerUnformatted in playersUnformatted:
        unformatted_player = playerUnformatted.text.split(',')

        fname = unformatted_player[1].lstrip(' ')
        lname = unformatted_player[0]
        players.append(fname + ' ' + lname)

    return players
