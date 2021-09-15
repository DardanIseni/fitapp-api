from ma import ma
from marshmallow import fields
from models.recipe import RecipeModel
class RecipeSchema(ma.SQLAlchemyAutoSchema):
    user_id = fields.Integer()
    class Meta:
        model = RecipeModel
        load_instance = True
