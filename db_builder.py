from pymongo import MongoClient

#facilitates CSV I/O
import csv 


#connect to server
#server = MongoClient('homer.stuy.edu')
server = MongoClient('127.0.0.1')

#open (or create) database
db = server.mydb


peeps_raw = open("peeps.csv")
courses_raw = open("courses.csv")
teachers_raw = open("teachers.csv")

peeps = csv.DictReader(peeps_raw)
courses = csv.DictReader(courses_raw)
teachers = csv.DictReader(teachers_raw)


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
    courses_raw.seek(0)
    next(courses)

    #put doc into students collection
    db.students.insert_one(insertStudent) 

for teacher in teachers:
    insertTeacher = {}
    insertTeacher['teacher'] = teacher['teacher']
    insertTeacher['code'] = teacher['code']
    insertTeacher['period'] = teacher['period']
    
    students = []
    for course in courses:
        if course['code'] == teacher['code']:
            students.append(course['id'])
    insertTeacher['students'] = students
    courses_raw.seek(0)
    next(courses)
    
    db.teachers.insert_one(insertTeacher)