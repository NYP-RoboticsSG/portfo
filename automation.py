from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

test_string ='I am what I am'
chrome_browser = webdriver.Chrome('..//chromedriver.exe')
#chrome_browser.implicitly_wait(10)
chrome_browser.maximize_window()
chrome_browser.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")


wait = WebDriverWait(chrome_browser, 10)


assert('Selenium Easy Demo' in chrome_browser.title)
show_message_button = chrome_browser.find_element_by_class_name('btn-default')
print(show_message_button.get_attribute('innerHTML'))
assert('Show Message' in chrome_browser.page_source)

#user_message = WebDriverWait(chrome_browser, 10).until(EC.presence_of_element_located((By.ID, "user-message")))

user_message = chrome_browser.find_element_by_id("user-message")
user_button2 = chrome_browser.find_element_by_css_selector("#get-input>.btn")
print("user_btn2",user_button2)
user_message.clear()
user_message.send_keys(test_string)


show_message_button.click()
output_message = chrome_browser.find_element_by_id('display')
print(output_message.text)
assert (test_string in output_message.get_attribute('innerHTML'))
#assert (test_string in output_message.text)

#chrome_browser.quit()
#chrome_browser.close()

