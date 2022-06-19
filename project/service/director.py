from project.dao.director import DirectorDAO
from project.service.base import BaseService


class DirectorService(BaseService[DirectorDAO]):
    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self):
        return self.dao.get_all()
