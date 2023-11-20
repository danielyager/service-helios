import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # To be used later. Still a work in progress.
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or ('sqlite:///' + os.path.join(basedir, 'helios_app.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False