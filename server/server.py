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
def load_products():
    print("Access Home Page")
    tableList=[]
    techData = []
    fashionData = []
    groceryData = []
    cosmeticData = []
    
    userID = request.json["user"]
    
    my_db = Postgres(filename="postgres/db_info.ini", section="postgres")
    try:
        data, colnames = my_db.fetch_all_user_products(user_id=userID)
        
        for row in data:
            tableList.append(list(zip(colnames, row)))
            
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
        
        return jsonify(tableData)
    except Exception as e:
        print(e)
        return json.dumps({'success': False}), 500, {'ContentType':'application/json'}

# New post request to add a new product to the database
@app.route("/api/addproduct", methods = ["POST"])
@cross_origin()
def add_product():
    # 1. Add product to database 
    # 2. If error in database, send back request with error 
    # 3. Otherwise, return status SUCCESS
    product = request.json            
    my_db = Postgres(filename="postgres/db_info.ini", section="postgres")      
    
    try:
        my_db.insert_product(user_data=product)
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
    
    except Exception as e:
        print(e)
        return json.dumps({'success':False}), 500, {'ContentType':'application/json'} 
    

# New post request to add a new product to the database
@app.route("/api/adduser", methods = ["POST"])
@cross_origin()
def add_user():

    data = request.json
    
    my_db = Postgres(filename="postgres/db_info.ini", section="postgres")    
    try:
        my_db.insert_user(user_id=data["user"])
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'}
    
    except Exception as e:
        print(e)
        return json.dumps({'success': False}), 500, {'ContentType':'application/json'}


if __name__ == "__main__":
    app.run(debug=True, port=8080)
    
    
    
    