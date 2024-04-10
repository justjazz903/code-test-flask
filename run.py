from flask import Flask, request, jsonify
import requests

api_key = "a697471847014605ae2105854241004"
api_base_url = "http://api.weatherapi.com/v1"

app = Flask(__name__)

@app.route("/city_weather_current", methods=["POST"])
def city_weather_current():
  city = "Nanjing"
  url = f"{api_base_url}/current.json?key={api_key}&q={city}"
  response = requests.get(url)
  data = response.json()
  return data

app.run(debug=True)