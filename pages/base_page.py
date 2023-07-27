
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from support.logger import logger
class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        self.base_url = 'https://shop.cureskin.com/collections/face'

    def open_url(self, url=''):
        print(f'Opening URL: {url}')
        logger.info(f'Opening URL: {url}')
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def click(self, *locator):
        logger.info('Clicking on {},{}'.format(*locator))
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        self.find_element(*locator).send_keys(text)

