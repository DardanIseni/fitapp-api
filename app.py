from flask import Flask
from flask_migrate import Migrate
from db import db
from ma import ma


app = Flask(__name__)
app.config.from_object('config.Config')
ma.init_app(app)
db.init_app(app)
migrate = Migrate(app,db)

if __name__ == '__main__':
    app.run(debug=True)
