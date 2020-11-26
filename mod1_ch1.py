# это проверка теста другого студента, его код
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# url = "http://suninjuly.github.io/registration1.html"
url = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
expected_message = "Congratulations! You have successfully registered!"

try:
    browser.get(url)
    browser.find_element(By.CSS_SELECTOR, "input[required].first").send_keys("Evgeni")
    browser.find_element(By.CSS_SELECTOR, "input[required].second").send_keys("Bayrambekov")
    browser.find_element(By.CSS_SELECTOR, "input[required].third").send_keys("oc4kxb@gmail.com")
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(1)
    actual_message = browser.find_element(By.TAG_NAME, "h1").text
    assert actual_message == expected_message
finally:
    browser.quit()
