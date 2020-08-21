# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
import pytest

caps = {}
caps["deviceName"] = "AVD"
caps["platformName"] = "Android"
caps["automationName"] = "UiAutomator2"
caps["ensureWebviewsHavePages"] = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
print('Connected?..')

driver.find_element_by_accessibility_id("Chrome").click()
print('Chrome dome!')
driver.find_element_by_id("com.android.chrome:id/search_box_text").click()
print('Inputs!')
driver.find_element_by_id("com.android.chrome:id/url_bar").send_keys('Pogo sticks!')
print('Pogo sticks!')

driver.quit()