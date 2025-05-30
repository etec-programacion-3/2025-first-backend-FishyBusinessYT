# scripts/init_database.py
from app import create_app
from models import db, Libro


def init_database():
    app = create_app()

    with app.app_context():
        # Drop all tables and recreate them
        db.drop_all()
        db.create_all()
        print("✅ Database initialized successfully.")

        # Add sample data
        seed_database()


def seed_database():
    # Sample books
    books = [
        Libro(titulo='El Principito', autor='Antoine de Saint-Exupéry'),
        Libro(titulo='Cien años de soledad', autor='Gabriel García Márquez'),
        Libro(titulo='Don Quijote de la Mancha', autor='Miguel de Cervantes')
    ]

    for book in books:
        db.session.add(book)

    db.session.commit()
    print("✅ Sample data added successfully.")


if __name__ == "__main__":
    init_database()
