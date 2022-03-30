from aat import db
from aat.models import Courses, Assessments, Type1Questions, Type2Questions

db.drop_all()
db.creat_all()

course1 = Course(courseCode = 'CMT120', courseName = 'Fundamentals of Programming')
course2 = Course(courseCode = 'CMT210', courseName = 'Algorithms, Data Structures and Programming')
course2 = Course(courseCode = 'CMT220', courseName = 'Databases and Modelling')

t1q1 = Type1Questions(
    course_id = 'CMT220', 
    content = 'What does SQL stand for?', 
    optA = 'Structured Query Language',
    optB = 'Sequel',
    optC = 'Standard Query Language',
    answer = 'A',
    difficulty = 'Easy',
    used = False )
t1q2 = Type1Questions(
    course_id = 'CMT220', 
    content = '_____ is used to denote a relationship in Chen notation.', 
    optA = 'Square',
    optB = 'Circle',
    optC = 'Diamond',
    optD = 'Hexagon',
    answer = 'C',
    difficulty = 'Easy',
    used = False )
t2q1 = Type2Questions(
    course_id = 'CMT220',
    content = 'The Cartesian product of sets A = {1, 2} and B = {3, 4} is {(1, 3), (1, 4), (2, 3), (2, 4)}', 
    answer = 'C',
    explanation = 'The Cartesian product X×Y between two sets X and Y is the set of all possible ordered pairs with first element from X and second element from Y: X×Y={(x,y):x∈X and y∈Y}.',
    difficulty = 'Easy',
    used = False )

db.session.add(course1)
db.session.add(course2)
db.session.add(course3)
db.session.add(t1q1)
db.session.add(t1q2)
db.session.add(t2q1)

db.session.commit()