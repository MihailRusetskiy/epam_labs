import time

from helpers.helpers import *


def register(driver, domain):
    try:
        driver.get(domain)

        register_button = driver.find_element_by_class_name("btn-danger")
        register_button.click()

        agree_rules_checkbox = driver.find_element_by_class_name("checkbox").find_element_by_tag_name("input")
        agree_rules_checkbox.click()

        input_email = driver.find_elements_by_class_name("form-control")[1]
        input_email.send_keys(generate_random_emails(1,7)[0])

        register_button = driver.find_elements_by_class_name("btn-block")[1]
        register_button.click()

        time.sleep(2)
        register_phone_button = driver.find_element_by_id("form_register_phone").find_element_by_class_name("btn-block")
        register_phone_button.click()

        time.sleep(2)
        page_header_text = driver.find_element_by_class_name("pageheader").text.strip()

        if page_header_text == "Добро пожаловать в SocialHammer!":
            return 1
        return 0

    except Exception:
        return 0


def login(driver, domain):
    try:
        username = ""
        password = ""

        driver.get(domain)

        login_input = driver.find_elements_by_class_name("form-control")[0]
        login_input.send_keys(username)

        password_input = driver.find_elements_by_class_name("form-control")[1]
        password_input.send_keys(password)

        login_button = driver.find_element_by_class_name("btn-block")
        login_button.click()

        time.sleep(1)
        page_header_text = driver.find_element_by_class_name("pageheader").text.strip()

        if page_header_text == "Сводная информация":
            return 1
        return 0

    except Exception:
        return 0


def add_vk_account(driver, domain):
    try:
        time.sleep(1)

        if register(driver, domain):
            account_name = get_random_string(5)
            accpunt_password = get_random_string(5)

            menu_accounts = driver.find_element_by_class_name("nav-pills").find_elements_by_tag_name("li")[3]
            menu_accounts.click()

            time.sleep(2)
            skip_intro_button = driver.find_element_by_class_name("introjs-button")
            skip_intro_button.click()

            time.sleep(1)
            add_vk_menu_item = menu_accounts.find_elements_by_tag_name("a")[2]
            add_vk_menu_item.click()

            time.sleep(2)
            button_add = driver.find_element_by_class_name("action_account_add")
            button_add.click()

            time.sleep(1)
            add_one_vk = driver.find_element_by_class_name("action_account_add_one")
            add_one_vk.click()

            time.sleep(1)
            close_notification_no_proxy = driver.find_element_by_class_name("onConfirmClose")
            close_notification_no_proxy.click()

            time.sleep(2)
            modal_window = driver.find_element_by_class_name("modal-content")
            login_input = modal_window.find_elements_by_class_name("form-control")[0]
            login_input.send_keys(account_name)

            password_input = modal_window.find_elements_by_class_name("form-control")[1]
            password_input.send_keys(accpunt_password)

            dont_change_proxy_checkbox = modal_window.find_element_by_class_name("checkbox")
            dont_change_proxy_checkbox.click()

            add_vk_acc = modal_window.find_element_by_class_name("btn-primary")
            add_vk_acc.click()

            time.sleep(2)
            close_button = modal_window.find_element_by_class_name("btn-default")
            close_button.click()

            time.sleep(2)

            added_account = driver.execute_script(
                open("/home/hpx/PycharmProjects/bot/helpers/js/find_vk_instagram_accounts_on_page.js").read() +
                "return find('account_vk_load');")

            if account_name == added_account:
                return 1

        return 0

    except Exception:
        return 0


