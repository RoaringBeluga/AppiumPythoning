from appium import webdriver
import pytest
import os
import xml.dom.minidom

@pytest.fixture()
def driver():
    test_app_name = "Apps/TestApp.app.zip" # App name for testing
    appdir = os.getcwd() + "/" + test_app_name
    print("\nTesting app: ", appdir)

    caps = {
        "deviceName": "iPhone SE (2nd generation)",
        "platformName": "iOS",
        "automationName": "XCUITest",
        "newCommandTimeout": 360,
        "app": appdir
    }
    print("Capabilities: ", caps)
    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    print("Driver initialized")

    yield driver

    driver.quit()


def xml_pretty(xml_string):
    """
    Pretty-print an XML string
    :param xml_string:  XML string with no pretty-printing
    :return: Formatted XML
    """
    return xml_string #xml.dom.minidom.parseString(xml_string).toprettyxml()


def test_positive_numbers(driver):
    integer_a = driver.find_element_by_accessibility_id("IntegerA")
    integer_a.click()
    print("Integer A tapped!")
    integer_a.send_keys("4")
    print("Integer A entered!")

    integer_b = driver.find_element_by_accessibility_id("IntegerB")
    integer_b.click()
    print("Integer B tapped!")
    integer_b.send_keys("5")
    print("Integer B entered!")

    compute_sum = driver.find_element_by_accessibility_id("ComputeSumButton")
    compute_sum.click()
    print("Compute Sum tapped!")
    answer = driver.find_element_by_accessibility_id("Answer")
    print(answer.text)
    print("'Answer' element value printed!")

    assert int(answer.text) > 0


def test_negative_numbers(driver):

    integer_a = driver.find_element_by_accessibility_id("IntegerA")
    integer_a.click()
    print("Integer A tapped!")
    integer_a.send_keys("-1")
    print("Integer A entered!")
    integer_b = driver.find_element_by_accessibility_id("IntegerB")
    integer_b.click()
    print("Integer B tapped!")
    integer_b.send_keys("-3")
    print("Integer B entered!")
    compute_sum = driver.find_element_by_accessibility_id("ComputeSumButton")
    compute_sum.click()
    print("Compute Sum tapped!")
    answer = driver.find_element_by_accessibility_id("Answer")
    print(answer.text)
    assert int(answer.text) < 0
    print("'Answer' element value printed!")


def test_alert_elements(driver):
    print("Pretty source:")
    print(xml_pretty(driver.page_source))
    print("Enumerating buttons:")
    for el in driver.find_elements_by_class_name("XCUIElementTypeButton"):
        print("\tButton: ", el.text, " [", el.get_attribute("name"), "]")

    driver.find_element_by_accessibility_id("show alert").click()
    print("Alerted!")

    assert driver.find_element_by_accessibility_id("this alert is so cool.").text == "this alert is so cool."
    print("Alert present!")
    print("Buttons present:")
    for el in driver.find_elements_by_class_name("XCUIElementTypeButton"):
        print("\tButton: ", el.text, " [", el.get_attribute("name"), "]")
    assert driver.find_element_by_accessibility_id("Cancel").text == "Cancel"
    print("Cancel present!")
    assert driver.find_element_by_accessibility_id("OK").text == "OK"
    print("OK present!")

    driver.find_element_by_accessibility_id("Cancel").click()
    print("Cancel pressed!")


def test_alert_elements(driver):
    driver.find_element_by_accessibility_id("show alert").click()

    assert driver.find_element_by_accessibility_id("this alert is so cool.").text == "this alert is so cool."
    assert driver.find_element_by_accessibility_id("Cancel").text == "Cancel"
    assert driver.find_element_by_accessibility_id("OK").text == "OK"

    driver.find_element_by_accessibility_id("Cancel").click()
