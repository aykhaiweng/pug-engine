#!/bin/sh

python3 pugengine/manage.py migrate
python3 pugengine/manage.py runserver 0.0.0.0:8000