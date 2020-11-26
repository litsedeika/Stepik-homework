from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    # нажимаем на кнопку
    button_page1 = browser.find_element_by_css_selector("button.trollface").click()

    # переходим на открывшуюся страницу
    # узнаем её имя
    new_window = browser.window_handles[1]
    # собственно переходим
    browser.switch_to.window(new_window)

    # считаем значение и отправляем форму
    x = int(browser.find_element_by_id("input_value").text)
    y = calc(x)
    input1 = browser.find_element_by_css_selector("input").send_keys(y)
    button_page2 = browser.find_element_by_css_selector("button.btn").click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
