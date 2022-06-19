from sqlalchemy.orm.scoping import scoped_session


class BaseDAO:

    def __init__(self, session: scoped_session):
        self.session = session

