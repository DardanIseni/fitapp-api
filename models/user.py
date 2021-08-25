from db import db

class UserModel(db.Model):

    id = db.Column(db.Integer,primary_key=True),
    username = db.Column(db.String,nullable=False),
    email = db.Column(db.String, nullable=False),
    password = db.Column(db.String, nullable=False),
    username = db.Column(db.String, nullable=False),
    isAdmin = db.Column(db.Boolean,default=False)



    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)