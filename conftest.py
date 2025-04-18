from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')
    chrome_browser = webdriver.Chrome(options=options)
    chrome_browser.maximize_window()
    chrome_browser.implicitly_wait(5)
    return chrome_browser