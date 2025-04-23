from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Libro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), nullable=False)
    autor = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<Libro {self.titulo}>'
