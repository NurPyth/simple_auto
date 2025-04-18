from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

button_selector = (By.ID, 'submit-id-submit')
result_selector = (By.ID, 'result-text')

class SimpleButtonPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        return self.browser.get('https://www.qa-practice.com/elements/button/simple')

    def button(self):
        return self.find(button_selector)

    def button_is_displayed(self):
        return self.button().is_displayed()

    def click_button(self):
        wait = WebDriverWait(self.browser, 10)  # Wait up to 10 seconds
        button = wait.until(EC.element_to_be_clickable(self.button()))
        return button.click()

    def result(self):
        return self.find(result_selector)

    @property
    def result_text(self):
        return self.result().text
