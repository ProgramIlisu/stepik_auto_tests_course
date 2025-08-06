"""Задание: загрузка файла
В этом задании в форме регистрации требуется загрузить текстовый файл.

Напишите скрипт, который будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/file_input.html
Заполнить текстовые поля: имя, фамилия, email
Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
Нажать кнопку "Submit"
Если все сделано правильно и быстро, вы увидите окно с числом. Отправьте полученное число в качестве ответа для этого задания."""

import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/file_input.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    # Заполняем поля: имя, фамилия, email
    browser.find_element(By.NAME, "firstname").send_keys("Den")
    browser.find_element(By.NAME, "lastname").send_keys("Testov")
    browser.find_element(By.NAME, "email").send_keys("den@example.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла

    # Создаем файл test.txt, если его нет (может быть пустым)
    with open(file_path, "w") as file:
        file.write("Это тестовый файл для загрузки")

    browser.find_element(By.ID, "file").send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()


finally:
    time.sleep(10) # время на копирование кода из alert
    browser.quit()























