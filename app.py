from flask import Flask, request, render_template
import pandas
import numpy as np
import pickle

with open("model.pkl", "rb") as f:
    model= pickle.load(f)

#flask app
app= Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route("/predict", methods = ['POST'])
def predict():
    pass

# python main
if __name__ == "__main__":
    app.run(debug=True)