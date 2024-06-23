FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1

# Install necessary packages
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    python3-pip

WORKDIR /app

COPY backend/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pytsp

COPY backend/ /app/

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "broadcast_server.wsgi:application"]