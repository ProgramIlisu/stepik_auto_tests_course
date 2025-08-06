"""Задание: работа с выпадающим списком
Для этой задачи мы придумали еще один вариант капчи для роботов. Придется немного переобучить нашего робота, чтобы он справился с новым заданием.

Напишите код, который реализует следующий сценарий:

Открыть страницу https://suninjuly.github.io/selects1.html
Посчитать сумму заданных чисел
Выбрать в выпадающем списке значение равное расчитанной сумме
Нажать кнопку "Submit"
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. Отправьте полученное число в качестве ответа для этого задания.


Когда ваш код заработает, попробуйте запустить его на странице https://suninjuly.github.io/selects2.html. Ваш код и для нее тоже ﻿должен пройти успешно.

Подсказка: """
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
try:
    #driver.get("https://suninjuly.github.io/selects1.html")
    driver.get("https://suninjuly.github.io/selects2.html")

    # Получаем числа и вычисляем сумму
    num1 = int(driver.find_element(By.ID, "num1").text)
    num2 = int(driver.find_element(By.ID, "num2").text)
    total = num1 + num2


    # Выбираем значение в выпадающем списке
    select = Select(driver.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(total)) # Выбираем по значению


    # Нажимаем кнопку Submit
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()


    # Переключаемся на алерт и получаем результат
    result = driver.switch_to.alert.text
    driver.switch_to.alert.accept()
    print(f"Результат {result}")

finally:
    driver.quit()