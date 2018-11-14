from flask import Flask, render_template
import urllib
import json

app = Flask(__name__)

KEY = "5V0KrwEagZa6ycjkWnf3gbeD0AgYHahYANKPHMzB"
api_url = "https://api.nasa.gov/planetary/apod?api_key=" + KEY

@app.route("/", methods=["GET"])
def index():
	req = urllib.request.urlopen(api_url)
	data = json.loads(req.read())
	return render_template("index.html", data=data)

if __name__ == "__main__":
	app.debug = True
	app.run()
