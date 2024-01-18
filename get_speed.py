from selenium.webdriver.common.by import By
import time

speed_test_url = "https://www.speedtest.net/"


def get_speed(driver):
    driver.get(speed_test_url)
    time.sleep(1)

    accept_button = driver.find_element(By.ID, "onetrust-accept-btn-handler")
    accept_button.click()
    go_button = driver.find_element(By.CLASS_NAME, "start-text")
    go_button.click()

    time.sleep(22)  # waiting for the test to complete, for full results wait 35s
    result = driver.find_element(By.CLASS_NAME, "result-data-large")
    print(result.text)
    return result.text
