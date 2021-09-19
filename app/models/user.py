from .db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from .joinedServer import joinedServers


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)

    messages = db.relationship("Message", back_populates="user")
    joined_servers = db.relationship("Server", secondary=joinedServers, back_populates="server_users")
    private_servers1 = db.relationship("PrivateServer", cascade="all, delete", passive_deletes=True, back_populates="user1")
    private_servers2 = db.relationship("PrivateServer", cascade="all, delete", passive_deletes=True, back_populates="user2")
    private_messages = db.relationship("PrivateMessage", back_populates="user")

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }
