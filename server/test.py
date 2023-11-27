import psycopg

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
            print(tableList)

        # Make the changes to the database persistent
        conn.commit()
# tableData = dict((x, y) for x in tableList)
# []
for row in tableList:
    productList = []
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

print(tableData)