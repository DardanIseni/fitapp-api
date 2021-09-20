
class Config():
    SQLALCHEMY_DATABASE_URI = "postgresql://develop:root123@localhost/fitapp"
    SECRET_KEY = "change-this-key-in-the-application-config"
    JWT_SECRET_KEY = "change-this-key-to-something-different-in-the-application-config"
    USER_EMAIL_SENDER_EMAIL = "noreply@example.com"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True