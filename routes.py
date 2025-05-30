# routes.py
from flask import Blueprint, jsonify, request
from models import db, Libro

bp = Blueprint('routes', __name__)

# 1. Listar todos los libros (GET /libros)
@bp.route('/libros', methods=['GET'])
def listar_libros():
    libros = Libro.query.all()  # Obtiene todos los libros de la base de datos
    resultados = [libro.__dict__ for libro in libros]  # Convierte objetos SQLAlchemy a diccionarios
    for resultado in resultados:
        resultado.pop('_sa_instance_state', None)

    return jsonify(resultados)

# 2. Obtener un libro específico (GET /libros/<id>)
@bp.route('/libros/<int:id>', methods=['GET'])
def obtener_libro(id):
    libro = Libro.query.get_or_404(id)  # Obtiene el libro por ID o devuelve error 404 si no existe
    resultado = libro.__dict__
    resultado.pop('_sa_instance_state', None)
    return jsonify(resultado)

# 3. Crear un nuevo libro (POST /libros)
@bp.route('/libros', methods=['POST'])
def crear_libro():
    data = request.get_json()  # Obtiene los datos del cuerpo de la petición (JSON)

    # Validación de datos
    if not data or 'titulo' not in data or 'autor' not in data:
        return jsonify({'message': 'Faltan datos'}), 400

    nuevo_libro = Libro(
        titulo=data['titulo'],
        autor=data['autor']
    )

    db.session.add(nuevo_libro)  # Agrega el nuevo libro a la sesión de la base de datos
    db.session.commit()  # Guarda los cambios en la base de datos
    db.session.refresh(nuevo_libro)
    
    resultado = nuevo_libro.__dict__
    resultado.pop('_sa_instance_state', None)
    return jsonify(resultado), 201  # Devuelve el nuevo libro y código 201 (creado)

# 4. Actualizar un libro (PUT /libros/<id>)
@bp.route('/libros/<int:id>', methods=['PUT'])
def actualizar_libro(id):
    libro = Libro.query.get_or_404(id)
    data = request.get_json()

    if not data:
        return jsonify({'message': 'No se proporcionaron datos para actualizar'}), 400

    # Actualiza los campos si están presentes en los datos
    libro.titulo = data.get('titulo', libro.titulo)
    libro.autor = data.get('autor', libro.autor)

    db.session.commit()
    db.session.refresh(libro)

    resultado = libro.__dict__
    resultado.pop('_sa_instance_state', None)
    return jsonify(resultado)

# 5. Eliminar un libro (DELETE /libros/<id>)
@bp.route('/libros/<int:id>', methods=['DELETE'])
def eliminar_libro(id):
    libro = Libro.query.get_or_404(id)
    db.session.delete(libro)  # Elimina el libro de la sesión de la base de datos
    db.session.commit()
    return jsonify({'message': 'Libro eliminado'}), 200

