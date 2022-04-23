from flask import *
from aat import app, db
from aat.forms import AssessmentForm, filterquestionform, chooseQuestions, deleteQuestions, sortAssessment
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

@app.route("/assessment", methods=['GET','POST'])
def assessment():
    allassessments = Assessments.query.order_by(Assessments.course_code, Assessments.status, Assessments.duedate).all()
    allcourses = Courses.query.order_by(Courses.courseCode).all()
    sortassessment = sortAssessment(sorttype='Course')
    # if sortassessment.validate_on_submit():
    sortBy = sortassessment.sorttype.data

    if request.method == 'POST':
        if request.form.get("assessment") == 'Create assessment':
            return redirect(url_for('addassessment'))
        elif request.form.get("assessment") == "Create questions":
            return redirect(url_for('addassessment'))
    return render_template("assessment.html", allassessments=allassessments, allcourses=allcourses, sortassessment=sortassessment, sortBy=sortBy)

@app.route("/indiassessment/<int:assessmentID>", methods=['GET','POST'])
def indiassessment(assessmentID):
    # access specific assessment
    assessment=Assessments.query.get_or_404(assessmentID)
    assessmentT1Qs = Type1Questions.query.filter_by(assessment_id = assessmentID).all()
    assessmentT2Qs = Type2Questions.query.filter_by(assessment_id = assessmentID).all()
    assessmentT1As = Type1Questions.query.filter_by(assessment_id = assessmentID).with_entities(Type1Questions.optionA,Type1Questions.optionB,Type1Questions.optionC,Type1Questions.optionD)
    marks = 0

    for q in assessmentT1Qs:
        marks += q.point
    for q in assessmentT2Qs:
        marks += q.point
    print(marks)
# edit assessment form
    edit_assessment = AssessmentForm(
        course = assessment.course_code,
        assessmenttitle = assessment.assessmenttitle,
        assessmenttype = assessment.assessmenttype,
        duedate = datetime.datetime.strptime(assessment.duedate,'%d/%m/%Y'),
        duedatetime = datetime.datetime.strptime(assessment.duedatetime,"%H:%M"),
        timelimit = assessment.timelimit,
        totalmark = assessment.totalmark,
        retake = assessment.retake)
        
    edit_question = chooseQuestions()
    delete_question = deleteQuestions()

# edit assessment details
    if request.form.get('Save_d') == 'Save':
        assessment.course_code = edit_assessment.course.data
        assessment.assessmenttitle = edit_assessment.assessmenttitle.data
        assessment.assessmenttype = edit_assessment.assessmenttype.data
        assessment.duedate = edit_assessment.duedate.data.strftime('%d/%m/%Y')
        assessment.duedatetime = edit_assessment.duedatetime.data.strftime("%H:%M")
        assessment.timelimit = edit_assessment.timelimit.data
        assessment.totalmark = edit_assessment.totalmark.data
        assessment.retake = edit_assessment.retake.data
        # print(edit_assessment.course.data,edit_assessment.assessmenttitle.data, edit_assessment.assessmenttype.data,edit_assessment.duedate.data,edit_assessment.duedatetime.data,edit_assessment.timelimit.data,edit_assessment.totalmark.data)
        db.session.commit()
        flash(f"{assessment.course_code} {assessment.assessmenttitle} has been updated")

    if request.form.get('del') == 'Delete Assessment':
        flash(f"{assessment.course_code} {assessment.assessmenttitle} has been deleted")
        # questions1todel = Type1Questions.query.filter_by(assessment_id = assessmentID).all()
        # questions2todel = Type2Questions.query.filter_by(assessment_id = assessmentID).all()
        # questions1todel.utilised = False
        # questions2todel.utilised = False
        db.session.delete(assessment)
        db.session.commit()
        for q in assessmentT1Qs:
            if q.assessment_id == None:
                q.utilised = False
        for q in assessmentT2Qs:
            if q.assessment_id == None:
                q.utilised = False
        db.session.commit()
        return redirect(url_for('assessment'))
    elif request.form.get('del') == 'Back':
        return redirect(url_for('assessment'))
    elif request.form.get('del') == 'Publish':
        if marks<assessment.totalmark:
            flash(f'{assessment.totalmark - marks} marks left to reach assigned assessment total marks')
        else:
            flash(f"{assessment.course_code} {assessment.assessmenttitle}  has been published")
            assessment.status = 'Published'
            db.session.commit()
            return redirect(url_for('assessment'))
    elif request.form.get('del') == 'Save':
        if marks<assessment.totalmark:
            flash(f'Total marks in {assessment.title} don\'t add up!')
            flash(f"{assessment.course_code} {assessment.assessmenttitle} has been saved")
            assessment.status = 'Draft'
            db.session.commit()
        else:
            flash(f"{assessment.course_code} {assessment.assessmenttitle} has been saved")
            assessment.status = 'Draft'
            db.session.commit()
        return redirect(url_for('assessment'))
    elif request.form.get('del') == 'Update':
        flash(f"{assessment.course_code} {assessment.assessmenttitle} has been updated")
    elif request.form.get('del') == 'Preview':
        return redirect(url_for('previewassessment', currentAssessmentID=assessmentID))

