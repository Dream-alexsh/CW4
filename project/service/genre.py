from project.dao.genre import GenreDAO
from project.dao.serialization.genre import GenreSchema
from project.exceptions import ItemNotFound
from project.service.base import BaseService


class GenreService(BaseService[GenreDAO]):

    def get_all(self):
        return self.dao.get_all()

    def get_by_id(self, gid) -> GenreSchema:
        genre = self.dao.get_by_id(gid)
        if not genre:
            raise ItemNotFound
        return genre

