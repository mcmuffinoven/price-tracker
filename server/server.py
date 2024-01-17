"""_summary_

Returns:
    _type_: _description_
"""

import sys
sys.path.append("..") # Adds higher directory to python modules path.
import json
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import random
from datetime import datetime
import psycopg

from postgres.postgres import Postgres

# app instance
app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/api/home", methods = ["GET", "POST"])
@cross_origin()
def return_home():
    print("Access Home Page")
    tableList=[]
    techData = []
    fashionData = []
    groceryData = []
    cosmeticData = []
    
    userID = request.json["user"]
    print(userID)
    with psycopg.connect(host="192.168.1.195", port="5432", dbname="price_tracker", user="postgres", password="postgres") as conn:
    # with psycopg.connect(host="price-tracker-db.cwukgvtlbuie.us-east-2.rds.amazonaws.com", port="5432", dbname="price-tracker", user="postgres", password="postgres") as conn:
        with conn.cursor() as cur:
            # Query the database and obtain data as Python objects.
            
            try:
                # select * from products inner join users on products.fk_user_id = users.id;
                cur.execute("select * from products inner join users on products.fk_user_id = (select id from users where user_id = %s);", (userID,))
                data = cur.fetchall()
                colnames = [desc[0] for desc in cur.description]
                for row in data:
                    tableList.append(list(zip(colnames, row)))

                # Make the changes to the database persistent
                conn.commit()
            except Exception as e:
                print(e)
                return json.dumps({'success': False}), 404, {'ContentType':'application/json'} 

    # Assign this dynamically in the future
    for row in tableList:
        # print(row)
        product = {}
        product["id"] = row[0][1]
        product["user_id"] = row[1][1]
        product["category"] = row[2][1]
        product["productName"] = row[3][1]
        product["startingProductPrice"] = row[4][1]
        product["currentProductPrice"] = row[5][1]
        product["lowestProductPrice"] = row[6][1]
        product["lowestProductPriceDate"] = row[7][1]
        product["trackedSinceDate"] = row[8][1]
        product["productLink"] = row[9][1]
        product["saleBool"]=row[10][1]
        rowCategory = row[2][1]
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
    print(tableData)
    return jsonify(tableData)

# New post request to add a new product to the database
@app.route("/api/addproduct", methods = ["POST"])
@cross_origin()
def add_product():
    # 1. Add product to database 
    # 2. If error in database, send back request with error 
    # 3. Otherwise, return status SUCCESS
    # handle the POST request
    print("add product")
    insertData = request.json
    prodStartPrice = random.randint(100,500)
    prodCurPrice = random.randint(100,500)
    prodLowestPrice = random.randint(100,500)
    prodLink = insertData["productLink"]
    
    print(insertData)
    with psycopg.connect(host="192.168.1.195", port="5432", dbname="price_tracker", user="postgres", password="postgres") as conn:
    # with psycopg.connect(host="price-tracker-db.cwukgvtlbuie.us-east-2.rds.amazonaws.com", port="5432", dbname="price-tracker", user="postgres", password="postgres") as conn:
        with conn.cursor() as cur:

            cur.execute("""insert into products (
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
                            values ((SELECT id from users where user_id=%s),%s, %s, %s, %s, %s, %s, %s, %s, %s);""",(insertData["user"],insertData["category"], insertData["productName"],prodStartPrice, prodCurPrice, prodLowestPrice, datetime.now().strftime("%Y-%m-%d"),datetime.now().strftime("%Y-%m-%d"), prodLink, True))


            conn.commit()
    
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

# New post request to add a new product to the database
@app.route("/api/adduser", methods = ["POST"])
@cross_origin()
def add_user():

    data = request.json
    
    my_db = Postgres(filename="postgres/db_info.ini", section="postgres")    
    my_db.insert_user(user_id=data["user"])
    
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 


if __name__ == "__main__":
    app.run(debug=True, port=8080)
    
    
    
    