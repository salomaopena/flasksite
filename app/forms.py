from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from App.models import Usuario
from flask_login import current_user

class FormCriarConta(FlaskForm):
    username = StringField("Nome do usuário", validators=[DataRequired(), Length(min=3, max=100)])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    palavra_passe = PasswordField("Palavra-passe", validators=[DataRequired(), Length(6, 20)])
    conf_palavra_passe= PasswordField("Confirmar Palavra-passe", validators=[DataRequired(), EqualTo("palavra_passe", message="A palavra-passe digitada não confere")])
    botao_submit_criarconta = SubmitField("Criar Conta")
    
    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError("E-mail já cadastrado. Cadastre-se com outro e-mail ou faça login para continuar")
    
    
class FormLogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    palavra_passe = PasswordField("Palavra-passe", validators=[DataRequired(), Length(6, 20)])
    lembrar_dados = BooleanField("Lembrar dados de acesso")
    botao_submit_login = SubmitField("Fazer Login")
    

class FormEditarPerfil(FlaskForm):
    username = StringField("Nome do usuário", validators=[DataRequired(), Length(min=3, max=100)])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    foto_perfil = FileField("Atualizar foto de perfil", validators=[FileAllowed(['jpg','png'])])
    botao_submit_editar_perfil = SubmitField("Confirmar Edição")
    
    def validate_email(self, email):
        # Pesquisar se o usuário mudou de e-mail.
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError("Já existe um usuário com esse e-mail. Cadastre outro e-mail.")