from selenium.webdriver.common.by import By
from pages.like_a_button import LikeAButton

def test_button2_exist(browser):
    Like_a_button = LikeAButton(browser)
    Like_a_button.open()
    assert Like_a_button.button_is_displayed

def test_button2_clicked(browser):
    Like_a_button = LikeAButton(browser)
    Like_a_button.open()
    Like_a_button.click_button()
    assert 'Submitted' == Like_a_button.result_text

