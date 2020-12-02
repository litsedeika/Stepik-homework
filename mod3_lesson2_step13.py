import unittest
from selenium import webdriver
import time


class TestAbs(unittest.TestCase):
    def test_link1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")
        # Код, который заполняет обязательные поля
        input1 = browser.find_element_by_class_name("first_block .first_class .first").send_keys("Vera")
        input2 = browser.find_element_by_class_name("first_block .second_class .second").send_keys("Voytanik")
        input3 = browser.find_element_by_class_name("first_block .third_class .third").send_keys("vv@mail.ru")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # тут надо переписать на нормальное ожидание
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered!" == welcome_text
        # self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "some_error_message")

    def test_link2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")
        # Код, который заполняет обязательные поля
        input1 = browser.find_element_by_class_name("first_block .first_class .first").send_keys("Vera")
        input2 = browser.find_element_by_class_name("first_block .second_class .second").send_keys("Voytanik")
        input3 = browser.find_element_by_class_name("first_block .third_class .third").send_keys("vv@mail.ru")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered!" == welcome_text
        # self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "some_error_message")


if __name__ == "__main__":
    unittest.main()
