import os

class Config:
    # Flask
    ENV = 'development'
    DEBUG = False
    TESTING = True
    BUNDLE_ERRORS = True
    PROPAGATE_EXCEPTIONS = True
    SECRET_KEY = os.getenv('JWT_SECRET_KEY', '\xf38\xd1\xa6=\xb5\xf0Q\x00\x15\xa9x\xd5\xf8\x04\xcf')

    # JWT
    JWT_SECRET_KEY = SECRET_KEY
    JWT_ACCESS_TOKEN_EXPIRES = 60 * 60 * 24  # 24 hours

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    ENV = 'product'
    TESTING = False

config_object = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
} 