from selenium.webdriver.remote.webdriver import WebDriver
from test_pages.projects_page import ProjectsPage
from utils import wait_url_changed, clear_input, wait_for_element


EMAIL_FIELD_SELECTOR = '#email'
PASSWORD_FIELD_SELECTOR = '#password'
SUBMIT_BUTTON_SELECTOR = 'button[type=submit]'
FORM_ERRORS_SELECTOR = '.ant-form-item-explain-error'
REDIRECT_TIMEOUT = 3
ELEMENT_VISIBLE_TIMEOUT = 2


class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def type_email(self, email):
        wait_for_element(self.driver, EMAIL_FIELD_SELECTOR, timeout=ELEMENT_VISIBLE_TIMEOUT)
        email_field = self.driver.find_element_by_css_selector(EMAIL_FIELD_SELECTOR)

        clear_input(email_field)
        email_field.send_keys(email)

        return LoginPage(self.driver)

    def type_password(self, password):
        wait_for_element(self.driver, PASSWORD_FIELD_SELECTOR, timeout=ELEMENT_VISIBLE_TIMEOUT)
        password_field = self.driver.find_element_by_css_selector(PASSWORD_FIELD_SELECTOR)

        clear_input(password_field)
        password_field.send_keys(password)

        return LoginPage(self.driver)

    def login_as(self, email, password):
        self.type_email(email)
        self.type_password(password)

        return self.submit_login_expecting_success()

    def submit_login_expecting_success(self):
        current_url = self.driver.current_url
        self._submit_login()
        wait_url_changed(self.driver, current_url, timeout=REDIRECT_TIMEOUT)

        return ProjectsPage(self.driver)

    def submit_login_expecting_failure(self):
        self._submit_login()

        return LoginPage(self.driver)

    def get_form_errors(self):
        wait_for_element(self.driver, FORM_ERRORS_SELECTOR, timeout=ELEMENT_VISIBLE_TIMEOUT)
        form_errors_elements = self.driver.find_elements_by_css_selector(FORM_ERRORS_SELECTOR)

        return [x.text for x in form_errors_elements]

    def _submit_login(self):
        wait_for_element(self.driver, SUBMIT_BUTTON_SELECTOR, timeout=ELEMENT_VISIBLE_TIMEOUT)
        submit_button = self.driver.find_element_by_css_selector(SUBMIT_BUTTON_SELECTOR)
        submit_button.click()
