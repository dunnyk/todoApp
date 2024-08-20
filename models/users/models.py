import jwt

from utilities.database import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timezone

from config import AppConfig
from models.tasks.models import Tag, Task


class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)

    # User Fields
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)

    # User Authentication fields
    email = db.Column(db.String(100), nullable=False, unique=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    tasks = db.relationship(Task, back_populates="user")
    tags = db.relationship(Tag, back_populates="user")

    def __str__(self) -> str:
        return f"{self.username}: Email {self.email}"

    def encode_auth_token(self, user_id) -> str:
        try:
            payload = {
                "exp": datetime.now(timezone.utc)
                + datetime.timedelta(days=AppConfig.TOKEN_EXP_TIME),
                "iat": datetime.now(timezone.utc),
                "sub": user_id,
            }
            return jwt.encode(payload, AppConfig.FLASK_SECRET_KEY, algorithm="HS256")
        except Exception as error:
            return f"{str(error)}, when encoding the Token"

    def decode_auth_token(self, auth_token) -> int | str:
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, AppConfig.FLASK_SECRET_KEY)
            return payload["sub"]
        except jwt.ExpiredSignatureError:
            return "Signature expired. Please log in again."
        except jwt.InvalidTokenError:
            return "Invalid token. Please log in again."

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        print(self.password_hash)
        if self.password_hash is None:
            return False
        return check_password_hash(self.password_hash, password)
