
class Config():
    SQLALCHEMY_DATABASE_URI = "sqlite:///app.sqlite"
    JWT_SECRET_KEY = "HELLOO",
    SECRET_KEY = "fix-this-after",
    SQLALCHEMY_TRACK_MODIFICATIONS = False,
    DEBUG = True,