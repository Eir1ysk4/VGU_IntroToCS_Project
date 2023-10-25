from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument("webdriver.chrome.driver=C:\\Users\\ASUS\\AppData\\Local\\Google\\Chrome\\Application")

browser = webdriver.Chrome(options=chrome_options)

class Task5:
    def __init__(self):
        print("Init task 5")
        return

    def Task5_Run(self):
        browser.get('https://robotsparebinindustries.com/')
        time.sleep(4)
        username_input = browser.find_element(By.ID, "username")
        password_input = browser.find_element(By.ID, "password")

        username_input.send_keys("maria")
        password_input.send_keys("thoushallnotpass")

        submit_button = browser.find_element(By.XPATH,'//*[@id="root"]/div/div/div/div[1]/form/button')
        submit_button.click()

        time.sleep(3)

        firstname_input = browser.find_element(By.ID, "firstname")
        lastname_input = browser.find_element(By.ID, "lastname")
        sale_result_input = browser.find_element(By.ID,"salesresult")
        firstname_input.send_keys("Lock")
        lastname_input.send_keys("Huynh")
        sale_result_input.send_keys("123")

        sales_target_element = browser.find_element(By.ID, 'salestarget')
        sales_target_select = Select(sales_target_element)
        sales_target_select.select_by_value('10000')
        submit_button = browser.find_element(By.XPATH,'//*[@id="sales-form"]/button')
        submit_button.click()

        print("Task 5 is activated!!!!")