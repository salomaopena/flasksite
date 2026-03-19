
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config["SECRET_KEY"] = "8ca9a711780a25374702f2dbc78cb29c900365efeaa4545d41cc0592d62ec45b"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flasksite.db'

# criar a instancia do banco de dados
database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_mmanager = LoginManager(app)
login_mmanager.login_view = "login"
login_mmanager.login_message_category = "alert-info"
login_mmanager.login_message = "Acesso não autorizado. Por favor, faça login ou crie conta"

# with app.app_context():
#     database.create_all()

# importar os routes | rotas
from App import routes
