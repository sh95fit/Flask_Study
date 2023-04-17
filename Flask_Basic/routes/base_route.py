from flask import Blueprint, render_template, g, redirect, url_for

NAME = 'base'

bp = Blueprint(NAME, __name__)


@bp.route('/')
def index():
    # app.logger.info('RUN Flask Server')
    # 전처리기(로그아웃 상태에서는 메인페이지 진입이 불가하도록 제한)
    if not g.user:
        return redirect(url_for('auth.login'))
    return render_template('index.html')
