import unittest
import time
from helpers.helpers import *
from helpers.screen_of_element import get_element_screen
from helpers.anticapcha import crack_capcha



class AntiCapcha(unittest.TestCase):

    def test_crack_capcha(self):
        directory = '/home/hpx/PycharmProjects/bot/screenshots/capchas'

        driver = create_webdriver()
        driver.get('https://demos.captcha.com/demos/features/captcha-demo.aspx')
        capcha_img = driver.find_element_by_id('c_captchademo_samplecaptcha_CaptchaImage')
        full_filename = get_filename(directory)
        get_element_screen(driver, capcha_img, full_filename)

        code = crack_capcha('', full_filename)

        check_input = driver.find_element_by_id('CaptchaCodeTextBox')
        check_input.send_keys(code)
        check_button = driver.find_element_by_id('ValidateCaptchaButton')
        check_button.click()
        check_result_span = driver.find_element_by_id('CaptchaCorrectLabel').text

        self.assertEqual('Correct!', check_result_span)

        driver.quit()
