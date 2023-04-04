import pytest
from Flask_Basic import create_app, db
from Flask_Basic.configs import TestingConfig
from Flask_Basic.models.user import User as UserModel
import sys
sys.path.append('.')


@pytest.fixture
def user_data():
    yield dict(
        user_id='tester',
        user_name='tester',
        password='tester'
    )


@pytest.fixture
def app(user_data):
    app = create_app(TestingConfig())
    with app.app_context():
        db.drop_all()   # db 초기화
        db.create_all()  # db 생성
        db.session.add(UserModel(**user_data))  # db에 값 입력
        db.session.commit()  # db 저장
    yield app


@pytest.fixture
def client(app):
    # app = create_app(TestingConfig())

    with app.test_client() as client:
        yield client
