from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello():
    return '<form action="/echo" method="POST"><input type="submit" > <input name="text1" value="om"><input type="submit" > <input name="text2" value="om1"></form>'


@app.route("/echo", methods=['POST'])
def echo():
    print(request.form)
    return "You said: " + request.form


if __name__ == "__main__":
    app.run()