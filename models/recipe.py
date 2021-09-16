from db import db

class RecipeModel(db.Model):
    __tablename__ = 'recipe'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String,nullable=False)
    description = db.Column(db.String, nullable=False)
    protein = db.Column(db.String)
    fat = db.Column(db.String)
    carb = db.Column(db.String)

    #Relations
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

    @classmethod
    def find_by_title(cls,t):
        return cls.query.filter_by(title=t).first()

    @classmethod
    def delete_all(cls):
        db.session.query(RecipeModel).delete()
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()