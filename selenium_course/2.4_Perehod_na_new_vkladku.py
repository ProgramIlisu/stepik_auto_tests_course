"""Задание: переход на новую вкладку
В этом задании после нажатия кнопки страница откроется в новой вкладке, нужно переключить WebDriver на новую вкладку и решить в ней задачу.

Сценарий для реализации выглядит так:

Открыть страницу http://suninjuly.github.io/redirect_accept.html
Нажать на кнопку
Переключиться на новую вкладку
Пройти капчу для робота и получить число-ответ
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом.
Отправьте полученное число в качестве ответа на это задание."""

import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By




def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажимаем на кнопку
    browser.find_element(By.CSS_SELECTOR, "button.trollface.btn").click()

    # Ждем пока откроется новая вкладка
    time.sleep(2)

    # Переключаемся на новую вкладку
    new_window = browser.window_handles[1] # список всех вкладок, 0 — старая, 1 — новая
    browser.switch_to.window(new_window)

    # Находим значение x на странице
    x_element = browser.find_element(By.ID, "input_value").text  # получаем текстовое значение x
    result = calc(x_element)  # вычисляем значение функции



    # Вводим результат в текстовое поле
    browser.find_element(By.ID, "answer").send_keys(result)
    # Нажимаем Submit
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()


finally:
    time.sleep(10)
    browser.quit()



