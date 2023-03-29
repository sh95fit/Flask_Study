from flask import Flask, g
from flask import render_template
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

csrf = CSRFProtect()

# db 세팅
# Mysql 도커 실행
# docker run -d --name testdb -p 3306:3306 -e MYSQL_ROOT_PASSWORD=1234 -e MYSQL_DATABASE=flask_basic  mysql:5.7 --character-set-server=utf8 --collation-server=utf8_general_ci
db = SQLAlchemy()
migrate = Migrate()


# __init__.py를 통해 디렉토리 지정


def create_app(config=None):
    print('run create_app()')
    app = Flask(__name__)

    '''FLASK CONFIGS'''
    from .configs import DevelopmentConfig, ProductionConfig

    if not config:
        if app.config['DEBUG']:
            config = DevelopmentConfig()
        else:
            config = ProductionConfig()

    print('run with : ', config)
    app.config.from_object(config)

    # # csrf 토큰을 정상적으로 생성됨
    # app.config['SECRET_KEY'] = 'secretkey'
    # app.config['SSESSION_COOKIE_NAME'] = 'huns_flask'

    # # DB 연결을 위한 config 설정
    # # pymysql을 추가해주거나 mysqlclient 설치를 통해  No module named 'MySQLdb' 에러 방지
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/flask_basic?charset=utf8'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # app.config['SWAGGER_UI_DOC_EXPANSION'] = 'list'

    # # 정적파일 캐시 지우기
    # if app.config['DEBUG']:
    #     # 즉, max-age를 1로 변경하여 바로바로 변경되는 것을 확인할 수 있게 해줌
    #     app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1
    #     # 디버그 모드에서는 CSRF 에러를 띄우지 않음!
    #     app.config['WTF_CSRF_ENABLED'] = False

    ''' CSRF INIT '''
    csrf.init_app(app)

    '''DB INIT'''
    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith('sqlite'):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)

    '''ROUTES INIT'''
    from Flask_Basic.routes import base_route, auth_route
    app.register_blueprint(base_route.bp)
    app.register_blueprint(auth_route.bp)

    '''RESTX INIT'''
    from Flask_Basic.apis import blueprint as api
    app.register_blueprint(api)

    ''' REQUEST HOOK'''
    @app.before_request
    def before_request():
        g.db = db.session

    @app.teardown_request
    def teardown_request(exception):
        if hasattr(g, 'db'):
            g.db.close()

    # @app.route('/')
    # def index():
    #     # app.logger.info('RUN Flask Server')
    #     return render_template('index.html')

    from Flask_Basic.forms.auth_form import LoginForm, RegisterForm

    # @app.route('/auth/login', methods=['GET', 'POST'])
    # def login():
    #     form = LoginForm()
    #     # validate_on_submit : POST, validate OK!임을 나타내는 함수
    #     if form.validate_on_submit():
    #         # TODO
    #         # 1) 유저 조회
    #         # 2) 유저가 이미 존재하는지 체크
    #         # 3) 패스워드 정합 확인
    #         # 4) 로그인 유지(세션)
    #         user_id = form.data.get('user_id')
    #         password = form.data.get('password')
    #         return f'{user_id}, {password}'
    #     else:
    #         # TODO: ERROR
    #         pass
    #     return render_template('login.html', form=form)

    # @app.route('/auth/register', methods=['GET', 'POST'])
    # def register():
    #     form = RegisterForm()
    #     if form.validate_on_submit():
    #         # TODO
    #         # 1) 유저 조회
    #         # 2) 유저가 이미 존재하는지 체크
    #         # 3) 없으면 유저 생성
    #         # 4) 로그인 유지(세션)
    #         user_id = form.data.get('user_id')
    #         user_name = form.data.get('user_name')
    #         password = form.data.get('password')
    #         repassword = form.data.get('repassword')
    #         return f'{user_id}, {user_name}, {password}, {repassword}'
    #     else:
    #         # TODO: ERROR
    #         pass
    #     return render_template('register.html', form=form)

    # @app.route('/auth/logout')
    # def logout():
    #     return 'logout'

    @app.errorhandler(404)
    def page_404(error):
        return render_template('/404.html')

    # ''' Routing Practice'''
    # from flask import jsonify, redirect, url_for
    # from markupsafe import escape

    # @app.route('/test/name/<name>')
    # def name(name):
    #     return f'Name is {name}, {escape(type(name))}'

    # @app.route('/test/id/<int:id>')
    # def id(id):
    #     return "ID : %d" % id

    # @app.route('/test/path/<path:subpath>')
    # def path(subpath):
    #     return subpath

    # @app.route('/test/json')
    # def json():
    #     return jsonify({'hello': 'flask'})

    # @app.route('/test/redirect/<path:subpath>')
    # def redirect_url(subpath):
    #     return redirect(subpath)

    # @app.route('/test/urlfor/<path:subpath>')
    # def urlfor(subpath):
    #     return redirect(url_for('path', subpath=subpath))

    # ''' Request Hook'''
    # from flask import g, current_app

    # @app.before_first_request
    # def before_first_request():
    #     app.logger.info('BEFORE_FIRST_REQUEST')

    # @app.before_request
    # def before_request():
    #     g.test = True
    #     app.logger.info('BEFORE_REQUEST')

    # @app.after_request
    # def after_request(response):
    #     app.logger.info(f'g.test:{g.test}')
    #     app.logger.info(f'current_app.config:{current_app.config}')
    #     app.logger.info('AFTER_REQUEST')
    #     return response

    # @app.teardown_request
    # def teardown_request(exception):
    #     app.logger.info('TEARDOWN_REQUEST')

    # @app.teardown_appcontext
    # def teardown_appcontext(exception):
    #     app.logger.info('TEARDOWN_CONTEXT')

    # '''Method'''
    # from flask import request

    # def on_json_loading_failed_return_dict(e):
    #     return {}

    # @app.route('/test/method/<id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
    # def method_test(id):
    #     request.on_json_loading_failed = on_json_loading_failed_return_dict

    #     return jsonify({
    #         'request.method': request.method,
    #         "request.args": request.args,
    #         "request.form": request.form,
    #         "request.json": request.json,
    #     })

    # return app.run(debug=True)
    return app
