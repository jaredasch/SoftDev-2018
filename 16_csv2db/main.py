# Team Dem Boys -- Jared Asch, Ryan Aday
# SoftDev1 pd7
# K16 -- No Trouble
# 2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

DB_FILE = "app.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

def csv_to_db(filename):
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        header = reader.fieldnames
        table_name = filename.split(".")[0].split("/")[-1]

        query = "CREATE TABLE " + table_name + "(" + ",".join([col + " TEXT" for col in header]) + ")"
        c.execute(query)

        for row in reader:
            query = "INSERT INTO " + table_name + " VALUES ("  + ",".join(["\"" + val + "\"" for val in row.values()]) + ")"
            c.execute(query)

csv_to_db("data/courses.csv")
csv_to_db("data/peeps.csv")

#==========================================================

db.commit() #save changes
db.close()  #close database