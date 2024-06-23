FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    tsduck \
    python3-pip

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pytsp pympeg2ts

COPY . /app/

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "broadcast_server.wsgi:application"]