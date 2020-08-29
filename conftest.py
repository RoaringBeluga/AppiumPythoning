from appium import webdriver
import pytest
import os

appsdir = os.getcwd() + "/Apps/"
screenshot_dir = os.getcwd() + "/Screenshots/"

ios_test_app_name = "TestApp.app.zip"  # App name for testing
android_test_app_name = "ApiDemos-debug.apk"

caps = {}

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

def pytest_addoption(parser):
    parser.addoption("--platform", action="store", default="ios", help="Values: ios or android")
    parser.addoption("--devicename", action="store", default="iPhone SE (2nd generation)", help="Device name")


@pytest.fixture()
def platform(request):
    return request.config.getoption("--platform")

@pytest.fixture()
def device_name(request):
    return request.config.getoption("--devicename")


@pytest.fixture()
def driver(platform, device_name, request):
    """
    Returns WebDriver instance with required capabilities.
    """

    print("Capabilities: ", caps[platform])
    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps[platform])
    print("Driver initialized")
    yield driver
    if request.session.testsfailed > 0:
        file_name = screenshot_dir + platform + "/" + request.node.name + ".png"
        driver.save_screenshot(file_name)
    driver.quit()
    print("Driver killed.")
