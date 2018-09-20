# Jared Asch
# SoftDev1 pd7
# K08 -- Fill Yer Flask
# 2018-09-20

from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def english():
    return "Hello world!<br><a href = '" + url_for('spanish') + "'>Spanish</a><br><a href = '" + url_for('french') + "'>French</a>"

@app.route("/spanish")
def spanish():
    return "Hola mundo!<br><a href = '" + url_for('english') + "'>English</a><br><a href = '" + url_for('french') + "'>French</a>"

@app.route("/french")
def french():
    return "Bonjour le monde!<br><a href = '" + url_for('english') + "'>English</a><br><a href = '" + url_for('spanish') + "'>Spanish</a>"


if __name__ == "__main__":
    app.debug = True # Remove in production
    app.run()
