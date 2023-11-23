FROM python:3.11-slim

ENV APP_HOME /app
WORKDIR $APP_HOME

ENV PYTHONUNBUFFERED 1

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 2 --timeout 30 rioaeroclub.wsgi:application