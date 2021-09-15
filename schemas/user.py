from marshmallow import  INCLUDE,fields
from ma import ma
from models.user import UserModel
from .body_data import BodyDataSchema

class UserSchema(ma.SQLAlchemyAutoSchema):
    body_data = fields.Nested(BodyDataSchema)
    class Meta:
        model = UserModel
        unknown = INCLUDE
        load_instance=True
