from selenium.webdriver.common.by import By
import selenium
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as EC


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    packet_button = (By.CSS_SELECTOR, ".btn-add-to-basket")
    book_name = (By.XPATH, "//h1[text()=['The shellcoder's handbook']")
