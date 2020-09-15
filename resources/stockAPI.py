from flask_restful import Resource, reqparse

# COMMON
from common.jwt_required import jwt_required

# MODELS
from models.stock import LittleStore, Material


class StockAPI(Resource):

    def get(self):
        little_store = LittleStore.query.first()
        return little_store.json
