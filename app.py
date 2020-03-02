from flask import Flask
from flask import render_template
from flask import request
from custom.objects.Job import Job
import json
import sqlite3
from custom.databaseConnection.stackOverflowToSQLite import *
import webbrowser

# GOOGLE_MAPS_API_KEY = None

latLongDict = {"Chicago": '41.881832, -87.623177',
			   "Los_Angeles": '34.052235, -118.243683',
			   "New_York": '40.730610, -73.935242'}


app = Flask(__name__)

def loadAPIKey():
	with open('API_KEY.txt', 'r') as txtFile:
		data = txtFile.read()
		if not data:
			print()
			print('WARNING: No Google API key was provided, the map will not work correctly')
			print()
			return None
		else:
			return data


def checkForDB():
	import os.path
	if not os.path.isfile('''StackOverflowJobs.db'''):
		print("The database hasn't been set up yet, it will now be created. (This will only happen on first run)")
		getAllJobs()


def buildQuery(location, distance=50, search=''):
	query = """select * from jobs_in_{} where distance <= {}""".format(location, distance)
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
		return render_template("jobList.html", jobs = jobsList, apikey = GOOGLE_MAPS_API_KEY, coords = latLongDict[location], circleRadiusInMeters = int(int(distance) * 1609.344))


if __name__ == "__main__":
	global GOOGLE_MAPS_API_KEY
	GOOGLE_MAPS_API_KEY = loadAPIKey()
	checkForDB()
	webbrowser.open('localhost:5000')
	app.run()


##Job Is a callable Object now
