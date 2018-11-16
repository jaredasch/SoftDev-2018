import urllib
import json

from flask import Flask, render_template

app = Flask(__name__)

darksky_key = "0515a77165ecc9864b1b8ebbe5a45c64"
darksky_url = "https://api.darksky.net/forecast/" + darksky_key + "/40.7179882,-74.0160594"

@app.route("/", methods=["GET"])
def index():
    bored_req = urllib.request.Request("https://www.boredapi.com/api/activity")
    bored_resp = json.loads(urllib.request.urlopen(bored_req).read())

    darksky_req = urllib.request.Request(darksky_url)
    weather = json.loads(urllib.request.urlopen(darksky_req).read())['currently']

    xkcd_req = urllib.request.Request("https://xkcd.com/info.0.json")
    xkcd_resp = json.loads(urllib.request.urlopen(xkcd_req).read())

    return render_template("index.html", bored_data = bored_resp, weather = weather, xkcd = xkcd_resp)

if __name__ == "__main__":
    app.debug = True
    app.run()
