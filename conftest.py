from datetime import datetime

from appium import webdriver
import pytest
import os


appsdir = os.getcwd() + "/Apps/"
screenshot_dir = os.getcwd() + "/Screenshots/"

ios_test_app_name = "TestApp.app.zip"  # App name for testing
android_test_app_name = "ApiDemos-debug.apk"


def timestamp():
    return datetime.now().strftime("%Y%m%d-%H%M%S")


def pytest_addoption(parser):
    parser.addoption("--platform", action="store", default="ios", help="Values: ios or android")
    parser.addoption("--devicename", action="store", default="iPhone SE (2nd generation)", help="Device name")
    parser.addoption("--app", action="store", default=ios_test_app_name)


@pytest.fixture()
def app(request):
    return request.config.getoption("--app")


@pytest.fixture()
def platform(request):
    return request.config.getoption("--platform").lower()


@pytest.fixture()
def device_name(request):
    return request.config.getoption("--devicename")


@pytest.fixture()
def driver(platform, device_name, app, request):
    """
    Returns WebDriver instance with required capabilities.
    """
    caps = {}
    caps["deviceName"] = device_name  # Device name of the emulator
    caps["platformName"] = platform
    caps["newCommandTimeout"] = 360
    if platform == 'ios':
        caps["automationName"] = "XCUITest"
        caps["app"] = appsdir + app
    elif platform == "android":
        # caps["deviceName"] = "Pixel_3a_API_29"
        # "deviceName": "ASUS ZenPhone",  # Name of the physical device
        # "udid": "JBAXB765F0793AA",  # udid of the physical device
        # caps["platformName"] = "Android"
        caps["automationName"] = "UiAutomator2"
        caps["app"] = appsdir + app  # Find test app in the Apps directory next to our tests
        caps["avd"] = "Pixel_3a_API_29"  # run the AVD with this name.
    else:
        pytest.fail(msg="Platform not supported!")
    print("Platform: ", platform, "\tDevice: ", device_name)
    print("Capabilities: ", caps)
    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    print("Driver initialized")
    failed_test_count = request.session.testsfailed
    yield driver
    # pytest.set_trace()
    if request.session.testsfailed > failed_test_count:
        file_name = screenshot_dir + platform + "/" + timestamp() + "_" + request.node.name + ".png"
        driver.save_screenshot(file_name)
        failed_test_count+=1
    driver.quit()
    print("Driver killed.")
