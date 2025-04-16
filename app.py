# app.py
from flask import Flask
from config import Config
from models import db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Inicializar SQLAlchemy
    db.init_app(app)

    # Registrar rutas (blueprint)
    from routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
