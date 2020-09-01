import pytest

@pytest.mark.piggy
def test_guinea_pig(driver, platform):
    # pytest.set_trace()
    if platform=="ios":
        page_content = driver.find_element_by_accessibility_id("I am some page content ")
        displayed_three_times = driver.find_elements_by_accessibility_id("i appear 3 times")
        unchecked_checkbox = driver.find_element_by_accessibility_id("unchecked_checkbox")
    elif platform=="android":
        page_content = driver.find_element_by_id("heading2_1")
        stuff = driver.find_elements_by_class_name("android.widget.TextView")
        print ("Got us ", len(stuff), " elements of TextView persuasion")
        displayed_three_times = []
        for item in stuff:
            if item.text == "i appear 3 times":
                displayed_three_times.append(item)
        unchecked_checkbox = driver.find_element_by_id("unchecked_checkbox")
    else:
        pytest.fail(msg="Platform " + platform + " not supported")

    assert page_content.text.strip() == "I am some page content"
    assert len(displayed_three_times) == 3
    assert displayed_three_times[2].text == "i appear 3 times"
    if platform == "ios":
        assert unchecked_checkbox.get_attribute("value") == "0"
        unchecked_checkbox.click()
        assert unchecked_checkbox.get_attribute("value") == "1"
        unchecked_checkbox.click()
        assert unchecked_checkbox.get_attribute("value") == "0"
    elif platform == "android":
        assert unchecked_checkbox.get_attribute("checked") == "false"
        unchecked_checkbox.click()
        assert unchecked_checkbox.get_attribute("checked") == "true"
        unchecked_checkbox.click()
        assert unchecked_checkbox.get_attribute("checked") == "false"
    else: # We WILL not get here
        pytest.fail(msg="Platform " + platform + " not supported")
    assert 0

