from flask import request, current_app

from project.dao.base import BaseDAO
from project.dao.model.director import Director


class DirectorDAO(BaseDAO):
    def get_one(self, bid):
        return self.session.query(Director).get(bid)

    def get_all(self):
        director_all = self.session.query(Director)
        args = request.args
        if 'page' in args:
            page = int(args.get('page'))
            directors = director_all.paginate(page, current_app.config['ITEMS_PER_PAGE'], False)
            return directors.items
        return director_all
