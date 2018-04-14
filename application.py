from flask import Flask, session, request, redirect, url_for

from flask import render_template
from workwithbd import bd
import sqlite3
app = Flask(__name__)
# -*- coding: utf-8 -*-
import sqlite3
database=bd('dat.sqlite')

@app.route("/",methods=['GET','POST'])
def hello():
    if(request.method=='GET'):
      #database.delete("users")
      #database.create("users")
      #database.add_user("psdaoqsdfodoq","фыылщащзайщзйа","stas","psoao")
      #database.prin_database()
      return render_template("Enter.html")





@app.route("/lk",methods=['POST'])
def func1():
    input1=request.form['text']
    return render_template("result.html",input1=input1)
@app.route("/registration",methods=['GET','POST'])
def func():
    if(request.method=='GET'):

     return render_template("Registration.html")
    else:
        login = request.form['login']
        password = request.form['password']
        name = request.form['name']
        family = request.form['family']
        Access = database.add_user(login,password,name,family)

        if (Access == True):
            database.prin_database()
            return render_template("Enter.html",Access="Вы успешно зарегестрированы")

        else:
            return render_template("Registration.html",wrong="Такие данные уже существуют или вы ввели неудовлетворяющие условиям логин или пароль")

@app.route("/",methods=['GET','POST'])
def echo():
    return ""


if __name__ == "__main__":
    app.run()