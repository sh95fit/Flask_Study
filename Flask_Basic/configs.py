import os
BASE_PATH = os.path.dirname(os.path.abspath(__file__))


class Config:
    '''Flask Config'''
    SECRET_KEY = 'secretkey'
    SSESSION_COOKIE_NAME = 'huns_flask'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@localhost/flask_basic?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER_UI_DOC_EXPANSION = 'list'
    USER_STATIC_BASE_DIR = 'user_images'

    def __init__(self) :
        db_env = os.environ.get('SQLALCHEMY_DATABASE_URI')
        if db_env :
            self.SQLALCHEMY_DATABASE_URI = db_env

    # 다른 방법
    # @property
    # def SSQLALCHEMY_DATABASE_URI(self) :
    #     db_env = os.environ.get('SQLALCHEMY_DATABASE_URI')
    #     if db_env :
    #         return db_env
    #     return self.SQLALCHEMY_DATABASE_URI


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


class ProductionConfig(Config):
    pass
