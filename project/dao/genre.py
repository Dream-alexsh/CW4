from flask import request

from project.dao.base import BaseDAO
from project.dao.model.genre import Genre
from flask import current_app


class GenreDAO(BaseDAO):
    def get_by_id(self, genre_id: int):
        return self.session.query(Genre).get(genre_id)

    def get_all(self):
        genre_all = self.session.query(Genre)
        args = request.args
        if 'page' in args:
            page = int(args.get('page'))
            genres = genre_all.paginate(page, current_app.config['ITEMS_PER_PAGE'], False)
            return genres.items
        return genre_all

