import pytest
from appium.options.android import UiAutomator2Options
from selene import browser
from config import user_name, access_key, url, time_out
import utils.allure
from appium import webdriver
import allure


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities({
        # Specify device and os_version for testing
        # "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",

        # Set URL of the application under test
        "app": "bs://sample.app",

        # Set other BrowserStack capabilities
        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",

            # Set your access credentials
            "userName": user_name,
            "accessKey": access_key
        }
    })

    browser.config.driver_remote_url = url

    browser.config.driver_options = options

    browser.config.timeout = time_out

    browser.config.driver = webdriver.Remote(url, options=options)

    yield

    session_id = browser.driver.session_id

    with allure.step('attach xml'):
        utils.allure.attach_xml(browser)

    with allure.step('attach screen'):
        utils.allure.attach_screen(browser)

    with allure.step('attach video'):
        utils.allure.attach_bstack_video(session_id)

    with allure.step('tear down app session'):
        browser.quit()
