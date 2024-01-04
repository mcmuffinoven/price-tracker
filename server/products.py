# Product class
# Product details 
# Product Auto Fetching
# Product logic to check sales
from datetime import datetime
from webScrapper import WebScrapper

class Product():
    def __init__(self, user_id, product_category, product_link):
        self.user_id = user_id
        self.product_category = product_category
        self.product_link = product_link
        self.product_tracked_date = datetime.now()
        
        # Scrape Related Functions
        self.product_name = WebScrapper.get_product_name()
        self.product_starting_price = WebScrapper.get_product_current_price()
        self.product_current_price = WebScrapper.get_product_current_price()
        self.product_lowest_price, self.product_lowest_price_date = self.get_lowest_price()
        self.product_sale = self.is_product_sale()
        
    def is_product_sale(self):
        return
    
    def get_lowest_price(self):
        return
            
        
        