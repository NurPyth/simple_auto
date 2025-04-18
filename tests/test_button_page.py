from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from pages.simple_button import  SimpleButtonPage

def test_button1_exist(browser):
    simple_page = SimpleButtonPage(browser)
    simple_page.open()
    assert simple_page.button_is_displayed()

def test_button1_clicked(browser):
    simple_page = SimpleButtonPage(browser)
    simple_page.open()
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, 'submit-id-submit')))
    simple_page.click_button()
    assert 'Submitted' == simple_page.result_text
