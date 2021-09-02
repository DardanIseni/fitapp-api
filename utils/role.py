from flask_jwt_extended import get_jwt_identity,verify_jwt_in_request
from functools import wraps
from models.user import UserModel


def admin_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            user_id = get_jwt_identity()
            user = UserModel.findById(user_id)
            if user.isAdmin:
                return fn(*args, **kwargs)
            else:
                return {"msg":"Admins only!"}, 403

        return decorator

    return wrapper