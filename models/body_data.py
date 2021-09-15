from db import db
from math import  sqrt

class BodyDataModel(db.Model):
    __tablename__ = 'body_data'
    id = db.Column(db.Integer,primary_key=True)
    weight = db.Column(db.Integer,nullable=False)
    height = db.Column(db.Integer, nullable=False)
    bmi = db.Column(db.Integer)

    #relationship
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    user = db.relationship('UserModel')


    def calculate_bmi(self):
        self.bmi = self.weight/sqrt(self.height)
