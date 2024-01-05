# Postgres Connection Class
# Add/Inserts
import psycopg2
from psycopg2 import OperationalError
from db_parser import get_db_info

filename='db_info.ini'
section='postgres'
params = get_db_info(filename,section)

class Postgres():
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