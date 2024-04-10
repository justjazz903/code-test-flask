from flask import Flask, request
from flask_cors import CORS
import requests

api_key = "a697471847014605ae2105854241004"
api_base_url = "http://api.weatherapi.com/v1"
forecast_url = "forecast.json"

app = Flask(__name__)
CORS(app)


@app.route("/forecast", methods=["POST"])
def forecast():
    try:
        data = request.get_json()
        city = data.get("city")
        url = f"{api_base_url}/{forecast_url}?key={api_key}&q={city}&days=2"
        response = requests.get(url)
        data = response.json()
        if 'error' in data:
            return {"error": data["error"]["message"]}
        return data
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
