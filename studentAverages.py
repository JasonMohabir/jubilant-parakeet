from pymongo import MongoClient

def averages(studentID): 
	doc = db.students.find_one({"id" : studentID});
	courses = doc["courses"]
	total = 0;
	for course in courses:
		total += int(courses["mark"])
	return doc["name"] + doc["id"] + int(total * 1.0 / len(courses))

c = db.students.find()
for doc in c:
	print averages(doc["id"])