# delete questions
    delete_question.t1opts.choices = [(q.id, q.title) for q in assessmentT1Qs]
    delete_question.t2opts.choices = [(q.id, q.title) for q in assessmentT2Qs]


    if request.form.get('del') == 'Delete Questions':
        for qID in delete_question.t1opts.data:
            T1Qs_todel = Type1Questions.query.get_or_404(qID)
            T1Qs_todel.assessment_id = None
            T1Qs_todel.utilised = False
        for qID in delete_question.t2opts.data:
            T1Qs_todel = Type2Questions.query.get_or_404(qID)
            T1Qs_todel.assessment_id = None
            T1Qs_todel.utilised = False
        db.session.commit()
        return redirect(url_for('indiassessment', assessmentID=assessment.id))
        # flash("Questions have been deleted")
        
    return render_template("indiassessment.html", assessment=assessment, assessmentT1Qs=assessmentT1Qs, assessmentT1As=assessmentT1As, assessmentT2Qs=assessmentT2Qs, edit_assessment=edit_assessment, edit_question=edit_question, assessmentID=assessmentID, delete_question=delete_question, marks = marks)

@app.route("/addassessment", methods=['GET','POST'])
def addassessment():
    addassessmentform = AssessmentForm()
    if addassessmentform.validate_on_submit():
        assessment = Assessments(course_code = addassessmentform.course.data,
                            assessmenttitle = addassessmentform.assessmenttitle.data,
                            assessmenttype = addassessmentform.assessmenttype.data,
                            duedate = addassessmentform.duedate.data.strftime('%d/%m/%Y'),
                            # duedate = addassessmentform.duedate.data,
                            duedatetime = addassessmentform.duedatetime.data.strftime('%H:%M'),
                            timelimit = addassessmentform.timelimit.data,
                            totalmark = addassessmentform.totalmark.data,
                            retake = addassessmentform.retake.data,
                            status = 'Draft')
        db.session.add(assessment)
        db.session.commit()
        currentAssessment = Assessments.query.order_by(desc(Assessments.id)).first()
        currentAssessmentID = currentAssessment.id
        print(f'{currentAssessmentID}currentAssessmentID')
        if request.form["submit_button"] == "Save and Exit":
            update_status = Assessments.query.get_or_404(currentAssessmentID)
            assessment.status = 'Draft'
            print(f'addassessmentform.savenexit.data {addassessmentform.savenexit.data}')
            return redirect(url_for('assessment'))
        elif request.form["submit_button"] == "Add Questions":
            return redirect(url_for('addassessmentquestion', currentAssessmentID=currentAssessment.id))
    return render_template("addassessment.html", addassessmentform = addassessmentform)

def t1question_query(coursecode, difficultylevel, ifutilised, key):
    return Type1Questions.query.filter_by(course_code = coursecode, difficulty=difficultylevel, utilised = ifutilised, tags = key).all()

def t2question_query(coursecode, difficultylevel, ifutilised, key):
    return Type2Questions.query.filter_by(course_code = coursecode, difficulty=difficultylevel, utilised = ifutilised, tags = key).all()

def t1question_query_noKey(coursecode, difficultylevel, ifutilised):
    return Type1Questions.query.filter_by(course_code = coursecode, difficulty=difficultylevel, utilised = ifutilised).all()

def t2question_query_noKey(coursecode, difficultylevel, ifutilised):
    return Type2Questions.query.filter_by(course_code = coursecode, difficulty=difficultylevel, utilised = ifutilised).all()

def t1question_query_noStatus(coursecode, difficultylevel):
    return Type1Questions.query.filter_by(course_code = coursecode, difficulty=difficultylevel, tags = key).all()

def t2question_query_noStatus(coursecode, difficultylevel):
    return Type2Questions.query.filter_by(course_code = coursecode, difficulty=difficultylevel, tags = key).all()


