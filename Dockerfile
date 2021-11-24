FROM python:3.9

WORKDIR /application

COPY ./requirements.txt /application/requirements.txt
RUN pip install -r requirements.txt
COPY . /app


CMD python manage.py runserver 0.0.0.0:8080