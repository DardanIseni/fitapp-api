from flask_jwt_extended import get_jwt_identity,verify_jwt_in_request
from functools import wraps
from models.user import UserModel


def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        jwt = get_jwt_identity()
        user = UserModel().findById(jwt)

        if not user.isAdmin:
            return {"message": "admin required"}, 403
        else:
            return fn(*args, **kwargs)

    return wrapper