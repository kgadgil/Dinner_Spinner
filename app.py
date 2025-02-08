from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/breakfast")
def breakfast():
    breakie = pd.read_csv("data/breakfast.csv")
    return breakie.to_dict()

@app.route("/dinner")
def dinner():
    dine = pd.read_csv("data/dinner.csv")
    return dine.to_dict()
