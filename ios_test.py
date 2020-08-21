# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
import pytest

caps = {}
caps["deviceName"] = "iPhone SE (2nd generation)"
caps["platformName"] = "iOS"
caps["automationName"] = "XCUITest"
caps["app"] = "./Apps/TestApp.app.zip"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
print("Driver!")
el1 = driver.find_element_by_accessibility_id("IntegerA")
el1.click()
print("Integer A tapped!")
el1.send_keys("4")
print("Integer A entered!")
el2 = driver.find_element_by_accessibility_id("IntegerB")
el2.click()
print("Integer B tapped!")
el2.send_keys("5")
print("Integer B entered!")
el3 = driver.find_element_by_accessibility_id("ComputeSumButton")
el3.click()
print("Compute Sum tapped!")
el4 = driver.find_element_by_accessibility_id("Answer")
print(el4.text)
print("'Answer' element value printed!")

driver.quit()