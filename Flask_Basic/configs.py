import os
BASE_PATH = os.path.dirname(os.path.abspath(__file__))


class Config:
    '''Flask Config'''
    SECRET_KEY = 'secretkey'
    SSESSION_COOKIE_NAME = 'huns_flask'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@localhost/flask_basic?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER_UI_DOC_EXPANSION = 'list'


class DevelopmentConfig(Config):
    '''Flask Config for dev'''
    DEBUG = True
    SEND_FILE_MAX_AGE_DEFAULT = 1
    # Front-end 호출 시 처리
    WTF_CSRF_ENABLED = False


class TestingConfig(DevelopmentConfig):
    __test__ = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BASE_PATH, "dummy_db/sqlite_test.db")}'
    PYTEST_URI = f'sqlite:///{BASE_PATH + "/dummy_db"}'


class ProductionConfig(DevelopmentConfig):
    pass
