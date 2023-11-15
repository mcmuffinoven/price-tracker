import json
from flask import Flask, jsonify
from flask_cors import CORS

# app instance
app = Flask(__name__)
CORS(app)


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


if __name__ == "__main__":
    app.run(debug=True, port=8080)
    
    
    