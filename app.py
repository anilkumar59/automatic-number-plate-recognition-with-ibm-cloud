# -*- coding: utf-8 -*-
"""
Created on Fri May 28 08:20:50 2021

@author: anil
"""


#importing the libraries
from flask import Flask,request,render_template
import requests
import re
import numpy as np
app = Flask(__name__)

def check(output):
   url = "https://zyanyatech1-license-plate-recognition-v1.p.rapidapi.com/recognize_url"
   querystring = {"image_url":output,"sourceType" :"url"}
   
   payload = '''{\r\n   \"image_url\": "'''+output+'''",\r\n   \"sourceType\": \"url\"\r\n}'''
   headers ={
           'x-rapidapi-key' : "cccef35aaemsh0038a4af5a6262ap1a5b21jsn9c49b411f2a6",
        'x-rapidapi-host': "zyanyatech1-license-plate-recognition-v1.p.rapidapi.com"
        }
   response = requests.request("POST",url,headers=headers,params=querystring)

   print(response.text)
   return response.json()["results"][0]["plate"],response.json()["results"][0]["confidence"]

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/predict',methods =['POST'])
def predict():
    output=request.form['output']
    plate,conf=check(output)
    return render_template('base.html',output=plate+"with confidence score: "+str(round(conf))+"%")
    
if __name__=="__main__":
    app.run(debug=True)
