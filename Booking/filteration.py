from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


#This file will include a class with instance methods.
#That will be responsible to interact with our website
#After we have some results, to apply filtrations.

class BookingFiltration:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def rating(self,chooseStar):
        star_filter_box=self.driver.find_element(By.CSS_SELECTOR,'div[data-filters-group="class"]')
        star_child_elements=star_filter_box.find_elements(By.CSS_SELECTOR,'*')
        
        
        for star in star_child_elements:
            if str(star.get_attribute('innerHTML')).strip()==f'{chooseStar} stars':
                star.click()

        time.sleep(2)

    def sort_price_lowest_first(self):
        click_drop_down=self.driver.find_element(By.CSS_SELECTOR,'button[data-testid="sorters-dropdown-trigger"]')
        click_drop_down.click()
        element = self.driver.find_element(By.CSS_SELECTOR,'button[data-id="price"]')
        element.click()
        time.sleep(5)