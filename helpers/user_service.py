import http

from models.users.models import User
from werkzeug.security import generate_password_hash

from http import HTTPStatus
from utilities.database import db
from flask_jwt_extended import create_access_token


def add_to_user_table(data: dict) -> dict:
    if not data:
        return "Registration data must be provided.", HTTPStatus.NO_CONTENT

    username = User.query.filter_by(username=data.get("username")).first()
    email = User.query.filter_by(email=data.get("email")).first()

    try:

        if email is not None:
            return {
                "message": f"User with {data.get('email')} email exists use another email"
            }, http.HTTPStatus.BAD_REQUEST

        if username is not None:
            return {
                "message": f"User with {data.get('username')} username already exists, use another username"
            }, http.HTTPStatus.BAD_REQUEST

        hashed_password = generate_password_hash(data.get("password_hash"))
        new_user_payload = {
            "first_name": data.get("first_name"),
            "last_name": data.get("last_name"),
            "username": data.get("username"),
            "email": data.get("email"),
        }
        new_user = User(**new_user_payload, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return {"mesage": "User registered successfully"}, HTTPStatus.CREATED
    except Exception as error:
        return {
            "error": f"{str(error)}, when trying to register {username}"
        }, http.HTTPStatus.NOT_ACCEPTABLE


def login_user(data: dict) -> dict:

    if not data:
        return {"msg": "Missing username or password"}, HTTPStatus.UNAUTHORIZED

    user = User.query.filter_by(username=data.get("username")).first()
    if user is None:
        return {"error": "Invalid username or password"}, http.HTTPStatus.UNAUTHORIZED

    username = user.username
    password_hash = generate_password_hash(
        data.get("password_hash", "No password is from UI")
    )
    user.set_password(password_hash)

    try:

        if not username:
            return {"message": "Invalid username"}, HTTPStatus.UNAUTHORIZED

        if not password_hash:
            {"message": "No password is from UI to harsh"}

        access_token = create_access_token(identity=user.id)
        return {"access_token": access_token}, HTTPStatus.OK

    except AttributeError as error:
        return {"error": f"{str(error)}"}, HTTPStatus.UNAUTHORIZED

    except Exception as error:
        return f"{str(error)}"
