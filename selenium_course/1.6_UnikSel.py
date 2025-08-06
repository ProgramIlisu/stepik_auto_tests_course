from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration1.html"
# link = "http://suninjuly.github.io/registration2.html"  # Для проверки, что тест падает

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Я использовал By.XPATH так как почему-то By.NAME непроходят,
    # Заполняем обязательные поля
    browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']").send_keys("Ivan")
    browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']").send_keys("Petrov")
    browser.find_element(By.XPATH, "//input[@placeholder='Input your email']").send_keys("test@example.com")
    # Отправляем форму
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # Проверка успешной регистрации
    time.sleep(1)
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    assert "Congratulations! You have successfully registered!" == welcome_text

    print("Привет и удачи тебе на этом курсе")

finally:
    time.sleep(5)
    browser.quit()