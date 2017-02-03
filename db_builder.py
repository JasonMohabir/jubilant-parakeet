from pymongo import MongoClient
import csv

server = MongoClient('127.0.0.1')

foo1 = open("peeps.csv")
foo2 = open("courses.csv")
d1 = csv.DictReader(foo1)
d2 = csv.DictReader(foo2)
