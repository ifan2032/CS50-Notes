from flask import Flask, jsonify, render_template, request
from flask_socketio import SocketIO, emit
import requests

app = Flask(__name__)
socketio = SocketIO(app)

lst = []
votes = {"yes": 0, "no": 0, "maybe": 0}

@app.route("/")
def index():
	return render_template("index.html", votes=votes)

@socketio.on("submit vote")
def vote(data):
	selection = data["selection"]
	votes[selection] += 1
	emit("vote totals", votes, broadcast=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port='80', debug=True) # debug=True
