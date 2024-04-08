from flask import Flask, render_template
from datetime import datetime
import requests

API_URL = "https://api.openbrewerydb.org/v1/breweries"
MAX_RES_PER_PAGE = 2000
app = Flask(__name__)

# OK
@app.route("/")
def index():
	year = datetime.now().year
	return render_template("index.html", year = year)

#FUNZIONANTE
@app.route("/random")
def random():
	''' Returns (by default) a random brewery '''
	year = datetime.now().year
	response = requests.get(url = f"{API_URL}/random")
	response.raise_for_status()
	data = response.json()
	#aggiungere un ritorno sensato
	return render_template("results.html", data = data, year = year)
	#return f"<p>{data}</p>"

# FUNZIONANTE
@app.route("/all")
def all():
	year = datetime.now().year
	parameters = {
		"per_page": MAX_RES_PER_PAGE
	}
	response = requests.get(url = f"{API_URL}", params = parameters)
	response.raise_for_status()
	data = response.json()
	return render_template("all.html", data = data, year = year)

if __name__ == "__main__":
	app.run(debug = True)
