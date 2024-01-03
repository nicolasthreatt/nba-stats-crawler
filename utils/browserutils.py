'''
BROWSER UTILS
'''


from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import itertools
import sys


def loadPageToComplete(browser):
    timeout = 30
    try:
        WebDriverWait(browser, 30).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    except TimeoutException:
        sys.exit('TimeoutException')      # TODO: Add to debug log
    except NoSuchElementException:
        sys.exit('NoSuchElementException') # TODO: Add to debug log


def loadTeamPage(browser, locator="//*[@class='StandingsGridRender_standingsContainer__2EwPy']"):
    timeout = 30
    try:
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
        WebDriverWait(browser, 30).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        return WebDriverWait(browser, 30,ignored_exceptions=ignored_exceptions)\
                            .until(EC.presence_of_all_elements_located((By.XPATH, locator)))
    except TimeoutException:
        print("Timed out waiting for page to load")


def loadTeamsPlayersPage(browser, locator="//*[@class='StandingsGridRender_standingsContainer__2EwPy']"):
    timeout = 30
    try:
        # ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
        WebDriverWait(browser, 30).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        # return WebDriverWait(browser, 30,ignored_exceptions=ignored_exceptions)\
        #                     .until(EC.presence_of_element_located((By.XPATH, locator)))
    except TimeoutException:
        print("Timed out waiting for page to load")


def loadStatTable(browser, rank=None):

    table = None
    timeout = 20   # seconds
    try:
        WebDriverWait(browser, timeout).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')

        element_present = EC.presence_of_element_located((By.XPATH, "//*[@stats-no-data-msg='noData && !isLoading']"))
        WebDriverWait(browser, timeout).until(element_present)

        if len(browser.find_element_by_xpath("//*[@stats-no-data-msg='noData && !isLoading']").text) == 0:
            browser.implicitly_wait(timeout)
            if rank is None:
                table = browser.find_element_by_class_name('nba-stat-table__overflow').text
            else:
                table = browser.find_element_by_class_name('nba-stat-table__overlay').text

        return table

    except TimeoutException:
        print('TimeoutException')      # TODO: Add to debug log
        return None

    except NoSuchElementException:
        print('NoSuchElementException') # TODO: Add to debug log
        return None


def loadPlayerInfo(browser, mode="rosters"):
    table = None
    timeout = 20   # seconds
    try:
        headers = browser.find_element(By.CLASS_NAME, "Crom_table__p1iZz").find_elements(By.TAG_NAME, 'th')
        rows    = browser.find_element(By.CLASS_NAME, "Crom_table__p1iZz").find_elements(By.TAG_NAME, 'td')
        # print(rows)

        table   = dict()
        players = list()
        i = 0
        for row in rows:
            header = headers[i].text
            table[header.strip()] = row.text.lstrip()
            i += 1
    
            if header == 'SCHOOL' and mode == 'rosters':  # END OF ROW
                players.append(table)
                table = dict()
                i = 0

        if mode == 'rosters':
            return players
        elif mode == 'bios':
            return table
        else:
            sys.exit("Error. Invalid mode {}".format(mode))

    except TimeoutException:
        print('TimeoutException')      # TODO: Add to debug log
        return None

    except NoSuchElementException:
        print('NoSuchElementException') # TODO: Add to debug log
        return None


# def loadPlayersList(browser):

#     players = None
#     timeout = 20   # seconds
#     try:
#         WebDriverWait(browser, timeout).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')

#         players = browser.find_elements_by_class_name('players-list__name')
#         return players

#     except TimeoutException:
#         print('TimeoutException')      # TODO: Add to debug log
#         return None

#     except NoSuchElementException:
#         print('NoSuchElementException') # TODO: Add to debug log
#         return None


def loadTeamRosters(browser):

    table = None
    timeout = 20   # seconds
    try:

        WebDriverWait(browser, timeout).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')

        jersey_nums = browser.find_elements_by_class_name('nba-player-trending-item__number')
        names = browser.find_elements_by_class_name('nba-player-index__name')
        position_height_weight = browser.find_elements_by_class_name('nba-player-index__details')

        return (jersey_nums, names, position_height_weight)

    except TimeoutException:
        # print('TimeoutException')      # TODO: Add to debug log
        return None

    except NoSuchElementException:
        # print('NoSuchElementException') # TODO: Add to debug log
        return None