from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
import time
from Booking import constant as const
import os
from Booking.filteration import BookingFiltration
from Booking.reporting import Report
from prettytable import PrettyTable
import pandas as pd


class Booking(webdriver.Chrome):
    def __init__(self,driver_path="/Users/manar/Downloads",teardown=False):
       # To understand __init__ Link: https://www.youtube.com/watch?v=mNpCPgdb2Jg
       self.driver_path=driver_path
       self.teardown=teardown
       os.environ['PATH'] += self.driver_path
       super(Booking,self).__init__() # this will initialize an object from webdriver.Chrome, like driver = webdriver.Chrome()
       self.implicitly_wait(15)
       self.maximize_window()
       
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()


    def first_page(self):
        self.get(const.base_URL)

    def place_to_go(self,place):
        #search=self.find_element(By.ID,"ss")
        search=self.find_element(By.XPATH,'//*[@id="ss"]')
        search.click()
        search.send_keys(place)
        time.sleep(3)
        first_result = self.find_element(By.CSS_SELECTOR,'li[data-i="0"]')
        first_result.click()
        time.sleep(3) # this is because the brower quit before actually it do something, so sleep until job is done
        

    def check_in_out(self,check_in,check_out):
        checkIn=self.find_element(By.CSS_SELECTOR,f'td[data-date="{check_in}"]')
        checkIn.click()

        checkOut=self.find_element(By.CSS_SELECTOR,f'td[data-date="{check_out}"]')
        checkOut.click()
        time.sleep(3)
        

    def No_of_Adults(self,count=1):
        clickB=self.find_element(By.ID,'xp__guests__toggle')
        clickB.click()
        

        
        while True:
            decrease_adults_element = self.find_element(By.CSS_SELECTOR,
                'button[aria-label="Decrease number of Adults"]'
            )
            decrease_adults_element.click()
            #If the value of adults reaches 1, then we should get out
            #of the while loop
            adults_value_element = self.find_element(By.ID,'group_adults')
            adults_value = adults_value_element.get_attribute('value') 
            # Should give back the adults count

            if int(adults_value) == 1:
                break

        increase_button_element = self.find_element(By.CSS_SELECTOR,
            'button[aria-label="Increase number of Adults"]'
        )

        for _ in range(count - 1):
            increase_button_element.click()
            time.sleep(1)
        time.sleep(2)
        
    
    def click_search(self):
        search_button = self.find_element(By.CSS_SELECTOR,
            'button[type="submit"]'
        )
        search_button.click()
        time.sleep(2)

    def apply_filtrations(self):
        filter = BookingFiltration(driver=self)
        filter.rating(5)
        filter.sort_price_lowest_first()

    def report_data(self):
        # to check number of results 
        # 1- search for container
        # 2- find all elements inside that
        """hotel_box=self.find_element(By.XPATH,'//*[@id="search_results_table"]/div[2]/div/div/div/div[3]'
        ).find_elements(By.CSS_SELECTOR,'div[data-testid="property-card"]')"""
        hotel_box=self.find_element(By.XPATH,'//*[@id="search_results_table"]/div[2]/div/div/div/div[3]')
        report=Report(hotel_box)
        table=PrettyTable(
            field_names=["Hotel Name","Hotel Price","Hotel Rate"]
        )
        table.add_rows(report.all_data())
        print(table)
        # want it as data frame
        dataFrame=report.all_data()
        df = pd.DataFrame (dataFrame, columns = ["Hotel Name","Hotel Price","Hotel Rate"])
        # save to csv file 
        df.to_csv('BookingData.csv') 

