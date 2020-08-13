#CREATES TABLE
#helps reference stuff in this table
#primary key = primary way I reference a flight (each flight = unique id) 
#each flight has an origin
#not null = I don't want a flight to be in this table if it doesn't have an origin

CREATE TABLE flights (
	id INTEGER PRIMARY KEY, 
	origin VARCHAR NOT NULL, 
	destination VARCHAR NOT NULL,
	duration INTEGER NOT NULL
); 

#INSERTION
INSERT INTO flights 
	(origin, destination, duration) 
	VALUES ('New York', 'London', 415);

#READING FROM DATABASE
SELECT * FROM flights; 
SELECT * FROM flights LIMIT 2;
SELECT origin, destination FROM flights;
SELECT * FROM flights WHERE destination = 'Paris' OR duration > 500;
SELECT AVG(duration) FROM flights WHERE origin = 'New York';
SELECT COUNT(*) FROM flights; 
SELECT MIN(duration) FROM flights;
SELECT * FROM flights WHERE origin LIKE '%a%'; #selects stuff with a in the origin string
SELECT * FROM flights ORDER BY duration ASC; #sorts
SELECT origin, COUNT(*) FROM flights GROUP BY origin HAVING COUNT(*) > 1; #Having is like Where for group by

#UPDATE 
UPDATE flights
	SET duration = 430
	WHERE origin = 'New York', #WHERE tells what rows to change
	AND destination = 'London'; 

#DELETE
DELETE FROM flights
	WHERE destination = 'Tokyo';

#JOINING STUFF (on specifies the connection between the two tables)

#inner join, join stuff that matches
SELECT origin, destination, name FROM flights JOIN passengers on
	passengers.flight_id = flights.id;
#left join (stuff is included even if there is no match)
SELECT origin, destination, name FROM flights LEFT JOIN passengers on
	passengers.flight_id = flights.id;



