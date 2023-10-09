
from flask import Flask, redirect, request, render_template
import pickle
import numpy as np

app=Flask(__name__)

@app.route("/")
def fun1():
    return render_template("info.html")

@app.route("/predict", methods = ["post"])
def fun2():
    nm = request.form['name']
    age = int(request.form['age'])
    gender = request.form['gender']
    bmi = int(request.form['bmi'])
    num_child = int(request.form['num_child'])
    smoker = request.form['smoker']
      # Preprocessing
    gender = 0 if gender.lower()=='male' else 1
    smoker = 0 if smoker.lower()=='n' else 1

    q = [[age,gender,bmi,num_child,smoker]]

    mymodel = pickle.load(open('model1.pkl', "rb"))
    premium = round(mymodel.predict(q)[0],2)
    #return "<h1> hi {} <br/> your predicted Premium Amount is {} </h1>".format(nm,premium)
    #return f"<h1> hi {nm} <br/> your predicted Premium Amount is {premium} </h1>"
     #return f"<h1> hi "+nm+"<br/> your predicted Premium Amount is "+premium+"</h1>"
    return render_template("second.html", name = nm , premium = premium )

    
if __name__ == "__main__" :
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=8080)

