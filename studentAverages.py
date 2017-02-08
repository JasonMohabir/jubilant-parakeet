from pymongo import MongoClient

#connect to server
#server = MongoClient('homer.stuy.edu')
server = MongoClient('127.0.0.1')

#open (or create) database
db = server.mydb

def averages(studentID): 
	doc = db.students.find_one({"id" : studentID});
	courses = doc["courses"]
	total = 0;
	for course in courses:
		total += int(course["mark"])
	#print courses
	#print len(courses)
	return doc["name"] + " " + doc["id"] + " " + str(total * 1.0 / len(courses))

c = db.students.find()
for doc in c:
	#print doc
	print averages(doc["id"])


