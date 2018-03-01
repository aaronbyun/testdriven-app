class BaseConfig:
    DEBUG = False
    TESTING = False

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class TestingConfig(BaseConfig):
    DEBUG = True
    TESTING = True

class ProdConfig(BaseConfig):
    DEBUG = False