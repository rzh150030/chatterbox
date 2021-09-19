from .db import db

class Message(db.Model):
    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(5000), nullable=False)
    channel_id = db.Column(db.Integer, db.ForeignKey("channels.id", ondelete="CASCADE"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    channel = db.relationship("Channel", back_populates="messages")
    user = db.relationship("User", back_populates="messages")
