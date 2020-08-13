from flask import Flask, render_template, request #imports flask, we want to use flask module. 
import datetime #allows us to see the date

app = Flask(__name__) #create new flask application

@app.route("/") #default page
def index():
	return render_template("index.html")
"""
@app.route('/<string:name>') #we can pass it any name we want!
def hello(name):
	return f"hello, {name}"

@app.route('/main') 
def main():
	headline="do you like trump"
	return render_template("index.html", headline=headline)
	#gives the index.html the headline variable
"""
data = []
#for forms NOTE: GET(allows access), POST (form data)
@app.route("/hello", methods=["GET", "POST"]) #people will be submitting data via POST
def hello(): #form --> route --> hello.html (display)
	if request.method == "GET":
		return render_template("hello.html")
	else:
		name = request.form.get("name")
		data.append(name)
		return render_template("hello.html", data=data)
"""
this checks if it is New Years

@app.route("newyear")
def index():
	now = datetime.datetime.now()
	new_year = new.month == 1 and now.day == 1
	return render_temmplate("index.html",, new_year=new_year)


"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port='80', debug=True) # debug=True