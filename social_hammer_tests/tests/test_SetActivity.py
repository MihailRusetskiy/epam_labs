import time
import unittest
from helpers.helpers import *


class SetActivity(unittest.TestCase):
    def test_set_activity(self):

        number_of_changed_buttons = 12

        driver = register()

        menu_settings = driver.find_element_by_class_name("nav-pills").find_elements_by_tag_name("li")[13]
        menu_settings.click()

        time.sleep(1)
        activity_menu_item = menu_settings.find_elements_by_tag_name("li")[0]
        activity_menu_item.click()

        button_state_before_clicks = []
        button_state_after_clicks = []
        button_state_after_refresh = []
        table = driver.find_element_by_id("activity_settings")
        table_rows = table.find_element_by_tag_name("tbody").find_elements_by_tag_name("tr")

        check_active_state_button(table_rows, button_state_before_clicks)

        while number_of_changed_buttons:
            number_of_changed_buttons-=1
            changed_row_number = random.randint(0, len(table_rows)-1)
            slider_buttons = table_rows[changed_row_number].find_elements_by_class_name("slider-button")
            numer_of_changed_button = random.randint(0, len(slider_buttons)-1)
            changed_button = slider_buttons[numer_of_changed_button]
            changed_button.click()

        check_active_state_button(table_rows, button_state_after_clicks)

        if is_equals_button_lists(button_state_before_clicks, button_state_after_clicks) == 1:
            return 0
        else:
            time.sleep(2)
            driver.refresh()

        table = driver.find_element_by_id("activity_settings")
        table_rows = table.find_element_by_tag_name("tbody").find_elements_by_tag_name("tr")
        check_active_state_button(table_rows, button_state_after_refresh)

        self.assertTrue(is_equals_button_lists(button_state_after_clicks, button_state_after_refresh))

        driver.quit()
