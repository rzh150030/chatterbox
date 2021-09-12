from .db import db

class Channel(db.Model):
    __tablename__ = "channels"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    server_id = db.Column(db.Integer, db.ForeignKey("servers.id", ondelete="CASCADE"), nullable=False)

    server = db.relationship("Server", back_populates="channels")
    messages = db.relationship("Message", cascade="all, delete", passive_deletes=True, back_populates="channel")
