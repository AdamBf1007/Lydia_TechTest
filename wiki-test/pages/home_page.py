from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class HomePage:
    def __init__(self, driver):
        self.driver = driver

 
    def swipe_carousel(self, times=5):
        size = self.driver.get_window_size()
        start_x = size['width'] * 0.8
        end_x = size['width'] * 0.2
        y = size['height'] * 0.5
        for _ in range(times):
            self.driver.swipe(start_x, y, end_x, y, 800)
            sleep(1)

    # Cliquer sur Get Started (après le carrousel)
    def click_get_started(self):
        self.driver.find_element(AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_done_button").click()
        sleep(2)

    # Recherche d'une ville
    def search_city(self, name):
        self.driver.find_element(AppiumBy.ID, "org.wikipedia.alpha:id/search_container").click()
        self.driver.find_element(AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text").send_keys(name)
        sleep(2)

    # Cliquer sur un résultat de recherche
    def click_search_result(self, text):
        element = self.driver.find_element(
            AppiumBy.XPATH, f"//android.widget.TextView[contains(@text, '{text}')]"
        )
        element.click()
        sleep(2)
    

    # Fermer popup si présent
    def dismiss_popup(self):
        try:
            self.driver.find_element(AppiumBy.ID, "org.wikipedia.alpha:id/closeButton").click()
        except:
            pass

    def change_language(self, language):
        # 1. Ouvrir le menu des langues
        self.driver.find_element(
            AppiumBy.ID, 
            "org.wikipedia.alpha:id/page_language"
        ).click()
        sleep(2)

        # 2. Ouvrir la recherche (bouton loupe)
        self.driver.find_element(
            AppiumBy.XPATH,
            "//android.view.View[3]//android.widget.Button"
        ).click()
        sleep(1)

        # 3. Champ de recherche Compose
        search_input = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.view.View").instance(1)'
        )
        sleep(1)

        # 3. Taper le texte via mobile: type
        self.driver.execute_script("mobile: type", {"text": "Français"})
        sleep(1)

        self.click_on(language)
        sleep(1)

    # Cliquer sur un élément par texte
    def click_on(self, text):
        sleep(1)
        self.driver.find_element(AppiumBy.XPATH, f"//android.widget.TextView[@text='{text}']").click()

    def open_in_new_tab(self, name):
        # Cliquer sur l’élément dynamique
        self.driver.find_element(
            AppiumBy.XPATH,
            f"//*[@text='{name}']"
        ).click()

        # Attendre l'apparition du bouton "Ouvrir dans un nouvel onglet"
        wait = WebDriverWait(self.driver, 10)
        new_tab_btn = wait.until(
            EC.presence_of_element_located((
                AppiumBy.ID,
                "org.wikipedia.alpha:id/link_preview_secondary_button"
            ))
        )

        # Cliquer sur le bouton
        new_tab_btn.click()
        sleep(1)


    def go_to_new_tab(self):
        wait = WebDriverWait(self.driver, 10)

        # Cliquer sur le bouton des onglets 
        tabs_button = wait.until(
            EC.presence_of_element_located(
                (AppiumBy.ID, "org.wikipedia.alpha:id/page_toolbar_button_tabs")
            )
        )
        tabs_button.click()
        sleep(1)

        # Sélectionner le dernier onglet ouvert
        all_tabs = wait.until(
            EC.presence_of_all_elements_located(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("org.wikipedia.alpha:id/tabContainer")')
            )
        )

        # Le nouvel onglet est toujours le dernier de la liste
        all_tabs[-1].click()
        sleep(1)

    def open_about_section(self):
        # Cliquer sur Contents
        self.driver.find_element(
            AppiumBy.ID,
            "org.wikipedia.alpha:id/page_contents"
        ).click()
        sleep(1)

        scroller = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().scrollable(true)'
        )

        target_text = "À propos de cet article"

        # Scroll jusqu'à trouver la ligne
        while True:
            elements = self.driver.find_elements(
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().text("{target_text}")'
            )

            if elements:
                elements[0].click()
                sleep(1)
                break

            # Scroll du menu Contents
            self.driver.execute_script(
                "mobile: scrollGesture",
                {
                    "elementId": scroller.id,
                    "direction": "down",
                    "percent": 0.85,
                    "speed": 1200
                }
            )
            sleep(0.4)

        # Une fois dans "À propos de cet article" → scroller 1 fois
        size = self.driver.get_window_size()

        start_x = size["width"] * 0.5
        start_y = size["height"] * 0.75
        end_y   = size["height"] * 0.25

        self.driver.swipe(start_x, start_y, start_x, end_y, 500)
