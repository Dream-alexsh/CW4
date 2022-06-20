from flask_restx import abort

from project.dao.genre import GenreDAO
from project.service.base import BaseService


class GenreService(BaseService[GenreDAO]):

    def get_all(self):
        return self.dao.get_all()

    def get_by_id(self, gid):
        genre = self.dao.get_by_id(gid)
        if not genre:
            abort(404)
        return genre

