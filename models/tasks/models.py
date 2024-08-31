from utilities.database import db


class Task(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(
        db.DateTime,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp(),
    )
    due_date = db.Column(db.DateTime())
    user_id = db.Column(
        db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False
    )
    tags = db.relationship("Tag", secondary="task_tags", back_populates="tasks")
    user = db.relationship("User", back_populates="tasks")

    def __str__(self) -> str:
        return self.task_name

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "task_name": self.task_name,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "due_date": self.due_date.isoformat() if self.due_date else None,
            "user_id": self.user_id,
            "tags": [tag.to_dict() for tag in self.tags] if self.tags else [],
        }


class Tag(db.Model):
    __tablename__ = "tags"
    id = db.Column(db.Integer, primary_key=True)
    tag_name = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User", back_populates="tags")
    tasks = db.relationship(Task, secondary="task_tags", back_populates="tags")

    def __str__(self) -> str:
        return self.name + " is the name of the tag"

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "tag_name": self.tag_name,
            "user_id": self.user_id,
            "tasks": [task.id for task in self.tasks],
        }


task_tags = db.Table(
    "task_tags",
    db.Column("task_id", db.Integer, db.ForeignKey("tasks.id"), primary_key=True),
    db.Column("tag_id", db.Integer, db.ForeignKey("tags.id"), primary_key=True),
)
