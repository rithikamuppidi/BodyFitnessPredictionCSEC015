# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 18:59:34 2020

@author: suchi
"""

from flask import Flask,render_template,request
app=Flask(__name__) #interface between server and application

import pickle
model=pickle.load(open("BodyFitnessPredictionModel.pkl","rb"))
scaler=pickle.load(open("BodyFitnessPredictionScaler.pkl","rb"))

@app.route('/') #bound to an URL
def helloworld():
    return render_template("project.html")

@app.route('/predict',methods=['POST']) #bound to an URL
def loginfunc():
    stroutput=""
    w=request.form["w"]
    sc=request.form["sc"]
    s=request.form["s"]
    c=request.form["c"]
    m=request.form["m"]
    if m=="b":
        s1,s2,s3=1,0,0
    if m=="n":
        s1,s2,s3=0,1,0
    if m=="g":
        s1,s2,s3=0,0,1
    t=[[s1,s2,s3,int(sc),int(c),int(s),int(w)]]
    y=model.predict(scaler.transform(t))
    if(y==0):
        Stroutput="You are fit,try to keep it up!"
    else:
        Stroutput="You are unfit,let's try to improve it!"
    
    return render_template("project.html",a=Stroutput)

@app.route('/user')
def user():
    return "Hi user"

if __name__=='__main__':
    app.run(debug=True) #gives an URL