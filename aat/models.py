from datetime import datetime
from aat import db

class Courses(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    courseCode = db.Column(db.String(7), nullable=False, primary_key=True)
    courseName = db.Column(db.Text, nullable=False)
    assessment = db.relationship('Assessments', backref='courses', lazy='dynamic')
    type1Qs = db.relationship('Type1Questions', backref='courses', lazy='dynamic')
    type2Qs = db.relationship('Type2Questions', backref='courses', lazy='dynamic')

class Assessments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_code = db.Column(db.String, db.ForeignKey('courses.courseCode'), nullable=False)
    ATitle = db.Column(db.Text, nullable=False)
    AType = db.Column(db.Text, nullable=False)
    dueDate = db.Column(db.Date, nullable=True)
    dueDateTime = db.Column(db.DateTime, nullable=True)
    timeLimit = db.Column(db.Integer, nullable=True)
    totalMark = db.Column(db.Integer, nullable=False, default=100)
    assessmentQs = db.relationship('AssessmentQuestions', backref='assessments', lazy='dynamic')

class AssessmentQuestions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    assessment_id = db.Column(db.Integer, db.ForeignKey('assessments.id'), nullable=False)
    questionT1_id = db.Column(db.Integer, db.ForeignKey('type1questions.id'), nullable=True)
    questionT2_id = db.Column(db.Integer, db.ForeignKey('type2questions.id'), nullable=True)
class Type1Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_code = db.Column(db.String, db.ForeignKey('courses.courseCode'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    optA = db.Column(db.Text, nullable=False)
    optB = db.Column(db.Text, nullable=False)
    optC = db.Column(db.Text, nullable=False)
    optD = db.Column(db.Text, nullable=True)
    answer = db.Column(db.String(1), nullable=False)
    explanation = db.Column(db.Text, nullable=True)
    difficulty = db.Column(db.String(15), nullable=False)
    used = db.Column(db.Boolean, nullable=False, default=False)
    assessmentQ = db.relationship('AssessmentQuestions', backref='type1questions', lazy='dynamic')
    
class Type2Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_code = db.Column(db.String, db.ForeignKey('courses.courseCode'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    answer = db.Column(db.String(5), nullable=False)
    explanation = db.Column(db.Text, nullable=True)
    difficulty = db.Column(db.String(15), nullable=False)
    used = db.Column(db.Boolean, nullable=False, default=False)
    assessmentQ = db.relationship('AssessmentQuestions', backref='type2questions', lazy='dynamic')