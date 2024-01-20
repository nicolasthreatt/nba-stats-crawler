from itertools import cycle
from rosters.tables.rosters import RosterPlayer
from selenium import webdriver
from selenium.webdriver.common.by import By
from teams.tables.team import Team
from webdriver_manager.chrome import ChromeDriverManager
from utils.browsertools import load_stat_table_page
from utils.mappings import nba_team_ids


def create_roster(teams: dict = None, season_year: str = '2019-20') -> None:
    """Create a roster for each team.

    Args:
        teams (dict): Dictionary of teams and their corresponding RosterTeam objects.
        season_year (str): Season year in the format 'YYYY-YY'.
        season_type (str): Type of season (e.g., 'Regular%20Season').
    """

    with webdriver.Chrome() as browser:

        for team in teams:
            teamId = nba_team_ids[team]

            url = 'https://www.nba.com/stats/team/' + str(teamId) + '?Season=' + season_year
            browser.get(url)
        
            headers = load_stat_table_page(browser).find_element(By.CLASS_NAME, 'Crom_headers__mzI_m').find_elements(By.TAG_NAME, 'th')
            rows    = load_stat_table_page(browser).find_element(By.CLASS_NAME, 'Crom_body__UYOcU').find_elements(By.TAG_NAME, 'td')
        
            players, bio = set(), dict()
            for header, data in zip(cycle(headers), rows):
                bio[header.text.strip()] = data.text.strip()
                if len(bio) == len(headers):
                    players.add(tuple(bio.items()))
                    bio.clear()

            add_players(teams[team], players)

    browser.quit()

  
def add_players(team: Team, players: set) -> None:
    """Add player information to the team's roster.

    Args:
        team (Team): The team to which players are added.
        players (set): Set of player dictionaries containing information.
    """

    for roster_num, player in enumerate(players):
        for key, value in dict(player).items():

            team.players.append(RosterPlayer())
            if key == "PLAYER":
                team.players[roster_num].name = str(value.strip())

            elif key == "NO.":
                team.players[roster_num].number = int(value.replace('#', '') or -1)

            elif key == "POS":
                team.players[roster_num].position = str(value)

            elif key == "HEIGHT":
                team.players[roster_num].height = str(value)

            elif key == "WEIGHT":
                team.players[roster_num].weight = int(value.strip(' lbs'))

            elif key == "BIRTHDATE":
                team.players[roster_num].birthdate = str(value)

            elif key == "AGE":
                team.players[roster_num].age = int(value)

            elif key == "EXP":
                team.players[roster_num].experience = str(value)

            elif key == "SCHOOL":
                team.players[roster_num].school = str(value)

            elif key == "HOW ACQUIRED":
                team.players[roster_num].school = str(value)

            else:
                exit("Error. Invalid key: {}".format(key))
