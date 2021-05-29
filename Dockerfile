############################################################
# Default build stage
############################################################
FROM python:3.9-alpine as base

LABEL maintainer="aykhaiweng@gmail.com"

ENV PYTHONBUFFERED 1

COPY . /opt/pug-engine/
WORKDIR /opt/pug-engine/

# System depedencies for Python
RUN apk add --update --virtual \
    build-essential \
    openssl-dev \
    libc-dev python3-dev gcc \
    libffi-dev musl-dev cargo \
    g++ \
    postgresql-dev

RUN pip install -U pip
RUN pip install pipenv


############################################################
# Primary stage
############################################################
FROM base as primary
RUN pipenv lock --requirements > /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
CMD ["python3", "manage.py", "migrate", "&&", "python3", "manage.py", "runserver", "0.0.0.0:8000"]


############################################################
# Dev stage
############################################################
FROM primary as dev
RUN pipenv lock --requirements --dev-only > /tmp/requirements-dev.txt
RUN pip install -r /tmp/requirements-dev.txt
CMD ["python3", "manage.py", "migrate", "&&", "python3", "manage.py", "runserver", "0.0.0.0:8000"]