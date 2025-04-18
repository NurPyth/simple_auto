from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')
    options.add_argument("--no-sandbox")
    chrome_browser = webdriver.Chrome(options=options)
    chrome_browser.implicitly_wait(3)
    return chrome_browser