from flask import Flask

app = Flask(__name__)

@app.route("/")
def sayHello():
    return "<h1>Hello!</h1>"