# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
app = Flask(__name__)

# -*- coding: utf-8 -*-
from flask import render_template

@app.route('/')
def start():
    return render_template("start1.html")
@app.route('/index')
def index():
    return render_template("start.html")
if __name__ == "__main__":
    app.run()