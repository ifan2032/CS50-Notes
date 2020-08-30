from flask import Flask, render_template, request, jsonify
import time
from table import *

app = Flask(__name__)

@app.route("/")
def main():
	return "Hello world"

@app.route("/posts", methods=["POST"]) #generate posts from an infinite list
def post():
	start = int(request.form.get("start") or 0)
	end = int(request.form.get("end") or (start + 9))

	#generate list of posts
	data = []
	for i in range(start, end + 1):
		data.append(f"Post #{i}")

	#delay speed
	time.sleep(1)

	return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port='80', debug=True) # debug=True