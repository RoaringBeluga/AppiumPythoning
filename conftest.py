from appium import webdriver
import pytest
import os

appsdir = os.getcwd() + "/Apps/"
ios_test_app_name = "TestApp.app.zip"  # App name for testing
android_test_app_name = "ApiDemos-debug.apk"

caps["ios"] = {
    "deviceName": "iPhone SE (2nd generation)",
    "platformName": "iOS",
    "automationName": "XCUITest",
    "newCommandTimeout": 360,
    "app": appsdir + ios_test_app_name
}
caps["android"] = {
    "deviceName": "Pixel_3a_API_29",  # Device name of the emulator
    # "deviceName": "ASUS ZenPhone",  # Name of the physical device
    # "udid": "JBAXB765F0793AA",  # udid of the physical device
    "platformName": "Android",
    "automationName": "UiAutomator2",
    "newCommandTimeout": 360,
    "androidDeviceReadyTimeout": 360,  # Waiting for the device to become available – AVD startup times are slooow
    "app": appsdir + android_test_app_name,  # Find test app in the Apps directory next to our tests
    "avd": "Pixel_3a_API_29"  # run the AVD with this name.
}

def pytes_addoptino(parser):
    parser.addoption("--platform", action="store", default="ios", help="Values: ios or android")


@pytest.fixture()
def platform(request):
    return request.config.getoption("--platform")


@pytest.fixture()
def driver(set_platform):
    """
    Returns WebDriver instance with required capabilities.
    """
    platform = set_platform
    if (platform not in ["ios", "android"]):
        platform = ios
    print("Capabilities: ", caps[platform])
    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    print("Driver initialized")
    yield driver
    driver.quit()
    print("Driver killed.")
