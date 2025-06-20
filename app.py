# app.py
from flask import Flask
from flask_migrate import Migrate
from config import Config
from models import db
from routes import bp as routes_bp
from flask_cors import CORS

migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config_class)

    # Inicializar SQLAlchemy
    db.init_app(app)

    migrate.init_app(app, db)
    # Registrar rutas (blueprint)
    app.register_blueprint(routes_bp)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
