from flask import Flask
from flask import render_template
from flask import request
from custom.objects.Job import Job
import json
import sqlite3
from custom.databaseConnection.stackOverflowToSQLite import *

app = Flask(__name__)


def checkForDB():
	import os.path
	if not os.path.isfile('''StackOverflowJobs.db'''):
		print("The database hasn't been set up yet, it will now be created. (This will only happen on first run)")
		getAllJobs()


def buildQuery(location, distance=50, search=''):
	query = """select * from jobs_in_{} where distance < {}""".format(location, distance)
	if search:
		query += ''' and title like '%{}%' '''.format(search)

	return query

def getDBResult(query, location):
	with sqlite3.connect('StackOverflowJobs.db') as conn:
		c = conn.cursor()
		tempArray = list()
		for row in c.execute(query):
			tempArray.append(Job(position=row[0],
								 location=location,
								 url = row[1],
								 distance = row[3]))			
		return tempArray


@app.route("/")
def hello():
	
	location = request.args.get("Location")
	search = request.args.get("Search")
	distance = request.args.get("Distance")
	if not distance:
		distance = 50

	if not location:
		return render_template("jobList.html", jobs = list())
	else:
		query = buildQuery(location, distance=distance, search=search)
		jobsList = getDBResult(query, location)
		return render_template("jobList.html", jobs = jobsList)


if __name__ == "__main__":
	checkForDB()
	app.run()

##Job Is a callable Object now
