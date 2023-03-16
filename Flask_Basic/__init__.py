from flask import Flask

# __init__.py를 통해 디렉토리 지정


def create_app():
    print('run create_app()')
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'hello world!!!'

    return app.run(debug=True)
