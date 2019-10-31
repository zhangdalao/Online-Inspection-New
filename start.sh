#!/bin/ash
nohup celery -A src.mainProgram.run.celery worker -B -l info &
nohup python -m  http.server 2>1 &
nginx
gunicorn -c unicorn.py src.mainProgram.run_server:app