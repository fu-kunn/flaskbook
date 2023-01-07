from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, Flaskbook!"


@app.route("/hello",
  methods=["GET", "POST"],
  endpoint="hello-endpoint")
def hello():
    return "Hello, World!"

# @app.route("/hello")
# def hello():
#     return "Hello, World!"