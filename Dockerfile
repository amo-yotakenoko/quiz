FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["flask", "--app", "flask_app", "run", "--debug", "--host", "0.0.0.0"]
