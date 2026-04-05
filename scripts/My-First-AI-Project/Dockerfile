# syntax=docker/dockerfile:1
FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt /app/requirements.txt
RUN python -m pip install --no-cache-dir -r /app/requirements.txt

COPY bot.py /app/bot.py

# Keep all bot-written files inside /app so the container is self-contained.
CMD ["python", "/app/bot.py", "--once"]

