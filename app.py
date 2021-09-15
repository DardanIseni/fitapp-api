from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import  JWTManager
from resources.load_resources import load_resources
from db import db
from ma import ma


app = Flask(__name__)
jwt = JWTManager(app)

app.config.from_object('config.Config')

ma.init_app(app)
db.init_app(app)
migrate = Migrate(app,db)

load_resources(app)


if __name__ == '__main__':
    app.run(debug=True)
