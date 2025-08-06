from selenium import webdriver  # Импортируем модуль Selenium для управления браузером
from selenium.webdriver.common.by import By  # Импортируем класс By для поиска элементов
import time  # Импортируем модуль time для задержек
import math  # Импортируем модуль math для математических вычислений

# Функция для вычисления нужного значения по формуле
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))  # Вычисляем значение по формуле и возвращаем как строку

link = "https://suninjuly.github.io/math.html"  # Ссылка на страницу с задачей

try:
    browser = webdriver.Chrome()  # Открываем браузер Chrome
    browser.get(link)  # Загружаем страницу по указанной ссылке

    x_element = browser.find_element(By.ID, "input_value")  # Ищем элемент на странице с id="input_value"
    x = x_element.text  # Получаем текст (число x) из найденного элемента
    y = calc(x)  # Вызываем функцию calc и передаём x, сохраняем результат в переменной y

    answer_input = browser.find_element(By.ID, "answer")  # Ищем поле для ввода ответа по id="answer"
    answer_input.send_keys(y)  # Вводим значение y в текстовое поле

    browser.find_element(By.ID, "robotCheckbox").click()  # Ставим галочку в чекбоксе "I'm the robot"
    browser.find_element(By.ID, "robotsRule").click()  # Выбираем радиокнопку "Robots rule!"

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()  # Ищем и нажимаем кнопку "Submit"

    time.sleep(10)  # Ждём 10 секунд, чтобы успеть увидеть результат (код в alert-окне)

finally:
    browser.quit()  # Закрываем браузер

