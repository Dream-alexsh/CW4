from flask import request

from project.dao.base import BaseDAO
from project.dao.model.movie import Movie
from project.config import BaseConfig

count = BaseConfig.ITEMS_PER_PAGE


class MovieDAO(BaseDAO):

    def get_one(self, bid):
        return self.session.query(Movie).get(bid)

    def get_all(self):
        movies_all = self.session.query(Movie)
        args = request.args
        if 'status' in args and args.get('status') == 'new' and 'page' in args:
            page = int(args.get('page'))
            movies = self.session.query(Movie).order_by(Movie.year.desc())
            movie = movies.paginate(page, count, False)
            return movie.items
        elif 'status' in args and args.get('status') == 'new':
            movies_all = self.session.query(Movie).order_by(Movie.year.desc()).all()
        elif 'page' in args:
            page = int(args.get('page'))
            movies = movies_all.paginate(page, count, False)
            return movies.items
        return movies_all

    def get_by_director_id(self, val):
        return self.session.query(Movie).filter(Movie.director_id == val).all()

    def get_by_genre_id(self, val):
        return self.session.query(Movie).filter(Movie.genre_id == val).all()

    def get_by_year(self, val):
        return self.session.query(Movie).filter(Movie.year == val).all()
