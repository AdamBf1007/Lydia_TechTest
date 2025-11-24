from appium import webdriver
from appium.options.android import UiAutomator2Options
from time import sleep
import os
from pages.home_page import HomePage

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

home = HomePage(driver)
sleep(2)

# Étapes du test
home.swipe_carousel(times=3)        # swiper 3 fois (je pense que je pourrais également compter les petits points de l'IHM pour swipe le nombre de fois voulu)
home.click_get_started()            # cliquer sur Get Started
home.search_city("Lydia")           # rechercher "Lydia"
home.click_search_result("Lydia")   # cliquer dessus
home.dismiss_popup()                # fermer popup si présent
home.change_language("Français")    # changer la langue
home.open_about_section()           # scroll via le raccourcis à droite
home.open_in_new_tab("Crésus")      # cliquer sur Crésus et l'ouvrir dans un nouvel onglet
home.go_to_new_tab()                # aller sur le dernier onglet de la liste

sleep(5)
driver.quit()
