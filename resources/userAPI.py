from flask_restful import Resource, reqparse
import bcrypt

# COMMON
from common.jwt_required import jwt_required

# MODELS
from models.user import User


class UserAPI(Resource):

    user_parser = reqparse.RequestParser()
    user_parser.add_argument("username", required=True,
                             help="Username required")
    user_parser.add_argument("password", required=True,
                             help="Password is required")

    @jwt_required
    def get(self, payload):
        user = User.query.filter_by(username=payload["username"]).first()
        return user.json

    def post(self):
        """
        Authenticate and send JWT token
        Not sign up!!!
        """
        args = self.user_parser.parse_args()
        user = User.query.filter_by(username=args["username"]).first()
        return user.login(args["password"])
