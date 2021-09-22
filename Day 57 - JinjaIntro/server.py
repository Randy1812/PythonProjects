from flask import Flask, render_template
import random
import datetime
import requests
from pprint import pprint

app = Flask(__name__)


@app.route('/')
def home():
    rnum = random.randint(1, 10)
    return render_template('index.html', rnum=rnum, year=datetime.datetime.now().year)


@app.route('/guess/<string:name>')
def guess(name):
    data = requests.get(f'https://api.genderize.io/?name={name}')
    gender = data.json()['gender']
    data = requests.get(f'https://api.agify.io/?name={name}')
    age = data.json()['age']
    data = requests.get(f'https://api.nationalize.io/?name={name}')
    country = data.json()['country'][0]['country_id']
    return render_template("guess.html", person_name=name, gender=gender, age=age, country=country)


@app.route('/blog')
def blog():
    data = requests.get('https://api.npoint.io/aa0d7f55d87e901a7469')
    all_posts = data.json()
    return render_template("blog.html", allPosts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
