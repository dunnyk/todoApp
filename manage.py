from flask import request

from app import create_app, tasks_api, tasks_bp, auth_api, auth_bp
from flask_restx import fields, Resource
from helpers.user_service import add_to_user_table, login_user

app = create_app()


user_model = auth_api.model(
    "User",
    {
        "first_name": fields.String(required=True, description="user first name"),
        "last_name": fields.String(required=True, description="user last name"),
        "username": fields.String(
            required=True, unique=True, description="user username"
        ),
        "email": fields.String(
            required=True, unique=True, description="user last name"
        ),
        "password_hash": fields.String(required=True, description="user password"),
    },
)

user_login_model = auth_api.model(
    "Login",
    {
        "username": fields.String(
            required=True, unique=True, description="user's username"
        ),
        "password_hash": fields.String(required=True, description="user password"),
    },
)

task_model = tasks_api.model(
    "Task",
    {
        "task_name": fields.String(required=True, unique=True, description="task name"),
        "description": fields.String(required=True, description="task name"),
        "completed": fields.Boolean(
            default=False, description="Task completion status"
        ),
        "created_at": fields.DateTime(required=True),
        "updated_at": fields.DateTime(required=True),
        "due_date": fields.DateTime(required=True),
        "user_id": fields.String(required=True, unique=True),
        "user": fields.String(required=True),
        "tag": fields.String(required=True),
    },
)


@tasks_api.route("/task_create", methods=["POST", "GET"])
@tasks_api.route("/task_create/<int:task_id>", methods=["GET", "PUT", "DELETE"])
class TaskCreationModel(Resource):

    @tasks_api.expect(task_model)
    def post(self: dict) -> dict:
        from api_endpoints.task_views import create_task

        data = request.get_json()
        return create_task(data)

    def get(self, task_id=None) -> dict:
        import http

        if request.method == "OPTIONS":
            return "", http.HTTPStatus.OK
        if task_id:
            from api_endpoints.task_views import get_task_by_id

            return get_task_by_id(task_id)
        else:
            from api_endpoints.task_views import get_all_task

            return get_all_task()

    def put(self, task_id=None) -> dict:
        from api_endpoints.task_views import update_task

        data = request.get_json()
        return update_task(task_id, data)

    def delete(self, task_id: int) -> dict:
        from api_endpoints.task_views import delete_task

        return delete_task(task_id)


tasks_api.add_resource(TaskCreationModel, "/task_create")


# @tasks_bp.route("/", methods=["POST"])
@auth_api.route("/register")
class RegistrationModel(Resource):

    @auth_api.expect(user_model)
    def post(self: dict) -> dict:
        data = request.get_json()
        return add_to_user_table(data)


@auth_api.route("/login")
class Login(Resource):

    @auth_api.expect(user_login_model)
    def post(self: dict) -> dict:
        data = request.get_json()
        return login_user(data)


app.register_blueprint(tasks_bp)
app.register_blueprint(auth_bp)

if __name__ == "__main__":
    app.run(debug=True, port=5002)
