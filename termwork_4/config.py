class Config(object):
    DEBUG = True
    JWT_SECRET = 'nopasanada'
    JWT_ALGO = 'HS256'
    PWD_SALT = b'bol7do'
    PWD_ITERATIONS = 100000
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./project.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False