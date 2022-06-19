from flask_restx import Resource, Namespace

from implemented import genre_service
from project.dao.serialization.genre import GenreSchema


genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        genre = genre_service.get_all()
        return GenreSchema(many=True).dump(genre), 200


@genre_ns.route('/<int:rid>/')
class GenreView(Resource):
    def get(self, rid):
        genre = genre_service.get_by_id(rid)
        return GenreSchema().dump(genre), 200

