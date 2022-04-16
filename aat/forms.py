from flask_wtf import FlaskForm
from flask_datepicker import datepicker
from wtforms import RadioField, SelectField, SubmitField, StringField, IntegerField, TimeField, RadioField, SelectMultipleField, widgets, SearchField
from wtforms.validators import InputRequired, ValidationError
from datetime import datetime
from wtforms.fields import DateField
from flask_sqlalchemy import SQLAlchemy
from wtforms_sqlalchemy.fields import QuerySelectMultipleField
from aat.models import Type1Questions, Type2Questions

class AssessmentForm(FlaskForm):
    course = SelectField('Course', validators=[InputRequired()], choices=[
        ('','Select Course'),
        ('CMT120','CMT120 Fundamentals of Programming'),
        ('CMT129','CMT129 Algorithms, Data Structures and Programming'),
        ('CMT220','CMT220 Databases and Modelling')])
    assessmenttitle = StringField('Assessment Title', validators=[InputRequired()])
    assessmenttype = SelectField('Assessment Type', validators=[InputRequired()], choices=[('', 'Select Type'),('Class quiz','Class quiz'), ('Test','Test'),('Exam','Exam')])
    duedate = DateField('Due Date', format='%Y-%m-%d', default=datetime.now())
    duedatetime = TimeField('Time', format='%H:%M', default=datetime.now())
    timelimit = IntegerField('Time Limit', default='60')
    totalmark = IntegerField('Total Mark', default='100')
    savenexit = SubmitField('Save and Exit')
    nextpage = SubmitField('Next')

    def validate_course(self, course):
        if course is None:
            raise ValidationError('Please select a course')
    
    def validate_assessmenttype(self, assessmenttype):
        if assessmenttype is None:
            raise ValidationError('Please select an assessment type')

class sortQuestionsByType(FlaskForm):
    qType = SelectField('Question Type', validators=[InputRequired()], choices=[('All', 'All'),('Type1', 'Multiple Choice'), ('Type2', 'True/False')])
    submit = SubmitField('Filter')

class MultipleCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(html_tag='ol', prefix_label=False)
    option_widget = widgets.CheckboxInput()

class chooseQuestions(FlaskForm):
    opts = MultipleCheckboxField(label='Questions', choices=[])
    submit = SubmitField('Add')
class searchKeywords(FlaskForm):
    searchbar = SearchField(label='Enter Keyword')
    submit = SubmitField('Search')
class QueryMultipleCheckboxField(QuerySelectMultipleField):
    widget = widgets.ListWidget(html_tag='ol', prefix_label=False)
    option_widget = widgets.CheckboxInput()

def t1_query():
    return Type1Questions.query

def t2_query():
    return Type2Questions.query
class chooseQuestions2(FlaskForm):
    t1opts = QueryMultipleCheckboxField(query_factory=t1_query)
    t2opts = QueryMultipleCheckboxField(query_factory=t2_query)
