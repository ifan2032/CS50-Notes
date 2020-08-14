import os
import csv
import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask, render_template, request #imports flask, we want to use flask module. 


app = Flask(__name__) #create new flask application



engine = create_engine('sqlite:///week3.db')
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
	flights = db.execute("SELECT * FROM flights").fetchall()
	return render_template("index.html", flights=flights)

@app.route("/book", methods=["POST"])
def book(): #book a flight
	name = request.form.get("name")
	try:
		flight_id = int(request.form.get("flight_id"))
	except:
		return render_template("index.html", message="Invalid number my dude")

	#insert into passengers table
	"""
	if db.execute("SELECT * FROM flights WHERE id=:id", {"id": flight_id}).rowcount == 0: #rowcount: how many rows exist
		return render_template("index.html", message="No such flight with that ID")
	db.execute("INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id)", {"name":name, "flight_id":flight_id})
	db.commit()
	"""
	return render_template("index.html", message="good job")

@app.route("/flights")
def flights():
	flights = db.execute("SELECT * FROM flights").fetchall()
	return render_template("flights.html", flights=flights)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port='80', debug=True) # debug=True