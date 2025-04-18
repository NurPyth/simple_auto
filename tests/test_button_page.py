from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, 'submit-id-submit')))
        browser.get_screenshot_as_file("screenshots/error.png")
    with allure.step("Click the button"):
        simple_page.click_button()
    with allure.step("Check the result"):
        assert 'Submitted' == simple_page.result_text
