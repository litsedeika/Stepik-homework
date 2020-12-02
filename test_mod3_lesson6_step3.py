import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# фикстура открытия и закрытия браузера, для каждого теста отдельная
@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


# фикстура вычисляющая время каждую функцию
@pytest.fixture(scope="function")
def what_time():
    return str(math.log(int(time.time())))


# параметризованный класс с тестом внутри
@pytest.mark.parametrize('page', ["236895", "236896", "236897", "236898",
                                  "236899", "236903", "236904", "236905"])
def test_stepik(browser, page, what_time):
    link = f"https://stepik.org/lesson/{page}/step/1"
    browser.get(link)

    # вписываем значение времени в поле
    input1 = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "textarea"))
    ).send_keys(what_time)

    # нажимаем на кнопку, как только она становится активна
    button_page = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
    ).click()

    # проверяем значение поля с подсказкой
    hint = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "smart-hints__hint"))
    ).text

    assert hint == "Correct!", "message incorrect"