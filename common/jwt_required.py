import jwt
from app import app
from flask import request
from flask_restful import reqparse

jwt_parser = reqparse.RequestParser()
jwt_parser.add_argument("token", required=True, help="Token is required")


def jwt_required(original_function):
    def check_jwt(self, payload=None):
        args = jwt_parser.parse_args()
        token = args["token"]
        try:
            payload = jwt.decode(token, app.config["SECRET_KEY"])
            return original_function(self, payload=payload)
        except (jwt.ExpiredSignatureError, jwt.DecodeError):
            return {"message": "You are not authorized"}, 403
    return check_jwt
