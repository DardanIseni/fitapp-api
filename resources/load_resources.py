from flask_restful import Api
from resources.user import UserRegister,UserLogin,UserLogout
from resources.recipe import Recipe
def load_resources(app):
    api = Api(app)
    api.add_resource(UserRegister,"/user/register")
    api.add_resource(UserLogin, "/user/login")
    api.add_resource(UserLogout, "/user/logout")
    api.add_resource(Recipe,"/recipe","/recipe/<string:title>")

