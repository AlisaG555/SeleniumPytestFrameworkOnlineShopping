import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def login_password():
    username = "standard_user"
    password = "secret_sauce"
    return (username,password)


@pytest.fixture(scope="module")
def driver():
    _driver = webdriver.Chrome()
    yield _driver
    _driver.quit()
