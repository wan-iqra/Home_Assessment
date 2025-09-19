import configparser
import allure

from pages.invoices.INV20250000023_page import INV20250000023Page
from pages.login_page import LoginPage
from pages.secure_area_page import SecureAreaPage
from pages.invoices_page import InvoicesPage


@allure.id("TC0005")
@allure.feature("Workflow")
@allure.title("View Invoice Details and Extract Data")
@allure.description("Opens a specific invoice to verify the listed products.")
def test_worfklow_1(driver):
    # 1. load credentials and URLs from config file
    config = configparser.ConfigParser()
    config.read("config/config.ini")
    email = config["credentials"]["email"]
    password = config["credentials"]["password"]
    login_url = config["urls"]["login_page"]

    # 2. initialize page objects
    login_page = LoginPage(driver)
    secure_page = SecureAreaPage(driver)
    invoice_page = InvoicesPage(driver)
    inv20250000023_page = INV20250000023Page(driver)

    # 3. perform login on Login Page
    login_page.load(login_url)
    login_page.login(email, password)

    # 4. verify successful login
    assert secure_page.jane_doe_account() == "Jane Doe"
    assert secure_page.get_my_account() == "My account"
    assert "account" in driver.current_url

    # 5. go to invoices page
    secure_page.go_to_invoices()

    # 6. verify invoices page
    assert invoice_page.invoices_title() == "Invoices"
    assert 'INV-20250000023' in driver.page_source

    # 7. open invoice details for INV-20250000025
    invoice_page.inv20250000023details()

    # 8. verify product name
    assert inv20250000023_page.get_slip_join_plier() == "Slip Joint Pliers"

    # 9. log out after test
    secure_page.logout()