def add_instagram_account(driver, domain):
    try:
        time.sleep(1)

        if register(driver, domain):
            account_name = get_random_string(5)
            accpunt_password = get_random_string(5)

            menu_accounts = driver.find_element_by_class_name("nav-pills").find_elements_by_tag_name("li")[3]
            menu_accounts.click()

            time.sleep(2)
            skip_intro_button = driver.find_element_by_class_name("introjs-button")
            skip_intro_button.click()

            time.sleep(1)
            add_instagram_menu_item = menu_accounts.find_elements_by_tag_name("a")[1]
            add_instagram_menu_item.click()

            time.sleep(2)
            button_add = driver.find_element_by_class_name("action_account_add")
            button_add.click()

            time.sleep(1)
            close_notification_no_proxy = driver.find_element_by_class_name("onConfirmClose")
            close_notification_no_proxy.click()

            time.sleep(2)
            modal_window = driver.find_element_by_class_name("modal-content")
            login_input = modal_window.find_elements_by_class_name("form-control")[0]
            login_input.send_keys(account_name)

            password_input = modal_window.find_elements_by_class_name("form-control")[1]
            password_input.send_keys(accpunt_password)

            dont_change_proxy_checkbox = modal_window.find_element_by_class_name("checkbox")
            dont_change_proxy_checkbox.click()

            add_instagram_acc = modal_window.find_element_by_class_name("btn-primary")
            add_instagram_acc.click()

            time.sleep(2)
            close_button = modal_window.find_element_by_class_name("btn-default")
            close_button.click()

            time.sleep(2)

            added_account = driver.execute_script(
                open("/home/hpx/PycharmProjects/bot/helpers/js/find_vk_instagram_accounts_on_page.js").read() +
                "return find('account_instagram_load');")

            if account_name == added_account:
                return 1

        return 0

    except Exception:
        return 0


def set_activity(driver, domain):
    try:
        number_of_changed_buttons = 12

        register(driver, domain)

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

        if is_equals_button_lists(button_state_after_clicks, button_state_after_refresh):
            return 1
        else:
            return 0

    except Exception:
        return 0


def add_to_white_list(driver, domain):
    try:

        register(driver, domain)
        account = get_random_string(8)

        menu_settings = driver.find_element_by_class_name("nav-pills").find_elements_by_tag_name("li")[13]
        menu_settings.click()

        time.sleep(1)
        activity_menu_item = menu_settings.find_elements_by_tag_name("li")[7]
        activity_menu_item.click()

        time.sleep(2)
        add_button = driver.find_element_by_id("main-content").find_element_by_class_name("dropdown-toggle")
        add_button.click()

        time.sleep(1)
        add_one = driver.find_element_by_id("main-content").find_element_by_class_name("action_add")
        add_one.click()

        time.sleep(2)
        input_login = driver.find_element_by_id("form_add").find_element_by_class_name("form-control")
        input_login.send_keys(account)
        add_modal_button = driver.find_element_by_id("window_modal").find_element_by_class_name("btn-primary")
        add_modal_button.click()

        time.sleep(3)
        added_account = driver.execute_script(
            open("/home/hpx/PycharmProjects/bot/helpers/js/find_vk_instagram_accounts_on_page.js").read() +
            "return find('setting_account_instagram_white_load');")

        time.sleep(3)
        if added_account.strip() == account:
            return 1
        else:
            return 0

    except Exception:
        return 0


def check_news_page(driver, domain):
    try:

        header_is_present = 0
        content_is_present = 0

        register(driver, domain)

        menu_settings = driver.find_element_by_class_name("nav-pills").find_elements_by_tag_name("li")[1]
        menu_settings.click()

        time.sleep(1)
        page_header = driver.find_element_by_class_name("pageheader").text
        if page_header == "Новости сервиса":
            header_is_present = 1

        page_content = driver.find_element_by_id("main-content").find_element_by_class_name("panel-default").text
        if page_content != "":
            content_is_present = 1

        if content_is_present and header_is_present:
            return 1
        else:
            return 0

    except Exception:
        return 0


