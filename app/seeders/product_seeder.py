import random
import string
from app import db, create_app
from app.models.product import Product


def random_name(length=10):
    return ''.join(random.choices(string.ascii_letters, k=length))


def random_price():
    return round(random.uniform(1.0, 100.0), 2)


def seed_products(quantity=20):
    """Seed the database with random products."""
    app = create_app()
    with app.app_context():
        for _ in range(quantity):
            product = Product(name=random_name(), price=random_price())
            db.session.add(product)
        db.session.commit()


if __name__ == "__main__":
    seed_products()
