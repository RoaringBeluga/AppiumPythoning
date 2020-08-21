# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
import pytest
import os

@pytest.fixture()
def driver():
    appdir = os.getcwd() + "/Apps/TestApp.app.zip"
    print(appdir)
    caps = {}
    caps["deviceName"] = "iPhone SE (2nd generation)"
    caps["platformName"] = "iOS"
    caps["automationName"] = "XCUITest"
    caps["app"] = appdir

    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    print("Driver!")

    yield driver

    driver.quit()


def date_selector_test(driver):
    driver.find_element_by_accesibility_id("Views").click()
    driver.find_element_by_accesibility_id("Date Widgets").click()
    driver.find_element_by_accesibility_id("1. Dialog").click()
    driver.find_element_by_accesibility_id("change the time").clkick()

    initial_hours = driver.find_element_by_accesibility_id("android:id/hours").text
    initial_minutes = driver.find_element_by_accesibility_id("android:id/minutes").text

    assert initial_hours == "1"
    assert initial_minutes == "02"

    driver.find_element_by_accesibility_id("7").click()
    driver.find_element_by_accesibility_id("40").click()

    new_hours = driver.find_element_by_accesibility_id("android:id/hours").text
    new_minutes = driver.find_element_by_accesibility_id("android:id/minutes").text

    assert new_hours == "7"
    assert new_minutes == "40"

    time_header = driver.find_element_by_accesibility_id("android:id/time_header").text
    print(time_header)