def check_start_page(driver, domain):
    try:
        register(driver, domain)

        header_is_present = 0
        balance_found = 0
        tp_found = 0
        paid_days_found = 0
        tasks_found = 0
        accounts_found = 0

        menu_settings = driver.find_element_by_class_name("nav-pills").find_elements_by_tag_name("li")[0]
        menu_settings.click()

        time.sleep(2)
        page_header = driver.find_element_by_class_name("pageheader").text
        if page_header == "Сводная информация":
            header_is_present = 1

        main_content_div = driver.find_element_by_id("main-content")

        balance_block = main_content_div.find_element_by_class_name("col-md-3")
        balance_block.find_element_by_class_name("icon-wallet")
        balance = balance_block.find_element_by_class_name("total").text
        if balance.find("$")+1:
            balance_found = 1
        balance_title = balance_block.find_element_by_class_name("title").text
        if balance_title != "Ваш баланс":
            balance_found = 0

        tp_block = main_content_div.find_element_by_class_name("col-md-6")
        tp_block.find_element_by_class_name("icon-bar-chart")
        tp_title = tp_block.find_element_by_class_name("title").text
        if tp_title == "Тарифный план":
            tp_found = 1

        paid_days_block = main_content_div.find_elements_by_class_name("col-md-3")[1]
        paid_days_block.find_element_by_class_name("icon-clock")
        int(paid_days_block.find_element_by_class_name("total").text)
        paid_days_title = paid_days_block.find_element_by_class_name("title").text
        if paid_days_title == "Оплаченных дней":
            paid_days_found = 1

        tasks_work_block = main_content_div.find_elements_by_class_name("col-md-6")[1]
        tasks_work_block.find_element_by_class_name("icon-rocket")
        int(tasks_work_block.find_element_by_class_name("total").text)
        tasks_title = tasks_work_block.find_element_by_class_name("title").text
        if tasks_title == "Работающих задач":
            tasks_found = 1

        added_accounts = main_content_div.find_elements_by_class_name("col-md-6")[2]
        added_accounts.find_element_by_class_name("icon-users")
        int(added_accounts.find_element_by_class_name("total").text)
        accounts_title = added_accounts.find_element_by_class_name("title").text
        if accounts_title == "Добавлено аккаунтов" or accounts_title == "Добавлено аккаунта":
            accounts_found = 1

        if accounts_found and balance_found and tp_found and tasks_found and paid_days_found and header_is_present:
            return 1
        else:
            return 0

    except Exception:
        return 0


def check_profile_page(driver, domain):
    try:
        register(driver, domain)

        header_found = 0
        current_balance_title_found = 0
        tp_block_found = 0

        dropdown_button = driver.find_element_by_class_name("dropdown-toggle")
        dropdown_button.click()

        time.sleep(1)
        profile_button = driver.find_element_by_class_name("dropdown-menu").find_element_by_tag_name("li")
        profile_button.click()

        time.sleep(1)
        page_header = driver.find_element_by_class_name("pageheader").text
        if page_header == "Профиль":
            header_found = 1

        balance_block = driver.find_element_by_id("main-content").find_elements_by_class_name("col-md-12")[1]
        balance_block.find_element_by_class_name("icon-wallet")
        current_balance = balance_block.find_elements_by_class_name("text-center")[0].text
        if current_balance.find("Ваш баланс: $")+1:
            current_balance_title_found = 1

        tp_block = driver.find_element_by_id("main-content").find_elements_by_class_name("col-md-12")[2]
        tp_block.find_element_by_class_name("icon-bar-chart")
        tp_sub_title = tp_block.find_elements_by_class_name("text-center")[1].text
        if tp_sub_title == "Тарифный план":
            tp_block_found = 1
        tp_sub_sub_title = tp_block.find_elements_by_class_name("text-center")[3].text
        if tp_sub_sub_title.find("Ограничение на количество задач:") +1:
            if tp_block_found:
                tp_block_found = 1
            else:
                tp_block_found = 0

        login_block = driver.find_element_by_id("main-content").find_elements_by_class_name("col-md-12")[3]
        login_block.find_element_by_class_name("icon-users")
        login_title = login_block.find_element_by_class_name("text-center").text
        if login_title.find("Текущий логин для входа в систему:")+1:
            login_found = 1

        if current_balance_title_found and header_found and tp_block_found:
            return 1
        else:
            return 0

    except Exception:
        return 0


