FROM python:3.9.5-alpine
WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
COPY ./scrypt.sh /usr/src/app/scrypt.sh
COPY . /usr/src/app/
ENTRYPOINT ["/usr/src/app/scrypt.sh"]