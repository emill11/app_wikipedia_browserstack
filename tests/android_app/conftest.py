import pytest
from selene import browser
import config
import utils.allure
from appium import webdriver
import allure


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    browser.config.driver_remote_url = config.url

    browser.config.driver_options = config.options

    browser.config.timeout = config.time_out

    browser.config.driver = webdriver.Remote(config.url, options=config.options)

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
