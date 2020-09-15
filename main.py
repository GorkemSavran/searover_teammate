from app import app
from flask_restful import Api


# Resources
from resources.userAPI import UserAPI
from resources.stockAPI import StockAPI

api = Api(app)


api.add_resource(UserAPI, "/user")
api.add_resource(StockAPI, "/stock")


if __name__ == "__main__":
    app.run(debug=True, port=8080)
