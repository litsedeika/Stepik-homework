from selenium import webdriver
import time
import os

browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    # заполняем текстовые поля
    input1 = browser.find_element_by_name("firstname").send_keys("Vera")
    input2 = browser.find_element_by_name("lastname").send_keys("V")
    input3 = browser.find_element_by_name("email").send_keys("my@mail.ru")

    # загружаем txt файл
    # получаю текущий каталог, где находится программа
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # файл лежит в той же папке
    file_path = os.path.join(current_dir, 'my_txt.txt')
    attach = browser.find_element_by_name("file").send_keys(file_path)

    # отправляем форму
    button = browser.find_element_by_css_selector("button.btn").click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()