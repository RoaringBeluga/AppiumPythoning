# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
import pytest

def test_positive_numbers():
    caps = {}
    caps["deviceName"] = "iPhone SE (2nd generation)"
    caps["platformName"] = "iOS"
    caps["automationName"] = "XCUITest"
    caps["app"] = "/Users/desman/Development/Python/Appium/Apps/TestApp.app.zip"

    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    print("Driver!")
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
    driver.quit()

def test_negative_numbers():
    caps = {}
    caps["deviceName"] = "iPhone SE (2nd generation)"
    caps["platformName"] = "iOS"
    caps["automationName"] = "XCUITest"
    caps["app"] = "./Apps/TestApp.app.zip"

    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    print("Driver!")
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

    driver.quit()