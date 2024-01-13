import sys
sys.path.append("..") # Adds higher directory to python modules path.
from postgres.postgres import Postgres

my_db = Postgres(filename="postgres/db_info.ini", section="postgres")


product = {}
product["user"] = "tester"
product["category"] = "Grocery"
product["productName"] = "Test prod"
product["productLink"] = "https://www.bestbuy.ca/en-ca/product/samsung-hw-q910c-9-1-channel-sound-bar-with-wireless-subwoofer-only-at-best-buy/16977351"
product["saleBool"]=True

product2 = {}
product2["user"] = "tester2"
product2["category"] = "Grocery"
product2["productName"] = "Test prod"
product2["productLink"] = "https://www.bestbuy.ca/en-ca/product/samsung-hw-q910c-9-1-channel-sound-bar-with-wireless-subwoofer-only-at-best-buy/16977351"
product2["saleBool"]=True

# my_db.insert_user(user_id="tester")
# my_db.insert_product(user_data=product)

# my_db.insert_user(user_id="tester2")
# my_db.insert_product(user_data=product2)

# print(my_db.fetch_product(product_name="Test prod", user_id="tester"))
my_db.update_current_product_price(product_name="Test prod", user_id="tester")
# my_db.scrape_data(url="https://www.bestbuy.ca/en-ca/product/samsung-hw-q910c-9-1-channel-sound-bar-with-wireless-subwoofer-only-at-best-buy/16977351")
# my_db.remove_product(product_name="Test prod", user_id="tester")