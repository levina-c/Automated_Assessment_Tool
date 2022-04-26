from flask_wtf import FlaskForm
from flask_datepicker import datepicker
from wtforms import RadioField, SelectField, SubmitField, StringField, IntegerField, TimeField, RadioField, SelectMultipleField, widgets, SearchField, BooleanField
from wtforms.validators import InputRequired, ValidationError, DataRequired
from wtforms.widgets import TextArea
from datetime import datetime
from wtforms.fields import DateField
from flask_sqlalchemy import SQLAlchemy
from wtforms_sqlalchemy.fields import QuerySelectMultipleField
from aat.models import Type1Questions, Type2Questions
from sqlalchemy.sql.expression import and_

class AssessmentForm(FlaskForm):
    course = SelectField('Course', validators=[InputRequired(message = 'Please select a course')], choices=[
        ('','Select Course'),
        ('CMT120','CMT120 Fundamentals of Programming'),
        ('CMT219','CMT219 Algorithms, Data Structures and Programming'),
        ('CMT220','CMT220 Databases and Modelling')])
    assessmenttitle = StringField('Assessment Title', validators=[InputRequired(message = 'Please enter a title')])
    assessmenttype = SelectField('Assessment Type', validators=[InputRequired(message = 'Please select a type')], choices=[('', 'Select Type'),('Class quiz','Class quiz'), ('Test','Test'),('Exam','Exam')])
    duedate = DateField('Due Date', format='%Y-%m-%d', default=datetime.now().date())
    duedatetime = TimeField('Time', format='%H:%M', validators=[InputRequired()], default=datetime.now())
    timelimit = IntegerField('Time Limit', default='60')
    totalmark = IntegerField('Total Mark', default='100')
    retake = BooleanField('Student Retake')
    savenexit = SubmitField('Save and Exit')
    nextpage = SubmitField('Next')
    update = SubmitField('Save')

    def validate_totalmark(self, totalmark):
        if totalmark.data<=0:
            raise ValidationError('Marks must be a positive integer greater than 0')

class MultipleCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(html_tag='ol', prefix_label=False)
    option_widget = widgets.CheckboxInput()

class chooseQuestions(FlaskForm):
    t1opts = MultipleCheckboxField(label='Questions', choices=[])
    t2opts = MultipleCheckboxField(label='Questions', choices=[])
    submit = SubmitField('Add')

class deleteQuestions(FlaskForm):
    t1opts = MultipleCheckboxField(label='AQuestions', choices=[])
    t2opts = MultipleCheckboxField(label='AQuestions', choices=[])
    deleteq = SubmitField('Delete')

class filterquestionform(FlaskForm):
    qType = SelectField('Question Type', validators=[InputRequired()], choices=[('All', 'All'),('Type1', 'Multiple Choice'), ('Type2', 'True/False')])
    used = SelectField('Used', validators=[InputRequired()], choices=[('All', 'All'),('Used', 'Used'), ('Unused', 'Unused')])
    difficulty = SelectField('Difficulty', validators=[InputRequired()], choices=[('All', 'All'),('Easy', 'Easy'), ('Medium', 'Medium'), ('Difficult', 'Difficult')])
    searchbar = SearchField(label='Enter Keyword')
    filterq = SubmitField('Filter')

class sortAssessment(FlaskForm):
    sorttype = SelectField('Sort By', choices=[('Course','Course'), ('Status','Status')])
    sort = SubmitField('Sort')

class McqForm(FlaskForm):
    title = StringField('Question title (Title)', validators=[InputRequired()])
    assessment_id = StringField('Assessment ID')
    coursecode = StringField('Coursecode')
    optionA = StringField('Option A')
    optionB = StringField('Option B')
    optionC = StringField('Option C')
    optionD = StringField('Option D')
    correct_answer = StringField('Correct answer', validators=[InputRequired()])
    tags = StringField('Tags')
    explanation = StringField('Explanation', validators=[InputRequired()])
    difficulty = IntegerField('Difficulty', validators=[InputRequired()])
    point = IntegerField('Points', validators=[InputRequired()])
    utilised = BooleanField('Utilised')
    submit = SubmitField('Submit')

class Question2Form(FlaskForm):
    # questiontype = SelectField('Question Type', validators=[DataRequired()], 
    #                             choices=[('','Select Question Type'), 
    #                                      ('Multiple Choice','Multiple Choice'),
    #                                      ('True/False','True/False')]
    #                           )

    course = SelectField('Course', validators=[DataRequired()], 
                          choices=[('','Select Course'),
                                   ('CMT120','CMT120 Fundamentals of Programming'),
                                   ('CMT219','CMT219 Algorithms, Data Structures and Programming'),
                                   ('CMT220','CMT220 Databases and Modelling')]
                        )
    # chapter = StringField('Chapter', validators=[InputRequired()])    
    difficulty = SelectField('Difficulty Level', validators=[DataRequired()], 
                              choices=[('','Select Difficulty Level'),('Easy','Easy'),('Medium', 'Medium'), ('Difficult', 'Difficult')])
    tags = StringField('Question Tags', validators=[DataRequired()])
    point = IntegerField('Point', default='2')
    title = StringField('Question Title', validators=[DataRequired()], widget=TextArea())
    correct_answer = RadioField('Question Answer', validators=[DataRequired()], choices=[('True','True'),('False','False')])
    explanation = StringField('Explanation', validators=[DataRequired()], widget=TextArea())
    # savequestion = SubmitField('Save')
    # addquestion = SubmitField('Add Question')

    def validate_course(self,course):
        if course is None:
            raise ValidationError('Please select a course')

    def validate_difficulty(self,difficulty):
        if difficulty is None:
            raise ValidationError('Please select a level')

    def validate_correct_answer(self,correct_answer):
        if correct_answer is None:
            raise ValidationError('Please select an answer')
