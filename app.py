from flask import Flask, render_template
import requests

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def index():
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=882360f00976cbb441f3ca5038c5c5d7"
    city = 'Vegas'

    r = requests.get(url.format(city)).json()#request to api


    weather = {
        'city' : 'Nairobi',
        'temparature': r['main']['temp'],
        'description' : r['weather'][0]['description'],
        'icon' : r['weather'][0]['icon']
    }

    print(weather)
    return render_template("weather.html", weather=weather)#pass weather to template

if __name__ == '__main__':
    app.run(debug=True)#start server
