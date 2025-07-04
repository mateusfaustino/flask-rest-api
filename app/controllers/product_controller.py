from flask import Blueprint, jsonify, request, abort
from sqlalchemy import or_
from app import db
from app.models import Product

product_bp = Blueprint("products", __name__, url_prefix="/products")


@product_bp.route("/", methods=["GET"])
def list_products():
    """List products with optional pagination and filtering.
    ---
    parameters:
      - name: page
        in: query
        type: integer
        required: false
        description: Page number
        default: 1
      - name: per_page
        in: query
        type: integer
        required: false
        description: Items per page
        default: 10
      - name: search
        in: query
        type: string
        required: false
        description: Search by id or name
      - name: name
        in: query
        type: string
        required: false
        description: Filter by product name
      - name: min_price
        in: query
        type: number
        required: false
        description: Minimum price
      - name: max_price
        in: query
        type: number
        required: false
        description: Maximum price
    responses:
      200:
        description: Paginated list of products
        content:
          application/json:
            schema:
              type: object
              properties:
                items:
                  type: array
                  items:
                    $ref: '#/components/schemas/Product'
                total:
                  type: integer
                page:
                  type: integer
                pages:
                  type: integer
                per_page:
                  type: integer
    """
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
    """Create a new product.
    ---
    requestBody:
      required: true
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Product'
    responses:
      201:
        description: Product created
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Product'
      400:
        description: Validation error
    """
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
    """Retrieve a single product by its ID.
    ---
    parameters:
      - name: product_id
        in: path
        type: integer
        required: true
        description: Identifier of the product
    responses:
      200:
        description: Product details
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Product'
      404:
        description: Product not found
    """
    product = Product.query.get(product_id)
    if product is None:
        abort(404, description="Product not found")

    return jsonify(id=product.id, name=product.name, price=float(product.price))


@product_bp.route("/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    """Update an existing product.
    ---
    parameters:
      - name: product_id
        in: path
        type: integer
        required: true
        description: Identifier of the product
    requestBody:
      required: true
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Product'
    responses:
      200:
        description: Updated product
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Product'
      404:
        description: Product not found
    """
    product = Product.query.get(product_id)
    if product is None:
        abort(404, description="Product not found")

    data = request.get_json() or {}

    name = data.get("name")
    price = data.get("price")

    if name is not None:
        product.name = name

    if price is not None:
        product.price = price

    db.session.commit()

    return jsonify(id=product.id, name=product.name, price=float(product.price))


@product_bp.route("/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    """Delete a product by its ID.
    ---
    parameters:
      - name: product_id
        in: path
        type: integer
        required: true
        description: Identifier of the product
    responses:
      204:
        description: Product deleted
      404:
        description: Product not found
    """
    product = Product.query.get(product_id)
    if product is None:
        abort(404, description="Product not found")

    db.session.delete(product)
    db.session.commit()

    return "", 204
