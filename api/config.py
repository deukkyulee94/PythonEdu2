import os

class Config:
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', '\xf38\xd1\xa6=\xb5\xf0Q\x00\x15\xa9x\xd5\xf8\x04\xcf')
    JWT_ACCESS_TOKEN_EXPIRES = 60 * 60 * 24  # 24 hours

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
} 