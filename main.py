from selenium import webdriver
from test_pages.login_page import LoginPage


BASE_URL = 'http://localhost:3000/login'
TEST_USER_EMAIL = '9IpvH4@issue-tracking.com'
TEST_USER_PASSWORD = 'aDLulorTZq'


def get_web_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    return webdriver.Chrome(options=options)


def run_tests():
    driver = get_web_driver()
    driver.get(BASE_URL)

    login_page = LoginPage(driver)

    login_page.type_email('invalid_user@gmail.com')
    login_page.type_password('invalid_password')
    login_page.submit_login_expecting_failure()

    projects_page = login_page.login_as(TEST_USER_EMAIL, TEST_USER_PASSWORD)


if __name__ == '__main__':
    try:
        run_tests()
        print('All tests were passed successfully')
    except Exception as e:
        print('An exception was thrown during running tests: ' + str(e))