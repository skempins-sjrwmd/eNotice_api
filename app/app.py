import flask
import enotice_data

app = flask.Flask(__name__)

@app.route("/")
def home():
	return "eNotices"

@app.route("/api/current")
def api_current():
	return flask.jsonify(enotice_data.db)
