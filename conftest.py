import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())


@pytest.fixture()
def initiate_Driver():
    driver.get("https://open.spotify.com/")
    driver.maximize_window()
    yield driver
    driver.quit()


