from flask import Blueprint, render_template

# Blueprintでcrudアプリを生成
curd = Blueprint(
    "crud",
    __name__,
    template_folder="templates",
    static_folder="static",
)

# indexエンドポイントを作成しindex.htmlを返す
@crud.route("/")
def index():
    return_template("crud/index.html")
