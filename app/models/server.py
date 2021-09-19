from .db import db
from .joinedServer import joinedServers

class Server(db.Model):
    __tablename__ = "servers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    topic = db.Column(db.String(500), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    channels = db.relationship("Channel", cascade="all, delete", passive_deletes=True, back_populates="server")
    server_users = db.relationship("User", secondary=joinedServers, back_populates="joined_servers")
