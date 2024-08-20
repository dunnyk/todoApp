from flask import Flask, Blueprint
from flask_login import LoginManager
from flask_restx import Api
from config import AppConfig
from models.users.models import User
from utilities.database import db
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager


# Blueprint for tasks-related routes
tasks_bp = Blueprint("tasks_blueprint", __name__, url_prefix="/tasks")
tasks_api = Api(tasks_bp)


# Blueprint for authentication-related routes
auth_bp = Blueprint("auth_blueprint", __name__)
auth_api = Api(auth_bp)


login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def create_app():
    app = Flask(__name__)
    app.config.from_object(AppConfig)
    db.init_app(app)
    login_manager.init_app(app)

    # create migration for the app
    Migrate(app, db)
    JWTManager(app)

    return app
