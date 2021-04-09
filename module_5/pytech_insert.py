#Katie Klein
#CSD 310
# 9 April 2021
#Assignment 5.3 - PyTech Insert

from pymongo import MongoClient

#Connect to database
url = "mongodb+srv://admin:admin@cluster0.rpse2.mongodb.net/pytech"
client = MongoClient(url)
students = client.pytech.students

#Insert student doc 1
harry = {
    "student_id": 1007,
    "first_name": "Harry",
    "last_name": "Potter",
}
harry_document_id = students.insert_one(harry).inserted_id

#Insert student doc 2
ron = {
    "student_id": 1008,
    "first_name": "Ron",
    "last_name": "Weasley",
}
ron_document_id = students.insert_one(ron).inserted_id

#Insert student doc 3
hermione = {
    "student_id": 1009,
    "first_name": "Hermione",
    "last_name": "Granger",
}
hermione_document_id = students.insert_one(hermione).inserted_id

#Print inserted statements
print("-- INSERT STATEMENTS --")
print(f"Inserted student record Harry Potter into the students collection with document id {harry_document_id}")
print(f"Inserted student record Ron Weasley into the students collection with document id {ron_document_id}")
print(f"Inserted student record Hermione Granger into the students collection with document id {hermione_document_id}")

input("\nEnd of program, press Enter to exit... ")