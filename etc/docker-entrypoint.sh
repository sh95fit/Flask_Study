#!/bin/bash

set -e

flask db upgrade
gunicorn --bind :9000 --workers 2 --threads 8 --access-logfile - 'Flask_Basic:create_app()'