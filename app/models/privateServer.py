from .db import db

class PrivateServer(db.Model):
    __tablename__ = "privateServers"

    id = db.Column(db.Integer, primary_key=True)
    db.Column("user_id_1", db.Integer, db.ForeignKey("users.id"), primary_key=True)
    db.Column("user_id_2", db.Integer, db.ForeignKey("users.id"), primary_key=True)
