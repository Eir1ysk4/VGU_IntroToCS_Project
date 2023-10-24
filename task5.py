from selenium import webdriver

chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument("webdriver.chrome.driver=C:\\Users\\ASUS\\AppData\\Local\\Google\\Chrome\\Application")

browser = webdriver.Chrome(options=chrome_options)

class Task5:
    def __init__(self):
        print("Init task 5")
        return

    def Task5_Run(self):
        browser.get('http://selenium.dev/')
        print("Task 5 is activated!!!!")