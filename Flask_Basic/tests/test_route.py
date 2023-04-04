# import pytest
# from Flask_Basic import create_app
# from Flask_Basic.configs import TestingConfig
# import sys
# sys.path.append('.')


# @pytest.fixture
# def client():
#     app = create_app(TestingConfig())

#     with app.test_client() as client:
#         yield client


def test_auth(client):

    r = client.get(
        '/auth/',
        follow_redirects=True
    )
    assert r.status_code == 200

    r = client.get(
        '/auth/register',
        follow_redirects=True
    )
    assert r.status_code == 200

    r = client.get(
        '/auth/login',
        follow_redirects=True
    )
    assert r.status_code == 200

    r = client.get(
        '/auth/logout',
        follow_redirects=True
    )
    assert r.status_code == 200


def test_base(client):
    r = client.get(
        '/',
        follow_redirects=True
    )
    assert r.status_code == 200

# pytest-watch 활용  ptw 입력 시 pytest -sv를 입력하지 않아도 수시로 test 진행
