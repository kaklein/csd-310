#Katie Klein
#CSD 310
#9 April 2021
#Assignment 5.2: PyTech Collection Creation

from pymongo import MongoClient

#Connect to database
url = "mongodb+srv://admin:admin@cluster0.rpse2.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech

#Print collection list
print(" -- Pytech Collection List --")
print(db.list_collection_names())
print("\n")

input(" End of program, press Enter to exit... ")