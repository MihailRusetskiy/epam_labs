import unittest
import time
from helpers.helpers import *


class CheckNewsPage(unittest.TestCase):

    def test_check_play_help_video(self):
        from helpers.screen_of_element import get_element_screen
        from helpers.helpers import get_filename, clear_directory
        from helpers.compare_images import MonitorPicture

        directory = "/home/hpx/PycharmProjects/bot/screenshots/check_video"
        number_of_screenshots = 5
        screens = []

        driver = register()

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

        self.assertTrue(compare_images_res)

        driver.quit()