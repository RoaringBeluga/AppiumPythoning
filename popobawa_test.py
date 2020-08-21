# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["deviceName"] = "AVD"
caps["platformName"] = "Android"
caps["automationName"] = "UiAutomator2"
caps["ensureWebviewsHavePages"] = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

el1 = driver.find_element_by_accessibility_id("Chrome")
el1.click()
el2 = driver.find_element_by_id("com.android.chrome:id/send_report_checkbox")
el2.click()
el3 = driver.find_element_by_id("com.android.chrome:id/terms_accept")
el3.click()
el3.click()
el4 = driver.find_element_by_id("com.android.chrome:id/negative_button")
el4.click()
el5 = driver.find_element_by_id("com.android.chrome:id/search_box_text")
el5.send_keys("Popobawa!")

driver.quit()