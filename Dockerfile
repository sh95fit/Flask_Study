FROM python:3.8

# root 권한
# 유저 추가 (패스워드를 입력하지 않아도 되도록 설정 + 홈디렉토리 자동생성)
RUN adduser --disabled-password python

# 유저 전환 (root -> 생성 유저)
USER python

# 의존성 패키지 복사
COPY ./requirements.txt /tmp/requirements.txt

# python 의존성 패키지 설치 + gunicorn 설치
RUN python -m pip install --upgrade pip
RUN pip install --user -r /tmp/requirements.txt
RUN pip install --user gunicorn==20.1.0

# 프로젝트 소스 복사
COPY --chown=python:python ./ /var/www/Flask_Basic

# 복사한 프로젝트 디렉토리로 이동
WORKDIR /var/www/Flask_Basic

# 설치한 패키지 명령어를 사용하기 위해 환경변수 등록
ENV PATH="/home/python/.local/bin:${PATH}"

# etc/docker-entrypoint.sh 실행을 위한 권한 변경
RUN chmod +x ./etc/docker-entrypoint.sh

# 9000 포트 노출
EXPOSE 9000

# gunicorn 실행 (etc/docker-entrypoint.sh로 명령어를 한번에 실행)
# CMD gunicorn --bind :9000 --workers 2 --threads 8 'Flask_Basic:create_app()'