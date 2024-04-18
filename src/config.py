import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URI", "postgresql://backend:backend123@localhost:6432/backend"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
