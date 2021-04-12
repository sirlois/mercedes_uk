import time

from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, \
    StaleElementReferenceException

from contants import RESULT_SCREENSHOT_FILE


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    def save_screenshot(self):
        self.driver.save_screenshot(RESULT_SCREENSHOT_FILE)

    def find_element_click(self, by, expression, timeout=32, ignore_exception=None,
                           poll_frequency=4):
        """It find the element and click then  handle all type of exception during click

        :param poll_frequency:
        :param by:
        :param expression:
        :param timeout:
        :param ignore_exception:list It is a list of exception which is need to ignore.
        :return:
        """
        if ignore_exception is None:
            ignore_exception = []

        ignore_exception.append(NoSuchElementException)
        ignore_exception.append(ElementClickInterceptedException)
        ignore_exception.append(StaleElementReferenceException)

        end_time = time.time() + timeout
        while True:
            try:
                web_element = self.driver.find_element(by=by, value=expression)
                self.driver.execute_script("arguments[0].scrollIntoView();", web_element)
                self.driver.execute_script("arguments[0].click();", web_element)
                return True
            except tuple(ignore_exception) as e:
                # print(str(e))
                if time.time() > end_time:
                    time.sleep(poll_frequency)
                    break
            except Exception as e:
                raise
        return False

    def find_element_get_text(self, by, expression, timeout=32, ignore_exception=None,
                              poll_frequency=4):
        """It find the element and get Text then  handle all type of exception during get operation

        :param poll_frequency:
        :param by:
        :param expression:
        :param timeout:
        :param ignore_exception:list It is a list of exception which is need to ignore.
        :return:
        """
        if ignore_exception is None:
            ignore_exception = []

        ignore_exception.append(NoSuchElementException)
        ignore_exception.append(ElementClickInterceptedException)
        ignore_exception.append(StaleElementReferenceException)

        end_time = time.time() + timeout
        while True:
            try:
                web_element = self.driver.find_element(by=by, value=expression)
                self.driver.execute_script("arguments[0].scrollIntoView();", web_element)
                return web_element.text
            except tuple(ignore_exception) as e:
                # print(str(e))
                if time.time() > end_time:
                    time.sleep(poll_frequency)
                    break
            except Exception as e:
                raise
        return None
