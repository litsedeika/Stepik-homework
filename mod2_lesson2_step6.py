from selenium import webdriver
import math
import time

browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)
    # вычисляем значение для ввода в поле
    x = int(browser.find_element_by_id("input_value").text)
    y = calc(x)

    # скроллим до поля
    input1 = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)

    # заполняем данные
    input1.send_keys(y)
    input2 = browser.find_element_by_id("robotCheckbox").click()
    input3 = browser.find_element_by_id("robotsRule").click()

    # отправляем форму
    button = browser.find_element_by_css_selector("button.btn").click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()