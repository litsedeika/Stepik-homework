from selenium import webdriver
import time

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser.get(link)

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Vera")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Voytanik")
    input3 = browser.find_element_by_class_name("form-control.city")
    input3.send_keys("Sankt-Peterburg")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    # ищем кнопку подтверждения по её тексту
    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()