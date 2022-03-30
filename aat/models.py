from datetime import datetime
from aat import db

class Courses(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    courseCode = db.Column(db.String(7), nullable=False, primary_key=True)
    courseName = db.Column(db.Text, nullable=False)
    assessment = db.relationship('Assessment', backref='course', lazy='dynamic')
    type1Qs = db.relationship('Type1Quesions', backref='course', lazy='dynamic')
    type2Qs = db.relationship('Type2Quesions', backref='course', lazy='dynamic')
    # question = db.relationship('Questions', backref='course', lazy='dynamic')

class Assessments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.String, db.ForeignKey('course.courseCode', nullable=False))
    ATitle = db.Column(db.Text, nullable=False)
    AType = db.Column(db.Text, nullable=False)
    dueDate = db.Column(db.Date, nullable=True)
    dueDateTime = db.Column(db.DateTime, nullable=True)
    timeLimit = db.Column(db.Integer, nullable=True)
    totalMark = db.Column(db.Integer, nullable=False, default=100)

# class Questions(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     questionT1_id = db.Column(db.Integer, db.ForeignKey('type1Questions.id'), nullable=True)
#     questionT2_id = db.Column(db.Integer, db.ForeignKey('type2Questions.id'), nullable=True)
#     used = db.Column(db.Boolean, nullable=False, default=False)

class Type1Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.String, db.ForeignKey('course.courseCode', nullable=False))
    content = db.Column(db.Text, nullable=False)
    optA = db.Column(db.Text, nullable=False)
    optB = db.Column(db.Text, nullable=False)
    optC = db.Column(db.Text, nullable=False)
    optD = db.Column(db.Text, nullable=True)
    answer = db.Column(db.String(1), nullable=False)
    explanation = db.Column(db.Text, nullable=True)
    difficulty = db.Column(db.String(15), nullable=False)
    used = db.Column(db.Boolean, nullable=False, default=False)
    # questions = db.relationship('Questions', backref='type1questions', lazy='dynamic')
    
class Type2Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.String, db.ForeignKey('course.courseCode', nullable=False))
    content = db.Column(db.Text, nullable=False)
    answer = db.Column(db.String(5), nullable=False)
    explanation = db.Column(db.Text, nullable=True)
    difficulty = db.Column(db.String(15), nullable=False)
    used = db.Column(db.Boolean, nullable=False, default=False)
    # questions = db.relationship('Questions', backref='type2questions', lazy='dynamic')