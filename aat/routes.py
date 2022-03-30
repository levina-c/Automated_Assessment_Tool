from flask import render_template, redirect, url_for, session
from aat import app
from aat.forms import AssessmentForm

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

@app.route("/addassessment", methods=['GET','POST'])
def addassessment():
    addassessmentform = AssessmentForm()
    if addassessmentform.validate_on_submit():
        assessment = Assessment(course_id = addassessmentform.coursename.data[:6],
                            ATitle = addassessmentform.assessmenttitle.data,
                            AType = addassessmentform.assessmenttype.data,
                            dueDate = addassessmentform.duedate.data,
                            dueDateTime = addassessmentform.duedatetime.data,
                            timeLimit = addassessmentform.timelimit.data,
                            totalMark = addassessmentform.totalmark.data)
        # session['duedate'] = addassessmentform.duedate.data
        # session['duedatetime'] = addassessmentform.duedatetime.data
        return redirect(url_for("addassessmentquestion"))
    return render_template("addassessment.html", addassessmentform = addassessmentform, course_id=course_id, ATitle=ATitle, AType=AType, dueDate=dueDate, dueDateTime=dueDateTime, timeLimit=timeLimit, totalMark=totalMark)

@app.route("/previewassessment", methods=['GET','POST'])
def previewassessment():
    duedate = session['duedate']
    duedatetime = session['duedatetime']
    return render_template('previewassessment.html')

@app.route("/feedback")
def feedback():
    return render_template("feedback.html") 

@app.route("/logout")
def logout():
    return render_template("index.html")