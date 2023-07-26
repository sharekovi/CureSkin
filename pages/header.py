from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):
    SEARCH_BTN = (By.XPATH, '"//span[@class=label][normalize-space()=Shop by Category]"')
    SEARCH_FACE = (By.XPATH, '"//span[@class=label][normalize-face()=Shop by Collection]"')


def click_category(self):
    self.click(*self.SEARCH_BTN)
    self.click(*self.SEARCH_FACE)
