FROM python:3.8.0-alpine3.10

# install system dependencies
RUN apk add gcc libc-dev linux-headers

RUN pip install pipenv

# set up project
COPY . /app
WORKDIR /app

RUN pipenv install --system --deploy --ignore-pipfile

# run
EXPOSE 80
CMD gunicorn -b 0.0.0.0:80 main:app
