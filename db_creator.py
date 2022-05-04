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
    totalmark = 20,
    retake = False,
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
    point = 10,
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
    point = 10,
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
    point = 10,
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
    point = 10,
    utilised = True )
t1q5 = Type1Questions(
    course_code = 'CMT220', 
    title = 'The top level of the hierarchy consists of ______ each of which can contain _____.', 
    optionA = 'Schemas, Catalogs',
    optionB = 'Schemas, Environment',
    optionC = 'Environment, Schemas',
    optionD = 'Catalogs, Schemas',
    correct_answer = 'D',
    tags = 'hierarchy',
    difficulty = 'Medium',
    point = 10,
    utilised = False )
t1q6 = Type1Questions(
    course_code = 'CMT220', 
    title = 'The user IDs can be added or removed using which of the following fixed roles?', 
    optionA = 'db_sysadmin',
    optionB = 'db_accessadmin',
    optionC = 'db_securityadmin',
    optionD = 'db_setupadmin',
    correct_answer = 'B',
    tags = 'fixed roles',
    difficulty = 'Medium',
    point = 10,
    utilised = False )
t1q7 = Type1Questions(
    course_code = 'CMT220', 
    title = 'After groups have been established, SQL applies predicates in the ___________ clause, allowing aggregate functions to be used.', 
    optionA = 'Where',
    optionB = 'Having',
    optionC = 'Group by',
    optionD = 'With',
    correct_answer = 'D',
    tags = 'aggregate',
    difficulty = 'Difficult',
    point = 10,
    utilised = False )
t2q1 = Type2Questions(
    course_code = 'CMT220',
    title = 'The Cartesian product of sets A = {1, 2} and B = {3, 4} is {(1, 3), (1, 4), (2, 3), (2, 4)}', 
    correct_answer = 'True',
    tags = 'cartesian',
    explanation = 'The Cartesian product X×Y between two sets X and Y is the set of all possible ordered pairs with first element from X and second element from Y: X×Y={(x,y):x∈X and y∈Y}.',
    difficulty = 'Easy',
    point = 10,
    utilised = False )
t2q2 = Type2Questions(
    course_code = 'CMT220',
    title = 'Database Management System is the full form of DBMS.', 
    correct_answer = 'True',
    tags = 'DBMS',
    explanation = 'DBMS is abbreviated as Database Management System. Database Management System stores the data and allows authorized users to manipulate and modify the data.',
    difficulty = 'Easy',
    point = 10,
    utilised = False )
t2q3 = Type2Questions(
    course_code = 'CMT220',
    title = 'High-resolution video display is a hardware component that is most important for the operation of a database management system.', 
    correct_answer = 'False',
    tags = 'operation',
    explanation = 'Since all the data are stored in form of memory in the disk, a high speed, and large-capacity disk is required for the operation of the database management system.',
    difficulty = 'Easy',
    point = 10,
    utilised = False )
t2q4 = Type2Questions(
    course_code = 'CMT220',
    title = 'Purge is used to remove a relation from an SQL.', 
    correct_answer = 'False',
    tags = 'drop table',
    explanation = 'Delete command is used to delete the existing record from the table. The drop table deletes the whole structure of the relation. Purge removes the table which cannot be obtained again.',
    difficulty = 'Medium',
    point = 10,
    utilised = False )
t2q5 = Type2Questions(
    course_code = 'CMT220',
    title = '4NF has a relation that contains information about a single entity.', 
    correct_answer = 'True',
    tags = 'NF',
    explanation = 'If and only if, for each of its non-trivial multivalued dependencies X \twoheadrightarrow Y, a table is in 4NF. X is a superkey—that is, X is either a candidate key or a superset thereof.',
    difficulty = 'Medium',
    point = 10,
    utilised = False )
t2q6 = Type2Questions(
    course_code = 'CMT219',
    title = 'In an instance method or a constructor, "this" is a reference to the current object.', 
    correct_answer = 'True',
    tags = 'this',
    difficulty = 'Easy',
    point = 10,
    utilised = False )
t2q7 = Type2Questions(
    course_code = 'CMT219',
    title = 'Constructor overloading is not possible in Java.', 
    correct_answer = 'False',
    tags = 'overloading',
    difficulty = 'Easy',
    point = 10,
    utilised = False )
t2q8 = Type2Questions(
    course_code = 'CMT219',
    title = 'Assignment operator is evaluated Left to Right.', 
    correct_answer = 'False',
    tags = 'operator',
    difficulty = 'Easy',
    point = 10,
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
db.session.add(t1q5)
db.session.add(t1q6)
db.session.add(t1q7)
db.session.add(t2q1)
db.session.add(t2q2)
db.session.add(t2q3)
db.session.add(t2q4)
db.session.add(t2q5)
db.session.add(t2q6)
db.session.add(t2q7)
db.session.add(t2q8)
db.session.add(comment1)

db.session.commit()