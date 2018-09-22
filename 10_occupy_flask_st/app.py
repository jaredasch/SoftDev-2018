from flask import Flask, render_template
app = Flask(__name__)

def readlines():
    f = open('data/occupations.csv', 'r')
    text = f.read().strip().split('\n')
    f.close()
    return text[1:][:-1]

def linesToDict(lines):
    info_dict = {}
    for line in lines:
        if line[0] is '\"':
            end = line[1:].find('\"')
            job = line[1:end]
            info_dict[job] = float(line[end+3:])
        else:
            job = line.split(',')[0]
            info_dict[job] = float(line.split(',')[1])
    return info_dict

def pickOccupation(occupations):
    percents = list(occupations.values())
    occs = list(occupations.keys())
    rand = random() * occupations["Total"]
    percentTot = percents[0];
    index = 0;
    while(percentTot < rand):
        index += 1
        percentTot += percents[index]
    return (occs[index])

@app.route("/occupations")
def occupations():
	jobs_dict = linesToDict(readlines())
	return render_template("occupations.html", jobs=jobs_dict, select=random_occupation(jobs_dict))

if __name__ == "__main__":
	app.debug = True
	app.run()
