
class Config():
    SQLALCHEMY_DATABASE_URI = "add_your_uri"
    SECRET_KEY = "change-this-key-in-the-application-config"
    JWT_SECRET_KEY = "change-this-key-to-something-different-in-the-application-config"
    USER_EMAIL_SENDER_EMAIL = "noreply@example.com"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'youremail@gmail.com'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_PASSWORD= 'pw'