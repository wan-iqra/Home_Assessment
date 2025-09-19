import configparser
import allure

from pages.login_page import LoginPage
from pages.secure_area_page import SecureAreaPage


@allure.id("TC0001")
@allure.feature("Login")
@allure.title("Valid User Login")
@allure.description("Login into page using valid email and valid password")
def test_valid_login(driver):
    # load credentials and URLs from config file
    config = configparser.ConfigParser()
    config.read("config/config.ini")

    email = config["credentials"]["email"]
    password = config["credentials"]["password"]
    login_url = config["urls"]["login_page"]

    # initialize page objects
    login_page = LoginPage(driver)
    secure_page = SecureAreaPage(driver)

    # perform login
    login_page.load(login_url)
    login_page.login(email, password)

    # assert that user is logged in successfully
    assert secure_page.jane_doe_account() == "Jane Doe"
    assert secure_page.get_my_account() == "My account"
    assert "account" in driver.current_url

    # log out after test
    secure_page.logout()


@allure.id("TC0002")
@allure.feature("Login")
@allure.title("Invalid Email Format")
@allure.description("Login into page using invalid email format, but valid password")
def test_invalid_email_format(driver):
    # load credentials and URLs from config file
    config = configparser.ConfigParser()
    config.read("config/config.ini")

    email = config["invalid_email"]["email"]
    password = config["credentials"]["password"]
    login_url = config["urls"]["login_page"]

    # perform login
    login_page = LoginPage(driver)
    login_page.load(login_url)
    login_page.login(email, password)

    # assert that user failed to log in due to invalid email format
    assert login_page.invalid_email_format() == "Email format is invalid"


@allure.id("TC0003")
@allure.feature("Login")
@allure.title("Invalid Email")
@allure.description("Login into page using invalid email, but valid password")
def test_invalid_email(driver):
    # load credentials and URLs from config file
    config = configparser.ConfigParser()
    config.read("config/config.ini")

    email = config["invalid_credentials"]["email"]
    password = config["credentials"]["password"]
    login_url = config["urls"]["login_page"]

    # initialize page objects
    login_page = LoginPage(driver)

    # perform login
    login_page.load(login_url)
    login_page.login(email, password)

    # assert that user failed to log in due to invalid credentials
    assert login_page.invalid_login() == "Invalid email or password"


@allure.id("TC0004")
@allure.feature("Login")
@allure.title("Invalid Password")
@allure.description("Login into page using valid email, but invalid password")
def test_invalid_password(driver):
    # load credentials and URLs from config file
    config = configparser.ConfigParser()
    config.read("config/config.ini")

    email = config["credentials"]["email"]
    password = config["invalid_credentials"]["password"]
    login_url = config["urls"]["login_page"]

    # initialize page objects
    login_page = LoginPage(driver)

    # perform login
    login_page.load(login_url)
    login_page.login(email, password)

    # assert that user failed to log in due to invalid credentials
    assert login_page.invalid_login() == "Invalid email or password"
