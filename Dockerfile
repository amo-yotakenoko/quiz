FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY flask_app ./flask_app
COPY migrations ./migrations
RUN flask --app flask_app db upgrade c8194b0a0911

EXPOSE 5000

CMD ["flask", "--app", "flask_app", "run", "--debug", "--host", "0.0.0.0"]
