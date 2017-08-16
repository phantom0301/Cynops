import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = '123'
    WTF_CSRF_SECRET_KEY = '123'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'database.db')

    @staticmethod
    def init_app(app):
        pass

config = {
    'default':Config
}