# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 05:15:29 2021

@author: LEGION
"""

from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
import math
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
#model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    Fuel_Type_Diesel=0
    if request.method == 'POST':
        Age=int(request.form['Age'])
        CRP=float(request.form['CRP'])
        Lymphocyte=float(request.form['Lymphocyte'])
        Neutrophils=float(request.form['Neutrophils'])
        LDH=float(request.form['LDH'])
        
        output= -3.662636+.0735038*Age+.0110451*CRP-.1624422*Lymphocyte-.0327053*Neutrophils+.0070514*LDH
        dp=1/(1+math.exp(-output))
        
        if dp<=0.05:
            return render_template('index.html',prediction_texts="Mortality risk is low")
        elif dp <=0.5 and dp >0.05:
            return render_template('index.html',prediction_text="Mortality risk is moderate")
        elif dp >0.5:
            return render_template('index.html',prediction_text="Mortality risk is high")
        
        
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

