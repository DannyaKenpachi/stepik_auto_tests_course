from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/explicit_wait2.html'
browser = webdriver.Chrome()
browser.get(link)

try:
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))

    button = browser.find_element(By.TAG_NAME, 'button').click()

    x = browser.find_element(By.ID, 'input_value').text
    x = calc(int(x))

    pole_voda = browser.find_element(By.CSS_SELECTOR, 'input[name="text"]')
    pole_voda.send_keys(x)

    button2 = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, 'solve')))
    button2.click()

    time.sleep(10)

finally:
    browser.quit()