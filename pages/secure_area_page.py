from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SecureAreaPage:
    def __init__(self, driver):
        self.driver = driver
        # page element locators
        self.jane_doe = (By.XPATH, '//a[normalize-space(text())="Jane Doe"]') # user profile
        self.my_account = (By.TAG_NAME, "h1") # main heading
        self.menu_button = (By.ID, "menu") # hamburger menu
        self.logout_button = (By.CSS_SELECTOR, "[data-test='nav-sign-out']") # sign out button
        self.invoice_button = (By.CSS_SELECTOR, "[data-test='nav-invoices']")

    def jane_doe_account(self):
        """wait for and return the user account name: 'Jane Doe'"""
        wait = WebDriverWait(self.driver, 10)
        account = wait.until(EC.visibility_of_element_located(self.jane_doe))
        return account.text.strip()

    def get_my_account(self):
        """wait for and return the main account page heading 'my account'"""
        wait = WebDriverWait(self.driver, 10)
        account = wait.until(EC.visibility_of_element_located(self.my_account))
        return account.text.strip()

    def logout(self):
        """click the menu button and then sign out"""
        self.driver.find_element(*self.menu_button).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.logout_button))
        self.driver.find_element(*self.logout_button).click()

    def go_to_invoices(self):
        """click the invoice button"""
        self.driver.find_element(*self.invoice_button).click()
        WebDriverWait(self.driver, 3)