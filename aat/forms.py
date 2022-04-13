from flask_wtf import FlaskForm
from flask_datepicker import datepicker
from wtforms import RadioField, SelectField, SubmitField, StringField, IntegerField, TimeField
from wtforms.validators import InputRequired, ValidationError
from datetime import datetime
from wtforms.fields import DateField

class AssessmentForm(FlaskForm):
    course = SelectField('Course', validators=[InputRequired()], choices=[('Select Course'),('CMT120 Fundamentals of Programming'),('CMT129 Algorithms, Data Structures and Programming'),('CMT220 Databases and Modelling')], default='Select Course')
    assessmenttitle = StringField('Assessment Title', validators=[InputRequired()])
    assessmenttype = SelectField('Select Type', validators=[InputRequired()], choices=[('Select Type'),('Class quiz'), ('Test'),('Exam')], default='Select Type')
    duedate = DateField('Due Date', format='%Y-%m-%d', default=datetime.now())
    duedatetime = TimeField('Time', format='%H:%M', default=datetime.now())
    timelimit = IntegerField('Time Limit', default='60')
    totalmark = IntegerField('Total Mark', default='100')
    savenexit = SubmitField('Save and Exit')
    nextpage = SubmitField('Next')

    def validate_course(self, course):
        if course != 'Select Course':
            raise ValidationError('Please select a course')
    
    def validate_assessmenttype(self, assessmenttype):
        if assessmenttype != 'Select Type':
            raise ValidationError('Please select an assessment type')