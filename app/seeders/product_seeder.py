"""Utility to seed the database with example menswear products."""

from app import db, create_app
from app.models.product import Product


PRODUCTS = [
    {"name": "Camisa Polo Classic", "price": 89.90},
    {"name": "Camisa Social Slim", "price": 129.90},
    {"name": "Camiseta Estampa Urbana", "price": 59.90},
    {"name": "Bermuda Jeans Azul", "price": 99.90},
    {"name": "Calça Chino Bege", "price": 149.90},
    {"name": "Jaqueta Corta Vento", "price": 199.90},
    {"name": "Jaqueta Jeans Masculina", "price": 219.90},
    {"name": "Blazer Casual Preto", "price": 249.90},
    {"name": "Suéter Gola V", "price": 109.90},
    {"name": "Cueca Boxer 3 unidades", "price": 69.90},
    {"name": "Tênis Casual Couro", "price": 299.90},
    {"name": "Mocassim Marrom", "price": 189.90},
    {"name": "Cinto Couro Preto", "price": 79.90},
    {"name": "Meia Cano Médio", "price": 25.90},
    {"name": "Boné Aba Curva", "price": 49.90},
    {"name": "Relógio Esportivo Digital", "price": 349.90},
    {"name": "Óculos de Sol Aviador", "price": 199.90},
    {"name": "Mochila Casual", "price": 159.90},
    {"name": "Carteira de Couro", "price": 89.90},
    {"name": "Sandália Slide", "price": 59.90},
]


def seed_products():
    """Persist the predefined products to the database."""
    app = create_app()
    with app.app_context():
        for item in PRODUCTS:
            product = Product(name=item["name"], price=item["price"])
            db.session.add(product)
        db.session.commit()


if __name__ == "__main__":
    seed_products()
