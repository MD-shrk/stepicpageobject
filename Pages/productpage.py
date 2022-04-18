from Pages.locators import *
from Pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as EC
import time


class ProductPage(BasePage):

    def take_book(self):
        self.open("http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear")
        #self.browser.get("http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear")
        time.sleep(7)
        add_click = wdw(self.browser, 5).until(EC.presence_of_element_located(MainPageLocators.packet_button)).click()
        time.sleep(5)
        self.solve_quiz_and_get_code()
        time.sleep(5)


