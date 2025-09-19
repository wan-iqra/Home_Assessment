from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # page element locators
        self.email_input = (By.ID, "email")
        self.password_input = (By.ID, "password")
        self.login_button = (By.CLASS_NAME, "btnSubmit")
        self.error_login = (By.CLASS_NAME, "help-block") # login error
        self.invalid_email = (By.CSS_SELECTOR, "[data-test='email-error']") # invalid email format

    def load(self, url):
        """navigate to the login page."""
        self.driver.get(url)

    def login(self, email, password):
        """fill in credentials and submit the login form"""
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def invalid_login(self):
        """wait for and return a general login error message"""
        wait = WebDriverWait(self.driver, 5)  # wait up to 5 seconds
        error_element = wait.until(EC.visibility_of_element_located(self.error_login))
        return error_element.text.strip()

    def invalid_email_format(self):
        """wait for and return an invalid email format error"""
        wait = WebDriverWait(self.driver, 5)  # wait up to 5 seconds
        error_element = wait.until(EC.visibility_of_element_located(self.invalid_email))
        return error_element.text.strip()