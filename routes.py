# routes.py
from flask import Blueprint, jsonify

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return jsonify({'message': '¡Bienvenido a la API de la biblioteca!'})
