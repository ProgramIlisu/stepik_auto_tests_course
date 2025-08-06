from selenium import webdriver  # Импортируем модуль Selenium для управления браузером
from selenium.webdriver.common.by import By  # Импортируем класс By для поиска элементов
import time  # Импортируем модуль time для задержек
import math  # Импортируем модуль math для математических вычислений

# Функция для вычисления нужного значения по формуле
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))  # Вычисляем значение по формуле и возвращаем как строку

link = "http://suninjuly.github.io/get_attribute.html"  # Ссылка на страницу с задачей

try:
    browser = webdriver.Chrome()  # Открываем браузер Chrome
    browser.get(link)  # Загружаем страницу по указанной ссылке

    # Находим элемент-картинку (сундук) и получаем значение атрибута valuex
    chest = browser.find_element(By.ID, "treasure") #Элемент с картинкой
    x_value = chest.get_attribute("valuex") # получаем значение атрибута valuex

    # Вычисляем значение выражения
    y = calc(x_value)

    # Вводим полученное значение в текстовое поле
    input_field = browser.find_element(By.ID,"answer")  # поле для ввода ответа
    input_field.send_keys(y)

    # Отмечаем чекбокс "I'm the robot"
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    # Выбираем радиокнопку "Robots rule!"
    radio =  browser.find_element(By.ID, "robotsRule")
    radio.click()
    #Нажимаем кнопку Submit для отправки формы
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    # Ждем 10 секунд, чтобы успеть скопировать ответ с алерта
    time.sleep(10)
    # Закрываем браузер
    browser.quit()


