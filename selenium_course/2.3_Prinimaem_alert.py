"""Задание: принимаем alert
В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/alert_accept.html
Нажать на кнопку
Принять confirm
На новой странице решить капчу для роботов, чтобы получить число с ответом
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом.
Отправьте полученное число в качестве ответа на это задание."""

import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By




def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажимаем на кнопку, которая вызывает alert
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # Переключаемся на alert и принимаем его
    alert = browser.switch_to.alert
    alert.accept()

    # Находим значение x на странице
    x_element = browser.find_element(By.ID, "input_value").text  # получаем текстовое значение x
    result = calc(x_element)  # вычисляем значение функции



    # Вводим результат в текстовое поле
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(result)
    # Нажимаем Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()


finally:
    time.sleep(10)
    browser.quit()



