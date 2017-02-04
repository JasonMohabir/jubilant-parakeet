from pymongo import MongoClient

#facilitates CSV I/O
import csv 


#connect to server
#server = MongoClient('localhost')
server = MongoClient('127.0.0.1')

#open (or create) database
db = server.mydb


peeps_raw = open("peeps.csv")
courses_raw = open("courses.csv")

peeps = csv.DictReader(peeps_raw)
courses = csv.DictReader(courses_raw)


for student in peeps:
    insertStudent = {} #the document
    insertStudent['name'] = student['name']
    insertStudent['age'] = student['age']
    insertStudent['id'] = student['id']

    grades = []
    for course in courses:
        if course['id'] == insertStudent['id']:
            grades.append( { 'code' : course['code'], 'mark' : course['mark'] } )
    insertStudent['courses'] = grades

    #put doc into students collection
    db.students.insert_one(oneStudent) 
