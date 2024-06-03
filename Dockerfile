FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir \
    Flask \
    Flask-SQLAlchemy \
    Flask-Migrate \
    Flask-Login \
    python-dotenv \
    watchdog

EXPOSE 8080

CMD ["python", "app.py"]
