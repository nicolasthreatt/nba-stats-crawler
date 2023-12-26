from parser import parse
from selenium import webdriver
from utils import browserutils
from utils.filters import groupBy
from webdriver_manager.chrome import ChromeDriverManager


# Browse to Page with Team Info
def initialize(season_year = '2020-21', season_type = 'Regular%20Season'):

    teams = dict()

    # Start browser
    browser = webdriver.Chrome(ChromeDriverManager().install())

    for groupBy_key, groupBy_url in groupBy.items():
        url = 'https://www.nba.com/standings?Section=overall'  + groupBy_url + '&Season=' + season_year # + '&SeasonType=' + season_type
        browser.get(url)

        tables = browserutils.loadTeamPage(browser)
        for table in tables:
            parse(table.text, teams)

    # Close browser
    browser.quit()

    # Recurisve (TODO: IMPROVE)
    if(len(teams) != 30):
        print("Error. Only loaded {} teams. Retrying...".format(len(teams)))
        initialize()
    else:  
        # Return initialized teams
        return teams
