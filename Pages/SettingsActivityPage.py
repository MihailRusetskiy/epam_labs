import random
import time
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class SettingsActivityPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.BASE_URL = "http://dev.socialhammer.com/setting/activity"
        # локаторы
        self._settings_menu_item = (By.XPATH, '//a[@title="Настройки"]')
        self._activity_menu_item = (By.XPATH, '//a[@title="Активность"]')
        self._trs = (By.XPATH, '//table[@id="activity_settings"]//tbody//tr')
        self.button_state_before_clicks = []
        self.button_state_after_clicks = []
        self.button_state_after_refresh = []
        self.number_of_changed_buttons = 12

    # открывает текущую страницу
    def open_page(self):
        self.driver.get(self.BASE_URL)
        time.sleep(2)
        self.logger.info("открыта страница настроек активности")

    # возвращает состояние переключателей активности
    def check_activity_state_button(self, button_state):
        table_rows = self.driver.find_elements(*self._trs)  # коллекция строк таблицы
        for table_row in table_rows:
            table_tds = table_row.find_elements_by_tag_name("td")

            c = table_tds[1].find_element_by_tag_name("span").get_attribute("class")
            if table_tds[1].find_element_by_tag_name("span").get_attribute("class").find(" on") > 0:  # если у переключателя есть класс on
                button_state.append(1)  # помечаем переключатель как отмеченный
            else:
                button_state.append(0)  # помечаем переключатель как неомеченный

            if table_tds[3].find_element_by_tag_name("span").get_attribute("class").find(" on") > 0:  # если у переключателя есть класс on
                button_state.append(1)  # помечаем переключатель как отмеченный
            else:
                button_state.append(0)  # помечаем переключатель как неомеченный
                
        self.logger.info("получено состояние переключателей активности")
        return button_state

    # сравнивает два списка состояния переключателей активности
    def is_equals_button_lists(self, list1, list2):
        button_index = len(list1)
        compare_res = 1

        while button_index:  # в цикле проверяем элементы списков до первого несовпадения
            button_index -= 1
            if list1[button_index] != list2[button_index]:
                compare_res = 0
                break

        self.logger.info("выполнено сравнение списов состояние переключателей активности")
        return compare_res

    # изменяет случайно состояие переключателей активности
    def change_button_state(self):
        table_rows = self.driver.find_elements(*self._trs)  # коллекция строк таблицы
        while self.number_of_changed_buttons:
            self.number_of_changed_buttons-=1
            changed_row_number = random.randint(0, len(table_rows)-1)  # выбираем случайную строку
            slider_buttons = table_rows[changed_row_number].find_elements_by_class_name("slider-button")
            numer_of_changed_button = random.randint(0, len(slider_buttons)-1)  # выбираем случайный переключатель в строке
            changed_button = slider_buttons[numer_of_changed_button]
            changed_button.click()  # изменяем положение случайного переключателя
        self.logger.info("случайным образом изменено состояние 12 переключателей активности")
