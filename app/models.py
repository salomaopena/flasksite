from App import database, login_mmanager
from datetime import datetime
from flask_login import UserMixin

@login_mmanager.user_loader
def preparar_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key = True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    palavra_passe = database.Column(database.String, nullable=False)
    foto_perfil = database.Column(database.String, default="default.png")
    posts = database.relationship('Post', backref='autor', lazy=True)
    cursos = database.Column(database.String, nullable=False, default="Não Informado")
    is_active = database.Column(database.Boolean, default=1)
   

class Post(database.Model):
    id = database.Column(database.Integer, primary_key = True)
    titulo = database.Column(database.String, nullable=False)
    texto = database.Column(database.Text, nullable=False)
    data_cricao = database.Column(database.DateTime, nullable=False, default=datetime.now())
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)