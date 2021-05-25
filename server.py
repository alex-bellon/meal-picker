from flask import Flask
from flask import render_template, request

import mealpicker

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/pick")
def pick():
    num = int(request.args.get('num'))
    meals = mealpicker.import_meals('meals.json')

    names, ingredients = mealpicker.pick(meals, num)

    return render_template('pick.html', names=names, ingredients=ingredients)
