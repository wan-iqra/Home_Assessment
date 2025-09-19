from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InvoicesPage:
    def __init__(self, driver):
        self.driver = driver
        # page element locators
        self.invoice_heading = (By.TAG_NAME, "h1") # main heading
        self.invoice_table = (By.CSS_SELECTOR, "table.table.table-hover")
        self.details_link = (By.CSS_SELECTOR, "a.btn.btn-sm.btn-primary")

    def invoices_title(self):
        """get invoices heading"""
        wait = WebDriverWait(self.driver, 10)
        heading = wait.until(EC.visibility_of_element_located(self.invoice_heading))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.invoice_table))
        return heading.text.strip()


    def inv20250000023details(self):
        """click details button"""
        self.driver.find_elements(*self.details_link)[2].click()
