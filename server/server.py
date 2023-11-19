import json
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import random
from datetime import datetime

# app instance
app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/api/home", methods = ["GET"])
def return_home():
    # Read json file, jsonify and send over
    with open("products.json", 'r') as f:
        data = json.load(f)
        return jsonify(data)
    # return jsonify({
    #     'message': "First Page",
    #     'people': ['Apple',"Banana","Cherry"]
    # })

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
    data = request.json
    
    productData = {
        "id":prodID,
        "productName": data["productName"],
        "startingProductPrice": prodStartPrice,
        "currentProductPrice": prodCurPrice,
        "lowestProductPrice": prodLowestPrice,
        "lowestProductPriceDate": datetime.now().strftime("%Y-%m-%d") ,
        "trackedSinceDate": datetime.now().strftime("%Y-%m-%d") ,
        "category": data["category"],
        "saleBool": False
    }
    
    prodCategory = data["category"]
    fileData = {}
    with open("products.json", 'r') as f:
        fileData = json.load(f)
        
    print(productData)
    for index, category in enumerate(fileData):
        if category['category'] == prodCategory:
            # insert new product into list
            fileData[index]["productList"].append(productData)
    
    print(fileData)
    with open("products.json", 'w') as f:
        # Write to file
        json_object = json.dumps(fileData, indent=4)
        f.write(json_object)
        
    return jsonify(fileData)

if __name__ == "__main__":
    app.run(debug=True, port=8080)
    
    
    