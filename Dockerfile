# Build everything in first stage
FROM python:3.8-alpine

WORKDIR /install

COPY requirements.txt .

# Requirements
RUN pip install -r requirements.txt

# Copy in build from previous stage
COPY web web
COPY scripts scripts

# Docker specific environment vars
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# server.py needs this to run in prod mode
ENV GATEWAY_INTERFACE 1

# Static files (index) port
EXPOSE 5666
# API port
EXPOSE 5667

ENTRYPOINT ./run.sh 5666 5667

