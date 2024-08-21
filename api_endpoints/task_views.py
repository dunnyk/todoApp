import http
from flask import jsonify, request
from models.tasks.models import Task

from flask_jwt_extended import jwt_required, get_jwt_identity
from models.users.models import User
from utilities.database import db


@jwt_required()
def create_task(data: dict) -> dict:

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


@jwt_required()
def get_all_task():
    users = Task.query.all()
    users_dict = [user.to_dict() for user in users]
    return jsonify(users_dict)


@jwt_required()
def get_task_by_id(task_id):

    task = Task.query.get_or_404(task_id, "That task does not exist")
    return task.to_dict()


@jwt_required()
def update_task(task_id: int, data: dict):

    task = Task.query.get_or_404(task_id, "This task has been deleted, does not exist")
    if not task:
        return {"error": "Task not found"}, http.HTTPStatus.NOT_FOUND

    if "task_name" in data:
        task.task_name = data.get("task_name")

    if "description" in data:
        task.description = data.get("description")

    if "due_date" in data:
        task.due_date = data.get("due_date")

    if "completed" in data:
        task.completed = data.get("completed")

    if "tags" in data:
        task.tags = data.get("tags")

    db.session.commit()
    # task = [tak.to_dict() for tak in task]
    return {
        "message": "Task updated successfully",
        "task": task.to_dict(),
    }, http.HTTPStatus.OK


@jwt_required()
def delete_task(task_id: int) -> dict:

    task = Task.query.get_or_404(task_id, "This task has been deleted, does not exist")
    if not task:
        return {"error": "Task not found"}, http.HTTPStatus.NOT_FOUND

    db.session.delete(task)
    db.session.commit()
    return {
        "message": "Task deleted successfully",
        "task": task.to_dict(),
    }, http.HTTPStatus.OK
