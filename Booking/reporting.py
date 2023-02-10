from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Report:
    def __init__(self, box_section_element:WebElement):
        self.box_section_element=box_section_element
        self.deal_boxes=self.all_property()
    
    def all_property(self):
        return self.box_section_element.find_elements(By.CSS_SELECTOR,'div[data-testid="property-card"]')
        # we use return so we can use the for loop in the title function

    def all_data(self):
        collection=[]
        for deal_boxes in self.deal_boxes:
            hotel_name=deal_boxes.find_element(By.CSS_SELECTOR,'div[data-testid="title"]').text
            #deal_boxes.find_element(By.CSS_SELECTOR,'div[data-testid="title"]')
            #print(hotel_name.text)
            hotel_price=deal_boxes.find_element(By.CSS_SELECTOR,'span[data-testid="price-and-discounted-price"]').text
            #print(hotel_price.text)
            hotel_rate=deal_boxes.find_element(By.CSS_SELECTOR,'div[data-testid="review-score"]').text
            #print(hotel_rate.text)

            collection.append([hotel_name,hotel_price,hotel_rate])
            
        return collection
