# Day 27

from flask import Flask, render_template
import os
import pymongo

MONGODB_URI = os.environ.get("MONGODB_URI")
client = pymongo.MongoClient(MONGODB_URI)

# Creating database
db = client.thirty_days_of_python

# Creating students collection and inserting a document
students = [
        {'name':'David','country':'UK','city':'London','age':34},
        {'name':'John','country':'Sweden','city':'Stockholm','age':28},
        {'name':'Sami','country':'Finland','city':'Helsinki','age':25},
    ]
for student in students:
    db.students.insert_one(student)

student = db.students.find_one()
print(student)

query = {
    "country":"Finland"
}

students = db.students.find(query).sort('age', -1).limit(3)
for student in students:
    print(student)

query = {'age':250}
new_value = {'$set':{'age':38}}

db.students.update_one(query, new_value)

query = {'name':'John'}
db.students.delete_one(query)

db.students.drop()


app = Flask(__name__)

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))
    app.run(debug = True, host = "0.0.0.0", port = port)
