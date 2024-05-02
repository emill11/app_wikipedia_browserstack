import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser


def test_open_article():
    with allure.step('Search article'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Tokyo')

    with allure.step('Click on article'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')).click()
