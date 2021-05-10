from selenium import webdriver
from test_pages.login_page import LoginPage
import time


BASE_URL = 'http://localhost:3000/login'

TEST_USER_EMAIL = '9IpvH4@issue-tracking.com'
TEST_USER_PASSWORD = 'aDLulorTZq'
EXISTING_PROJECT_NAME = 'My First Project'

INVALID_USER_EMAIL = 'invalid_user@gmail.com'
INVALID_USER_PASSWORD = 'invalid_password'
NOT_EXISTING_PROJECT_NAME = 'Not Existing Project'


def get_web_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    return webdriver.Chrome(options=options)


def run_tests():
    driver = get_web_driver()
    driver.get(BASE_URL)

    login_page = LoginPage(driver)

    login_page.type_email(INVALID_USER_EMAIL)
    login_page.type_password(INVALID_USER_PASSWORD)
    login_page.submit_login_expecting_failure()

    projects_page = login_page.login_as(TEST_USER_EMAIL, TEST_USER_PASSWORD)
    time.sleep(2)

    projects_names = projects_page.get_projects_names()
    projects_page.expect_project_exists(EXISTING_PROJECT_NAME)
    projects_page.expect_project_not_exists(NOT_EXISTING_PROJECT_NAME)

    issues_page = projects_page.open_project(0)
    time.sleep(2)

    issues_page.expect_project_name(projects_names[0])
    driver.close()


if __name__ == '__main__':
    try:
        run_tests()
        print('All tests were passed successfully')
    except Exception as e:
        print('An exception was thrown during running tests: ' + str(e))
