from apps.crud.forms import UserForm
from flask import Blueprint, render_template, redirect, url_for
from apps.app import db
from apps.crud.models import User

# Blueprintでcrudアプリを生成
crud = Blueprint(
    "crud",
    __name__,
    template_folder="templates",
    static_folder="static",
)

# indexエンドポイントを作成しindex.htmlを返す
@crud.route("/")
def index():
    return render_template("crud/index.html")

@crud.route("/sql")
def sql():
    db.session.query(User).all()
    return "コンソールログを確認してください"

@crud.route("/users/new", methods=["GET", "POST"])
def create_user():
    # UserFormをインスタンス化する
    form = UserForm()
    # フォームの値をバリデートする
    if form.validate_on_submit():
        # ユーザ作成
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
        )
        # ユーザを追加してコミット
        db.session.add(user)
        db.session.commit()
        # ユーザの一覧画面へリダイレクト
        return redirect(url_for("crud.users"))
    return render_template("crud/create.html", form=form)


@crud.route("/users")
def users():
    """ユーザの一覧を取得する"""
    users = User.query.all()
    return render_template("crud/index.html", users=users)