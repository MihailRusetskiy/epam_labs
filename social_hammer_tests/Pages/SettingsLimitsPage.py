import random
import time
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Utils.helpers import push_random_int


class SettingsLimitsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.BASE_URL = "http://new.socialhammer.com"
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

        self.input_values = []
        self.input_values_after_refresh = []

    def open_page(self):
        self.driver.get(self.BASE_URL)
        time.sleep(1)
        self.driver.find_element(*self._settings_menu_item).click()
        time.sleep(1)
        self.driver.find_element(*self._limits_menu_item).click()
        time.sleep(1)

    def check_all_checkboxes(self):
        self.driver.find_element(*self._instagram_is).click()
        self.driver.find_element(*self._instagram_like_is).click()
        self.driver.find_element(*self._instagram_following_is).click()
        self.driver.find_element(*self._instagram_unfollowing_is).click()
        self.driver.find_element(*self._vk_is).click()
        self.driver.find_element(*self._vk_invitations_friends_is).click()
        self.driver.find_element(*self._vk_like_is).click()
        self.driver.find_element(*self._vk_invitations_group_friends_is).click()

    def fill_all_inputs_random_values(self):
        self.driver.find_element(*self._instagram_like_value).send_keys(push_random_int(5, 15, self.input_values))
        self.driver.find_element(*self._instagram_following_value).send_keys(push_random_int(5, 15, self.input_values))
        self.driver.find_element(*self._instagram_unfollowing_value).send_keys(push_random_int(5, 15, self.input_values))
        self.driver.find_element(*self._vk_invitations_friends_value).send_keys(push_random_int(5, 15, self.input_values))
        self.driver.find_element(*self._vk_like_value).send_keys(push_random_int(5, 15, self.input_values))
        self.driver.find_element(*self._vk_invitations_group_friends_value).send_keys(push_random_int(5, 15, self.input_values))

    def get_all_inputs_values(self):
        self.input_values_after_refresh.append(self.driver.find_element(*self._instagram_like_value).text)
        self.input_values_after_refresh.append(self.driver.find_element(*self._instagram_following_value).text)
        self.input_values_after_refresh.append(self.driver.find_element(*self._instagram_unfollowing_value).text)
        self.input_values_after_refresh.append(self.driver.find_element(*self._vk_invitations_friends_value).text)
        self.input_values_after_refresh.append(self.driver.find_element(*self._vk_like_value).text)
        self.input_values_after_refresh.append(self.driver.find_element(*self._vk_invitations_group_friends_value).text)
        return self.input_values_after_refresh





