from flask import Blueprint, jsonify, request, abort
from sqlalchemy import or_
from app import db
from app.models import Product

product_bp = Blueprint("products", __name__, url_prefix="/products")


@product_bp.route("/", methods=["GET"])
def list_products():
    """List products with optional pagination and filtering."""
    page = request.args.get("page", default=1, type=int)
    per_page = request.args.get("per_page", default=10, type=int)

    search = request.args.get("search")
    name = request.args.get("name")
    min_price = request.args.get("min_price", type=float)
    max_price = request.args.get("max_price", type=float)

    query = Product.query

    if search:
        like = f"%{search}%"
        try:
            search_id = int(search)
            query = query.filter(or_(Product.name.ilike(like), Product.id == search_id))
        except ValueError:
            query = query.filter(Product.name.ilike(like))

    if name:
        query = query.filter(Product.name.ilike(f"%{name}%"))

    if min_price is not None:
        query = query.filter(Product.price >= min_price)

    if max_price is not None:
        query = query.filter(Product.price <= max_price)

    pagination = query.paginate(page=page, per_page=per_page, error_out=False)

    result = [
        {
            "id": product.id,
            "name": product.name,
            "price": float(product.price),
        }
        for product in pagination.items
    ]

    return jsonify(
        items=result,
        total=pagination.total,
        page=pagination.page,
        pages=pagination.pages,
        per_page=pagination.per_page,
    )


@product_bp.route("/", methods=["POST"])
def create_product():
    """Create a new product."""
    data = request.get_json() or {}

    name = data.get("name")
    price = data.get("price")

    if name is None or price is None:
        abort(400, description="'name' and 'price' are required fields")

    product = Product(name=name, price=price)
    db.session.add(product)
    db.session.commit()

    return (
        jsonify(id=product.id, name=product.name, price=float(product.price)),
        201,
    )


@product_bp.route("/<int:product_id>", methods=["GET"])
def get_product(product_id):
    """Retrieve a single product by its ID."""
    product = Product.query.get(product_id)
    if product is None:
        abort(404, description="Product not found")

    return jsonify(id=product.id, name=product.name, price=float(product.price))