def check_play_help_video(driver, domain):
    try:
        from helpers.screen_of_element import get_element_screen
        from helpers.helpers import get_filename, clear_directory
        from helpers.compare_images import MonitorPicture

        directory = "/home/hpx/PycharmProjects/bot/screenshots/check_video"
        number_of_screenshots = 5
        screens = []

        register(driver, domain)

        menu_accounts = driver.find_element_by_class_name("nav-pills").find_elements_by_tag_name("li")[3]
        menu_accounts.click()

        time.sleep(1)
        add_instagram_menu_item = menu_accounts.find_elements_by_tag_name("a")[1]
        add_instagram_menu_item.click()

        show_help_video_button = driver.find_element_by_class_name("fa-question-circle")
        show_help_video_button.click()

        time.sleep(2)
        video_iframe = driver.find_element_by_id("window_modal").find_element_by_tag_name("iframe")
        video_iframe.click()

        time.sleep(2)
        video = driver.find_element_by_id("window_modal").find_element_by_class_name("modal-body")

        clear_directory(directory)

        while number_of_screenshots:
            full_filename = get_filename(directory)
            screens.append(full_filename)
            get_element_screen(driver, video, full_filename)
            time.sleep(5)
            number_of_screenshots -= 1

        image_number = len(screens) - 1
        compare_images_res = 1

        while image_number:

            compare_images_res = MonitorPicture(screens[image_number], screens[image_number-1])
            image_number -= 1
            if compare_images_res:
                break

        if compare_images_res:
            return 1

        else:
            return 0

    except Exception:
        return 0


