from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


@given('User Open main page')
def open_main(context):
    context.app.main_page.open_main_page()


@when('User Click on Shop by category')
def click_category(context):
    context.driver.find_element(By.XPATH, '"//span[@class=label][normalize-space()=Shop by Category]"').click()


@then('Verify face header is shown')
def step_impl(context):
    def face_header(context):
        context.app.search_results_page.face_header()


@then('Click on the face')
def click_face(context):
    context.driver.find_element(By.XPATH, '"//span[@class=label][normalize-space()=Shop by Category]"').click()
