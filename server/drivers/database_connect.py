from pymongo import MongoClient
client = MongoClient("mongodb://{User}:{password}@{address}:{port}/")
try: 
    database = client[{database}]
    print(databases)
    collection = database.list_collection_names(include_system_collections=False)
    for collect in collection:
        print (collect)
except Exception as e: 
    print(e)
else: 
    print("You are connected!")
client.close()