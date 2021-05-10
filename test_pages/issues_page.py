from selenium.webdriver.remote.webdriver import WebDriver

ISSUES_URL_PART = '/dashboard/issues'
PROJECT_NAME_SELECTOR = 'header div.title div.ant-space-item'


class IssuesPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

        if ISSUES_URL_PART not in self.driver.current_url:
            raise Exception('This is not an issues page')

    def expect_project_name(self, project_name):
        project_name_element = self.driver.find_element_by_css_selector(PROJECT_NAME_SELECTOR)
        if project_name_element.text != project_name:
            raise Exception('Project name is not matching')
