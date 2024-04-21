#!/usr/bin/env python3
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from time import sleep


def get_driver():
    '''Get Chrome/Firefox driver from Selenium Hub'''
    try:
        options = webdriver.ChromeOptions()
        driver = webdriver.Remote(
                command_executor='http://localhost:4444/wd/hub',
                options=options)
    except WebDriverException:
        options = webdriver.FirefoxOptions()
        driver = webdriver.Remote(
                command_executor='http://localhost:4444/wd/hub',
                options=options)

    driver.implicitly_wait(15)
    driver.get("http://opencart:8080/")

    return driver

def before_all(context):
    """Actions before all scenarios"""
    sleep(10) # wait for the Selenium Hub to start

def before_scenario(context, scenario):
        """Actions before each scenario"""
        context.driver = get_driver()

def after_scenario(context, scenario):
    """Actions after each scenario"""
    if context.driver:
        context.driver.quit()