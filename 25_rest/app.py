import urllib
import json

from flask import Flask, render_template

app = Flask(__name__)

KEY = "21fc0ce63e424432a88332975a8a8a08"
base_url = "http://api.football-data.org"
endpoint = "/v2/teams"

@app.route("/", methods=["GET"])
def index():
	req = urllib.request.Request(base_url + endpoint)
	req.add_header("X-Auth-Token", KEY)
	json_resp = json.loads(urllib.request.urlopen(req).read());
	return render_template("teams.html", teams = json_resp['teams'])

if __name__ == "__main__":
	app.debug = True
	app.run()
