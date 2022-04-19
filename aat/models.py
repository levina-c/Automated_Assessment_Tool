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
    tags = db.Column(db.Text, nullable=True)
    explanation = db.Column(db.Text, nullable=True)
    difficulty = db.Column(db.String(15), nullable=False)
    utilised = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f'{self.title}'
class Type2Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_code = db.Column(db.String, db.ForeignKey('courses.courseCode'), nullable=False)
    assessment_id = db.Column(db.Integer, db.ForeignKey('assessments.id'), nullable=True)
    title = db.Column(db.Text, nullable=False)
    correct_answer = db.Column(db.String(5), nullable=False)
    tags = db.Column(db.Text, nullable=True)
    explanation = db.Column(db.Text, nullable=True)
    difficulty = db.Column(db.String(15), nullable=False)
    utilised = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f'{self.title}'
class Assessments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_code = db.Column(db.String, db.ForeignKey('courses.courseCode'), nullable=False)
    assessmenttitle = db.Column(db.Text, nullable=False)
    assessmenttype = db.Column(db.Text, nullable=False)
    duedate = db.Column(db.String, nullable=True)
    duedatetime = db.Column(db.String, nullable=True)
    timelimit = db.Column(db.Integer, nullable=True)
    totalmark = db.Column(db.Integer, nullable=False, default=100)
    status = db.Column(db.String, nullable=False)
    assessmentT1Qs = db.relationship('Type1Questions', backref='assessments', lazy=True)
    assessmentT2Qs = db.relationship('Type2Questions', backref='assessments', lazy=True)
    comments = db.relationship('Comments', backref = 'assessments', lazy=True)

    # @property
    # def format_duedate(self):
    #     return self.duedate.strftime('%Y-%m-%d')

    def __repr__(self):
        return f"Assessment('{self.course_code}',''{self.assessmenttitle}','{self.assessmenttype}','{self.duedate}','{self.duedatetime}')"

class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    assessment_id = db.Column(db.Integer, db.ForeignKey('assessments.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    submissiontime = db.Column(db.DateTime, nullable=False, default = datetime.now())
    rating = db.Column(db.Integer, nullable=False)
