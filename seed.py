from app import create_app
from app.extensions import db
from app.models import Usuario, Categoria, Anuncio

def run_seed():
    app = create_app()
    
    with app.app_context():
        if Usuario.query.first() or Categoria.query.first() or Anuncio.query.first():
            print("La base de datos ya tiene datos.")
            return

        cat1 = Categoria(nombre="Tecnología")
        cat2 = Categoria(nombre="Empleos")
        cat3 = Categoria(nombre="Ventas")
        
        db.session.add_all([cat1, cat2, cat3])
        db.session.commit()

        user1 = Usuario(nombre="Ana Pérez", email="ana@example.com")
        user1.set_password("123456")
        
        user2 = Usuario(nombre="Carlos Gómez", email="carlos@example.com")
        user2.set_password("123456")

        user3 = Usuario(nombre="María Rodríguez", email="maria@example.com")
        user3.set_password("123456")
        
        db.session.add_all([user1, user2, user3])
        db.session.commit()

        anuncio1 = Anuncio(
            titulo="Vendo Laptop Gamer",
            contenido="Laptop en excelente estado, 16GB RAM, 512GB SSD. Interesados contactar.",
            usuario_id=user1.id,
            categoria_id=cat3.id
        )
        
        anuncio2 = Anuncio(
            titulo="Se busca desarrollador Python",
            contenido="Empresa busca desarrollador con experiencia en Flask. Medio tiempo.",
            usuario_id=user2.id,
            categoria_id=cat2.id
        )
        
        anuncio3 = Anuncio(
            titulo="Nuevo curso de Flask disponible",
            contenido="Aprende a crear aplicaciones web con el patrón Application Factory.",
            usuario_id=user3.id,
            categoria_id=cat1.id
        )

        db.session.add_all([anuncio1, anuncio2, anuncio3])
        db.session.commit()

        print("Datos insertados correctamente.")

if __name__ == '__main__':
    run_seed()