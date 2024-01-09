# Postgres Connection Class

# ----- Imports ----- #
import psycopg2
from psycopg2 import OperationalError
from db_parser import get_db_info
from datetime import datetime
from web_scrapper import WebScrapper


# ----- Config Parameters ----- #
filename='db_info.ini'
section='postgres'
params = get_db_info(filename,section)

class Postgres():
    # Class defaults for products
    default_prod_start_price = WebScrapper.get_product_current_price()
    default_prod_cur_price = WebScrapper.get_product_current_price()
    default_prod_lowest_price = WebScrapper.get_product_current_price()
    default_lowest_product_price_date = datetime.now().strftime("%Y-%m-%d")
    default_tracked_since_date = datetime.now().strftime("%Y-%m-%d")
    default_sale_bool = False
    default_table_name = "products"
    
    def __init__(self):
        try:
            self.connection = psycopg2.connect(**params)
            print("Successfully connected to the database.")

        except OperationalError:
            print("Error connecting to the database :/")
            
        finally:
            if self.connection:
                self.connection.close()
                print("Closed connection.")
    
    @staticmethod
    def generic_insert(connection, query, parameters):
        
        with connection.cursor() as cur:

            try:
                cur.execute(query,(parameters,))
            
            except Exception as error:
                print ("Oops! An exception has occured:", error)
                print ("Exception TYPE:", type(error))
                            
            connection.commit()
        return
    
    @staticmethod
    def generic_fetch(connection, query, parameters):
        with connection.cursor() as cur:

            try:
                cur.execute(query,(parameters,))
                data = cur.fetchall()
            except Exception as error:
                print ("Oops! An exception has occured:", error)
                print ("Exception TYPE:", type(error))
        return data
    
    # ----- Create  ----- #
    # Add new product
    def insert_product(self, data):
                
        query = f"""
            insert into {self.default_table_name} (
            fk_user_id,
            category,
            product_name,
            starting_product_price,
            current_product_price,
            lowest_product_price,
            lowest_product_price_date,
            tracked_since_date,
            product_link,
            sale_bool
            )
            values ((SELECT id from users where user_id=%s),%s, %s, %s, %s, %s, %s, %s, %s, %s);
            """
        
        # Parse Data
        fk_user_id = data["user"]   
        category = data["category"]    
        product_name = data["productName"]         
        product_link = data['productLink']
        
        parameters = (
                        fk_user_id, category, product_name, 
                        Postgres.default_prod_start_price, Postgres.default_prod_cur_price, 
                        Postgres.default_prod_lowest_price, Postgres.default_lowest_product_price_date, 
                        Postgres.default_tracked_since_date, product_link, Postgres.default_sale_bool
                        )                    

        Postgres.generic_insert(connection=self.connection, query=query, parameters=parameters)
        
        return


    # ----- Read ----- #
    def fetch_product(self):
        query = f"""
                    select * from {self.default_table_name} inner join users on products.fk_user_id = (select id from users where user_id = %s);
        """
        parameters = ()
        Postgres.generic_fetch(connection=self.connection, query=query, parameters=parameters)
        return
    

    # ----- Update ----- #

    # Update product price
    def update_current_product_price(self):
        
        query = f"""
                    UPDATE {self.default_table_name}
                    SET current_product_price = %s
                    WHERE fk_user_id = (SELECT id from users where user_id=%s) AND product_name = %s
        """
        parameters = None
        
        Postgres.generic_insert(connection=self.connection, query=query, parameters=parameters)
        
        # Check if sale
        sale = False
        
        if sale:
            self.update_product_sale()
        else:
            return
        
        return
    
    
    # Update is_sale bool
    def update_product_sale(self):
        
        query = f"""
                    UPDATE {self.default_table_name}
                    SET sale_bool = %s
                    WHERE fk_user_id = (SELECT id from users where user_id=%s) AND product_name = %s
        """
        parameters = None
        
        Postgres.generic_insert(connection=self.connection, query=query, parameters=parameters)
        
        return
    
    # Update entire row
    def update_product_info(self):
        return
    
    # ----- Delete  ----- #
    # Delete row
    def remove_product(self):
        
        query = f"""
                    DELETE FROM {self.default_table_name} 
                    WHERE fk_user_id = (SELECT id from users where user_id=%s) AND product_name = %s
        """
        
        parameters = None
        
        Postgres.generic_insert(connection=self.connection, query=query, parameters=parameters)
        
        return
    