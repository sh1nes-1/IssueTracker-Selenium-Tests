from selenium.webdriver.remote.webdriver import WebDriver
from test_pages.projects_page import ProjectsPage
from utils import wait_url_changed, clear_input

LOGIN_URL_PART = '/login'
EMAIL_FIELD_SELECTOR = '#email'
PASSWORD_FIELD_SELECTOR = '#password'
SUBMIT_BUTTON_SELECTOR = 'button[type=submit]'
REDIRECT_TIMEOUT = 3


class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

        if LOGIN_URL_PART not in self.driver.current_url:
            raise Exception('This is not a login page')

    def type_email(self, email):
        email_field = self.driver.find_element_by_css_selector(EMAIL_FIELD_SELECTOR)

        clear_input(email_field)
        email_field.send_keys(email)

        return LoginPage(self.driver)

    def type_password(self, password):
        password_field = self.driver.find_element_by_css_selector(PASSWORD_FIELD_SELECTOR)

        clear_input(password_field)
        password_field.send_keys(password)

        return LoginPage(self.driver)

    def login_as(self, email, password):
        self.type_email(email)
        self.type_password(password)

        return self.submit_login_expecting_success()

    def submit_login_expecting_success(self):
        is_success_login = self._try_submit_login()

        if not is_success_login:
            raise Exception('Expected login success but url is not changed')

        return ProjectsPage(self.driver)

    def submit_login_expecting_failure(self):
        is_success_login = self._try_submit_login()

        if is_success_login:
            raise Exception('Expected login failure but url is changed')

        return LoginPage(self.driver)

    def _try_submit_login(self):
        current_url = self.driver.current_url

        submit_button = self.driver.find_element_by_css_selector(SUBMIT_BUTTON_SELECTOR)
        submit_button.click()

        return wait_url_changed(self.driver, current_url, timeout=REDIRECT_TIMEOUT)
