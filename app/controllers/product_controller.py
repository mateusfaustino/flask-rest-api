from flask import Blueprint, jsonify
from app.models import Product

product_bp = Blueprint('products', __name__, url_prefix='/products')


@product_bp.route('/', methods=['GET'])
def list_products():
    """Return a list of all products."""
    products = Product.query.all()
    result = [
        {
            "id": product.id,
            "name": product.name,
            "price": float(product.price),
        }
        for product in products
    ]
    return jsonify(products=result)
