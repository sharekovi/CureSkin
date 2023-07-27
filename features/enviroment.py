import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from app.application import Application
from selenium.webdriver.support import expected_conditions as EC

from support.logger import logger


# Allure command:
# python3 -m behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/Product_result_page.feature

def browser_init(context):
    def browser_int(context, test_name):
        """
    :param context: Behave context
    :param test_name: scenario.name
    """
        driver_path = ChromeDriverManager().install()
        service = Service(driver_path)
        context.driver = webdriver.Chrome(service=service)
        context.driver.maximize_window(4)

        #   context.driver = webdriver.Firefox(executable_path='/Users/sharekovi/Desktop/CureSkin/geckodriver')

        #### HEADLESS MODE
        # driver_path = ChromeDriverManager().install()
        # service = Service(driver_path)
        # options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        # context.driver = webdriver.Chrome(
        #  chrome_options=options,
        #  service=service
        # )

        #### BROWSERSTACK
        # desired_cap = {
        #     'browser': 'Firefox',
        #     'os_version': '11',
        #     'os': 'Windows',
        #     'name': test_name
        # }
        # bs_user = 'mohammadovi_TyhA7O'
        # bs_key = 'Yy4pq4SMjqFhUax35cbe'
        # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
        # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

        context.driver.maximize_window()
        context.driver.implicitly_wait(4)
        context.driver.implicitly_wait(5)
        context.driver.wait = WebDriverWait(context.driver, 10)

        context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)
    # print('\nStarted scenario: ', scenario.name)
    logger.info(f'Started scenario: {scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)
    # print('\nStarted step: ', step)
    logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        logger.error(f'Step failed: {step}')
        print('\nStep failed: ', step)

def after_scenario(context, feature):







