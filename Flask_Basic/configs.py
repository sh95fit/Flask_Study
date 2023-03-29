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


class ProductionConfig(DevelopmentConfig):
    pass
