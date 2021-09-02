from db import db

class UserModel(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    surnname = db.Column(db.String)
    age = db.Column(db.Integer)
    email = db.Column(db.String, nullable=False,unique=True)
    password = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False, unique=True)
    isAdmin = db.Column(db.Boolean,default=False)

    #relations

    #TODO


    @classmethod
    def findById(cls,id):
        return UserModel.query.filter_by(id=id).first()

    @classmethod
    def findByUsername(cls, username):
        return UserModel.query.filter_by(username=username).first()

    @classmethod
    def findByEmail(cls, email):
        return UserModel.query.filter_by(email=email).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)