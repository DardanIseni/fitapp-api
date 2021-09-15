from flask import  request
from flask_restful import Resource
from flask_jwt_extended import create_access_token,create_refresh_token,get_jwt,get_jwt_identity,jwt_required
from models.user import UserModel
from schemas.user import UserSchema
from blacklist import  BLACKLIST

user_login_schema = UserSchema(only=('username','password',))
class UserRegister(Resource):
    def post(self):
        input = request.get_json()
        user =UserSchema().load(input)
        if  UserModel.findByUsername(user.username):
            return {"message": "User with this username already exist"}, 400
        if UserModel.findByEmail(user.email):
            return {"message": "User with this email already exist"}, 400
        try:
            user.body_data.calculate_bmi()
            user.save_to_db()
            return {"message":"User created"},200

        except Exception as e :
            return {"message":e}

class UserLogin(Resource):

    def post(self):
        data =user_login_schema.load(request.get_json())
        user = UserModel.findByUsername(data.username)

        if user:
            if user.password == data.password:
                access_token = create_access_token(identity=user.id,fresh=True)
                refresh_token = create_refresh_token(identity=user.id)
                return{
                    "access_token":access_token,
                    "refresh_token":refresh_token
                },200

            return {"message":"Password is not correct"},403
        return {"message":"User does not exist"},404

class UserLogout(Resource):
    @jwt_required()
    def post(self):
        jti = get_jwt()["jti"]  # jti is "JWT ID", a unique identifier for a JWT.
        user_id = get_jwt_identity()
        BLACKLIST.add(jti)
        return {"message": "User <id={}> successfully logged out.".format(user_id)}, 200


