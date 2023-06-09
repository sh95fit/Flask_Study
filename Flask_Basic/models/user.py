from Flask_Basic import db
from sqlalchemy import func

# 도커 실행 관련
'''
docker run -d --name testdb -p 3306:3306 -e MYSQL_DATABASE=flask_test -e MYSQL_ROOT_PASSWORD=1234 mysql:5.7 --character-set-server=utf8 --collation-server=utf8_general_ci
'''


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(20), unique=True, nullable=False)
    user_name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    # server_default : column 추가 시 기존에 값이 없는 테이블들에 값을 채워줌 <-> default : 값이 없는 테이블들의 값을 채워주지 않음
    created_at = db.Column(db.DateTime(), server_default=func.now())

    @classmethod
    def find_one_by_user_id(cls, user_id):
        return User.query.filter_by(user_id=user_id).first()


# flask shell 활용
# DB insert
'''
ex>
db.session.add(User(user_id='admin', user_name='KIM', password='1234')
commit을 해줘야만 실제 DB에 저장된다!
db.session.commit()
'''
# DB select
'''
ex> filter_by를 통해 where 조건 주기
User.query.filter_by(user_name='KIM').first()

ex> ~로 끝나는 값을 포함하는 조건 주기
User.query.filter(User.user_name.endswith('M')).first()


이외 order_by, limit(x), get(x) 등 다양한 쿼리 활용 가능!
'''
