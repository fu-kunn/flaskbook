from email_validator import validate_email, EmailNotValidError
from flask import (
    Flask, 
    current_app,
    g,
    redirect,
    render_template, 
    url_for, 
    request, 
    flash,
)
import logging

app = Flask(__name__)
# SECRET_KEYを追加する
app.config["SECRET_KEY"] = "2AZSMss3p5QPbcY2hBsJ"
# ログレベルの設定
app.logger.setLevel(logging.DEBUG)

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
        
        # 入力チェック
        is_valid = True

        if not username:
            flash("ユーザ名は必須です")
            is_valid = False

        if not email:
            flash("メールアドレスは必須です")
            is_valid = False
        
        try:
            validate_email(email)
        except EmailNotValidError:
            flash("メールアドレスの形式で入力してください")
            is_valid = False
        
        if not description:
            flash("問い合わせ内容は必須です")
            is_valid = False
        
        if not is_valid:
            return redirect(url_for("contact"))

      # メールを送る




        # contactエンドポイントへリダイレクトする
        flash("問い合わせ内容はメールにて送信しました。問い合わせありがとうございます。")
        return redirect(url_for("contact_complete"))
    return render_template("contact_complete.html")
