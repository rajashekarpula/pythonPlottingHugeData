import sqlite3 as sql
from random import randint
import random

noOfrecords = 1000000
maxValue = 10000
typeValues = ['TCP', 'UDP']

connection = sql.connect("pythonDatabase.sqlite") # connection to the database sample, if the database doesn't exist then it creates by the name given

c = connection.cursor()
c.execute("create table pythonTable(TYPE text, SIZE real)")

for i in range(0, noOfrecords): # insert into the table with random values and random TCP/UDP
	c.execute("insert into pythonTable values(?,?)"
		    ,[random.choice(typeValues),randint(0,maxValue-1)])

connection.commit()
connection.close()







