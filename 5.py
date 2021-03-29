from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
import time 
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Edge()
    #browser.implicitly_wait(10)
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    #button = browser.find_element_by_id("book")
    WebDriverWait(browser, 30).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100")
    ) 
    button = browser.find_element_by_id("book")
    button.click()

    x = browser.find_element_by_id("input_value")
    xx = x.text
    result = calc(xx)
    answer = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    answer.send_keys(result)
    submit = browser.find_element_by_id("solve")
    submit.click()
    
    

   
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
