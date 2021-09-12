from .db import db

joinedServers = db.Table(
    "joinedServers",
    db.Column("server_id", db.Integer, db.ForeignKey("servers.id"), primary_key=True),
    db.Column("user_id", db.Integer, db.ForeignKey("users.id"), primary_key=True)
)
