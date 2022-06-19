from project.setup_db import db
from project.dao.model.base import BaseMixin


class Director(BaseMixin, db.Model):
    __tablename__ = "director"

    name = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"<Director '{self.name.title()}'>"


