from app import app
from flask import render_template

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/log-in")
def login():
    return render_template('log-in.html')


@app.route("/home-base")
def homebase():
    return render_template('home-base.html')
