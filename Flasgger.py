## Can be used for Front End

from flask import Flask, request
import pandas as pd
import numpy as np
import pickle
import flasgger
from flasgger import Swagger
app = Flask(__name__)
Swagger(app)


pickle_in = open('model.pkl','rb')
classifier = pickle.load(pickle_in)

@app.route('/')
def Welcome():
    return "Welcome to the  Magesh's Prediction"

@app.route('/predict')
def predict_():
    """Let's predict Using Values
    This is using docstrings for specifications.
    ---
    parameters:
      - name: vect_30
        in: query
        type: number
        required: true
      - name: vect_1
        in: query
        type: number
        required: true
      - name: vect_25
        in: query
        type: number
        required: true
      - name: vect_2
        in: query
        type: number
        required: true
      - name: duration
        in: query
        type: number
        required: true
      - name: vect_5
        in: query
        type: number
        required: true
      - name: vect_6
        in: query
        type: number
        required: true
      - name: vect_10
        in: query
        type: number
        required: true
      - name: vect_27
        in: query
        type: number
        required: true
      - name: vect_123
        in: query
        type: number
        required: true
      - name: vect_19
        in: query
        type: number
        required: true
      - name: vect_61
        in: query
        type: number
        required: true
      - name: vect_29
        in: query
        type: number
        required: true
      - name: vect_16
        in: query
        type: number
        required: true
      - name: vect_24
        in: query
        type: number
        required: true


    responses:
        200:
            description: The output values
    """
    vect_30 = request.args.get('vect_30')
    vect_1 = request.args.get('vect_1')
    vect_25 = request.args.get('vect_25')
    vect_2 = request.args.get('vect_2')
    duration = request.args.get('duration')
    vect_5 = request.args.get('vect_5')

    vect_6 = request.args.get('vect_6')
    vect_10 = request.args.get('vect_10')
    vect_27 = request.args.get('vect_27')
    vect_123 = request.args.get('vect_123')
    vect_19 = request.args.get('vect_19')
    vect_61 = request.args.get('vect_61')

    vect_29 = request.args.get('vect_29')
    vect_16 = request.args.get('vect_16')
    vect_24 = request.args.get('vect_24')

    prediction = classin.predict([[vect_30, vect_1, vect_25, vect_2, duration, vect_5, vect_6, vect_10, vect_27,
                                   vect_123, vect_19, vect_61, vect_29, vect_16, vect_24]])

    return str(prediction)


@app.route('/predict_file',methods = ["POST"])
def predict_test_file():
    """Let's Predict using Files
    This is using docstrings for specifications.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
    responses:
        200:
            description: The output values
    """

    test = pd.read_csv(request.files.get('file'))
    prediction = classifier.predict(test)
    return 'The prediction for the test FIle is' + str(list(prediction))



if __name__=='__main__':
    app.run()