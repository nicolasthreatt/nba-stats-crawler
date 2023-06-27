"""
ROSTERS
"""

# Load up all packages
import itertools
import sys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from utils import browserutils
 
mascots = [
#            City              Mascot
         [ "ATLANTA",          "HAWKS"         ],
         [ "BROOKLYN",         "NETS"          ],
         [ "BOSTON",           "CELTICS"       ],
         [ "CHARLOTTE",        "HORNETS"       ],
         [ "CHICAGO",          "BULLS"         ],
         [ "CLEVELAND",        "CAVALIERS"     ],
         [ "DALLAS",           "MAVERICKS"     ],
         [ "DENVER",           "NUGGETS"       ],
         [ "DETROIT",          "PISTONS"       ],
         [ "GOLDEN STATE",     "WARRIORS"      ],
         [ "HOUSTON",          "ROCKETS"       ],
         [ "INDIANA",          "PACERS"        ],
         [ "LA",               "CLIPPERS"     ],
         [ "LOS ANGELES",      "LAKERS"       ],
         [ "MEMPHIS",          "GRIZZLIES"    ],
         [ "MIAMI",            "HEAT"         ],
         [ "MILWAUKEE",        "BUCKS"        ],
         [ "MINNESOTA",        "TIMBERWOLVES" ],
         [ "NEW ORLEANS",      "PELICANS"     ],
         [ "NEW YORK",         "KNICKS"       ],
         [ "OKLAHOMA CITY",    "THUNDER"      ],
         [ "ORLANDO",          "MAGIC"        ],
         [ "PHILADELPHIA",     "SIXERS"       ],
         [ "PHOENIX",          "SUNS"         ],
         [ "PORTLAND",         "Blazers"      ],
         [ "SACRAMENTO",       "KINGS"        ],
         [ "SAN ANTONIO",      "SPURS"        ],
         [ "TORONTO",          "RAPTORS"      ],
         [ "UTAH",             "JAZZ"         ],
         [ "WASHINGTON",       "WIZARDS"      ],
]

# Team class to hold each team's roster
class Team:
    def __init__(self, team, player = None):
        self.team = team
        self.players = []

    def getTeam(self):
        return (self.team)


# Player info class
class rosterPlayers:
    def __init__(self):
        self.name       = str() # Name
        self.number     = int() # Jersey Number
        self.height     = str() # Height
        self.weight     = int() # Weight
        self.position   = str() # Position
        self.birthdate  = str() # Birthdate
        self.age        = int() # Age
        self.experience = str() # Experience
        self.school     = str() # School


# Collect stats    
def getPlayersInfo(team, players):

    num_players = 0

    for player in players:
        for key, value in player.items():

            # Add player
            team.rosterPlayers.append(rosterPlayers())

            if key == "PLAYER":
                team.rosterPlayers[num_players].name = str(value.strip())

            elif key == "#":
                team.rosterPlayers[num_players].number = int(value) if value else int(-1)

            elif key == "POS":
                team.rosterPlayers[num_players].position = str(value)

            elif key == "HEIGHT":
                team.rosterPlayers[num_players].height = str(value)

            elif key == "WEIGHT":
                team.rosterPlayers[num_players].weight = int(value.strip(' lbs'))

            elif key == "BIRTHDATE":
                team.rosterPlayers[num_players].birthdate = str(value)

            elif key == "AGE":
                team.rosterPlayers[num_players].age = int(value)

            elif key == "EXP":
                team.rosterPlayers[num_players].experience = value

            elif key == "SCHOOL":
                team.rosterPlayers[num_players].school = str(value)

            else:
                sys.exit("Error. Invalid key")

        num_players += 1


def collectTraditionalRosters(teams=None, season_year = '2019-20', season_type = 'Regular%20Season'):

    # Start browser
    browser = webdriver.Chrome(ChromeDriverManager().install())

    for team in teams:
        teams[team].addTable('rosterPlayers', list())

        for team_info in mascots:

            # Get Team Info
            city         = team_info[0]
            mascot       = team_info[1]

            if (city + ' ') in team:

                # URL to teams roster
                url = 'https://www.nba.com/teams/' + mascot.lower()
                browser.get(url)
                # Load stat page HERE (TODO: Create function in browserutils.py)

                # Scrape stats
                roster_table = browser.find_element_by_class_name("MockStatsTable_statsTable__2edDg")
                players      = browserutils.loadPlayerInfo(roster_table)

                # Store Roster Info
                getPlayersInfo(teams[team], players)

                # TODO: Move to Debug Directory (Need to create)
                # print()
                # print(url)
                # for player in players:
                #     for k, v in player.items():
                #         print(k, ": ", v)
                #     print()

    # Close browser
    browser.quit()
