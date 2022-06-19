from project.dao.director import DirectorDAO
from project.dao.genre import GenreDAO
from project.dao.movie import MovieDAO
from project.dao.user import UserDAO
from project.service.auth import AuthService
from project.service.director import DirectorService
from project.service.genre import GenreService
from project.service.movie import MovieService
from project.service.user import UserService
from project.setup_db import db


movie_dao = MovieDAO(session=db.session)
director_dao = DirectorDAO(session=db.session)
genre_dao = GenreDAO(session=db.session)

user_dao = UserDAO(session=db.session)

movie_service = MovieService(dao=movie_dao)
director_service = DirectorService(dao=director_dao)
genre_service = GenreService(dao=genre_dao)

user_service = UserService(dao=user_dao)
auth_service = AuthService(user_service=user_service)







