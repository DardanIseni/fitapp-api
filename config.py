
class Config():
    SQLALCHEMY_DATABASE_URI = "sqlite:///app.sqlite"
    JWT_SECRET_KEY = "test-hello-world",
    SECRET_KEY = "fix-this-after",
    SQLALCHEMY_TRACK_MODIFICATIONS = False,
    DEBUG = True,