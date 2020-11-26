from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)
    # Дождаться, когда цена дома уменьшится до $100
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    # Нажать на кнопку "Book"
    button = browser.find_element(By.ID, "book").click()
    # Решить уже известную нам математическую задачу
    x = int(browser.find_element(By.ID, "input_value").text)
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, "input").send_keys(y)
    button2 = browser.find_element(By.ID, "solve").click()
    # button2 = WebDriverWait(browser, 5).until(
    #     EC.element_located_to_be_selected((By.CSS_SELECTOR, "button.btn"))
    # )
    button2.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()