from flask import Flask, request

app = Flask(__name__)

def sum(a):
    t=0
    for i in a:
        t=t+int(i)
    return t
@app.route("/")
def hello():
    return '<form action="/" method="GET"><input name="text"><input type="submit" value="INput"></form>'


@app.route("/",methods=['GET','POST'])
def echo():
    return "You said: " + request.form


if __name__ == "__main__":
    app.run()