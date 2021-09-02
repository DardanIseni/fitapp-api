from flask_restful import Api
from resources.user import UserRegister,UserLogin,UserLogout

def load_resources(app):
    api = Api(app)
    api.add_resource(UserRegister,"/user/register")
    api.add_resource(UserLogin, "/user/login")
    api.add_resource(UserLogout, "/user/logout")

