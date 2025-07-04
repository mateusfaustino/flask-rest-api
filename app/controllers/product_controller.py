from flask import Blueprint, jsonify, request
from sqlalchemy import or_
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
