import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:

    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Явное ожидание: ждём, пока цена станет $100
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    # Нажимаем кнопку "Book"
    browser.find_element(By.ID, "book").click()

    # Получаем значение x и решаем задачу
    x_value = browser.find_element(By.ID, "input_value").text
    result = calc(x_value)

    # Вводим ответ
    browser.find_element(By.ID, "answer").send_keys(result)

    # Нажимаем кнопку "Submit"
    browser.find_element(By.ID, "solve").click()



finally:
    time.sleep(10)
    browser.quit()







