from project.dao.model.base import BaseMixin
from project.setup_db import db


class User(BaseMixin, db.Model):
    __tablename__ = 'user'
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    favourite_genre = db.Column(db.Integer, db.ForeignKey("genre.id"))

    genre = db.relationship("Genre")

    def __repr__(self):
        return f"<User '{self.email.title()}'>"


