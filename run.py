from flask import Flask, request, jsonify
import requests
from datetime import datetime, timedelta

api_key = "a697471847014605ae2105854241004"
api_base_url = "http://api.weatherapi.com/v1"
current_url = "current.json"
forecast_url = "forecast.json"
history_url = "history.json"

app = Flask(__name__)

@app.route("/current", methods=["GET"])
def current():
    city = "Nanjing"
    url = f"{api_base_url}/{current_url}?key={api_key}&q={city}"
    response = requests.get(url)
    data = response.json()
    return data


@app.route("/forecast", methods=["GET"])
def forecast():
    city = "Nanjing"
    url = f"{api_base_url}/{forecast_url}?key={api_key}&q={city}&days=3"
    response = requests.get(url)
    data = response.json()
    return data


@app.route("/history", methods=["GET"])
def history():
    city = "Nanjing"
    # dt should be 3 days ago
    dt = datetime.now() - timedelta(days=3)
    dt = dt.strftime("%Y-%m-%d")
    url = f"{api_base_url}/{history_url}?key={api_key}&q={city}&dt={dt}"
    response = requests.get(url)
    data = response.json()
    return data


app.run(debug=True)
