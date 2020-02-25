from flask import Flask
from flask import render_template
from custom.objects.Job import Job
import json


app = Flask(__name__)

@app.route("/")
def hello():

	testJobList = [
		Job(position="Test1", salary = 100 , location="Chicago"),
		Job(position="Test2", salary = 200 , location="Chicago"), 
		Job(position="Test3", salary = 300 , location="Chicago"),
		Job(position="Test1", salary = 100 , location="Chicago"),
		Job(position="Test2", salary = 200 , location="Chicago"), 
		Job(position="Test3", salary = 300 , location="Chicago"),
		Job(position="Test1", salary = 100 , location="Chicago"),
		Job(position="Test2", salary = 200 , location="Chicago"), 
		Job(position="Test3", salary = 300 , location="Chicago"),
		Job(position="Test1", salary = 100 , location="Chicago"),
		Job(position="Test2", salary = 200 , location="Chicago"), 
		Job(position="Test3", salary = 300 , location="Chicago"),
		Job(position="Test1", salary = 100 , location="Chicago"),
		Job(position="Test2", salary = 200 , location="Chicago"), 
		Job(position="Test3", salary = 300 , location="Chicago"),
		Job(position="Test1", salary = 100 , location="Chicago"),
		Job(position="Test2", salary = 200 , location="Chicago"), 
		Job(position="Test3", salary = 300 , location="Chicago"),
		Job(position="Test1", salary = 100 , location="Chicago"),
		Job(position="Test2", salary = 200 , location="Chicago"), 
		Job(position="Test3", salary = 300 , location="Chicago"),
		Job(position="Test1", salary = 100 , location="Chicago"),
		Job(position="Test2", salary = 200 , location="Chicago"), 
		Job(position="Test3", salary = 300 , location="Chicago")
		]


	return render_template("jobList.html", jobs = testJobList)

if __name__ == "__main__":
	app.run()

##Job Is a callable Object now
