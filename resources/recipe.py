from flask_restful import Resource,request
from flask_jwt_extended import get_jwt_identity,jwt_required
from models.recipe import RecipeModel
from models.user import UserModel
from schemas.recipe import RecipeSchema

recipe_schema = RecipeSchema()

class Recipe(Resource):
    @jwt_required()
    def post(self):
        input = request.get_json()
        user = UserModel.findById(get_jwt_identity())
        input['user_id'] = user.id
        data = recipe_schema.load(input)

        try:
            data.save_to_db()
            return {"message":"Successfuly created a recipe"},200

        except Exception as e:
            return {"message":e}

    def get(self,title = None):

        if title is not None:
           try:
               recipe = RecipeModel().find_by_title(title)
               return recipe_schema.dump(recipe),200
           except:
               return {"message":"Couldnt find recipe with title {}".format(title)},404

        recipes = RecipeModel().query.all()
        return RecipeSchema(many=True).dump(recipes),200


