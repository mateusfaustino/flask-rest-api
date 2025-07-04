from flask import Blueprint, jsonify

home_bp = Blueprint('home', __name__)


@home_bp.route('/')
def index():
    """Return a simple greeting.
    ---
    responses:
      200:
        description: API status message
        schema:
          type: object
          properties:
            message:
              type: string
              example: Hello World
    """
    return jsonify(message="Hello World")
