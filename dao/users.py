from dao.model.users import Users


class UsersDAO:
    def __init__(self, session):
        self.session = session

    def get_user_by_username(self, username):
        user = Users.query.filter(Users.username == username).first()
        return user

    def create_user(self, user):
        user = Users(**user)
        self.session.add(user)
        self.session.commit()
        return user
