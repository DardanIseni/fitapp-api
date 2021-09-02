from marshmallow import  fields,INCLUDE
from ma import ma
from models.user import UserModel

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model =UserModel
        unknown = INCLUDE
        load_instance=True

class UserLoginSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields