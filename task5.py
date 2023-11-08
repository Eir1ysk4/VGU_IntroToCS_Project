from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl
from xhtml2pdf import pisa
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Task5:
    browser = None

    chrome_options = None
    def __init__(self):
        print("Init task 5")
        self.chrome_options = webdriver.ChromeOptions()

        self.chrome_options.add_argument(
            "webdriver.chrome.driver=C:\\Users\\ASUS\\AppData\\Local\\Google\\Chrome\\Application")

        self.chrome_options.add_experimental_option("prefs", {
            "download.default_directory": "D:\\VGU\\Intro to CS\\project"
        })


        return

    def Task5_Run(self, search_query):
        print("Task 5 is activated!!!!")
        self.browser = webdriver.Chrome(options=self.chrome_options)

        self.play_Youtube_music_by_search(search_query)
        # username_input = browser.find_element(By.ID, "username")
        # password_input = browser.find_element(By.ID, "password")
        #
        # username_input.send_keys("maria")
        # password_input.send_keys("thoushallnotpass")
        # #
        # submit_button = browser.find_element(By.XPATH,'//*[@id="root"]/div/div/div/div[1]/form/button')
        # submit_button.click()
        #
        # time.sleep(3)
        #
        # browser.execute_script("window.location.href = 'https://robotsparebinindustries.com/SalesData.xlsx';")
        #
        # time.sleep(3)
        #
        # workbook = openpyxl.load_workbook("D:\\VGU\\Intro to CS\\project\\SalesData.xlsx")
        #
        # worksheet = workbook.active  # This selects the first sheet by default
        #
        # # Example: Read data from a specific cell
        # # cell_value = sheet['A1'].value
        #
        # # Close the Excel file when you're done
        # workbook.close()
        #
        # for row in worksheet.iter_rows(min_row=2, values_only=True):
        #     # Assuming the first column (column A) contains the data you want
        #     if (row[0]):
        #         self.fill_and_submit_sales_form(row)
        #
        # time.sleep(3)
        #
        # browser.save_screenshot('C:\\Users\\ASUS\\Pictures\\Screenshots\\screenshot.png')
        #
        # time.sleep(3)
        #
        # self.export_as_pdf()
        #
        # time.sleep(3)
        #
        # self.log_out()
    def search_page_on_browser(self, link):
        self.browser.get(link)
        time.sleep(5)
    def play_Youtube_music_by_search(self, search_query):
        self.search_page_on_browser("https://www.youtube.com/")
        search_bar = self.browser.find_element(By.NAME, "search_query")
        print(search_bar)

        search_bar.send_keys(search_query)

        search_bar_button = self.browser.find_element(By.ID, "search-icon-legacy")
        search_bar_button.click()

        time.sleep(5)

        element = self.browser.find_element(By.XPATH, '//*[@id="contents"]/ytd-video-renderer[1]')
        print(element)
        element.click()
        time.sleep(2)
        self.browser.refresh()
        time.sleep(2)
        self.browser.refresh()
        time.sleep(2)
        self.browser.refresh()
        time.sleep(100)

    # def fill_and_submit_sales_form(self, sales_rep):
    #
    #     firstname_input = browser.find_element(By.ID, "firstname")
    #     lastname_input = browser.find_element(By.ID, "lastname")
    #     sale_result_input = browser.find_element(By.ID,"salesresult")
    #
    #     firstname_input.send_keys(sales_rep[0])
    #     lastname_input.send_keys(sales_rep[1])
    #     sale_result_input.send_keys(str(sales_rep[2]))
    #
    #     sales_target_element = browser.find_element(By.ID, 'salestarget')
    #     sales_target_select = Select(sales_target_element)
    #     sales_target_select.select_by_value(str(sales_rep[3]))
    #     submit_button = browser.find_element(By.XPATH,'//*[@id="sales-form"]/button')
    #     submit_button.click()
    #
    #
    #     print("Task 5 is activated!!!!")
    #
    # def export_as_pdf(self):
    #     element = browser.find_element(By.ID, "sales-results")
    #     sales_results_html = element.get_attribute('innerHTML')
    #     OUTPUT_FILENAME = "test.pdf"
    #     result_file = open(OUTPUT_FILENAME, "w+b")  # w+b to write in binary mode.
    #     pisa_status = pisa.CreatePDF(
    #         sales_results_html,  # the HTML to convert
    #         dest=result_file  # file handle to recieve result
    #     )
    #     # Create an instance of HTML2PDF
    #
    #     # Convert HTML to PDF and save it to a file
    #     result_file.close()
    #
    #     result = pisa_status.err
    #
    #     if not result:
    #         print("Successfully created PDF")
    #     else:
    #         print("Error: unable to create the PDF")
    #         # converter.convert(sales_results_html, 'sample.pdf')
    #
    # def log_out(self):
    #     logout_button = browser.find_element(By.ID, "logout")
    #     logout_button.click()