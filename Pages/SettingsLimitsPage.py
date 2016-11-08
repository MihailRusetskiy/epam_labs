import time
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Utils.helpers import push_random_int


class SettingsLimitsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.BASE_URL = "http://dev.socialhammer.com/setting/account-limit"
        # локаторы
        self._settings_menu_item = (By.XPATH, '//a[@title="Настройки"]')
        self._limits_menu_item = (By.XPATH, '//a[@title="Контроль лимитов"]')

        self._instagram_is = (By.XPATH, '//input[@name="user.setting_account_limit.instagram_is"]')
        self._instagram_like_is = (By.XPATH, '//input[@name="user.setting_account_limit.instagram_like_is"]')
        self._instagram_following_is = (By.XPATH, '//input[@name="user.setting_account_limit.instagram_following_is"]')
        self._instagram_unfollowing_is = (By.XPATH, '//input[@name="user.setting_account_limit.instagram_unfollowing_is"]')
        self._vk_is = (By.XPATH, '//input[@name="user.setting_account_limit.vk_is"]')
        self._vk_invitations_friends_is = (By.XPATH, '//input[@name="user.setting_account_limit.vk_invitations_friends_is"]')
        self._vk_like_is = (By.XPATH, '//input[@name="user.setting_account_limit.vk_like_is"]')
        self._vk_invitations_group_friends_is = (By.XPATH, '//input[@name="user.setting_account_limit.vk_invitations_group_friends_is"]')

        self._instagram_like_value = (By.XPATH, '//input[@name="user.setting_account_limit.instagram_like_value"]')
        self._instagram_following_value = (By.XPATH, '//input[@name="user.setting_account_limit.instagram_following_value"]')
        self._instagram_unfollowing_value = (By.XPATH, '//input[@name="user.setting_account_limit.instagram_unfollowing_value"]')
        self._vk_invitations_friends_value = (By.XPATH, '//input[@name="user.setting_account_limit.vk_invitations_friends_value"]')
        self._vk_like_value = (By.XPATH, '//input[@name="user.setting_account_limit.vk_like_value"]')
        self._vk_invitations_group_friends_value = (By.XPATH, '//input[@name="user.setting_account_limit.vk_invitations_group_friends_value"]')

        # списки для хранения состояний инпутов до и после перезагрузки страницы
        self.input_values = []
        self.input_values_after_refresh = []

    # открывает текущую страницу
    def open_page(self):
        self.driver.get(self.BASE_URL)
        time.sleep(1)
        self.logger.info("открыта страница настроек лимитов")

    # кликает на все чекбоксы
    def check_all_checkboxes(self):
        self.driver.find_element(*self._instagram_is).click()
        self.driver.find_element(*self._instagram_like_is).click()
        self.driver.find_element(*self._instagram_following_is).click()
        self.driver.find_element(*self._instagram_unfollowing_is).click()
        self.driver.find_element(*self._vk_is).click()
        self.driver.find_element(*self._vk_invitations_friends_is).click()
        self.driver.find_element(*self._vk_like_is).click()
        self.driver.find_element(*self._vk_invitations_group_friends_is).click()
        self.logger.info("отмечены все чекбоксы на странице настройки ограничений")

    # заполняет все инпуты случайными значениями
    def fill_all_inputs_random_values(self):
        self.driver.find_element(*self._instagram_like_value).send_keys(push_random_int(5, 15, self.input_values))
        self.driver.find_element(*self._instagram_following_value).send_keys(push_random_int(5, 15, self.input_values))
        self.driver.find_element(*self._instagram_unfollowing_value).send_keys(push_random_int(5, 15, self.input_values))
        self.driver.find_element(*self._vk_invitations_friends_value).send_keys(push_random_int(5, 15, self.input_values))
        self.driver.find_element(*self._vk_like_value).send_keys(push_random_int(5, 15, self.input_values))
        self.driver.find_element(*self._vk_invitations_group_friends_value).send_keys(push_random_int(5, 15, self.input_values))
        self.logger.info("поля были зпролнены случайными значеиями на странице настройки лимитов")
        
    # получает значения всех инпутов
    def get_all_inputs_values(self):
        self.input_values_after_refresh.append(self.driver.find_element(*self._instagram_like_value).text)
        self.input_values_after_refresh.append(self.driver.find_element(*self._instagram_following_value).text)
        self.input_values_after_refresh.append(self.driver.find_element(*self._instagram_unfollowing_value).text)
        self.input_values_after_refresh.append(self.driver.find_element(*self._vk_invitations_friends_value).text)
        self.input_values_after_refresh.append(self.driver.find_element(*self._vk_like_value).text)
        self.input_values_after_refresh.append(self.driver.find_element(*self._vk_invitations_group_friends_value).text)
        self.logger.info("получено значение всех полей ввода на странице настройки лимитов")
        return self.input_values_after_refresh
        