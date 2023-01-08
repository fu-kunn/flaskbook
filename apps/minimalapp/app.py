from flask import(
    Flask, 
    current_app,
    g,
    redirect,
    render_template, 
    url_for, 
    request, 
    flash
)

app = Flask(__name__)
# SECRET_KEYを追加する
app.config["SECRET_KEY"] = "2AZSMss3p5QPbcY2hBsJ"

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


"""
1.3問い合わせフォームの作成
"""
@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/contact/complete", methods=["GET", "POST"])
def contact_complete():
    if request.method == "POST":
        # フォーム属性を使ってフォームの値を取得する
        username = request.form["username"]
        email = request.form["email"]
        description = request.form["description"]
        # メールを送る
        # contactエンドポイントへリダイレクトする
        return redirect(url_for("contact_complete"))
    return render_template("contact_complete.html")
