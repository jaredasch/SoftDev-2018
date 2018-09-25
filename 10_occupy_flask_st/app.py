# Team Peglegs -- Jared Asch, Vincent Lin
# SoftDev pd7
# K10 -- Jinja Tuning
# 2018-09-24

from flask import Flask, render_template
import csv 
from random import random   # importing all necessary functions

app = Flask(__name__)

def parse_jobs_csv():
    jobs_dict = {}    # creates dictionary of jobs and percentages
    header = [] # the first line of the csv file and the table heading
    reader = csv.reader(open('data/occupations.csv', 'r'))
    r = 0
    for row in reader:  # reads every line except the first(header) in the csv file and adds the job/percentage to the dict
        if r != 0:
           jobs_dict[row[0]] = float(row[1])
        else:
            header = row    # adds the header to the header list
        r += 1
    return header, jobs_dict

def rand_job(occupations):
    percents = list(occupations.values())
    occs = list(occupations.keys())
    rand = random() * 99.8
    percentTot = percents[0];
    index = 0;
    while(percentTot < rand):
        index += 1
        percentTot += percents[index]
    return (occs[index])   # choose a random job from list

header, jobs = parse_jobs_csv()

@app.route("/")
def home(): # creates an unnecessary home page with a link to assignment
    return "<a href = occupations>Click here for occupations</a>"

@app.route("/occupations") 
def occupations(): # uses template to create the table
    return render_template('occupations.html', random = rand_job(jobs), jobs = jobs, header = header)

if __name__ == "__main__": 
    app.debug = True    # Set False for production
    app.run()
