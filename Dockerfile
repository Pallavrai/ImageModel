FROM python:3.11-slim-buster

RUN apt-get update && apt-get upgrade -y

ENV APP_ROOT /app
WORKDIR ${APP_ROOT}

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . ${APP_ROOT}

CMD ["gunicorn", "-c", "gunicorn.conf.py", "config.wsgi:application"]
