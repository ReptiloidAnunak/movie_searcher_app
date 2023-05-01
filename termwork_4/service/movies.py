from dao.movies import MovieDAO

class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_all(self):
        return self.dao.get_all()

    def get_all_paginated(self, page):
        return self.dao.get_all_paginated(page)

    def get_new_paginated(self, page):
        return self.dao.get_new_paginated(page)

    def get_by_genre_id(self, gid):
        return self.dao.get_by_genre_id(gid)

    def get_by_director_id(self, did):
        return self.dao.get_by_director_id(did)

    def get_by_year(self, year):
        return self.dao.get_by_year(year)

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        self.dao.update(data)
        return self.dao

    def delete(self, mid):\
        return self.dao.delete(mid)