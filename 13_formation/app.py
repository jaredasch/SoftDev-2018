from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("form.html")

@app.route("/greet", methods=["GET", "POST"])
def greet():
	if request.method == "GET":
		username = request.args["username"]
	else:
		username = request.form["username"]
	return render_template("greet.html", username = username, method = request.method)

if __name__ == "__main__":
	app.debug = True;
	app.run()
