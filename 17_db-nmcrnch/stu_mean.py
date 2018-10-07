# Team C Ya Later -- Jared Asch, William Lu
# SoftDev1 pd7
# K17 -- Average, ... or Basic?
# 2018-10-09 T

import sqlite3   #enable control of an sqlite database

DB_FILE="app.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

c.execute('CREATE TABLE peeps_avg (id INTEGER, avg REAL)')

# Data returned from DB in format (name, age, id, course_name, grade, id)

data = c.execute("SELECT * FROM peeps, courses WHERE peeps.id = courses.id;")

grade_dict = {}

# Stores data as {id: (name, [grades])}

for row in data:
    if row[2] in grade_dict.keys():
        grade_dict[row[2]][1].append(row[4])
    else:
        grade_dict[row[2]] = (row[0], [row[4]])

print('name, id, average')

for student_id in grade_dict:
    grades = grade_dict[student_id][1]
    avg = float(sum(grades)/len(grades))
    print("%s, %s, %s" % (grade_dict[student_id][0], student_id, avg))
    c.execute('INSERT INTO peeps_avg VALUES (%s , %s);' % (student_id, str(avg)))

def add_course(name, grade, student_id):
    c.execute('INSERT INTO courses VALUES (\"%s\", %s, %s);' % (name, grade, student_id))

db.commit() #save changes
db.close()  #close database
