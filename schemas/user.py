from marshmallow import  INCLUDE,fields
from ma import ma
from models.user import UserModel
from .body_data import BodyDataSchema
from .recipe import RecipeSchema

class UserSchema(ma.SQLAlchemyAutoSchema):
    body_data = fields.Nested(BodyDataSchema)
    recipe = fields.Nested(RecipeSchema,many=True)
    class Meta:
        model = UserModel
        unknown = INCLUDE
        load_instance=True
