import os


class Config:
    DEBUG = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    FLASK_SECRET_KEY = os.getenv(
        "FLASK_SECRET_KEY", "No Secret key, did u forget to source .env file?"
    )
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    DEBUG = True
    TOKEN_EXP_TIME = 24


AppConfig = DevelopmentConfig
