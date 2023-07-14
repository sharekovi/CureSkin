from selenium.webdriver.common.by import By
from behave import given, when, then


@then("Verify first product name face")
def verify_face(context):
    context.app.search_results_page.face_header()


