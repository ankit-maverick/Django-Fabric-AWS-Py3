#!/bin/bash
# Starts the Gunicorn server
set -e

# Activate the virtualenv for this project
%(ACTIVATE)s

# Start gunicorn going
exec gunicorn %(PROJECT_NAME)s.wsgi:application --chdir=/home/ubuntu/webapps/%(PROJECT_NAME)s/%(PROJECT_NAME)s/ -c %(PROJECT_PATH)s/gunicorn.conf.py 