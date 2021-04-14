#Katie Klein
#CSD 310
#12 April 2021
#Assignment 6.2 - PyTech Update

'''
This program updates a document in the connected database
'''

from pymongo import MongoClient

#Connect to database
url = "mongodb+srv://admin:admin@cluster0.rpse2.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech
students = db.students

#Display original documents
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
docs = students.find({})
for doc in docs:
    print(f"Student ID: {doc['student_id']}")
    print(f"First Name: {doc['first_name']}")
    print(f"Last Name: {doc['last_name']}\n")

#Update document
students.update_one({
    "student_id": 1007
}, 
{"$set":
    {
        "last_name": "Houdini"
    }
})

#Display updated document
print("-- DISPLAYING STUDENT DOCUMENT 1007 --")
doc = students.find_one({"student_id": 1007})
print(f"Student ID: {doc['student_id']}")
print(f"First Name: {doc['first_name']}")
print(f"Last Name: {doc['last_name']}\n")

input("\nEnd of program, press Enter to exit...")