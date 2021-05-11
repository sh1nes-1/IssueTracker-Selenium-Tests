from selenium.webdriver.remote.webdriver import WebDriver

from utils import wait_for_element, wait_for_element_disappeared

PROJECT_NAME_SELECTOR = 'header div.title div.ant-space-item'
PROJECT_NAME_SKELETON_SELECTOR = '.ant-skeleton.project-title'
ELEMENT_VISIBLE_TIMEOUT = 2


class SettingsPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_project_name(self):
        wait_for_element(self.driver, PROJECT_NAME_SKELETON_SELECTOR, timeout=ELEMENT_VISIBLE_TIMEOUT)
        wait_for_element_disappeared(self.driver, PROJECT_NAME_SKELETON_SELECTOR, timeout=ELEMENT_VISIBLE_TIMEOUT)
        project_name_element = self.driver.find_element_by_css_selector(PROJECT_NAME_SELECTOR)

        return project_name_element.text
