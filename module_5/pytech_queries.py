#Katie Klein
#CSD 310
# 9 April 2021
#Assignment 5.3 - PyTech Queries

from pymongo import MongoClient

#Connect to database
url = "mongodb+srv://admin:admin@cluster0.rpse2.mongodb.net/pytech"
client = MongoClient(url)
students = client.pytech.students

#Find all documents in students collection
docs = students.find({})
#Print information for each document
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in docs:
    print(f"Student ID: {doc['student_id']}")
    print(f"First Name: {doc['first_name']}")
    print(f"Last Name: {doc['last_name']}\n")

#Perform find_one query
doc = students.find_one({"student_id": 1008})
#Print find_one results
print("-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print(f"Student ID: {doc['student_id']}")
print(f"First Name: {doc['first_name']}")
print(f"Last Name: {doc['last_name']}\n")

input("\nEnd of program, press Enter to exit... ")
