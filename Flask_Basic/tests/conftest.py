import pytest
from Flask_Basic import create_app, db
from Flask_Basic.configs import TestingConfig
from Flask_Basic.models.user import User as UserModel
from Flask_Basic.models.memo import Memo as MemoModel
import sys
import os
import shutil
# import win32file
# import win32con
# import win32api
# import win32process
import psutil

sys.path.append('.')


@pytest.fixture(scope='session')
def user_data():
    yield dict(
        user_id='tester',
        user_name='tester',
        password='tester'
    )

@pytest.fixture(scope='session')
def memo_data() :
    yield dict(
        title='title',
        content='content'
    )


@pytest.fixture(scope='session')
def app(user_data, memo_data):
    app = create_app(TestingConfig())
    with app.app_context():
        db.drop_all()   # db 초기화
        db.create_all()  # db 생성
        user = UserModel(**user_data)
        db.session.add(user)  # db에 값 입력

        db.session.flush()  # user.id 값이 유효하도록 만들기 위함
        memo_data['user_id'] = user.id
        db.session.add(MemoModel(**memo_data))

        db.session.commit()  # db 저장
        # db.session.close()
        yield app
        # 불필요 디비 정리 및 삭제

        # /static/user_images/tester(=user_id)
        path = os.path.join(
            app.static_folder,
            app.config['USER_STATIC_BASE_DIR'],
            'tester'
        )
        shutil.rmtree(path, True)

        db.drop_all()
        # db_path = app.config['SQLALCHEMY_DATABASE_URI'].replace(
        #     'sqlite:///',
        #     ''
        # )
        # pytest_path = app.config['PYTEST_URI'].replace(
        #     'sqlite:///',
        #     ''
        # )

        # if os.path.isfile(db_path):

        # sqlite db를 물고 있는 프로세스 강제 종료 처리 (but, test가 정상 진행되지 않음)
        # for proc in psutil.process_iter():
        #     try:
        #         files = proc.open_files()

        #         for f in files:
        #             if f.path == db_path:
        #                 proc.kill()
        #                 break
        #     except (psutil.NoSuchProcess, psutil.AccessDenied):
        #         pass

        # 파일이 잠금되어 있는 경우 파일 잠금을 해제하는 소스 (but, 잠겨있는 것과는 무관하여 효과 x)
        # handle = win32file.CreateFile(db_path, win32file.GENERIC_READ, 0,
        #                               None, win32con.OPEN_EXISTING, win32file.FILE_ATTRIBUTE_NORMAL, None)

        # try:
        #     win32file.UnlockFile(handle, 0, 0, 0, 0)
        # finally:
        #     win32file.CloseHandle(handle)

        # 파일이 존재하는 경우 삭제 처리 (잔존하는 프로세스가 존재하여 삭제처리 불가)
        # shutil.rmtree(pytest_path)
        # os.remove(db_path)


@pytest.fixture(scope='session')
def client(app, user_data):
    # app = create_app(TestingConfig())

    with app.test_client() as client:
        # NOTE: 세션 입혀기주기
        with client.session_transaction() as session:
            session['user_id'] = user_data['user_id']
            # session['user_id'] = user_data.get('user_id')
        # db.session.close()
        yield client
