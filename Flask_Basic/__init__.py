from flask import Flask
from flask import render_template
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()

# __init__.py를 통해 디렉토리 지정


def create_app():
    print('run create_app()')
    app = Flask(__name__)

    # csrf 토큰을 정상적으로 생성됨
    app.config['SECRET_KEY'] = 'secretkey'

    # 정적파일 캐시 지우기
    if app.config['DEBUG']:
        # 즉, max-age를 1로 변경하여 바로바로 변경되는 것을 확인할 수 있게 해줌
        app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

    ''' CSRF INIT '''
    csrf.init_app(app)

    @app.route('/')
    def index():
        # app.logger.info('RUN Flask Server')
        return render_template('index.html')

    from Flask_Basic.forms.auth_form import LoginForm, RegisterForm

    @app.route('/auth/login')
    def login():
        form = LoginForm()
        return render_template('login.html', form=form)

    @app.route('/auth/register')
    def register():
        form = RegisterForm()
        return render_template('register.html', form=form)

    @app.route('/auth/logout')
    def logout():
        return 'logout'

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