@app.route("/addassessmentquestion/<int:currentAssessmentID>", methods=['GET','POST'])
def addassessmentquestion(currentAssessmentID):
    assessment=Assessments.query.get_or_404(currentAssessmentID)
    assessmentT1Qs = Type1Questions.query.filter_by(assessment_id = currentAssessmentID).with_entities(Type1Questions.point)
    assessmentT2Qs = Type2Questions.query.filter_by(assessment_id = currentAssessmentID).with_entities(Type2Questions.point)
    coursename = Courses.query.filter_by(courseCode = assessment.course_code).first()
    marks = 0
    noOfQuestions = 0
    for q in assessmentT1Qs:
        marks+=q.point
        noOfQuestions+=1
    for q in assessmentT2Qs:
        marks+=q.point
        noOfQuestions+=1
    filterform = filterquestionform()

    selectquestions = chooseQuestions()
    typeofQs = filterform.qType.data
    status = filterform.used.data
    keyword = filterform.searchbar.data
    difficulty = filterform.difficulty.data
    T1questions = Type1Questions.query.filter_by(course_code = assessment.course_code).all()
    T2questions = Type2Questions.query.filter_by(course_code = assessment.course_code).all()
    
    
    # print(T1questions)
    # print(T2questions)
    if request.form.get("add_question") == "Filter":
        try: 
            if keyword != '':
                # has keyword input
                if status == 'Used':
                    if difficulty == 'Easy':
                        T1questions = t1question_query(assessment.course_code, 'Easy', True, keyword).all()
                        T2questions = t2question_query(assessment.course_code, 'Easy', True, keyword).all()
                    elif difficulty == 'Medium':
                        T1questions = t1question_query(assessment.course_code, 'Medium', True, keyword).all()
                        T2questions = t2question_query(assessment.course_code, 'Medium', True, keyword).all()
                    elif difficulty == 'Difficult':
                        T1questions = t1question_query(assessment.course_code, 'Difficult', True, keyword).all()
                        T2questions = t2question_query(assessment.course_code, 'Difficult', True, keyword).all()
                    # has keyword input + used + all difficulty level
                    else:
                        T1questions = Type1Questions.query.filter_by(course_code = assessment.course_code, utilised = True, tags = keyword).all()
                        T2questions = Type2Questions.query.filter_by(course_code = assessment.course_code, utilised = True, tags = keyword).all()
                # has keyword input + unused
                elif status == 'Unused':
                    if difficulty == 'Easy':
                        T1questions = t1question_query(assessment.course_code, 'Easy', False, keyword).all()
                        T2questions = t2question_query(assessment.course_code, 'Easy', False, keyword).all()
                    elif difficulty == 'Medium':
                        T1questions = t1question_query(assessment.course_code, 'Medium', False, keyword).all()
                        T2questions = t2question_query(assessment.course_code, 'Medium', False, keyword).all()
                    elif difficulty == 'Difficult':
                        T1questions = t1question_query(assessment.course_code, 'Difficult', False, keyword).all()
                        T2questions = t2question_query(assessment.course_code, 'Difficult', False, keyword).all()
                # has keyword input + unused + all difficulty level  
                    else:
                        T1questions = Type1Questions.query.filter_by(course_code = assessment.course_code, utilised = False, tags = keyword).all()
                        T2questions = Type2Questions.query.filter_by(course_code = assessment.course_code, utilised = False, tags = keyword).all()
                # has keyword input + all used status 
                else:
                    if difficulty == 'Easy':
                        T1questions = t1question_query_noStatus(assessment.course_code, 'Easy', keyword).all()
                        T2questions = t2question_query_noStatus(assessment.course_code, 'Easy', keyword).all()
                    elif difficulty == 'Medium':
                        T1questions = t1question_query_noStatus(assessment.course_code, 'Medium', keyword).all()
                        T2questions = t2question_query_noStatus(assessment.course_code, 'Medium', keyword).all()
                    elif difficulty == 'Difficult':
                        T1questions = t1question_query_noStatus(assessment.course_code, 'Difficult', keyword).all()
                        T2questions = t2question_query_noStatus(assessment.course_code, 'Difficult', keyword).all()
                    # has keyword input + all used status + all difficulty level
                    else:
                        T1questions = Type1Questions.query.filter_by(course_code = assessment.course_code, tags = keyword).all()
                        T2questions = Type2Questions.query.filter_by(course_code = assessment.course_code, tags = keyword).all()
            # no keyword input
            else:
                # no keyword input + used
                if status == 'Used':
                    if difficulty == 'Easy':
                        T1questions = t1question_query_noKey(assessment.course_code, 'Easy', True).all()
                        T2questions = t2question_query_noKey(assessment.course_code, 'Easy', True).all()
                    elif difficulty == 'Medium':
                        T1questions = t1question_query_noKey(assessment.course_code, 'Medium', True).all()
                        T2questions = t2question_query_noKey(assessment.course_code, 'Medium', True).all()
                    elif difficulty == 'Difficult':
                        T1questions = t1question_query_noKey(assessment.course_code, 'Difficult', True).all()
                        T2questions = t2question_query_noKey(assessment.course_code, 'Difficult', True).all()
                    # no keyword input + all difficulty level
                    else:
                        T1questions = Type1Questions.query.filter_by(course_code = assessment.course_code, utilised = True).all()
                        T2questions = Type2Questions.query.filter_by(course_code = assessment.course_code, utilised = True).all()
                # no keyword input + unused
                elif status == 'Unused':
                    if difficulty == 'Easy':
                        T1questions = t1question_query_noKey(assessment.course_code, 'Easy', False).all()
                        T2questions = t2question_query_noKey(assessment.course_code, 'Easy', False).all()
                    elif difficulty == 'Medium':
                        T1questions = t1question_query_noKey(assessment.course_code, 'Medium', False).all()
                        T2questions = t2question_query_noKey(assessment.course_code, 'Medium', False).all()
                    elif difficulty == 'Difficult':
                        T1questions = t1question_query_noKey(assessment.course_code, 'Difficult', False).all()
                        T2questions = t2question_query_noKey(assessment.course_code, 'Difficult', False).all()
                    # no keyword input + unused + all difficulty level  
                    else:
                        T1questions = Type1Questions.query.filter_by(course_code = assessment.course_code, utilised = False).all()
                        T2questions = Type2Questions.query.filter_by(course_code = assessment.course_code, utilised = False).all()
                # no keyword input + all used status
                else:
                    if difficulty == 'Easy':
                        T1questions = t1question_query_noStatus(assessment.course_code, 'Easy').all()
                        T2questions = t2question_query_noStatus(assessment.course_code, 'Easy').all()
                    elif difficulty == 'Medium':
                        T1questions = t1question_query_noStatus(assessment.course_code, 'Medium').all()
                        T2questions = t2question_query_noStatus(assessment.course_code, 'Medium').all()
                    elif difficulty == 'Difficult':
                        T1questions = t1question_query_noStatus(assessment.course_code, 'Difficult').all()
                        T2questions = t2question_query_noStatus(assessment.course_code, 'Difficult').all()
                # no keyword input + all used status + all difficulty level 
                    else:
                        T1questions = Type1Questions.query.filter_by(course_code = assessment.course_code).all()
                        T2questions = Type2Questions.query.filter_by(course_code = assessment.course_code).all()
            selectquestions.t1opts.choices = [(T1q.id, T1q.title) for T1q in T1questions]
            selectquestions.t2opts.choices = [(T2q.id, T2q.title) for T2q in T2questions]
            print(type(T1questions))
        except:
            print("no such query")    
    
    elif request.form.get("add_question") == "Add Questions":
        # try:
        
        for qID in selectquestions.t1opts.data:
            selectedQs = Type1Questions.query.get_or_404(qID)
            if selectedQs.utilised == False:
                marks += selectedQs.point
                noOfQuestions+=1
                selectedQs.assessment_id = currentAssessmentID
                selectedQs.utilised = True
                db.session.commit()
                flash("Questions added")
            elif selectedQs.assessment_id == currentAssessmentID:
                flash(f'{selectedQs.title} has already been added to this assessment.')
            elif selectedQs.utilised == True:
                flash(f'{selectedQs.title} has been used.')
        for qID in selectquestions.t2opts.data:
            selectedQs = Type2Questions.query.get_or_404(qID)
            if selectedQs.utilised == False:
                marks += selectedQs.point
                noOfQuestions+=1
                selectedQs.assessment_id = currentAssessmentID
                selectedQs.utilised = True
                db.session.commit()
                flash("Questions added")
            elif selectedQs.assessment_id == currentAssessmentID:
                flash(f'{selectedQs.title} has already been added to this assessment.')
            elif selectedQs.utilised == True:
                flash(f'{selectedQs.title} has been used.')
        
            # return redirect(url_for('previewassessment', currentAssessmentID=currentAssessmentID))
        # except:
        #     flash('No questions have been selected')
        #     print('no t1/t2 questions have been chosen')

    elif request.form.get("add_question") == "Edit Assessment":
        return redirect(url_for('indiassessment', assessmentID = currentAssessmentID))
    elif request.form.get("add_question") == "Save":
        if marks<assessment.totalmark:
            flash(f'Total marks in {assessment.assessmenttitle} don\'t add up!')
            flash(f"{assessment.course_code} {assessment.assessmenttitle} has been saved as draft")
            assessment.status = 'Draft'
            db.session.commit()
        else:
            flash(f"{assessment.course_code} {assessment.assessmenttitle} has been saved as draft")
            assessment.status = 'Draft'
            db.session.commit()
        return redirect(url_for('assessment'))

    elif request.form.get("add_question") == "Preview":
        return redirect(url_for('previewassessment', currentAssessmentID=currentAssessmentID))

    elif request.form.get("add_question") == "Publish":
        if marks<assessment.totalmark:
            flash(f'{assessment.totalmark - marks} marks left to reach assigned assessment total marks')
        else:
            flash(f"{assessment.course_code} {assessment.assessmenttitle}  has been published")
            assessment.status = 'Published'
            db.session.commit()
        # flash(f"{assessment.course_code} {assessment.assessmenttitle} has been published")
            return redirect(url_for('assessment'))

    return render_template("addassessmentquestion.html", assessment=assessment, filterform=filterform, selectquestions=selectquestions, typeofQs=typeofQs, marks=marks, coursename=coursename, noOfQuestions=noOfQuestions)

