from flask import Blueprint, jsonify

home_bp = Blueprint('home', __name__)


@home_bp.route('/')
def index():
    """Return a simple greeting."""
    return jsonify(message="Hello World")
