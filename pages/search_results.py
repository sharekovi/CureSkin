from selenium.webdriver.common.by import By

from pages.base_page import Page


class SearchResultsPage(Page):
    def face_header(self):
        expected_result = 'face'
        actual_result = self.driver.find_element(By.XPATH, '"//span[@class=label][normalize-space()=Shop by Category]"').text

        assert expected_result == actual_result,\
            f'Error! Expected {expected_result} bot got actual {actual_result}'



