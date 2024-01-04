import psycopg

from datetime import date
# pylint: disable=E1129

# Parent class will hold properties about that site
# IE: the xpaths to the CSS components we are looking for. (Since this is unique to each site)


class Industry:
    def __init__(self, category):
        self.category = category


class Website(Industry):
    def __init__(self, category, name, price_xpath, title_xpath, saving_xpath):
        super().__init__(category)
        self.name = name
        self.price_xpath = price_xpath
        self.title_xpath = title_xpath
        self.saving_xpath = saving_xpath

# Create a child class that inherits from website


class Product(Website):
    def __init__(self, category=None, name=None, price_xpath=None, title_xpath=None, item=None, lowest_price=None, lowest_price_date=None, tracked_date=None, current_price=None, highest_price=None, highest_price_date=None, cheapest_price_site=None, saving_xpath=None, is_tracked=False):
        super().__init__(category, name, price_xpath, title_xpath, saving_xpath)
        self.category = category
        self.item = item
        self.lowest_price = lowest_price
        self.lowest_price_date = lowest_price_date
        self.tracked_date = tracked_date
        self.current_price = current_price
        self.highest_price = highest_price
        self.highest_price_date = highest_price_date
        self.cheapest_price_site = cheapest_price_site
        self.is_tracked = is_tracked

    @classmethod
    def from_parent(cls, parent=None, item=None, lowest_price=None, lowest_price_date=None, tracked_date=None, current_price=None, highest_price=None, highest_price_date=None, cheapest_price_site=None):
        return cls(
            category=parent.category,
            name=parent.name,
            price_xpath=parent.price_xpath,
            title_xpath=parent.title_xpath,
            saving_xpath=parent.saving_xpath,
            item=item,
            lowest_price=lowest_price,
            lowest_price_date=lowest_price_date,
            tracked_date=tracked_date,
            current_price=current_price,
            highest_price=highest_price,
            highest_price_date=highest_price_date,
            cheapest_price_site=cheapest_price_site
        )

    def insertIntoDB(self):

        insertQuery = "INSERT INTO price_tracker (item, lowest_price, lowest_price_date, tracked_date, current_price, highest_price, highest_price_date, cheapest_price_site, category, is_tracked)values ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"

        item = 'monitor'
        lowest_price = 100
        lowest_price_date = date.today()
        tracked_date = date.today()
        current_price = 100
        highest_price = 100
        highest_price_date = date.today()
        cheapest_price_site = 'https://www.bestbuy.ca/en-ca/product/lg-65-4k-uhd-hdr-led-webos-smart-tv-65uq7590pub-2022-dark-iron-grey/16158041?source=collection&adSlot=2'
        category = 'tech'
        is_tracked =  True
        # Equiv to try, except, finally
        with psycopg.connect("user=postgres password=postgres host=192.168.1.144 port=5432 dbname=price_tracker") as conn:
            #     # Connect to an existing database
            #     # Create a cursor to perform database operations
            with conn.cursor() as cur:
                # Executing a SQL query
                cur.execute(insertQuery, (item, lowest_price, lowest_price_date, tracked_date,
                            current_price, highest_price, highest_price_date, cheapest_price_site,  category, is_tracked))

                records = cur.execute("SELECT * FROM price_tracker").fetchall()

                for record in records:
                  print(record)

                conn.commit()

    def fetchProductFromDB(self, item):
        
        fetch_query = "Select * from price_tracker where item = %s"
        
        with psycopg.connect("user=postgres password=postgres host=192.168.1.144 port=5432 dbname=price_tracker") as conn:
            #     # Connect to an existing database
            #     # Create a cursor to perform database operations
            with conn.cursor() as cur:
                records = cur.execute(fetch_query, (item,)).fetchall()

                item = records[1]
                lowest_price = records[2]
                lowest_price_date = records[3]
                tracked_date = records[4]
                current_price = records[5]
                highest_price = records[6]
                highest_price_date = records[7]
                cheapest_price_site = records[8]
                category = records[9]
                is_tracked = records[10]
                
                print("Item: %s", item )
                print("Lowest Price: %s", lowest_price)
                print("lowest_price_date", lowest_price_date)
                print("tracked_date",tracked_date)
                print("current_price",current_price)
                print("highest_price",highest_price)
                print("highest_price_date",highest_price_date)
                print("cheapest_price_site",cheapest_price_site)
                print("category",category)
                print("is_tracked",is_tracked)
                
                return Product(
                            item = records[1],
                            lowest_price = records[2],
                            lowest_price_date = records[3],
                            tracked_date = records[4],
                            current_price = records[5],
                            highest_price = records[6],
                            highest_price_date = records[7],
                            cheapest_price_site = records[8],
                            category = records[9],
                            is_tracked= records[10]
                            )


    # Returns a list of tuples of currently tracked items. 
    def fetchTrackedFromDB(self):
        fetch_query = "Select item from price_tracker where is_tracked is not false"
        
        with psycopg.connect("user=postgres password=postgres host=192.168.1.144 port=5432 dbname=price_tracker") as conn:
            with conn.cursor() as cur:
                records = cur.execute(fetch_query).fetchall()
                return records


    def getSitePrice(self, item):
        priceBox = browser.find_element(By.XPATH,".//span[@data-automation='product-price']/span")
        priceBox=priceBox.get_attribute("innerHTML")
        # priceBox = re.findall(r'\d+', priceBox)[0]

        priceSaving = browser.find_element(By.XPATH, ".//span[@data-automation='product-saving']")
        priceSaving=priceSaving.get_attribute("innerHTML")

        #Can use $ delimiter too, but not every website is the same 
        priceSaving = re.findall(r'\d+', priceSaving)[0]

        # Get Price, Save Price, Rerun script every 24 hrs. Check if price < current, email user if cheaper. 

        print("price: " + priceBox + " with " + priceSaving + " savings")
        return curPrice
    def updatePrice(self, product):
        
        return
    
    def refreshPrice(self):
        
        # Fetch the current data current in the database. 
        trackedItems = self.fetchTrackedFromDB()
        for items in trackedItems:
            product = self.fetchProductFromDB(items[0])
            self.updatePrice(product)
        
   
    def unTrackItem(self, item):
        return item
    
    def trackItem(self, item):
        return item