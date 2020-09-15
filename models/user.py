from db import db
from app import app

import bcrypt
import jwt
import datetime


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    rank = db.Column(db.String(60), nullable=False)
    username = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def create(self):
        db.session.add(self)
        db.session.commit()

    def login(self, password):
        if bcrypt.checkpw(password.encode("utf-8"), self.password.encode("utf-8")):
            payload = self.json
            payload["exp"] = datetime.datetime.utcnow() + \
                datetime.timedelta(seconds=60)
            return {"token": jwt.encode(payload=payload, key=app.config["SECRET_KEY"], algorithm='HS256').decode()}, 200
        else:
            return {"message": "Username or password incorrect"}

    @property
    def json(self):
        return {"username": self.username,
                "name": self.name,
                "rank": self.rank}
