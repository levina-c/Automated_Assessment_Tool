from aat import db
from aat.models import Courses, Assessments, Type1Questions, Type2Questions, Comments
import datetime

db.drop_all()
db.create_all()

course1 = Courses(courseCode = 'CMT120', courseName = 'Fundamentals of Programming')
course2 = Courses(courseCode = 'CMT219', courseName = 'Algorithms, Data Structures and Programming')
course3 = Courses(courseCode = 'CMT220', courseName = 'Databases and Modelling')

assessment1 = Assessments(
    course_code = "CMT219",
    assessmenttitle = "Assessment 1",
    assessmenttype = "Test",
    duedate = '01/05/2022',
    duedatetime = '09:30',
    totalmark = 100,
    status = 'Published'
    )

t1q1 = Type1Questions(
    course_code = 'CMT220', 
    title = 'What does SQL stand for?', 
    optionA = 'Structured Query Language',
    optionB = 'Sequel',
    optionC = 'Standard Query Language',
    correct_answer = 'A',
    tags = 'SQL',
    difficulty = 'Easy',
    utilised = False )
t1q2 = Type1Questions(
    course_code = 'CMT220', 
    title = '_____ is used to denote a relationship in Chen notation.', 
    optionA = 'Square',
    optionB = 'Circle',
    optionC = 'Diamond',
    optionD = 'Hexagon',
    correct_answer = 'C',
    tags = 'notation',
    difficulty = 'Medium',
    utilised = False )
t1q3 = Type1Questions(
    course_code = 'CMT219', 
    assessment_id = 1,
    title = 'What is the value returned by function compareTo() if the invoking String is less than the String compared?', 
    optionA = 'zero',
    optionB = 'value less than zero',
    optionC = 'value greater than zero',
    optionD = 'None of the mentioned',
    correct_answer = 'B',
    tags = 'compareto',
    difficulty = 'Difficult',
    utilised = True )
t1q4 = Type1Questions(
    course_code = 'CMT219',
    assessment_id = 1,
    title = 'What are valid statements for suspend() and resume() methods of the Thread class?', 
    optionA = 'Suspend() method is deadlock prone.',
    optionB = 'If the target thread holds a lock on object when it is suspended, no thread can lock this object until the target thread is resumed.',
    optionC = 'If the thread that would resume the target thread attempts to lock this monitor prior to calling resume, it results in deadlock formation.',
    optionD = 'All',
    correct_answer = 'D',
    tags = 'thread',
    difficulty = 'Medium',
    utilised = True )
t2q1 = Type2Questions(
    course_code = 'CMT220',
    title = 'The Cartesian product of sets A = {1, 2} and B = {3, 4} is {(1, 3), (1, 4), (2, 3), (2, 4)}', 
    correct_answer = 'True',
    tags = 'cartesian',
    explanation = 'The Cartesian product X×Y between two sets X and Y is the set of all possible ordered pairs with first element from X and second element from Y: X×Y={(x,y):x∈X and y∈Y}.',
    difficulty = 'Easy',
    utilised = False )

comment1 = Comments(
    assessment_id = 1,
    content = 'Good',
    rating = 7
)

db.session.add(course1)
db.session.add(course2)
db.session.add(course3)
db.session.add(assessment1)
db.session.add(t1q1)
db.session.add(t1q2)
db.session.add(t1q3)
db.session.add(t1q4)
db.session.add(t2q1)
db.session.add(comment1)

db.session.commit()