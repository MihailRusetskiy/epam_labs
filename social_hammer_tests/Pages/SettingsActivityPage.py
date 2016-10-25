import random
import time
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class SettingsActivityPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.BASE_URL = "http://new.socialhammer.com"
        self._settings_menu_item = (By.XPATH, '//a[@title="Настройки"]')
        self._activity_menu_item = (By.XPATH, '//a[@title="Активность"]')
        self._trs = (By.XPATH, '//table[@id="activity_settings"]//tbody//tr')

        self.button_state_before_clicks = []
        self.button_state_after_clicks = []
        self.button_state_after_refresh = []
        self.number_of_changed_buttons = 12

    def open_page(self):
        self.driver.get(self.BASE_URL)
        self.driver.find_element(*self._settings_menu_item).click()
        time.sleep(1)
        self.driver.find_element(*self._activity_menu_item).click()
        time.sleep(2)

    def check_activity_state_button(self, button_state):
        table_rows = self.driver.find_elements(*self._trs)
        for table_row in table_rows:
            table_tds = table_row.find_elements_by_tag_name("td")

            c = table_tds[1].find_element_by_tag_name("span").get_attribute("class")
            if table_tds[1].find_element_by_tag_name("span").get_attribute("class").find(" on") > 0:
                button_state.append(1)
            else:
                button_state.append(0)

            if table_tds[3].find_element_by_tag_name("span").get_attribute("class").find(" on") > 0:
                button_state.append(1)
            else:
                button_state.append(0)

        return button_state

    def is_equals_button_lists(self, list1, list2):
        button_index = len(list1)
        compare_res = 1

        while button_index:
            button_index -= 1
            if list1[button_index] != list2[button_index]:
                compare_res = 0
                break

        return compare_res

    def change_button_state(self):
        table_rows = self.driver.find_elements(*self._trs)
        while self.number_of_changed_buttons:
            self.number_of_changed_buttons-=1
            changed_row_number = random.randint(0, len(table_rows)-1)
            slider_buttons = table_rows[changed_row_number].find_elements_by_class_name("slider-button")
            numer_of_changed_button = random.randint(0, len(slider_buttons)-1)
            changed_button = slider_buttons[numer_of_changed_button]
            changed_button.click()
