# import pdb
# import xml.dom.minidom
import pytest


def xml_pretty(xml_string):
    """
    Pretty-print an XML string
    :param xml_string:  XML string with no pretty-printing
    :return: Formatted XML
    """
    return xml_string  # xml.dom.minidom.parseString(xml_string).toprettyxml()


@pytest.mark.numbers
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


@pytest.mark.numbers
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


@pytest.mark.alerts
def test_alert_elements_cancel(driver):
    pytest.set_trace()
    driver.find_element_by_accessibility_id("show alert").click()
    assert driver.find_element_by_accessibility_id("this alert is so cool.").text == "this alert is so cool."
    assert driver.find_element_by_accessibility_id("Cancel").text == "Cancel"
    assert driver.find_element_by_accessibility_id("OK").text == "OK"
    driver.find_element_by_accessibility_id("Cancel").click()
    print("Cancel pressed!")
    assert not driver.find_element_by_accessibility_id("Cancel").is_displayed()


@pytest.mark.alerts
def test_alert_elements_ok(driver):
    driver.find_element_by_accessibility_id("show alert").click()
    assert driver.find_element_by_accessibility_id("this alert is so cool.").text == "this alert is so cool."
    assert driver.find_element_by_accessibility_id("Cancel").text == "Cancel"
    assert driver.find_element_by_accessibility_id("OK").text == "OK"
    driver.find_element_by_accessibility_id("Cancel").click()
