from dataclasses import dataclass
from flask import Blueprint, render_template, redirect, url_for, flash, session, request

from Flask_Basic.forms.auth_form import LoginForm, RegisterForm

from werkzeug import security

NAME = 'auth'

bp = Blueprint(NAME, __name__, url_prefix='/auth')


'''only for testing'''
USERS = []


@dataclass
class User:
    ''' 기본 클래스 형태를 간소화한 것이 dataclass이다
        class User:
            def __init__(self, user_id, user_name, password) :
                self.user_id = user_id
                self.user_name = user_name
                self.password = password
    '''
    user_id: str
    user_name: str
    password: str


USERS.append(User('test_admin', 'admin',
             security.generate_password_hash('1234')))
USERS.append(User('test_user', 'user', security.generate_password_hash('1234')))
USERS.append(User('test_developer', 'developer',
             security.generate_password_hash('1234')))


@bp.route('/')
def index():
    return redirect(url_for(f'{NAME}.login'))


@bp.route('/login', methods=['GET', 'POST'])
def login():
    # flash('login ERROR!') # 테스트용
    form = LoginForm()
    # validate_on_submit : POST, validate OK!임을 나타내는 함수
    if form.validate_on_submit():
        # TODO
        # 1) 유저 조회
        # 2) 유저가 이미 존재하는지 체크s
        # 3) 패스워드 정합 확인
        # 4) 로그인 유지(세션)

        # 메모리에 저장된 유저 정보 가져오기

        user_id = form.data.get('user_id')
        password = form.data.get('password')

        user = [user for user in USERS if user.user_id == user_id]
        if user:
            user = user[0]
            if not security.check_password_hash(user.password, password):
                flash('Password is not valid.')
            else:
                session['user_id'] = user_id
                return redirect(url_for('base.index'))

        else:
            flash('User ID is not exists.')
        # return f'{user_id}, {password}'
    else:
        flash_form_errors(form)
    return render_template(f'{NAME}/login.html', form=form)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    # flash('register ERROR!')  # 테스트용
    form = RegisterForm()
    if form.validate_on_submit():
        # TODO
        # 1) 유저 조회
        # 2) 유저가 이미 존재하는지 체크
        # 3) 없으면 유저 생성
        # 4) 로그인 유지(세션)
        user_id = form.data.get('user_id')
        user_name = form.data.get('user_name')
        password = form.data.get('password')
        repassword = form.data.get('repassword')

        user = [user for user in USERS if user.user_id == user_id]
        if user:
            flash('User ID is already exists.')
            return redirect(request.path)
        else:
            USERS.append(
                User(
                    user_id=user_id,
                    user_name=user_name,
                    password=security.generate_password_hash(password),
                )
            )
            session['user_id'] = user_id
            return redirect(url_for('base.index'))

        return f'{user_id}, {user_name}, {password}, {repassword}'
    else:
        flash_form_errors(form)
    return render_template(f'{NAME}/register.html', form=form)


@bp.route('/logout')
def logout():
    session.pop('user_id', None)
    # return 'logout'
    return redirect(url_for(f'{NAME}.login'))


def flash_form_errors(form):
    for _, errors in form.errors.items():
        for e in errors:
            flash(e)
