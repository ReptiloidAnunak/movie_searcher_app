from dao.models.director import Director
from config import Config

class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, did):
        return self.session.query(Director).get(did)

    def get_all(self):
        return self.session.query(Director).all()

    def get_all_paginated(self, page):
        pagination = Director.query.order_by(Director.name.asc()).paginate(
            page, per_page=Config.FLASKY_POSTS_PER_PAGE, error_out=False)
        directors = pagination.items
        return directors

    def create(self, data):
        director = Director(**data)
        self.session.add(director)
        self.session.commit()
        return director

    def update(self, data):
        did = data.get("id")
        director = self.get_one(did)
        director.name = data.get("name")
        self.session.add(director)
        self.session.commit()
        return director

    def delete(self, did):
        director = self.get_one(did)
        self.session.delete(director)
        self.session.commit()