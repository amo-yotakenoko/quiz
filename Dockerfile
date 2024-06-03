FROM python:3.11-bullseye

RUN pip install Flask Flask-SQLAlchemy Flask-Migrate flask-login mysqlclient
RUN pip install Flask
RUN pip install SQLAlchemy
RUN pip install flask_sqlalchemy
RUN pip install flask_migrate
RUN pip install flask_login
RUN pip install MySQLdb
RUN pip install sqlalchemy
RUN pip install mysqlclient

WORKDIR /app
COPY * /app/

EXPOSE 8080

CMD ["python", "app.py"]