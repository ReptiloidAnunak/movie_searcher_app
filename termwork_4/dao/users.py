from dao.models.user import User
from utils import generate_pw_hash

class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def get_all(self):
        return self.session.query(User).all()

    def create(self, data):
        new_user = User(**data)
        pwd = new_user.password
        new_user.password = generate_pw_hash(pwd)
        self.session.add(new_user)
        self.session.commit()
        return new_user

    def update_partial(self, data):
        uid = data.get("id")
        user = self.get_one(uid)
        if "name" in data:
            name = data.get("name")
            user.name = name
        if "surname" in data:
            surname = data.get("surname")
            user.surname = surname
        if "favorite_genre" in data:
            favorite_genre = data.get("favorite_genre")
            user.favorite_genre = favorite_genre
        self.session.add(user)
        self.session.commit()
        return user

    def update_password(self, data):
        uid = data.get("id")
        user = self.get_one(uid)
        password_1 = data.get('password_1', None)
        password_2 = data.get('password_2', None)
        if user.compare_password(password_1) == True:
            user.password = generate_pw_hash(password_2)
            self.session.add(user)
            self.session.commit()
            return user
        else:
            return False


    def delete(self, uid):
        user = self.get_one(uid)
        self.session.delete(user)
        self.session.commit()