from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/find_link_text"
what_i_look = str(math.ceil(math.pow(math.pi, math.e) * 10000))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # ищем правильную ссылку и нажимаем на неё
    mylink = browser.find_element_by_link_text(what_i_look)
    mylink.click()

    # ожидание нужно для того, чтобы мой ноут успел прогрузить страницу
    time.sleep(1)

    # заполняем форму на открывшейся странице
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Vera")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Voytanik")
    input3 = browser.find_element_by_class_name("form-control.city")
    input3.send_keys("Sankt-Peterburg")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
