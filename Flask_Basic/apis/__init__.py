from flask import Blueprint, g, abort
from flask_restx import Api
from .user import ns as UserNamespace
from .memo import ns as MemoNamespace

from functools import wraps


# 전처리기 만들기(로그아웃 상태에서는 API DOCS를 열지 못하도록 제한)
def check_session(func):
    @wraps(func)
    def __wrapper(*args, **kwargs):
        if not g.user:
            abort(401)  # 에러를 표출해줌
        return func(*args, **kwargs)
    return __wrapper


blueprint = Blueprint(
    'api',
    __name__,
    url_prefix='/api'
)

api = Api(
    blueprint,
    title="Hun's Flask API",
    version='1.0',
    doc='/docs',
    decorators=[check_session],
    description="Hun's Flask API Docs"
)


# TODO : add namespace to Blueprint
api.add_namespace(UserNamespace)
api.add_namespace(MemoNamespace)
