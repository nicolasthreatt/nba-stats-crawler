"""
PLAY TYPES

- TODO: Add offensive and defensive advanced filter
"""

import itertools

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from utils import browserutils
from utils.filters import type_grouping
from utils.headers import getStatColumnType
from utils.Types import TableType


playtypes = {
    'Transition':   'transition/',       # Transition
    'Isolation':    'isolation/',        # Iso
    'Ball Handler': 'ball-handler/',     # Pick & Role Ball Handler
    'Roll Man':     'roll-man/',         # Pick & Roll Roll Man
    'Post-Up':      'playtype-post-up/', # Post Up
    'Spot-Up':      'spot-up/',          # Spot Up
    'Hand-Off':     'hand-off/',         # Handoff
    'Cut':          'cut/',              # Cut
    'Off-Screen':   'off-screen/',       # Off Screen
    'Putbacks':     'putbacks/',         # Put Backs
    'Misc':         'playtype-misc/',    # Misc
}


class Playtype(dict):
    def __init__(self):
        initPlaytypes(self)

    def __getattr__(self, key):
        return self[key]


# Stat info class
class PlaytypeStats:
    def __init__(self):
        self.poss       = float() # Possessions
        self.freq       = float() # Frequency
        self.ppp        = float() # Points Per Possession
        self.pts        = float() # Points
        self.fg_m       = float() # Fields Goals Made
        self.fg_a       = float() # Field Goals Attempted
        self.fg_pct     = float() # Field Goal Percentage
        self.efg_pct    = float() # Effective Field Goal Percentage
        self.ft_freq    = float() # Free Throw Frequency
        self.tov_freq   = float() # Turnover Frequency
        self.sf_freq    = float() # Shooting Foul Frequency
        self.and1_freq  = float() # And1 Frequency
        self.score_freq = float() # Scoring Frequency
        self.percentile = float() # Percentile


# Get Playtyes Stats
def initPlaytypes(StatClass):
    for playtype in playtypes:
        for typegroup_key in type_grouping:
            key = playtype + ' (' + typegroup_key.title() + ')'
            StatClass[key] = PlaytypeStats()


# Store Stats to Player
def scrape_player(player, season_year = '2020-21', season_type = 'Regular%20Season'):
    '''
    Produces each player's playtype stats from:
        - https://www.nba.com/stats/players/transition/
        - https://www.nba.com/stats/players/isolation/
        - https://www.nba.com/stats/players/ball-handler/
        - https://www.nba.com/stats/players/roll-man/
        - https://www.nba.com/stats/players/playtype-post-up/
        - https://www.nba.com/stats/players/spot-up/
        - https://www.nba.com/stats/players/hand-off/
        - https://www.nba.com/stats/players/cut/
        - https://www.nba.com/stats/players/off-screen/
        - https://www.nba.com/stats/players/putbacks/
        - https://www.nba.com/stats/players/playtype-misc/
    '''

    # Add stat class to player
    player.addTable('playtypes', Playtype())

    # URL Configurations
    name       = player.name.split(' ')[0] + '%20' + player.name.split(' ')[1]
    table_type = 'players/'
    stat       = 'PLAYER_NAME'

    # Start browser
    browser = webdriver.Chrome(ChromeDriverManager().install())

    # Get stats from correct url path
    for playtype_key, playtype_url in playtypes.items():
        for typegroup_key, typegroup_url in type_grouping.items():

            # Browse to correct stat category
            url = 'https://nba.com/stats/' + table_type + playtype_url + '#!?CF=PLAYER_NAME*E*' + name + '&sort=' + stat + '&Season=' + season_year + '&SeasonType=' + season_type + typegroup_url
            browser.get(url)

            # Scrape stats if table exist
            table = browserutils.loadStatTable(browser)
            
            if table is not None:
                getPlaytypeStats(table, playtype_key +' (' + typegroup_key.title() + ')', player=player)

    # Close browser
    browser.quit()


