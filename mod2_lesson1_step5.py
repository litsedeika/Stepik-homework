from selenium import webdriver
import math
import time

browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/math.html"
    browser.get(link)
    # вычисление ответа
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    # заполняем данные
    input1 = browser.find_element_by_id("answer").send_keys(y)
    input2 = browser.find_element_by_id("robotCheckbox").click()
    input3 = browser.find_element_by_id("robotsRule").click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
