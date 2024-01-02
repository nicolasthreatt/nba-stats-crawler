from teams.parser import parse
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.filters import groupBy


# Browse to Page with Team Info
def initialize(season_year = '2020-21', season_type = 'Regular%20Season'):
    teams = dict()

    # Start browser
    browser = webdriver.Chrome()

    for groupBy_key, groupBy_url in groupBy.items():
        url = 'https://www.nba.com/standings?Section=overall'  + groupBy_url + '&Season=' + season_year + '&SeasonType=' + season_type
        browser.get(url)

        tables = browser.find_elements(By.CLASS_NAME, "Crom_table__p1iZz")
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
