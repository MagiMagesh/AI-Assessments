from flask import Flask, render_template, request
import requests
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)

pickl = open('model.pkl', 'rb')
classin = pickle.load(pickl)


@app.route('/')
def Welcome():
    return "Welcome to Magesh Prediction AI Team"


@app.route('/predict', methods=['GET'])
def Prediction():
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


@app.route('/predict_file', methods=["POST"])
def predict_test_file():
    test = pd.read_csv(request.files.get('file'))
    prediction = classin.predict(test)
    a = (prediction)
    for i in a:
        if i==0:
            i = 'jazz and blues'
            print(i)
        if i==1:
            i = 'dance and electronica'
            print(i)
        if i==2:
            i = 'pop'
            print(i)
        if i==3:
            i = 'punk'
            print(i)
        if i==4:
            i = 'soul and reggae'
            print(i)
        if i==5:
            i = 'metal'
            print(i)
        if i==6:
            i = 'folk'
            print(i)
        if i==7:
            i = 'classic pop and rock'
            print(i)
    return f'''Welcome to Magesh Prediction AI Team
    The Test File has len of {str(len(a))}
    'jazz and blues': 0,
 'dance and electronica': 1,
 'pop': 2,
 'punk': 3,
 'soul and reggae': 4,
 'metal': 5,
 'folk': 6,
 'classic pop and rock': 7

 The Output is :
{str(a)} and The total number of values are {str(len(a))}'''


if __name__ == '__main__':
    app.run()

# predict?loudness=-8.539&tempo=104.31&time_signature=3&key=7&mode=1&duration=298.735&vect_1=44.462