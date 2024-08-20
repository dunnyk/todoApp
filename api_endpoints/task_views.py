import http
from flask import request
from flask_login import current_user
from helpers.log import login_user
from models.tasks.models import Task

from flask_jwt_extended import jwt_required, get_jwt_identity
from models.users.models import User
from utilities.database import db


# @tasks_bp.route("/", methods=["POST"])
@jwt_required()
def task_create(data: dict) -> dict:

    user_id = get_jwt_identity()

    user = User.query.get(user_id)

    """create a new task, and return the task instance"""
    data = request.get_json()

    if not data:
        return {"error": "No data is supplied"}, http.HTTPStatus.BAD_REQUEST

    if not user:
        return {"error": "User is not authenticated"}, http.HTTPStatus.UNAUTHORIZED

    db_task = Task.query.filter_by(task_name=data.get("task_name")).first()

    if db_task:
        return {"error": "Task already exists"}, http.HTTPStatus.CONFLICT

    task = Task(**data)
    db.session.add(task)
    db.session.commit()
    return {"message": "Task created successfully"}, http.HTTPStatus.CREATED
