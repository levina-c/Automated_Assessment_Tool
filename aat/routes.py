from flask import render_template
from aat import app

# @app.route("/")
# @app.route("/index")
# def index():
#     return render_template("index.html")

@app.route("/")
@app.route("/index")
@app.route("/activitystream")
def activitystream():
    return render_template("activitystream.html")

@app.route("/course")
def course():
    return render_template("course.html")

@app.route("/assessment")
def assessment():
    return render_template("assessment.html")

@app.route("/add_assessment")
def add_assessment():
    return render_template("add_assessment.html")

@app.route("/feedback")
def feedback():
    return render_template("feedback.html") 

@app.route("/logout")
def logout():
    return render_template("index.html")