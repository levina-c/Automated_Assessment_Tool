from flask import render_template, redirect, url_for, session
from aat import app, db
from aat.forms import AssessmentForm
from aat.models import Courses, Assessments, Type1Questions, Type2Questions

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
        print("as")
        print(addassessmentform.duedate.data,type(addassessmentform.duedate.data), addassessmentform.duedatetime.data, type(addassessmentform.duedatetime.data))
        assessment = Assessments(course_code = addassessmentform.course.data[:6],
                            ATitle = addassessmentform.assessmenttitle.data,
                            AType = addassessmentform.assessmenttype.data,
                            dueDate = addassessmentform.duedate.data,
                            dueDateTime = addassessmentform.duedatetime.data,
                            timeLimit = addassessmentform.timelimit.data,
                            totalMark = addassessmentform.totalmark.data)
        print(addassessmentform.duedate.data,type(addassessmentform.duedate.data), addassessmentform.duedatetime.data, type(addassessmentform.duedatetime.data))
        print("asdfsdfas")
        db.session.add(assessment)
        db.session.commit()
        return redirect(url_for("addassessmentquestion"))
    return render_template("addassessment.html", addassessmentform = addassessmentform)

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