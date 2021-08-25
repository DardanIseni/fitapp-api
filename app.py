from flask import Flask
from db import db
from ma import ma

app = Flask(__name__)
ma.init_app(app)
db.init_app(app)

if __name__ == '__main__':
    app.run()
