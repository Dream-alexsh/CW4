# from unittest.mock import Mock, patch
#
# import pytest
#
# from project.dao.model.genre import Genre
# from project.exceptions import ItemNotFound
# from project.dao.serialization.genre import GenreSchema
# from project.service.genre import GenreService
#
#
# class TestGenresService:
#     @pytest.fixture(autouse=True)
#     def service(self, db):
#         self.service = GenreService(db.session)
#
#     @pytest.fixture
#     def genre(self):
#         return Genre(id=1, name="genre_1")
#
#     @pytest.fixture
#     def genre_dao_mock(self, genre):
#         with patch("project.service.genre.GenreService") as mock:
#             mock.return_value = Mock(
#                 get_by_id=Mock(return_value=GenreSchema().dump(genre)),
#                 get_all=Mock(return_value=GenreSchema(many=True).dump([genre])),
#             )
#             yield mock
#
#     def test_get_all_genres(self, genre_dao_mock, genre):
#         assert self.service.get_all() == GenreSchema(many=True).dump([genre])
#         genre_dao_mock().get_all.assert_called_once()
#
#     def test_get_item_by_id(self, genre_dao_mock, genre):
#         assert self.service.get_by_id(genre.id) == GenreSchema().dump(genre)
#         genre_dao_mock().get_by_id.assert_called_once_with(genre.id)
#
#     def test_get_item_by_id_not_found(self, genre_dao_mock):
#         genre_dao_mock().get_by_id.return_value = None
#
#         with pytest.raises(ItemNotFound):
#             self.service.get_by_id(1)
