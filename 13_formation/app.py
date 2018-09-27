from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("form.html")

@app.route("/greet")
def greet():
	return render_template("greet.html", username = request.args["username"], method = request.method)

if __name__ == "__main__":
	app.debug = True;
	app.run()
