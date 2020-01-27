from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!"

@app.route("/ReturningJson")
def returnJson():
	return json.dumps([1, 2, 3, {'4': 5, '6': 7}])

if __name__ == "__main__":
	app.run()