def check_limits_xpath(driver, domain):
    try:
        res = 1
        instagram_like_value_n = 1
        instagram_following_value_n = 2
        instagram_unfollowing_value_n = 3
        vk_invitations_friends_value_n = 4
        vk_like_value_n = 5
        vk_invitations_group_friends_value_n = 6

        register(driver, domain)

        menu_settings = driver.find_element_by_xpath('//*[@id="main-wrapper"]/aside/nav/ul/li[7]/a')
        menu_settings.click()

        time.sleep(1)
        menu_limits = driver.find_element_by_xpath('//*[@id="main-wrapper"]/aside/nav/ul/li[7]/ul/li[2]/a')
        menu_limits.click()

        time.sleep(2)
        instagram_is = driver.find_element_by_xpath('//*[@id="form_setting_account_limit_update"]/div[1]/div[1]/label/input')
        instagram_is.click()

        instagram_like_is = driver.find_element_by_xpath('//*[@id="form_setting_account_limit_update"]/div[1]/div[2]/div/label/input')
        instagram_like_is.click()

        instagram_following_is = driver.find_element_by_xpath('//*[@id="form_setting_account_limit_update"]/div[1]/div[3]/div/label/input')
        instagram_following_is.click()

        instagram_unfollowing_is = driver.find_element_by_xpath('//*[@id="form_setting_account_limit_update"]/div[1]/div[4]/div/label/input')
        instagram_unfollowing_is.click()

        vk_is = driver.find_element_by_xpath('//*[@id="form_setting_account_limit_update"]/div[2]/div[1]/label/input')
        vk_is.click()

        vk_invitations_friends_is = driver.find_element_by_xpath('//*[@id="form_setting_account_limit_update"]/div[2]/div[2]/div/label/input')
        vk_invitations_friends_is.click()

        vk_like_is = driver.find_element_by_xpath('//*[@id="form_setting_account_limit_update"]/div[2]/div[3]/div/label/input')
        vk_like_is.click()

        vk_invitations_group_friends_is = driver.find_element_by_xpath('//*[@id="form_setting_account_limit_update"]/div[2]/div[4]/div/label/input')
        vk_invitations_group_friends_is.click()

        instagram_like_value = driver.find_element_by_xpath('//*[@id="form_setting_account_limit_update"]/div[1]/div[2]/div/input')
        instagram_like_value.clear()
        instagram_like_value.send_keys(instagram_like_value_n)

        instagram_following_value = driver.find_element_by_xpath('//*[@id="form_setting_account_limit_update"]/div[1]/div[3]/div/input')
        instagram_following_value.clear()
        instagram_following_value.send_keys(instagram_following_value_n)

        instagram_unfollowing_value = driver.find_element_by_xpath('//*[@id="form_setting_account_limit_update"]/div[1]/div[4]/div/input')
        instagram_unfollowing_value.clear()
        instagram_unfollowing_value.send_keys(instagram_unfollowing_value_n)

        vk_invitations_friends_value = driver.find_element_by_xpath('//*[@id="form_setting_account_limit_update"]/div[2]/div[2]/div/input')
        vk_invitations_friends_value.clear()
        vk_invitations_friends_value.send_keys(vk_invitations_friends_value_n)

        vk_like_value = driver.find_element_by_xpath('//*[@id="form_setting_account_limit_update"]/div[2]/div[3]/div/input')
        vk_like_value.clear()
        vk_like_value.send_keys(vk_like_value_n)

        vk_invitations_group_friends_value = driver.find_element_by_xpath('//*[@id="form_setting_account_limit_update"]/div[2]/div[4]/div/input')
        vk_invitations_group_friends_value.clear()
        vk_invitations_group_friends_value.send_keys(vk_invitations_group_friends_value_n)
        time.sleep(2)

        driver.refresh()

        time.sleep(1)

        instagram_like_value = driver.find_element_by_xpath(
            '//*[@id="form_setting_account_limit_update"]/div[1]/div[2]/div/input')
        if instagram_like_value == str(instagram_like_value_n):
            is_instagram_like_value = 1

        instagram_following_value = driver.find_element_by_xpath(
            '//*[@id="form_setting_account_limit_update"]/div[1]/div[3]/div/input').text
        if instagram_following_value == str(instagram_following_value_n):
            instagram_following_value = 1

        instagram_unfollowing_value = driver.find_element_by_xpath(
            '//*[@id="form_setting_account_limit_update"]/div[1]/div[4]/div/input').text
        if instagram_unfollowing_value == str(instagram_unfollowing_value_n):
            instagram_unfollowing_value = 1

        vk_invitations_friends_value = driver.find_element_by_xpath(
            '//*[@id="form_setting_account_limit_update"]/div[2]/div[2]/div/input').text
        if vk_invitations_friends_value == str(vk_invitations_friends_value_n):
            vk_invitations_friends_value = 1

        vk_like_value = driver.find_element_by_xpath('//*[@id="form_setting_account_limit_update"]/div[2]/div[3]/div/input').text
        if vk_like_value == str(vk_like_value_n):
            vk_like_value = 1

        vk_invitations_group_friends_value = driver.find_element_by_xpath(
            '//*[@id="form_setting_account_limit_update"]/div[2]/div[4]/div/input')
        if vk_invitations_group_friends_value == str(vk_invitations_group_friends_value_n):
            vk_invitations_group_friends_value = 1

        if vk_invitations_group_friends_value and vk_like_value and vk_invitations_friends_value and instagram_unfollowing_value and instagram_following_value and is_instagram_like_value:
            res = 1

        return res

    except Exception:
        return 0


