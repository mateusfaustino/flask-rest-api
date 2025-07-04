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

## Database migrations

Use `Flask-Migrate` to manage schema changes. Set the `FLASK_APP` variable to
`app:create_app` and run the commands below.

```bash
# Initialise the migrations folder (run once)
flask --app app:create_app db init

# Generate migration scripts after changing the models
flask --app app:create_app db migrate -m "Migration message"

# Apply migrations to the database
flask --app app:create_app db upgrade
```
