import http
from flask import request
from models.tasks.models import Task

from flask_jwt_extended import jwt_required, get_jwt_identity
from models.users.models import User
from utilities.database import db
from helpers.task_tag_service import create_tag


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

    tags = data.pop("tags", [])
    task = Task(**data)
    db.session.add(task)
    create_tag(task, tags, user_id)
    db.session.commit()
    return {"message": "Task created successfully"}, http.HTTPStatus.CREATED


@jwt_required()
def get_all_task():
    tasks = Task.query.all()
    tasks_dict = [task.to_dict() for task in tasks]
    return {"message": "All tasks retrieved successfully", "tasks_dict": tasks_dict}


@jwt_required()
def get_task_by_id(task_id):

    task = Task.query.get_or_404(task_id, "That task does not exist")
    return {
        "message": f"`{task.task_name}` Task retrieved successfully",
        "task": task.to_dict(),
    }


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
        tag_names = data.get("tags")
        create_tag(task, tag_names, task.user_id)

    db.session.commit()
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
