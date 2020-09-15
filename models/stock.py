from db import db


class Material(db.Model):
    __tablename__ = "material"

    material_id = db.Column(db.Integer, primary_key=True)
    material_name = db.Column(db.String(100), nullable=False)
    material_features = db.Column(db.String(200), nullable=True)
    amount = db.Column(db.Integer, nullable=False)
    group = db.Column(db.String(200), nullable=True)
    little_store_id = db.Column(db.Integer, db.ForeignKey(
        'little_store.little_store_id'), nullable=False)


class LittleStore(db.Model):
    __tablename__ = "little_store"

    little_store_id = db.Column(db.Integer, primary_key=True)
    little_store_name = db.Column(db.String(100), nullable=False)
    materials = db.relationship('Material', backref='little_store', lazy=True)
    big_store_id = db.Column(db.Integer, db.ForeignKey(
        'big_store.big_store_id'), nullable=False)

    @property
    def json(self):
        return {
            "little_store_id": self.little_store_id,
            "little_store_name": self.little_store_name,
            "big_store_id": self.big_store_id
        }


class BigStore(db.Model):
    __tablename__ = "big_store"

    big_store_id = db.Column(db.Integer, primary_key=True)
    big_store_name = db.Column(db.String(100), nullable=False)
    little_stores = db.relationship(
        'LittleStore', backref='big_store', lazy=True)
