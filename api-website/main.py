# Get API Key : https://openweathermap.org/api
from flask import Flask, render_template, request
import requests
import json
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        api_key = '3b20675c2ec00a16754d2ada9b3e7650'
        city = ''
        country = ''
        url = 'http://api.openweathermap.org/data/2.5/weather?appid={}&q={}'.format(api_key, city, country)
        response = requests.get(url)
        data = response.json()

        temp = round(data["main"]["temp"])
        temperature = temp - 273
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]

        return render_template("result.html", temperature=temperature, humidity=humidity, pressure=pressure, city=city)

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)