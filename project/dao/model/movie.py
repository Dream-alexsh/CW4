from project.setup_db import db
from project.dao.model.base import BaseMixin


class Movie(BaseMixin, db.Model):
    __tablename__ = "movie"

    title = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.String(255))
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    genre = db.relationship("Genre")
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))
    director = db.relationship("Director")

