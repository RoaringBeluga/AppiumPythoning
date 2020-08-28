import pdb

from appium import webdriver
import pytest
import os


@pytest.fixture()
def driver():
    """
    Returns WebDriver instance with required capabilities.
    """
    test_app_name = "Apps/ApiDemos-debug.apk" # App name for testing
    appdir = os.getcwd() + "/" + test_app_name
    print("Testing app: ", appdir)
    # Set device capabilities
    caps = {
        "deviceName" : "Pixel_3a_API_29",  # Device name of the emulator
        # "deviceName": "ASUS ZenPhone",  # Name of the physical device
        # "udid": "JBAXB765F0793AA",  # udid of the physical device
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "newCommandTimeout": 360,
        "androidDeviceReadyTimeout": 360,  # Waiting for the device to become available – AVD startup times are slooow
        "app": appdir,  # Find test app in the Apps directory next to our tests
        "avd" : "Pixel_3a_API_29" # run the AVD with this name.
    }
    print("Capabilities: ", caps)
    # Initialize the driver
    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    print("Driver initialized.")
    # ... and here we go!
    yield driver
    # Clean up after use
    driver.quit()


def test_time_selector(driver):
    # Getting to the dialog...
    driver.find_element_by_accessibility_id("Views").click()
    driver.find_element_by_accessibility_id("Date Widgets").click()
    driver.find_element_by_accessibility_id("1. Dialog").click()
    # Getting the initial time from the datetime string...
    initial_date_display = driver.find_element_by_id("io.appium.android.apis:id/dateDisplay").text.split(" ")
    initial_time = initial_date_display[1].split(":")
    # Opening the Set time dialog
    driver.find_element_by_accessibility_id("change the time").click()
    # Wait for the dialog to appear
    driver.implicitly_wait(5)
    # Save initial settings...
    initial_hours = driver.find_element_by_id("android:id/hours").text
    initial_minutes = driver.find_element_by_id("android:id/minutes").text
    # Convert str to int so we don't have to deal with leading zero
    # Check that it's the same time as we got from the previous screen
    assert int(initial_hours) == int(initial_time[0])
    assert int(initial_minutes) == int(initial_time[1])
    driver.find_element_by_accessibility_id("7").click()  # Set new hours value
    driver.find_element_by_accessibility_id("40").click()  # Set new minutes value
    new_hours = driver.find_element_by_id("android:id/hours").text  # Get new hour setting
    new_minutes = driver.find_element_by_id("android:id/minutes").text  # Get new minutes setting
    assert new_hours == "7"  # Hours set correctly?
    assert new_minutes == "40"  # Minutes set correctly?
    # Just print the time.
    time_header = driver.find_element_by_id("android:id/time_header").text
    print(time_header)
    # Close the dialog
    driver.find_element_by_id("android:id/button1").click()
    # Get the time portion of datetime display and split it
    result_date_display = driver.find_element_by_id("io.appium.android.apis:id/dateDisplay").text.split(" ")
    result_time = result_date_display[1].split(":")
    assert int(new_hours) == int(result_time[0])  # Hours set correctly?
    assert int(new_minutes) == int(result_time[1])  # Minutes set correctly?


def test_date_selector(driver):
    # Getting to the dialog...
    # pdb.set_trace()
    driver.find_element_by_accessibility_id("Views").click()
    driver.find_element_by_accessibility_id("Date Widgets").click()
    driver.find_element_by_accessibility_id("1. Dialog").click()
    # Getting the initial time from the datetime string...
    [initial_month, initial_day, initial_year] = driver.find_element_by_id("io.appium.android.apis:id/dateDisplay").text.split(" ")[0].split("-")
    print("Month #", initial_month)
    # Opening the Set time dialog
    driver.find_element_by_accessibility_id("change the date").click()
    # Wait for the dialog to appear
    driver.implicitly_wait(5)
    # Save initial settings...
    initial_hours = driver.find_element_by_id("android:id/hours").text
    initial_minutes = driver.find_element_by_id("android:id/minutes").text
    # Convert str to int so we don't have to deal with leading zero
    # Check that it's the same time as we got from the previous screen
    assert int(initial_hours) == int(initial_date)
    assert int(initial_minutes) == int(initial_time[1])
    driver.find_element_by_accessibility_id("7").click()  # Set new hours value
    driver.find_element_by_accessibility_id("40").click()  # Set new minutes value
    new_hours = driver.find_element_by_id("android:id/hours").text  # Get new hour setting
    new_minutes = driver.find_element_by_id("android:id/minutes").text  # Get new minutes setting
    assert new_hours == "7"  # Hours set correctly?
    assert new_minutes == "40"  # Minutes set correctly?
    # Just print the time.
    time_header = driver.find_element_by_id("android:id/time_header").text
    print(time_header)
    # Close the dialog
    driver.find_element_by_id("android:id/button1").click()
    # Get the time portion of datetime display and split it
    result_date_display = driver.find_element_by_id("io.appium.android.apis:id/dateDisplay").text.split(" ")
    result_time = result_date_display[1].split(":")
    assert int(new_hours) == int(result_time[0])  # Hours set correctly?
    assert int(new_minutes) == int(result_time[1])  # Minutes set correctly?