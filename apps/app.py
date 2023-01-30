from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from apps.config import config

# SQLAlchemyをインスタンス化する
db = SQLAlchemy()
# CSRFProtectをインスタンス化
csrf = CSRFProtect()
# LoginManagerをインスタンス化
login_manager = LoginManager()
# login_view属性に未ログイン時にダイレクトするエンドポイントを指定する
login_manager = "auth_signup"
# login_message属性にログイン後に表示するメッセージを指定する
# ここでは何も表示しないよう空を指定する
login_manager.login_message = ""


# create_app関数の作成
# def create_app():
#     # Flaskインスタンス生成
#     app = Flask(__name__)
#     # アプリのコンフィグ設定
#     app.config.from_mapping(
#         SECRET_KEY = "2AZSMss3p5QPbcY2hBsJ",
#         SQLALCHEMY_DATABASE_URI = f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}", 
#         SQLALCHEMY_TRACK_MODIFICATIONS = False,
#         SQLALCHEMY_ECHO=True,
#         WTF_CSRF_SECRET_KEY="AuwzyszU5sugKN7KZs6f"
#     )

# コンフィグのキーを渡す
def create_app(config_key):
    app = Flask(__name__)

    # config_keyにマッチする環境のコンフィグクラスを読み込む
    app.config.from_object(config[config_key])
    
    # SQLAlchemyとアプリを連携
    db.init_app(app)
    # Migrateとアプリ連携
    Migrate(app, db)
    # csrf.init_app関数を使ってアプリ連携
    csrf.init_app(app)
    # login_managerをアプリケーションと連携する
    login_manager.init_app(app)

    # crudパッケージからviewsをimportする
    from apps.crud import views as crud_views
    # register_blueprintを使いviewsのcrudをアプリへ登録する
    app.register_blueprint(crud_views.crud, url_prefix="/crud")
    
    # これから作成するauthパッケージからviewsをimportする
    from apps.auth import views as auth_views
    # register_blueprintを使いviewsのauthをアプリへ登録する
    app.register_blueprint(auth_views.auth, url_prefix="/auth")

    return app
