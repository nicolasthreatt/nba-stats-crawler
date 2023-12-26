from parser import parse
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from utils import browserutils
from utils.mappings import mascots


def scraper(teams: dict = None, season_year: str = '2019-20', season_type: str = 'Regular%20Season'):
    # Start browser
    browser = webdriver.Chrome(ChromeDriverManager().install())

    # TODO: DICTIONARY/HASHMAP MIGHT BE MORE EFFICIENT (O(30) vs. O(30^2))
    for team in teams:
        teams[team].addTable('roster', list())

        for team_info in mascots:

            # Get Team Info
            city, mascot = team_info
            if (city + ' ') in team:
                # URL to teams roster
                url = 'https://www.nba.com/teams/' + mascot.lower()
                browser.get(url)

                # Scrape stats (TODO: MIGHT NEED TO REDO)
                roster_table = browser.find_element_by_class_name("MockStatsTable_statsTable__2edDg")
                players      = browserutils.loadPlayerInfo(roster_table)

                # Store Roster Info
                parse(teams[team], players)

    # Close browser
    browser.quit()
