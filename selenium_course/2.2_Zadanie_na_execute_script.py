"""
Задание на execute_script

В данной задаче вам нужно будет снова преодолеть капчу для роботов и справиться с ужасным и огромным футером, который дизайнер всё никак не успевает переделать. Вам потребуется написать код, чтобы:

    Открыть страницу https://SunInJuly.github.io/execute_script.html.
    Считать значение для переменной x.
    Посчитать математическую функцию от x.
    Проскроллить страницу вниз.
    Ввести ответ в текстовое поле.
    Выбрать checkbox "I'm the robot".
    Переключить radiobutton "Robots rule!".
    Нажать на кнопку "Submit".

Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. Отправьте полученное число в качестве ответа для этого задания.

Для этой задачи вам понадобится использовать метод execute_script, чтобы сделать прокрутку в область видимости элементов, перекрытых футером.
"""
import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# Функция для вычисления значения по формуле
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    # Открываем браузер и загружаем страницу
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим значение x на странице
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text  # получаем текстовое значение x
    y = calc(x) # вычисляем значение функции

    # Вводим вычисленное значение в текстовое поле
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    # Скроллим страницу, чтобы сделать кнопки и элементы видимыми
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    # Отмечаем чекбокс "I'm the robot"
    chekbox =  browser.find_element(By.ID, "robotCheckbox")
    chekbox.click()

    # Выбираем радиокнопку "Robots rule!"
    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()

    # Нажимаем кнопку "Submit"
    button.click()
finally:
    # Ждем 10 секунд, чтобы скопировать результат
    time.sleep(10)
    # Закрываем браузер
    browser.quit()








