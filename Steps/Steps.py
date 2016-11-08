import time
from Utils.driver.DriverInstance import DriverInstance
from Utils.helpers import *
from Pages.LoginPage import LoginPage
from Pages.RegisterPage import RegisterPage
from Pages.UsefulToolsPage import UsefulToolsPage
from Pages.StartPage import StartPage
from Pages.NewsPage import NewsPage
from Pages.ProfilePage import ProfilePage

balance = '$0,01'         # допустимый баланс на странице профиль
tariff_plan = 'Master'    # допустимый тариф на странице профиль


# получить webdriver
def get_driver():
    return DriverInstance.get_instance()


# завершить работу с webdriver
def dispose_driver():
    DriverInstance.get_instance().quit()


# вход в систему по логину и паролю
def login(login, password):
    if not is_logged(login):
        login_page = LoginPage(get_driver())
        login_page.open_page()
        login_page.login(login, password)


# проверка удалось ли войти в систему
def is_logged(login):
    login_page = LoginPage(get_driver())
    return login in login_page.get_current_login()


# регистация нового пользователя
def register(name, email, phone):
    register_page = RegisterPage(get_driver())
    register_page.open_page()
    register_page.register(name, email, phone)


# проверка наличия на странице Полезные инстументы контента
def is_useful_tools_page_present():
    useful_tools_page = UsefulToolsPage(get_driver())
    useful_tools_page.open_page()
    return useful_tools_page.is_header_present() and useful_tools_page.is_content_present()


# проверка наличия на страице сводная информация контента
def is_summary_info_present():
    start_page = StartPage(get_driver())
    start_page.open_page()
    balance = start_page.get_balance()
    tp = start_page.get_tp()
    paid_days = start_page.get_paid_days()
    work_task_count = start_page.get_work_task()
    added_account_count = start_page.get_added_counts()

    return balance and tp and paid_days and work_task_count and added_account_count


# проверка наличия на странице новости контента
def is_news_content_present():
    news_page = NewsPage(get_driver())
    news_page.open_page()
    return news_page.get_header() != '' and news_page.get_content() != ''


# проверка наличия блока баланс на странице профиль
def is_profile_page_balance_block_present():
    profile = ProfilePage(get_driver())
    profile.open_page()
    return profile.get_balance() == balance and profile.is_balance_icon_present() and profile.is_balance_discount_present() and profile.is_balance_pay_button_present()


# проверка наличия блока тариф на странице профиль
def is_profile_page_tp_block_present():
    profile = ProfilePage(get_driver())
    profile.open_page()
    return profile.get_tp() == tariff_plan and profile.is_tp_icon_present()


# проверка наличия блока настройки на странице профиль
def is_profile_page_settings_block_present():
    profile = ProfilePage(get_driver())
    profile.open_page()
    return profile.is_settings_icon_present() and profile.is_settings_change_login_button_present() and profile.is_settings_change_password_button_present() and profile.is_settings_delete_account_button_present()


# выход из системы
def logout():
    page = StartPage(get_driver())
    page.logout()
