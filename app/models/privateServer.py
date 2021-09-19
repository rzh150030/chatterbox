from .db import db

class PrivateServer(db.Model):
    __tablename__ = "privateServers"

    id = db.Column(db.Integer, primary_key=True)
    db.Column("user_id_1", db.Integer, db.ForeignKey("users.id"), primary_key=True)
    db.Column("user_id_2", db.Integer, db.ForeignKey("users.id"), primary_key=True)

    user1 = db.relationship("User", back_populates="private_servers1")
    user2 = db.relationship("User", back_populates="private_servers2")
    private_server_messages = db.relationship("PrivateMessage", cascade="all, delete", passive_deletes=True, back_populates="private_server")
