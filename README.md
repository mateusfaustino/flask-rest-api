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

## Listing products

The `/products` endpoint supports optional pagination and filtering. Use the
`page` and `per_page` query parameters to control pagination (defaults are `1`
and `10`). Filtering by `name`, `min_price` and `max_price` can also be applied
alongside a free text `search` that checks the product `id` and `name` fields.

## Retrieving a single product

Use `GET /products/<id>` to fetch the details for a specific product. The
response body will contain the product `id`, `name` and `price`.

## Creating a product

Send a JSON payload to `POST /products` with the fields `name` and `price`:

```bash
curl -X POST http://localhost:5000/products \
  -H "Content-Type: application/json" \
  -d '{"name": "New Shirt", "price": 99.90}'
```

The response will include the created product with its generated `id`.

## Updating a product

Send a JSON payload to `PUT /products/<id>` with any fields you wish to change.
Omitted fields will keep their existing values.

```bash
curl -X PUT http://localhost:5000/products/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "Updated Shirt", "price": 79.90}'
```

## Deleting a product

Send a `DELETE` request to `/products/<id>` specifying the product identifier in
the URL. A successful deletion will return status code `204` with an empty
response body.

```bash
curl -X DELETE http://localhost:5000/products/1
```
