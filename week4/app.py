from flask import Flask, render_template, request
from table import *
import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
	db.create_all() 


	"""
	flights = Flight.query.all()
	for flight in flights:
		print(flight.origin + flight.destination)
	"""

	#add passenger
	#flight.add_passenger("Bob") [WE ALREADY WROTE THE METHOD IN TABLE.PY!!]

	#get all passengers:
	#passengers = flight.passengers [LINE 11 in table.py]



if __name__ == "__main__":
	with app.app_context():
		main()

"""
INSERTION

flight = Flight("New York", "Paris", 540)
db.session.add(flight)
db.session.commit() #go ahead and "save" changes

SELECTION

SELECT * FROM flights WHERE origin= 'Paris'; --> Flight.query.filter_by(origin="Paris").all() 
SELECT COUNT(*) FROM flights WHERE origin="Paris" --> 
	Flight.query.filter_by(origin="Paris").count() OR
	Flight.query.filter(Flight.origin != "Paris").all()
SELECT * FROM flights WHERE origin LIKE "%a%" -->
	Flight.query.filter(Flight.origin.like("%a%")).all()
SELECT * FROM flights WHERE origin IN ('Tokyo', 'Paris');
	Flight.query.filter(Flight.origin.in_(["Tokyo", "Paris"])).all()
SELECT * FROM flights WHERE blah blah OR blah blah
	Flight.query.filter(or_(Flight.blah == blah, Flight.blah == blah)).all()
SELECT * FROM flights JOIN passengers ON flights.id = passengers.fought_id;

UPDATE

UPDATE flights SET duration = 280 WHERE id = 6; --> flight = Flight.query.get(6) then flight.duration = 280 then commit

ORDER

Flight.query.order_by(Flight.origin).all()