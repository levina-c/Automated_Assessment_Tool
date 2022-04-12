from datetime import datetime
from aat import db

class Courses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    courseCode = db.Column(db.String(7), unique=True, nullable=False)
    courseName = db.Column(db.Text, nullable=False)
    assessment = db.relationship('Assessments', backref='courses', lazy=True)
    type1Qs = db.relationship('Type1Questions', backref='courses', lazy=True)
    type2Qs = db.relationship('Type2Questions', backref='courses', lazy=True)
class Type1Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_code = db.Column(db.String(7), db.ForeignKey('courses.courseCode'), nullable=False)
    assessment_id = db.Column(db.Integer, db.ForeignKey('assessments.id'), nullable=True)
    title = db.Column(db.Text, nullable=False)
    optionA = db.Column(db.Text, nullable=False)
    optionB = db.Column(db.Text, nullable=False)
    optionC = db.Column(db.Text, nullable=False)
    optionD = db.Column(db.Text, nullable=True)
    correct_answer = db.Column(db.String(1), nullable=False)
    tags = db.Column(db.PickleType, nullable=True)
    explanation = db.Column(db.Text, nullable=True)
    difficulty = db.Column(db.String(15), nullable=False)
    utilised = db.Column(db.Boolean, nullable=False, default=False)
class Type2Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_code = db.Column(db.String, db.ForeignKey('courses.courseCode'), nullable=False)
    assessment_id = db.Column(db.Integer, db.ForeignKey('assessments.id'), nullable=True)
    title = db.Column(db.Text, nullable=False)
    correct_answer = db.Column(db.String(5), nullable=False)
    explanation = db.Column(db.Text, nullable=True)
    difficulty = db.Column(db.String(15), nullable=False)
    utilised = db.Column(db.Boolean, nullable=False, default=False)
class Assessments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_code = db.Column(db.String, db.ForeignKey('courses.courseCode'), nullable=False)
    ATitle = db.Column(db.Text, nullable=False)
    AType = db.Column(db.Text, nullable=False)
    dueDate = db.Column(db.Date, nullable=True)
    dueDateTime = db.Column(db.DateTime, nullable=True)
    timeLimit = db.Column(db.Integer, nullable=True)
    totalMark = db.Column(db.Integer, nullable=False, default=100)
    assessmentT1Qs = db.relationship('Type1Questions', backref='assessments', lazy=True)
    assessmentT2Qs = db.relationship('Type2Questions', backref='assessments', lazy=True)

    def __repr__(self):
        return f"Assessment('{self.course_code}',''{self.ATitle}','{self.AType}','{self.dueDate}','{self.dueDateTime}')"
