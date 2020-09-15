from flask import Flask
from db import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///searover.db'
app.config['SECRET_KEY'] = "hQyLIXWJ2NI9RKHmTgkn9aUu5K5jtktD"
db.init_app(app)
