from flask import Flask, render_template, request, session
from cs50 import SQL
from tempfile import mkdtemp
from flask_session import Session

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/more")
def more():
    return render_template("more.html")

@app.route("/trips")
def trips():
    return render_template("trips.html")

@app.route("/donate")
def donate():
    return render_template("donate.html")

@app.route("/result")
def result():
    answer = request.args.get('answer')
    if answer == '2':
        db.execute('update work set points = points + 1 where id = :id', id=session["user_id"])
    total_points = db.execute('select Points from work where id = :id', id=session["user_id"])
    return render_template("result.html", total_points=total_points[0]['Points'])

@app.route("/contact")
def contact():

    return render_template("contact.html")
