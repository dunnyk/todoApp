from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "7ac9eac1cb5417a0"  # Use a unique identifier
down_revision = None  # Set this if this is your first migration or to the previous migration's revision ID
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "user",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("first_name", sa.String(length=50), nullable=False),
        sa.Column("last_name", sa.String(length=50), nullable=False),
        sa.Column("email", sa.String(length=100), nullable=False, unique=True),
        sa.Column("username", sa.String(length=50), nullable=False, unique=True),
        sa.Column("password_hash", sa.String(length=100), nullable=False),
    )


def downgrade():
    op.drop_table("user")
