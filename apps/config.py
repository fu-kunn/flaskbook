from pathlib import Path

basedir = Path(__file__).parent.parent

# BaseConfigクラスを作成
class BaseConfig:
    SECRET_KEY = "2AZSMss3p5QPbcY2hBsJ"
    WTF_CSRF_SECRET_KEY = "AuwzyszU5sugKN7KZs6f"
    # 画像アップロード先にapp/imagesを指定
    UPLOAD_FOLDER = str(Path(basedir, "apps", "images"))


# BaseConfigクラスを継承してLocalConfigクラスを作成
class LocalConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir / 'local.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True


# BaseConfigクラスを継承してTestingConfigクラスを作成
class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir / 'testing.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False


# Config辞書にマッピングする
config = {
    "testing": TestingConfig,
    "local": LocalConfig,
}