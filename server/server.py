"""_summary_

Returns:
    _type_: _description_
"""
import json
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import random
from datetime import datetime
import psycopg

# app instance
app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/api/home", methods = ["GET"])
def return_home():
    tableList=[]
    techData = []
    fashionData = []
    groceryData = []
    cosmeticData = []
    # Connect to an existing database
    with psycopg.connect(host="price-tracker-db.cwukgvtlbuie.us-east-2.rds.amazonaws.com", port="5432", dbname="price-tracker", user="postgres", password="postgres") as conn:
        # Open a cursor to perform database operations
        with conn.cursor() as cur:
            # Query the database and obtain data as Python objects.
            
            cur.execute("SELECT * FROM price_tracker;")
            data = cur.fetchall()
            # will return (1, 100, "abc'def")

            # You can use `cur.fetchmany()`, `cur.fetchall()` to return a list
            # of several records, or even iterate on the cursor
            colnames = [desc[0] for desc in cur.description]
            for row in data:
                tableList.append(list(zip(colnames, row)))

            # Make the changes to the database persistent
            conn.commit()
    # tableData = dict((x, y) for x in tableList)
    # []
    for row in tableList:
        product = {}
        product["id"] = row[0][1]
        product["category"] = row[1][1]
        product["productName"] = row[2][1]
        product["startingProductPrice"] = row[3][1]
        product["currentProductPrice"] = row[4][1]
        product["lowestProductPrice"] = row[5][1]
        product["lowestProductPriceDate"] = row[6][1]
        product["trackedSinceDate"] = row[7][1]
        product["productLink"] = row[8][1]
        product["saleBool"]=row[9][1]
        rowCategory = row[1][1]
        if rowCategory == "Tech":
            techData.append(product)
        elif rowCategory == "Fashion":
            fashionData.append(product)
        elif rowCategory == "Grocery":
            groceryData.append(product)
        elif rowCategory == "Cosmetics":
            cosmeticData.append(product)
        else: 
            raise Exception("Error, not a valid category")

    techTable={"category":"Tech", "productList":techData}
    fashionTable={"category":"Fashion", "productList":fashionData}
    groceryTable={"category":"Grocery", "productList":groceryData}
    cosmeticTable={"category":"Cosmetics", "productList":cosmeticData}

    tableData = [techTable, fashionTable, groceryTable, cosmeticTable]
    
    return jsonify(tableData)

# New post request to add a new product to the database
@app.route("/api/addProduct", methods = ["POST"])
@cross_origin()
def addProduct():
    # 1. Add product to database 
    # 2. If error in database, send back request with error 
    # 3. Otherwise, return status SUCCESS
    # handle the POST request
    
    prodID = random.randint(100, 1000)
    prodStartPrice = random.randint(100,500)
    prodCurPrice = random.randint(100,500)
    prodLowestPrice = random.randint(100,500)
    insertData = request.json
    print(insertData)
    prodLink = insertData["productLink"]
    
    # productData = {
    #     "id":prodID,
    #     "productName": insertData["productName"],
    #     "startingProductPrice": prodStartPrice,
    #     "currentProductPrice": prodCurPrice,
    #     "lowestProductPrice": prodLowestPrice,
    #     "lowestProductPriceDate": datetime.now().strftime("%Y-%m-%d") ,
    #     "trackedSinceDate": datetime.now().strftime("%Y-%m-%d") ,
    #     "category": insertData["category"],
    #     "saleBool": False
    # }
    
    with psycopg.connect(host="price-tracker-db.cwukgvtlbuie.us-east-2.rds.amazonaws.com", port="5432", dbname="price-tracker", user="postgres", password="postgres") as conn:
        # Open a cursor to perform database operations
        with conn.cursor() as cur:
            # Query the database and obtain data as Python objects.
            
            cur.execute("""insert into price_tracker (
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
                            values (%s, %s, %s, %s, %s, %s, %s, %s, %s);""",(insertData["category"], insertData["productName"],prodStartPrice, prodCurPrice, prodLowestPrice, datetime.now().strftime("%Y-%m-%d"),datetime.now().strftime("%Y-%m-%d"), prodLink, True))

            conn.commit()
    
    chopstick = {
        'color': 'bamboo',
        'left_handed': True
    }

    return jsonify(chopstick)

if __name__ == "__main__":
    app.run(debug=True, port=8080)
    
    
    