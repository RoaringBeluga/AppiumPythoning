# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
import pytest
import os

@pytest.fixture()
def driver():
    """
    Create WebDriver instance with required capabilities
    Returns: WebDriver object
    """
    appdir = os.getcwd() + "/Apps/ApiDemos-debug.apk"
    print(appdir)
    caps = {}
    caps["deviceName"] = "Pixel_3a_API_29"
    caps["platformName"] = "Android"
    caps["automationName"] = "UiAutomator2"
    caps["app"] = appdir

    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    print("Driver!")

    yield driver

    driver.quit()


def test_date_selector(driver):
    driver.find_element_by_accessibility_id("Views").click()
    driver.find_element_by_accessibility_id("Date Widgets").click()
    driver.find_element_by_accessibility_id("1. Dialog").click()

    initial_date_display = driver.find_element_by_id("io.appium.android.apis:id/dateDisplay").text.split(" ")
    initial_time = initial_date_display[1].split(":")

    driver.find_element_by_accessibility_id("change the time").click()

    driver.implicitly_wait(5)

    initial_hours = driver.find_element_by_id("android:id/hours").text
    initial_minutes = driver.find_element_by_id("android:id/minutes").text

    assert int(initial_hours) == int(initial_time[0])
    assert int(initial_minutes) == int(initial_time[1])

    driver.find_element_by_accessibility_id("7").click()
    driver.find_element_by_accessibility_id("40").click()

    new_hours = driver.find_element_by_id("android:id/hours").text
    new_minutes = driver.find_element_by_id("android:id/minutes").text

    assert new_hours == "7"
    assert new_minutes == "40"

    time_header = driver.find_element_by_id("android:id/time_header").text
    print(time_header)

    driver.find_element_by_id("android:id/button1").click()
    result_date_display = driver.find_element_by_id("io.appium.android.apis:id/dateDisplay").text.split(" ")
    result_time = result_date_display[1].split(":")

    assert int(new_hours) == int(result_time[0])
    assert int(new_minutes) == int(result_time[1])