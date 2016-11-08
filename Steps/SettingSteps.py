import time
from Utils.helpers import *
from Steps.Steps import get_driver
from Pages.SettingsActivityPage import SettingsActivityPage
from Pages.SettingsLimitsPage import SettingsLimitsPage
from Pages.SettingsInstagramWhiteListPage import SettingsInstagramWhiteListPage


# кликает на случайные переключатели настроек активности
def change_active_state_button():
    settings_active_page = SettingsActivityPage(get_driver())
    settings_active_page.open_page()
    settings_active_page.number_of_changed_buttons = 12
    settings_active_page.check_activity_state_button(settings_active_page.button_state_before_clicks)
    settings_active_page.change_button_state()
    settings_active_page.check_activity_state_button(settings_active_page.button_state_after_clicks)
    return settings_active_page


# проверяет изменилось ли положение переключателей активности
def is_active_state_button_changed(settings_active_page):
    time.sleep(2)
    settings_active_page.driver.refresh()
    time.sleep(1)
    settings_active_page.check_activity_state_button(settings_active_page.button_state_after_refresh)
    return settings_active_page.is_equals_button_lists(settings_active_page.button_state_after_clicks,
                                                       settings_active_page.button_state_after_refresh)

# изменяет состояние переключателей настроек лимитов
def change_limits_state():
    limits_page = SettingsLimitsPage(get_driver())
    limits_page.open_page()
    limits_page.check_all_checkboxes()
    limits_page.fill_all_inputs_random_values()


# проверяет изменилось ли положение переключателей лимитов
def is_limits_page_changed():
    limits_page = SettingsLimitsPage(get_driver())
    limits_page.driver.refresh()
    inputs_after_refresh = limits_page.get_all_inputs_values()
    counter = len(limits_page.input_values)
    compare_res = True
    while counter:
        counter -= 1
        if limits_page.input_values[counter] != inputs_after_refresh[counter]:
            compare_res = False
    return compare_res


# добавляет заданный аккаунт в список белых инстаграмм аккаунтов
def add_account_to_instagram_white_list(account):
    white_page = SettingsInstagramWhiteListPage(get_driver())
    white_page.open_page()
    white_page.add_account_to_instagram_white_list(account)


# возвращает коллекцию инстаграмм аккаунтов на странице
def get_instagram_white_accounts():
    white_page = SettingsInstagramWhiteListPage(get_driver())
    white_page.open_page()
    return white_page.get_instagram_white_account()
