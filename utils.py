from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys


def wait_url_changed(driver, old_url, timeout):
    try:
        WebDriverWait(driver, timeout).until(EC.url_changes(old_url))
    except TimeoutException:
        return False
    return True


def clear_input(element):
    element.send_keys(Keys.CONTROL + "a")
    element.send_keys(Keys.DELETE)
