FROM python:3.9-slim-buster
MAINTAINER "Salma Doma"

RUN mkdir /app
WORKDIR /app

COPY ./services/scoring /app
COPY ./packaging/docker/scoring/docker-entrypoint.sh /

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r ./requirements.txt

RUN adduser --disabled-password app_user
RUN chown -R app_user:app_user /app/

USER app_user

ENTRYPOINT ["/docker-entrypoint.sh"]