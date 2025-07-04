"""Simple script to seed the database with sample products."""

from app.seeders import seed_products

if __name__ == "__main__":
    seed_products()