@app.route("/previewassessment/<int:currentAssessmentID>", methods=['GET','POST'])
def previewassessment(currentAssessmentID):
    assessment=Assessments.query.get_or_404(currentAssessmentID)
    assessmentT1Qs = Type1Questions.query.filter_by(assessment_id = currentAssessmentID).with_entities(Type1Questions.title, Type1Questions.optionA,Type1Questions.optionB,Type1Questions.optionC,Type1Questions.optionD, Type1Questions.point)
    assessmentT2Qs = Type2Questions.query.filter_by(assessment_id = currentAssessmentID).with_entities(Type2Questions.title, Type2Questions.point)
    allassessmentQs = assessmentT1Qs.union(assessmentT2Qs)
    assessmentT1As = Type1Questions.query.filter_by(assessment_id = currentAssessmentID).with_entities(Type1Questions.optionA,Type1Questions.optionB,Type1Questions.optionC,Type1Questions.optionD)
    coursename = Courses.query.filter_by(courseCode = assessment.course_code).first()
    marks = 0
    for q in assessmentT1Qs:
        marks += q.point
    for q in assessmentT2Qs:
        marks += q.point
    
    if request.form.get("preview") == 'Add Questions':
        return redirect(url_for('addassessmentquestion', currentAssessmentID=currentAssessmentID))
    elif request.form.get("preview") == 'Back':
        return redirect(url_for('assessment'))
    elif request.form.get("preview") == 'Edit Assessment':
        return redirect(url_for('indiassessment', assessmentID=assessment.id))
    elif request.form.get("preview") == 'Publish':
        if marks==assessment.totalmark:
            flash(f"{assessment.course_code} {assessment.assessmenttitle}  has been published")
            assessment.status = 'Published'
            db.session.commit()
            return redirect(url_for('assessment'))
        elif marks < assessment.totalmark:
            flash(f'{assessment.totalmark - marks} marks left to reach assigned assessment total marks')
        else:
            flash(f'{marks - assessment.totalmark } marks over assigned assessment total marks')
    elif request.form.get("preview") == 'Save':
        if marks==assessment.totalmark:
            flash(f"{assessment.course_code} {assessment.assessmenttitle} has been saved")
            assessment.status = 'Draft'
            db.session.commit()
        else:
            flash(f'Total marks in {assessment.assessmenttitle} don\'t add up!')
            flash(f"{assessment.course_code} {assessment.assessmenttitle} has been saved")
            assessment.status = 'Draft'
            db.session.commit()
        return redirect(url_for('assessment'))
    elif request.form.get("preview") == 'Update':
        if marks<assessment.totalmark:
            flash(f'Total marks in {assessment.title} don\'t add up!')
            flash(f"{assessment.course_code} {assessment.assessmenttitle} has been updated")
        else:
            flash(f"{assessment.course_code} {assessment.assessmenttitle} has been updated")
        return redirect(url_for('assessment'))
    return render_template('previewassessment.html', assessment=assessment, assessmentT1Qs=assessmentT1Qs, assessmentT1As=assessmentT1As, assessmentT2Qs=assessmentT2Qs, allassessmentQs=allassessmentQs, marks=marks, coursename=coursename)

@app.route("/feedback")
def feedback():
    return render_template("feedback.html") 

@app.route("/logout")
def logout():
    return render_template("index.html")