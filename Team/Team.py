"""
TEAM

TODO
    - Use threading to improve performance
"""

# Load up all packages
import itertools
import re

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from utils import browserutils

from utils.filters import groupBy


class Team:
    def __init__(self):
        self.overall         = {'W': int(), 'L': int()} # Overall Record
        self.win_pct         = float()                  # Winning Percentage
        self.games_back      = float()                  # Games Back
        self.conference_rank = int()                    # Conference Ranking
        self.conference      = {'W': int(), 'L': int()} # Conference Record
        self.division_rank   = int()                    # Dvision Ranking
        self.division        = {'W': int(), 'L': int()} # Dvision Record
        self.home            = {'W': int(), 'L': int()} # Home Record
        self.road            = {'W': int(), 'L': int()} # Road Record
        self.ot              = {'W': int(), 'L': int()} # OT Record
        self.last10          = {'W': int(), 'L': int()} # Last 10 Games Record
        self.streak          = str()                    # Current Streak

    def addTable(self, name, table):
        setattr(self, name, table)


# Browse to Page with Team Info
def initTeamsWithInfo(season_year = '2020-21', season_type = 'Regular%20Season'):

    teams = dict()

    # Start browser
    browser = webdriver.Chrome(ChromeDriverManager().install())

    for groupBy_key, groupBy_url in groupBy.items():
        url = 'https://www.nba.com/standings?Section=overall'  + groupBy_url + '&Season=' + season_year # + '&SeasonType=' + season_type
        browser.get(url)

        tables = browserutils.loadTeamPage(browser)
        for table in tables:
            getTeamsInfo(table.text, teams)

    # Close browser
    browser.quit()

    if(len(teams) != 30):
        print("Error. Only loaded {} teams. Retrying...".format(len(teams)))
        initTeamsWithInfo()
    else:  
        # Return initialized teams
        return teams


def getTeamsInfo(table, teams):

    rank = 1
    isTeamNotinDict = False

    # Parse statistic table
    for row, info in enumerate(table.split('\n')):

        # Throwaway junk lines (column names)
        if row > 0:

            data = info.split(' ')

            # Grab Team Name
            if((len(data) == 2 or len(data) == 3)):
                if info not in teams:
                    # print(info)  # Team Name
                    team = info.upper()
                    teams[team] = Team()
                    isTeamNotinDict = True
                else:
                    isTeamNotinDict = False

            # Grab Team's Respective Stats
            elif(len(data) == 12 and isTeamNotinDict):
                # print(info)  # Team Stats
                # print()

                # Create iterator
                itr = itertools.count()

                overall_w = data[next(itr)]
                teams[team].overall['W'] = int(overall_w)

                overall_l = data[next(itr)]
                teams[team].overall['L'] = int(overall_l)

                win_pct = data[next(itr)]
                teams[team].win_pct = float(win_pct)

                games_back = data[next(itr)]
                if games_back == '--':
                    teams[team].games_back = float()
                else:
                    teams[team].games_back = float(games_back)

                conf = data[next(itr)].split('-')

                conf_w = conf[0]
                teams[team].conference['W'] = int(conf_w)

                conf_l = conf[1]
                teams[team].conference['L'] = int(conf_l)

                div = data[next(itr)].split('-')

                div_w = div[0]
                teams[team].division['W'] = int(div_w)

                div_l = div[0]
                teams[team].division['L'] = int(div_l)

                home = data[next(itr)].split('-')

                home_w = home[0]
                teams[team].division['W'] = int(home_w)

                home_l = home[1]    
                teams[team].division['L'] = int(home_l)

                road = data[next(itr)].split('-')

                road_w = road[0]
                teams[team].road['W'] = int(road_w)

                road_l = road[1]
                teams[team].road['L'] = int(road_l)

                ot = data[next(itr)].split('-')

                ot_w = ot[0]
                teams[team].ot['W'] = int(ot_w)

                ot_l = ot[1]
                teams[team].ot['L'] = int(ot_l)

                last10 = data[next(itr)].split('-')

                last10_w = last10[0]
                teams[team].last10['W'] = int(last10_w)

                last10_l = last10[1]
                teams[team].last10['L'] = int(last10_l)

                streak_result = data[next(itr)]
                streak_num = data[next(itr)]
                streak = streak_result + streak_num
                teams[team].streak = str(streak)
        

def getDivisionRank(table, teams):

    for row, info in enumerate(table.split('\n')):

        # Throwaway table header
        if (row > 0) and (re.search(r'\s[\w\s]+\s', info)):
            (rank, team) = formatTeamInfo(info.upper())
            teams[team].division_rank = int(rank)
