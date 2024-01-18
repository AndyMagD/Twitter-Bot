from selenium.webdriver.common.by import By
import secret_tw  # Hidden personal information used for loging in
import time

tw_url = "https://twitter.com"

def twitter_post(driver):
    time.sleep(1)
    driver.get(tw_url)

    time.sleep(2)
    cookies = driver.find_element(By.CSS_SELECTOR, 'div[role="button"][tabindex="0"].css-175oi2r')
    cookies.click()

    time.sleep(1)
    sign_in = driver.find_element(By.CSS_SELECTOR,
                                          'div[dir="ltr"].css-1rynq56.r-bcqeeo.r-qvutc0.r-37j5jr.r-q4m81j.r-a023e6.r-rjixqe.r-b88u0q.r-1awozwy.r-6koalj.r-18u37iz.r-16y2uox.r-1777fci[style*="color: rgb(29, 155, 240)"]')
    sign_in.click()

    time.sleep(2)
    input_username = driver.find_element(By.CLASS_NAME, "r-30o5oe")
    input_username.send_keys(secret_tw.email_tw)
    time.sleep(1)
    next_click = driver.find_element(By.XPATH, '//*[text()="Next"]')
    next_click.click()

    time.sleep(1)
    give_phone = driver.find_element(By.CLASS_NAME, "r-30o5oe")
    give_phone.send_keys(secret_tw.phone)
    next_click = driver.find_element(By.XPATH, '//*[text()="Next"]')
    next_click.click()

    time.sleep(1)
    input_passw = driver.find_element(By.XPATH, '//input[@name="password" and @type="password"]')
    input_passw.send_keys(secret_tw.pasw_tw)

    login = driver.find_element(By.XPATH,
                                    '//div[@dir="ltr" and contains(@class, "css-1rynq56") and contains(@style, "text-overflow: unset; color: rgb(15, 20, 25)")]/span/span[text()="Log in"]')
    login.click()


