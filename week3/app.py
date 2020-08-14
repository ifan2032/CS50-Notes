#GOAL: integrate python and sql

import os
import csv
import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('sqlite:///week3.db')
db = scoped_session(sessionmaker(bind=engine))

def main():
	#SELECTING DATA
	flights = db.execute("SELECT origin, destination, duration FROM flights").fetchall()
	for flight in flights:
		print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")

	#IMPORTING DATA
	f = open("flights.csv")
	reader = csv.reader(f)
	for origin, destination, duration in reader:
		db.execute("INSERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, :duration)", 
			{"origin": origin, "destination": destination, "duration": duration})
		print(f"Added flight from {origin} to {destination} lasting {duration}")
	db.commit() #saves the changes

	#LOOKING UP
	flight_id = int(input("\nFlight ID: "))
	flight = db.execute("SELECT origin,destination, duration FROM flights WHERE id= :id",
		{"id":flight_id}).fetchone()

	if flight is None:
		print("NO such flight")
		return
	"""
	passengers = db.execute("SELECT name FROM passengers WHERE flight_id=:flight_id",
		{"flight_id": fligth_id}).fetchall()
	"""



if __name__ == "__main__":
	main()