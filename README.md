# CS50-Notes
A collection of my notes while self-learning CS50's Web Development Course


## WEEK 1

## WEEK 2 - FLASK
* How to setup a flask backend for a web application
* Make sure you have templates folder storing html files
* Gather and store information from frontend

### How to setup Flask

```
from flask import Flask, render_template, request #imports flask, we want to use flask module. 
import datetime #allows us to see the date

app = Flask(__name__) #create new flask application

@app.route("/") #default page
def index():
	return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port='80', debug=True) # debug=True
```

## WEEK 3 - SQL

* How to create/insert/delete/select from db using SQL
* SQL inner join vs left join
* How to use SQL within a Flask framework using SQLALCHEMY (see app.py or site.py for flask documentation)
* Review of Jinja notation 

### How to setup sqlalchemy

```
pip install sqlalchemy
```
Make sure you have this at the start of your python file:

```
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('sqlite:///week3.db') #relative path
db = scoped_session(sessionmaker(bind=engine))
```

## WEEK 4 - Flask-SQLAlchemy and APIs

* Creating/Inserting/Delating/Selecting using Flask-SQLAlchemy
* Introduction to using/creating APIs
* Object Oriented Programming

APIs:

```
pip install requests
```

Flask-SQLAlchemy

```
pip install flask_sqlalchemy
```

Put this on top of your file:

```
import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
```

## Week 5 - Javascript