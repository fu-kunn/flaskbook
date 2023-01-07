from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, Flaskbook!"

# エンドポイントの作成
@app.route("/hello/<name>",
  methods=["GET", "POST"],
  endpoint="hello-endpoint")
def hello(name):
    return f"Hello, {name}!"

# show_nameエンドポイントの作成
@app.route("/name/<name>")
def show_name(name):
    # 変数をテンプレートエンジンに渡す
    return render_template("index.html", name=name)

with app.test_request_context():
    # /
    print(url_for("index"))
    # /hello/world
    print(url_for("hello-endpoint", name="world"))
    # /name/ichiro?page=1
    print(url_for("show_name", name="ichiro", page="1"))


with app.test_request_context("users?updated=true"):
    print(request.args.get("updated"))
