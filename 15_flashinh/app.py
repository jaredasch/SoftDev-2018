# Team C Ya Later -- Jared Asch, William Lu
# SoftDev pd7
# K15 -- Oh yes, perhaps I do...
# 2018-10-02

from flask import Flask, request, render_template, session, redirect, url_for, flash
from os import urandom

app = Flask(__name__)
app.secret_key = urandom(32)

users = {"jaredasch":"pass"}

@app.route("/")
def index():
	if "username" not in session.keys():
		return redirect(url_for("login"))
	return render_template("index.html", username=session["username"])

@app.route("/login", methods=["POST", "GET"])
def login():
	if request.method == "GET":
		return render_template("login.html");
	else:
		if request.form.get("username") not in users.keys():
			flash("User does not exist!")
			return render_template("login.html")
		elif users[request.form.get("username")] != request.form.get("password"):
			flash("Password is incorrect!")
			return render_template("login.html")
		elif users[request.form.get("username")] == request.form.get("password"):
			session["username"] = request.form.get("username")
			return redirect(url_for("index"))
		else:
			flash("Uh we screwed up, come back later")
			return render_template("login.html")

@app.route('/logout')
def logout():
	session.pop("username")
	return redirect(url_for("index"))

if __name__ == "__main__":
	app.debug = True
	app.run()
