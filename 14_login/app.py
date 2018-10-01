from flask import Flask, request, render_template, session, redirect, url_for
from os import urandom

app = Flask(__name__)
app.secret_key = urandom(32)

users = {"jaredasch":"passy"}

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
            return render_template("login.html", error = "User does not exist!")
        elif users[request.form.get("username")] != request.form.get("password"):
            return render_template("login.html", error = "Password is incorrect")
        elif users[request.form.get("username")] == request.form.get("password"):
            session["username"] = request.form.get("username")
            return redirect(url_for("index"))
        else:
            return render_template("login.html", error = "Uh we screwed up")

@app.route('/logout')
def logout():
    session.pop("username")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.debug = True
    app.run()
        
