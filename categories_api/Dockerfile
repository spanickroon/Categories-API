FROM python:3.8.5-alpine

WORKDIR /usr/src/categories_api

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["/usr/src/categories_api/entrypoint.sh"]