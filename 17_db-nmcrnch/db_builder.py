# Team C Ya Later -- Jared Asch, William Lu
# SoftDev1 pd7
# K17 -- Average, ... or Basic?
# 2018-10-09

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

def csvToDB(fileName, types):
    DB_FILE="app.db"

    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops

    #==========================================================
    #INSERT YOUR POPULATE CODE IN THIS ZONE

    file = open("data/" + fileName, "rU")
    reader = csv.DictReader(file)
    #for row in reader:
    #    print(row['code'], row['mark'], row['id'])

    tableName = fileName[: fileName.find('.')]

    command = 'CREATE TABLE ' + tableName + ' ('
    for key in types:
        # print(col)
        command += key + ' ' + types[key] + ', '#build SQL stmt, save as string

    command = command[: command.rfind(',')]
    command += ');'

    #print(command)

    c.execute(command)    #run SQL statement

    for row in reader:
        # print(row)
        command = 'INSERT INTO ' + tableName + ' VALUES ('

        for key in row:
            # print(key)
            if types[key] == 'TEXT':
                command += '"' + row[key] + '", '
            else:
                command += row[key] + ', '
        command = command[: command.rfind(',')]
        command += ');'
        #print(command)
        c.execute(command)

    db.commit() #save changes

    db.close()  #close database

csvToDB("courses.csv", {'code':'TEXT', 'mark':'INTEGER', 'id':'INTEGER'})
csvToDB("occupations.csv", {'Job Class':'TEXT', 'Percentage':'REAL'})
csvToDB("peeps.csv", {'name':'TEXT', 'age':'INTEGER', 'id':'INTEGER'})
