from db import db
from mail import mail,Message as MSG
class UserModel(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    surnname = db.Column(db.String)
    age = db.Column(db.Integer)
    email = db.Column(db.String, nullable=False,unique=True)
    password = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False, unique=True)
    isAdmin = db.Column(db.Boolean,default=False)

    #relations
    body_data = db.relationship('BodyDataModel',back_populates="user", uselist=False,)
    recipe = db.relationship('RecipeModel',backref="user",)


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

    def send_bulk_sms(self, users, json, ):
        with mail.connect() as conn:
            for user in users:
                message = json['message']
                subject = json['subject']
                msg = MSG(recipients=[user.email],
                          sender="dardaniseni2000@gmail.com",
                          body=message,
                          subject=subject)
                conn.send(msg)

    def set_recipe(self,recipe):
        self.recipe = recipe

    @classmethod
    def send_sms(cls, user, json):
        with mail.connect() as conn:
                message = json['message']
                subject = json['subject']
                msg = MSG(recipients=[user.email],
                          sender="dardaniseni2000@gmail.com",
                          body=message,
                          subject=subject)
                conn.send(msg)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)