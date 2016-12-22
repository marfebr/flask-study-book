class Config(object):
    SECRET_KEY = '736670cb10a600b695a55839ca3a5aa54a7d7356cdef815d2ad6e19a2031182b'
    RECAPTCHA_PUBLIC_KEY = "6LeRZA8UAAAAADI4j15DFVF4eZ60CyZ--BD4y9-u"
    RECAPTCHA_PRIVATE_KEY = '6LeRZA8UAAAAAKkZ7tSEgvrqG-WA44gRXAyhet-r'


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite://../database.db'


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../database.db'
