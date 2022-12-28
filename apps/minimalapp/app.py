from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, Flaskbook!"


# @app.route("/hello",
#   methods=["GET"],
#   endopoint="hello-endopoint")
# def hello():
#     return "Hello, World!"

@app.route("/hello")
def hello():
    return "Hello, World!"