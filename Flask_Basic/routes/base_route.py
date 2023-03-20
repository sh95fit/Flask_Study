from flask import Blueprint, render_template

NAME = 'base'

bp = Blueprint(NAME, __name__)


@bp.route('/')
def index():
    # app.logger.info('RUN Flask Server')
    return render_template('index.html')
