from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd
from random import *

app = Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/insurance')
def insurance():
    return render_template('insurance.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    int_features=[float(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model.predict(final)
    output = int(prediction)
    result_string = "The predicted Insurance cost is around: " + str(output)

    return render_template('insurance.html', pred=result_string)


if __name__ == '__main__':
    app.run(debug=True)