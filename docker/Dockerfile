FROM python:3.7

MAINTAINER Sammy Kariuki

EXPOSE 8000

WORKDIR /app

COPY Pipfile /app
COPY Pipfile.lock /app

RUN pip install pipenv && pipenv install

ENTRYPOINT ["python", "manage.py", "runserver"]