from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.webdriver.common.by import By
from .locators import *
import math


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self, url):
        self.browser.get(url)
    # def open(self):
    #     self.browser.get(self.url)

    # is_element_present(By.CSS_SELECTOR, "#login_link_invalid")
    def is_element_present(self, css):
        css = MainPageLocators.LOGIN_LINK
        try:
            self.browser.find_element(By.CSS_SELECTOR, css)
        except (NoSuchElementException):
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
