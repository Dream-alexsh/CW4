class ItemNotFound(Exception):
    pass


class GenreNotFound(ItemNotFound):
    pass


class UserNotFound(ItemNotFound):
    pass


class WrongPassword(ItemNotFound):
    pass


class NoResultFound(ItemNotFound):
    pass


class IncorrectPassword(Exception):
    pass


class InvalidToken(ItemNotFound):
    pass


class UserAlreadyExists(Exception):
    pass

