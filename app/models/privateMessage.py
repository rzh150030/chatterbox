from .db import db

class PrivateMessage(db.Model):
    __tablename__ = "privateMessages"

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(5000), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    private_server_id = db.Column(db.Integer, db.ForeignKey("privateServers.id", ondelete="CASCADE"), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    private_server = db.relationship("PrivateServer", back_populates="private_server_messages")
    user = db.relationship("User", back_populates="private_messages")
