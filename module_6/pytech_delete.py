#Katie Klein
#CSD 310
#12 April 2021
#Assignment 6.2 - PyTech Delete

'''
This program demonstrates inserting and deleting a document
within the connected database
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

#Add new document
fred = {
    "student_id": 1010,
    "first_name": "Fred",
    "last_name": "Weasley",
}
fred_document_id = students.insert_one(fred).inserted_id

#Display insert statement
print("\n-- INSERT STATEMENTS --")
print(f"Inserted student record Fred Weasley into the students collection with document id {fred_document_id}\n")

#Display new document
doc = students.find_one({"student_id": 1010})
print("-- DISPLAYING STUDENT TEST DOC --")
print(f"Student ID: {doc['student_id']}")
print(f"First Name: {doc['first_name']}")
print(f"Last Name: {doc['last_name']}\n")

#Delete new document
students.delete_one({"student_id": 1010})

#Display all documents
print("\n-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
docs = students.find({})
for doc in docs:
    print(f"Student ID: {doc['student_id']}")
    print(f"First Name: {doc['first_name']}")
    print(f"Last Name: {doc['last_name']}\n")

input("\nEnd of program, press Enter to exit...")