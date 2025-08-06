from selenium import webdriver
from selenium.webdriver.common.by import By
import time
try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
    input1.send_keys("Rita")
    input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
    input2.send_keys("Belashova")
    input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
    input3.send_keys("yanevivozhu")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()