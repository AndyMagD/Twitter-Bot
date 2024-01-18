import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from get_speed import get_speed
from twitting_bot import twitter_post

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options)

PROMISED_DOWN = 110
down_speed = get_speed(driver)


if int(float(down_speed)) < PROMISED_DOWN:
    def make_tweet():
        time.sleep(2)
        new_box = driver.find_element(By.CSS_SELECTOR, "a[href='/compose/tweet']")
        new_box.click()
        time.sleep(1)
        tweet_box = driver.find_element(By.XPATH, '//div[@data-testid="tweetTextarea_0"]')
        tweet_box.send_keys(f"@cosmote why is my speed {down_speed} when i pay for 100mbps")
        #tweet_button = element = driver.find_element(By.CSS_SELECTOR, 'div[data-testid="tweetButton"]')
        #tweet_button.click()

    twitter_post(driver)
    make_tweet()
else:
    print(down_speed)