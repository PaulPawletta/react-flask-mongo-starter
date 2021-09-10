class BaseConfig:
    HOST = "0.0.0.0"
    PORT = 5000
    DEBUG = False

class Development(BaseConfig):
    MONGODB_URL = "mongodb://localhost"
    DEBUG = True

class Production(BaseConfig):
    pass