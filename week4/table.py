from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Flight(db.Model):
	__tablename__ = "flights"
	id = db.Column(db.Integer, primary_key=True)
	origin = db.Column(db.String, nullable=False)
	destination = db.Column(db.String, nullable=False)
	duration = db.Column(db.Integer, nullable=False)
	#relationships
	passengers = db.relationship("Passenger", backref="flight", lazy=True)
	#backref="flight" --> use flight to access the flight of a passenger
	#lazy=True --> passenger property exists, only extract if we NEED it

	"""
	Basically SELECT * FROM flights JOIN passengers ON flights.id = passengers.flight_id
		WHERE passengers.name = 'Leon';

	Becomes:

	Passenger.query.filter_by(name='Leon').first().flight




	"""
	def add_passenger(self, name): #makes life easier for us
		p = Passenger(name, self.id)
		db.session.add(p)
		db.session.commit()

class Passenger(db.Model):
	__tablename__ = "passengers"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	#flight_id = db.Column(db.Integer, db.ForeignKey("flights.id"), nullable=False)

""" 
So instead of CREATE TABLE flights (blah blah blah)

we can just: db.create_all()
"""