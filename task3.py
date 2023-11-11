from selenium import webdriver
from selenium.webdriver.common.by import By
from shared_resources import resources
from scheduler import *
import openpyxl
from xhtml2pdf import pisa
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Task3:
    browser = None

    chrome_options = None

    play_task_3_and_task_5 = False

    def __init__(self):
        print("Init task 3")
        self.chrome_options = webdriver.ChromeOptions()

        self.chrome_options.add_argument(
            "webdriver.chrome.driver=C:\\Users\\ASUS\\AppData\\Local\\Google\\Chrome\\Application")

        self.chrome_options.add_experimental_option("prefs", {
            "download.default_directory": "D:\\VGU\\Intro to CS\\project"
        })


    def Task3_Run(self, scheduler, task4, task5):
        task2_output = resources.shared_data.get('task2_output')
        if task2_output is not None:
            task2_output = task2_output.lower()
            print("Task 3 is activated!!!!")
            if 'weather' in task2_output:
                index = task2_output.find('in')
                start_index = index + len('in')
                substring = task2_output[start_index:]

                resources.shared_data['task3_output'] = substring
                scheduler.SCH_Add_Task(task4.Task4_Run, 1000, 100000)
                scheduler.SCH_Add_Task(task5.Task5_Run, 1000, 100000)
            elif 'play' in task2_output:
                parts = task2_output.split('play')
                self.browser = webdriver.Chrome(options=self.chrome_options)
                self.play_Youtube_music_by_search(parts)
            elif task2_output == 'web':
                self.browser = webdriver.Chrome(options=self.chrome_options)
                self.search_page_on_browser('https://demo.thingsboard.io/dashboards/?accessToken=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJob3ZpZXRiYWNoQGdtYWlsLmNvbSIsInVzZXJJZCI6IjBlYTdlZmIwLTc1YTMtMTFlZS1iYzE5LWE1MzM4OThjNGMyYSIsInNjb3BlcyI6WyJURU5BTlRfQURNSU4iXSwic2Vzc2lvbklkIjoiZmY2M2I4N2EtYzY4ZC00YzFiLTg4NzctODU3Njg2ODE4NGE2IiwiaXNzIjoidGhpbmdzYm9hcmQuaW8iLCJpYXQiOjE2OTk2Njk3MTUsImV4cCI6MTcwMTQ2OTcxNSwiZmlyc3ROYW1lIjoiSOG7kyIsImxhc3ROYW1lIjoiVmnhur90IELDoWNoIiwiZW5hYmxlZCI6dHJ1ZSwicHJpdmFjeVBvbGljeUFjY2VwdGVkIjp0cnVlLCJpc1B1YmxpYyI6ZmFsc2UsInRlbmFudElkIjoiMGNiMGRhYTAtNzVhMy0xMWVlLWJjMTktYTUzMzg5OGM0YzJhIiwiY3VzdG9tZXJJZCI6IjEzODE0MDAwLTFkZDItMTFiMi04MDgwLTgwODA4MDgwODA4MCJ9.59VRFhHhVqJBZKIW03bxLWrQWsvpFJN_sFwj2qq2K-dqGvQs-2fq0pSsx8WPvjzb7ZszrH6qk1wihaWR8mHjIw&refreshToken=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJob3ZpZXRiYWNoQGdtYWlsLmNvbSIsInVzZXJJZCI6IjBlYTdlZmIwLTc1YTMtMTFlZS1iYzE5LWE1MzM4OThjNGMyYSIsInNjb3BlcyI6WyJSRUZSRVNIX1RPS0VOIl0sInNlc3Npb25JZCI6ImZmNjNiODdhLWM2OGQtNGMxYi04ODc3LTg1NzY4NjgxODRhNiIsImlzcyI6InRoaW5nc2JvYXJkLmlvIiwiaWF0IjoxNjk5NjY5NzE1LCJleHAiOjE3MzU2Njk3MTUsImlzUHVibGljIjpmYWxzZSwianRpIjoiYTY5MTBkZjAtMDdjYS00ZDUyLWJjN2UtNjRkNTMxYWFkMWQ5In0.9BI4OszZP1Mmvsy0Q8_sTWhw6KRqOAECYSJcF5M8jVFLHUbDXnyGFLMGFSswRPbIQP-kY7Gm4U3JMPOMdlBQNQ')
                time.sleep(1)
                dashboard_button = self.browser.find_element(By.XPATH, "/html/body/tb-root/tb-home/mat-sidenav-container/mat-sidenav-content/div/div/tb-entities-table/mat-drawer-container/mat-drawer-content/div/div/div/table/tbody/mat-row[3]")
                dashboard_button.click()
                time.sleep(100)
                self.browser.close()
            resources.shared_data['task2_output'] = ''

        else:
            print("Task 2 output is not available yet.")
        # print(resources.shared_data['task2_output'])

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
        time.sleep(3)

    def play_Youtube_music_by_search(self, search_query):
        self.search_page_on_browser("https://www.youtube.com/")
        search_bar = self.browser.find_element(By.NAME, "search_query")

        search_bar.send_keys(search_query)

        search_bar_button = self.browser.find_element(By.ID, "search-icon-legacy")
        search_bar_button.click()

        time.sleep(3)

        element = self.browser.find_element(By.XPATH, '//*[@id="contents"]/ytd-video-renderer[2]')
        print(element)
        element.click()
        time.sleep(2)
        self.browser.refresh()
        time.sleep(1)
        self.browser.refresh()
        time.sleep(1)
        self.browser.refresh()
        time.sleep(10)
        self.browser.close()

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
