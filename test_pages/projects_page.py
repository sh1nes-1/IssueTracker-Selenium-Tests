from selenium.webdriver.remote.webdriver import WebDriver

from test_pages.issues_page import IssuesPage
from utils import wait_url_changed, wait_for_element

PROJECT_LINK_SELECTOR = 'div.ant-col a'
PROJECT_NAME_SELECTOR = 'div.ant-card-meta-title'
REDIRECT_TIMEOUT = 3
ELEMENT_VISIBLE_TIMEOUT = 2


class ProjectsPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_projects_names(self):
        wait_for_element(self.driver, PROJECT_NAME_SELECTOR, timeout=ELEMENT_VISIBLE_TIMEOUT)
        projects_names_elements = self.driver.find_elements_by_css_selector(PROJECT_NAME_SELECTOR)

        return [x.text for x in projects_names_elements]

    def open_project(self, project_index):
        wait_for_element(self.driver, PROJECT_LINK_SELECTOR, timeout=ELEMENT_VISIBLE_TIMEOUT)
        projects_links_elements = self.driver.find_elements_by_css_selector(PROJECT_LINK_SELECTOR)

        current_url = self.driver.current_url
        projects_links_elements[project_index].click()

        wait_url_changed(self.driver, current_url, timeout=REDIRECT_TIMEOUT)
        return IssuesPage(self.driver)
