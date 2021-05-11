from selenium import webdriver
from test_pages.login_page import LoginPage


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

    # login page tests
    login_page = LoginPage(driver)

    login_page.type_email(INVALID_USER_EMAIL)
    login_page.type_password(INVALID_USER_PASSWORD)
    login_page.submit_login_expecting_failure()

    form_errors = login_page.get_form_errors()
    assert len(form_errors) > 0

    projects_page = login_page.login_as(TEST_USER_EMAIL, TEST_USER_PASSWORD)

    # projects page tests
    projects_names = projects_page.get_projects_names()
    assert EXISTING_PROJECT_NAME in projects_names
    assert NOT_EXISTING_PROJECT_NAME not in projects_names

    # issues page tests
    issues_page = projects_page.open_project(0)
    assert issues_page.get_project_name() == projects_names[0]

    # settings page tests
    project_settings_page = issues_page.open_project_settings()
    assert project_settings_page.get_project_name() == projects_names[0]

    print('All tests were passed successfully')
    input()


if __name__ == '__main__':
    try:
        run_tests()
    except Exception as e:
        print('An exception was thrown during running tests: ' + str(e))
