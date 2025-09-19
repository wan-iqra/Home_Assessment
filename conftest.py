import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Set up Chrome browser options
    options = webdriver.ChromeOptions()

    # optional: remove if you do not want to see browser
    # options.add_argument("--headless")

    # optional: maximized for consistent layout rendering
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    # optional: remove if you want to find elements without delay
    driver.implicitly_wait(1)

    # provide the driver to the test
    yield driver

    # teardown: close the browser after each test
    driver.quit()
