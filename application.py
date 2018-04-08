from flask import Flask, request
from flask import render_template
from workwithbd import bd
import sqlite3
app = Flask(__name__)
# -*- coding: utf-8 -*-
import sqlite3
database=bd('dat.sqlite')

@app.route("/",methods=['GET'])
def hello():
   return render_template("Registration.html")


@app.route("/lk",methods=['POST'])
def func1():
    input1=request.form['text']
    input2=request.form['text1']
    database.add_user(input1,input2)
    database.prin_database()
    return render_template("result.html",input1=input1)
@app.route("/",methods=['GET','POST'])
def echo():
    return ""


if __name__ == "__main__":
    app.run()