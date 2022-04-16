from flask import *
from aat import app, db
from aat.forms import AssessmentForm, sortQuestionsByType, chooseQuestions, searchKeywords, chooseQuestions2
from aat.models import Courses, Assessments, Type1Questions, Type2Questions
import datetime
from sqlalchemy import desc, asc

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
        assessment = Assessments(course_code = addassessmentform.course.data,
                            assessmenttitle = addassessmentform.assessmenttitle.data,
                            assessmenttype = addassessmentform.assessmenttype.data,
                            duedate = addassessmentform.duedate.data.strftime('%Y-%m-%d'),
                            duedatetime = addassessmentform.duedatetime.data.strftime('%H:%M'),
                            timelimit = addassessmentform.timelimit.data,
                            totalmark = addassessmentform.totalmark.data)
        db.session.add(assessment)
        db.session.commit()
        currentAssessment = Assessments.query.order_by(desc(Assessments.id)).first()
        currentAssessmentID = currentAssessment.id
        print(f'{currentAssessmentID}currentAssessmentID')
        if request.form["submit_button"] == "Save and Exit":
            print(f'addassessmentform.savenexit.data {addassessmentform.savenexit.data}')
            return redirect(url_for('assessment'))
        elif request.form["submit_button"] == "Add Questions":
            return redirect(url_for('addassessmentquestion', currentAssessmentID=currentAssessment.id))
    return render_template("addassessment.html", addassessmentform = addassessmentform)

def t1question_query(coursecode):
    return Type1Questions.query.filter_by(course_code=coursecode).all()

def t2question_query(coursecode):
    return Type2Questions.query.filter_by(course_code=coursecode).all()

@app.route("/addassessmentquestion/<int:currentAssessmentID>", methods=['GET','POST'])
def addassessmentquestion(currentAssessmentID):
    assessment=Assessments.query.get_or_404(currentAssessmentID)
    questions = Type1Questions.query.all()
    sortselection = sortQuestionsByType(qType='All')
    selected = sortselection.qType.data
    chooseQs = chooseQuestions()
    searchform = searchKeywords()
    keyword = searchform.searchbar.data
    filteredquestion = []
    print(keyword)
    # if sortselection.validate_on_submit():
    #     if selected == 'Type1':
    #         questions = t1question_query(assessment.course_code)
    #         if keyword != '':
    #             questions = Type1Questions.query.filter_by(course_code = assessment.course_code, tags=keyword).all()
    #     else:
    #         questions = t2question_query(assessment.course_code)
    #         if keyword != '':
    #             questions = Type2Questions.query.filter_by(course_code = assessment.course_code, tags=keyword).all()
    #     for q in questions:
    #         filteredquestion.append(q)
            # print(q.title)
            # print(filteredquestion)
        # chooseQs.opts.choices = [(filteredquestion.title, filteredquestion.title) for filteredquestion in questions]
    # if request.form["add_q_btn"] == "Add Question(s)":
        # print('adsded')
        # change question used status
    # if chooseQs.validate_on_submit():
    #     print(f"selected {request.form.getlist('opts')}")
    #     selectedquestions = []
        # print(chooseQs.opts.data)
        # add assessment id to question

    # if request.method == 'POST':
    #     print(request.form.getlist("CQ"))

    form = chooseQuestions2()

    if form.validate_on_submit():
        print(f'chosen: {form.t1opts.data}')

    return render_template("addassessmentquestion.html", assessment=assessment, sortselection=sortselection, questions=questions, selected=selected, chooseQs=chooseQs, filteredquestion=filteredquestion, searchform=searchform, form=form)

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