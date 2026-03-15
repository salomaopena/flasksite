from main import app, database
from app.models import Usuario, Post

# with app.app_context():
#     database.create_all()
#with app.app_context():
    
    # usuario = Usuario(
    # username="Salomão", 
    # email="salomao@email.com",
    # palavra_passe = '123456'
    # )
    
    # usuario2 = Usuario(
    # username="Pena", 
    # email="pena@email.com",
    # palavra_passe = '123456'
    # )

    # database.session.add(usuario)
    # database.session.add(usuario2)

    # database.session.commit()
    
    # meus_usuarios = Usuario.query.all()
    
    # for usuario in meus_usuarios:
    #     print(f' id: {usuario.id}, nome: {usuario.username}, {usuario.email}, {usuario.palavra_passe}, posts: {usuario.post}')
 
    # post = Post(
    #     id_usuario = 1, 
    #     titulo="Meu primeiro Post",
    #     texto = 'Salomão Voando'
    #     )
    # database.session.add(post)

    # database.session.commit()

    # posts = Post.query.all()
    # for post in posts:
    #     print(f"Autor: {post.autor.username}, titulo: {post.titulo}, texto: {post.texto}")
    
# with app.app_context():
#     database.drop_all()
#     database.create_all()