import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from pages.home_page import HomePage
import os
from time import sleep

@pytest.fixture
def driver():
    app_path = os.path.abspath("app/wikipedia.apk")
    options = UiAutomator2Options().load_capabilities({
        "platformName": "Android",
        "deviceName": "Android Emulator",
        "appPackage": "org.wikipedia.alpha",
        "appActivity": "org.wikipedia.DefaultIcon",
        "noReset": False,
        "fullReset": False
    })
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    yield driver
    driver.quit()

def test_wikipedia_flow(driver):
    home = HomePage(driver)
    sleep(2)
    
    # Étapes du test
    home.swipe_carousel(times=3)
    home.click_get_started()
    home.search_city("Lydia")
    home.click_search_result("Lydia")
    home.dismiss_popup()
    home.change_language("Français")
    home.open_about_section()
    home.open_in_new_tab("Crésus")
    home.go_to_new_tab()
    
    sleep(2)