# Store Stats to Teams
def collectTeamStats(teams, season_year = '2020-21', season_type = 'Regular%20Season'):
    '''
    Produces each player's playtype stats from:
        - https://www.nba.com/stats/teams/transition/
        - https://www.nba.com/stats/teams/isolation/
        - https://www.nba.com/stats/teams/ball-handler/
        - https://www.nba.com/stats/teams/roll-man/
        - https://www.nba.com/stats/teams/playtype-post-up/
        - https://www.nba.com/stats/teams/spot-up/
        - https://www.nba.com/stats/teams/hand-off/
        - https://www.nba.com/stats/teams/cut/
        - https://www.nba.com/stats/teams/off-screen/
        - https://www.nba.com/stats/teams/putbacks/
        - https://www.nba.com/stats/teams/playtype-misc/
    '''

    # Add stat class to teams
    for team in teams:
        teams[team].addTable('playtypes', Playtype())

    # URL Configuration
    table_type = 'teams/'
    stat       = 'TEAM_NAME'

    # Start browser
    browser = webdriver.Chrome(ChromeDriverManager().install())

    # Get stats from correct url path
    for playtype_key, playtype_url in playtypes.items():
        for typegroup_key, typegroup_url in type_grouping.items():

            # Browse to correct stat category
            url = 'https://nba.com/stats/' + table_type + playtype_url + '?sort=' + stat + '&dir=-1' + '&Season=' + season_year + '&SeasonType=' + season_type + typegroup_url
            browser.get(url)

            # Scrape stats if table exist
            table = browserutils.loadStatTable(browser)
            if table is not None:
                getPlaytypeStats(table, playtype_key +' (' + typegroup_key.title() + ')', teams=teams)

    # Close browser
    browser.quit()


def reformatData(data):
    # Number of columns based on how many words it takes to build a team's name
    two_word_team   = 17
    three_word_team = 18

    # Merge Team Info into One Element
    if len(data) == two_word_team:
        data[0 : 2] = [' '.join(data[0 : 2])]
    elif len(data) == three_word_team:
        data[0 : 3] = [' '.join(data[0 : 3])]


# Collect Stats
def getPlaytypeStats(table, playtype, player=None, teams=None):

    table_type = TableType.PLAYER.name if player is not None else TableType.TEAM.name
    (table_header_row, table_column_offset) = getStatColumnType('Playtype', table_type)

    # Parse statistic table
    index = 1

    # Parse statistic table if it exists
    for row, info in enumerate(table.split('\n')):

        # Throw away header rows
        if row > table_header_row:

            # Get Correct Player
            if (index % 2) == 1 and (player is not None):

                name = info.title()
                player.name = name
                StatClass = player

            # Extract stats
            if (index % 2) == 0 or (teams is not None):

                # Create iterator
                itr = itertools.count(table_column_offset)

                # Split info from table into a list
                data = info.split(' ')
                data = [stat.replace("-", "0") for stat in data]

                if teams:
                    reformatData(data)
                    team = data[next(itr)].upper()
                    StatClass = teams[team]

                    # Skip Games Played
                    next(itr)

                # Collect Stats
                poss       = data[next(itr)]
                StatClass.playtypes[playtype].poss = float(poss)

                freq       = data[next(itr)]
                StatClass.playtypes[playtype].freq = float(freq.strip('%'))

                ppp        = data[next(itr)]
                StatClass.playtypes[playtype].ppp = float(ppp)

                pts        = data[next(itr)]
                StatClass.playtypes[playtype].pts = float(pts)

                fg_m       = data[next(itr)]
                StatClass.playtypes[playtype].fg_m = float(fg_m)

                fg_a       = data[next(itr)]
                StatClass.playtypes[playtype].fg_a = float(fg_a)

                fg_pct     = data[next(itr)]
                StatClass.playtypes[playtype].fg_pct = float(fg_pct.strip('%'))

                efg_pct    = data[next(itr)]
                StatClass.playtypes[playtype].efg_pct = float(efg_pct.strip('%'))

                ft_freq    = data[next(itr)]
                StatClass.playtypes[playtype].ft_freq = float(ft_freq.strip('%'))

                tov_freq   = data[next(itr)]
                StatClass.playtypes[playtype].tov_freq = float(tov_freq.strip('%'))

                sf_freq    = data[next(itr)]
                StatClass.playtypes[playtype].sf_freq = float(sf_freq.strip('%'))

                and1_freq  = data[next(itr)]
                StatClass.playtypes[playtype].and1_freq = float(and1_freq.strip('%'))

                score_freq = data[next(itr)]
                StatClass.playtypes[playtype].score_freq = float(score_freq.strip('%'))

                percentile = data[next(itr)]
                StatClass.playtypes[playtype].percentile = float(percentile)

        index += 1
