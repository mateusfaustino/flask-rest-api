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
`app:create_app` and ensure the models module is imported inside the application
factory (for example `from . import models`). With that in place, run the
commands below.

```bash
# Initialise the migrations folder (run once)
flask --app app:create_app db init

# Generate migration scripts after changing the models
flask --app app:create_app db migrate -m "Migration message"

# Apply migrations to the database
flask --app app:create_app db upgrade
```

## Seeding sample data

Run the `seed.py` script to populate the database with random products. If the
containers are already running you can execute:

```bash
docker compose exec app python seed.py
```

Alternatively, start a one-off container to run the script:

```bash
docker compose run --rm app python seed.py
```

If running the project without Docker, simply call:

```bash
python seed.py
```
