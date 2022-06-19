from project.dao.base import BaseDAO
from project.dao.model.user import User
from project.exceptions import NoResultFound


class UserDAO(BaseDAO):
    def get_by_email(self, email: str):
        try:
            return self.session.query(User).filter(User.email == email).one_or_none()
        except NoResultFound:
            return None

    def create(self, user_d):
        user = User(**user_d)
        self.session.add(user)
        self.session.commit()
        return user

    def update(self, user_d, email):
        self.session.query(User).filter(User.email == email).update(user_d)
        self.session.commit()
