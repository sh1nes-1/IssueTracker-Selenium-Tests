from selenium.webdriver.remote.webdriver import WebDriver

from test_pages.issues_page import IssuesPage
from utils import wait_url_changed

PROJECTS_URL_PART = '/dashboard/projects'
PROJECT_LINK_SELECTOR = 'div.ant-col a'
PROJECT_NAME_SELECTOR = 'div.ant-card-meta-title'
REDIRECT_TIMEOUT = 3


class ProjectsPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

        if PROJECTS_URL_PART not in self.driver.current_url:
            raise Exception('This is not a projects page')

    def get_projects_names(self):
        project_names = []

        projects_names_elements = self.driver.find_elements_by_css_selector(PROJECT_NAME_SELECTOR)
        for x in projects_names_elements:
            project_names.append(x.text)

        return project_names

    def expect_project_exists(self, project_name):
        project_names = self.get_projects_names()
        if project_name not in project_names:
            raise Exception('Project does not exists')

    def open_project(self, project_index):
        projects_links_elements = self.driver.find_elements_by_css_selector(PROJECT_LINK_SELECTOR)

        if project_index >= len(projects_links_elements):
            raise Exception('Invalid index of project')

        current_url = self.driver.current_url
        projects_links_elements[project_index].click()

        is_project_opened = wait_url_changed(self.driver, current_url, timeout=REDIRECT_TIMEOUT)
        if not is_project_opened:
            raise Exception('Failed to open project page')

        return IssuesPage(self.driver)
