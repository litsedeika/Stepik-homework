from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser.get(link)

    # вычисляем ответ
    num1 = int(browser.find_element_by_id("num1").text)
    num2 = int(browser.find_element_by_id("num2").text)
    summa = num1 + num2

    # ищем полученную сумму в списке
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(summa))

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()