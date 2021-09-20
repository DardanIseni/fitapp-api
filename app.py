from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import  JWTManager
from flask_mail import Mail,Message
from resources.load_resources import load_resources
from db import db
from ma import ma


app = Flask(__name__)
jwt = JWTManager(app)
app.config.from_object('config.Config')
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']= 465
app.config['MAIL_USERNAME'] = 'dardaniseni2000@gmail.com'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL']= True
app.config['MAIL_PASSWORD'] = 'dardiiseni123321'
mail = Mail(app)
ma.init_app(app)
db.init_app(app)
migrate = Migrate(app,db)

def create_tables():
    with app.app_context():
        db.create_all()
@app.route('/hello')
def index():
    msg = Message("Hello",
                  sender='dardaniseni2000@gmail.com',
                  recipients=["dardaniseni20@gmail.com"])
    mail.send(msg)
    return 'hello'
load_resources(app)
create_tables()

if __name__ == '__main__':
    app.run(debug=True)
