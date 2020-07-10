import time
from random import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from login_details import username, password

PATH = "/home/jacob/Documents/chromedriver/chromedriver"

driver = webdriver.Chrome(PATH)
#load webpage
driver.get("https://tinder.com/app/recs")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button")))
#click fb login and change to fb window
driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button').click()
driver.switch_to_window(driver.window_handles[1])
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "email")))
#login
driver.find_element_by_xpath('//*[@id="email"]').send_keys(username)
driver.find_element_by_xpath('//*[@id="pass"]').send_keys(password)
driver.find_element_by_xpath('//*[@id="u_0_0"]').click()
#switch back to original window
driver.switch_to_window(driver.window_handles[0])
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]/span')))
#allow all popups
driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]/span').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]/span').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button/span').click()
time.sleep(2)
#tinder autoswipe
while True:
    time.sleep(random()) #change sleep time to random number between 0 and 1 to help stop bot detection
    try:
        if random() < .93:
            driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button').click()
        else:
            driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button').click()
    except Exception:
            driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]').click()







