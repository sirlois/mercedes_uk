import sys
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

import page
from contants import CHROME_DRIVER, WEBSITE_URL, XPATH_DIESEL_CHECKBOX, \
    XPATH_STRING_NUMBER_OF_CARS, XPATH_NEXT_CAR_BUTTON, get_xpath_from_car, XPATH_COOKIES_BANNER, OPERA_DRIVER
from support import convert_string_price_to_float, save_results_to_txt_file


class MercedesTest(unittest.TestCase):
    CHROME_BROWSER = True

    def setUp(self):
        if self.CHROME_BROWSER:
            self.driver = webdriver.Chrome(CHROME_DRIVER)
        else:
            self.driver = webdriver.Chrome(OPERA_DRIVER)

    def test_website(self):
        self.driver.maximize_window()
        self.driver.get(WEBSITE_URL)
        mainPage = page.MainPage(self.driver)

        # Remove cookies banner to activate page
        mainPage.find_element_click(By.XPATH, XPATH_COOKIES_BANNER, timeout=32,
                                    ignore_exception=None,
                                    poll_frequency=4)

        # Select Diesel cars
        mainPage.find_element_click(By.XPATH, XPATH_DIESEL_CHECKBOX, timeout=32,
                                    ignore_exception=None,
                                    poll_frequency=4)

        # Save screenshot
        mainPage.save_screenshot()

        # Get number of cars
        string = mainPage.find_element_get_text(By.XPATH, XPATH_STRING_NUMBER_OF_CARS, timeout=32,
                                                ignore_exception=None,
                                                poll_frequency=4)
        if string is None:
            assert False

        number = int(string.split(' vehicles')[0])
        list_prices = []

        for j in range(number):
            price = mainPage.find_element_get_text(By.XPATH, get_xpath_from_car(j + 1), timeout=32,
                                                   ignore_exception=None,
                                                   poll_frequency=4)
            if price is None:
                assert False

            list_prices.append(convert_string_price_to_float(price))
            # Click button to show next car
            if j < (number - 2):
                mainPage.find_element_click(By.XPATH, XPATH_NEXT_CAR_BUTTON, timeout=32,
                                            ignore_exception=None,
                                            poll_frequency=4)

        save_results_to_txt_file(list_prices)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        MercedesTest.CHROME_BROWSER = True
    elif len(sys.argv) == 2:
        value = str(sys.argv.pop())
        if value == 'chrome':
            MercedesTest.CHROME_BROWSER = True
        elif value == 'opera':
            MercedesTest.CHROME_BROWSER = False
        else:
            print('usage: main.py <opera/chrome>')
            sys.exit(2)
    else:
        print('usage: main.py <opera/chrome>')
        sys.exit(2)

    unittest.main()