def remove_instagram_account(driver, domain):
    try:
        if add_instagram_account(driver, domain):

            select_button = driver.find_element_by_class_name("panel-heading").find_element_by_class_name(
                "btn-group").find_element_by_class_name("dropdown-toggle")
            select_button.click()

            time.sleep(1)
            select_all_button = driver.find_element_by_class_name("panel-heading").find_element_by_class_name(
                "action_select_all")
            select_all_button.click()

            time.sleep(1)
            delete_acc_button = driver.find_element_by_class_name("action_account_destroy")
            delete_acc_button.click()

            time.sleep(2)
            confirm_delete_button = driver.find_element_by_id("window_modal").find_element_by_class_name("onConfirmYes")
            confirm_delete_button.click()

            time.sleep(4)
            added_account = driver.execute_script(
                open("/home/hpx/PycharmProjects/bot/helpers/js/find_vk_instagram_accounts_on_page.js").read() +
                "return find('account_instagram_load');")
            if added_account == 'В таблице отсутствуют данные':
                return 1
            else:
                return 0

    except Exception:
        return 0


def remove_vk_account(driver, domain):
    try:
        if add_vk_account(driver, domain):

            select_button = driver.find_element_by_class_name("panel-heading").find_elements_by_class_name(
                "btn-group")[1].find_element_by_class_name("dropdown-toggle")
            select_button.click()

            time.sleep(1)
            select_all_button = driver.find_element_by_class_name("panel-heading").find_element_by_class_name(
                "action_select_all")
            select_all_button.click()

            time.sleep(1)
            delete_acc_button = driver.find_element_by_class_name("action_account_destroy")
            delete_acc_button.click()

            time.sleep(2)
            confirm_delete_button = driver.find_element_by_id("window_modal").find_element_by_class_name("onConfirmYes")
            confirm_delete_button.click()

            time.sleep(4)
            added_account = driver.execute_script(
                open("/home/hpx/PycharmProjects/bot/helpers/js/find_vk_instagram_accounts_on_page.js").read() +
                "return find('account_vk_load');")
            if added_account == 'В таблице отсутствуют данные':
                return 1
            else:
                return 0

    except Exception:
        return 0


def logout(driver, domain):
    try:
        register(driver, domain)

        dropdown_button = driver.find_element_by_class_name("dropdown-toggle")
        dropdown_button.click()

        time.sleep(1)
        profile_button = driver.find_element_by_class_name("dropdown-menu").find_elements_by_tag_name("li")[4]
        profile_button.click()

        time.sleep(2)
        submit_logout_button = driver.find_element_by_id("window_modal").find_element_by_class_name("onConfirmYes")
        submit_logout_button.click()

        time.sleep(2)
        driver.find_element_by_id("login-wrapper")

        return 1

    except Exception:
        return 0


def check_useful_tools_page_xpath(driver, domain):
    try:
        header_found = 0
        body_content_found = 0

        register(driver, domain)

        utools = driver.find_element_by_xpath('//*[@id="main-wrapper"]/aside/nav/ul/li[10]/a')
        utools.click()

        time.sleep(1)
        page_header = driver.find_element_by_xpath('//*[@id="main-wrapper"]/section/div/h1').text
        if page_header == "Полезные инструменты":
            header_found = 1

        body_content = driver.find_element_by_xpath('//*[@id="main-content"]/div/div/div/div/div/div/table').text
        if body_content != "":
            body_content_found = 1

        if header_found and body_content_found:
            return 1

        else:
            return 0

    except Exception:
        return 0


def main():
    domain = "http://new.socialhammer.com"

    tests = [#login,
             register,
             add_vk_account,
             add_instagram_account,
             set_activity,
             add_to_white_list,
             check_news_page,
             check_start_page,
             check_profile_page,
             check_play_help_video,
             logout,
             remove_instagram_account,
             check_limits_xpath,
             remove_vk_account,
             check_useful_tools_page_xpath]

    for test in tests:
        driver = create_webdriver()
        res = call_func(test, driver, domain)
        print(str(test) + ": " + str(res))
        driver.quit()


main()
