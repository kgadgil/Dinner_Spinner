from flask import Flask, render_template, jsonify, flash
import json
import pandas as pd
import random

app = Flask(__name__)
app.secret_key = 'super secret key'

def read_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/breakfast")
def breakfast():
    data = read_json("data/breakfast.csv")
    choice = random.choice(list(data.keys()))
    flash(f"You should have {choice} for breakfast")
    return render_template("breakfast.html", data=data)

@app.route("/dinner")
def dinner():
    data = read_json("data/dinner.csv")
    choice = random.choice(list(data.keys()))
    flash(f"You should have {choice} for dinner")
    return render_template("dinner.html", data=data)

if __name__ == "__main__":
    app.debug = True
    app.run()