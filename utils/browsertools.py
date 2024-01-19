import re
from itertools import cycle
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def load_stat_table_page(browser, table_html_class="Crom_table__p1iZz", timeout=30):
    try:
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
        
        WebDriverWait(browser, timeout).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        
        return WebDriverWait(browser, timeout, ignored_exceptions=ignored_exceptions).until(
            EC.presence_of_element_located((By.CLASS_NAME, table_html_class))
        )
    except TimeoutException:
        print("Timed out waiting for page to load")
        return None


def find_team_name(text):
    """
    Extracts and concatenates the City and Mascot from a given text containing team information.

    Args:
        text (str): The input text containing team information.

    Returns:
        str: A string containing the concatenated City and Mascot information.
    """
    # Pattern for cases where the City and Mascot are both in title case
    pattern1 = r'^([A-Za-z\s]+)\s([A-Za-z\s]+)'

    # Pattern for cases where the City starts with an uppercase letter and
    # the mascot starts with a number (i.e. 76ers)
    pattern2 = r'^([A-Z][A-Za-z\s]+)\s(\d+\s?[A-Za-z]+)'

    matches = [match for match in re.findall(f'{pattern1}|{pattern2}', text) if any(match)]
    team = ' '.join([' '.join(match) for match in matches])

    return team.strip()
