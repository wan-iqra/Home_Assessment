from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class INV20250000023Page:
    def __init__(self, driver):
        self.driver = driver
        # page element locators
        self.invoice_date = (By.CSS_SELECTOR, 'input[data-test="invoice-date"]')
        self.slip_joint_cell = (By.XPATH, "//td[contains(normalize-space(), 'Slip Joint Pliers')]")

    def invoice_date_input(self):
        """get invoice date"""
        invoice_date_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.invoice_date))
        return invoice_date_input.get_attribute("value")

    def get_slip_join_plier(self):
        """get product slip joining plier"""
        plier = self.driver.find_elements(*self.slip_joint_cell)[0]
        return plier.text.strip()
