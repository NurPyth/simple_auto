from selenium.webdriver.common.by import By
from pages.simple_button import  SimpleButtonPage
import allure


@allure.feature("Simple button")
@allure.story("existence")
def test_button1_exist(browser):
    with allure.step("Open Simple button page"):
        simple_page = SimpleButtonPage(browser)
        simple_page.open()
    with allure.step("Check the button"):
        assert simple_page.button_is_displayed()

@allure.story("clickability")
@allure.feature("Simple button")
def test_button1_clicked(browser):
    with allure.step("Open Simple button page"):
        simple_page = SimpleButtonPage(browser)
        simple_page.open()
    with allure.step("Click the button"):
        simple_page.click_button()
    with allure.step("Check the result"):
        assert 'Submitted' == simple_page.result_text

def test_me():
    assert 1 == 1
