from utilities.database import db
from models.tasks.models import Tag, Task


def create_tag(task: Task, tag_names: list, user_id: int):

    for name in tag_names:
        tag = Tag.query.filter_by(tag_name=name, user_id=user_id).first()
        if not tag:
            tag = Tag(tag_name=name, user_id=user_id)
            db.session.add(tag)
            db.session.flush()
        if tag not in task.tags:
            task.tags.append(tag)
