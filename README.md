# Flask REST API

Simple REST API using Flask 2.3 with MySQL and Docker Compose.

## Requirements

- Docker
- Docker Compose

## Setup

```bash
# Build and start the containers
docker compose up --build
```

The API will be available on `http://localhost:5000/` returning a JSON message.

phpMyAdmin will be accessible at `http://localhost:8080/`.

The MySQL server listens on host port `3308`.
