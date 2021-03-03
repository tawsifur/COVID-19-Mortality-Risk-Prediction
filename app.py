# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 00:54:16 2021

@author: LEGION
"""

  
# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np
import math



app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        Age=int(request.form['Age'])
        CRP=float(request.form['CRP'])
        Lymphocyte=float(request.form['Lymphocyte'])
        Neutrophils=float(request.form['Neutrophils'])
        LDH=float(request.form['LDH'])
        
        output= -3.662636+.0735038*Age+.0110451*CRP-.1624422*Lymphocyte-.0327053*Neutrophils+.0070514*LDH
        dp=1/(1+math.exp(-output))
        
        return render_template('result.html', prediction=dp)

if __name__ == '__main__':
	app.run(debug=True)