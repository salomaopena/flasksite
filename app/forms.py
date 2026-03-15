from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class FormCriarConta(FlaskForm):
    username = StringField("Nome do usuário", validators=[DataRequired(), Length(min=3, max=100)])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    palavra_passe = PasswordField("Palavra-passe", validators=[DataRequired(), Length(6, 20)])
    conf_palavra_passe= PasswordField("Confirmar Palavra-passe", validators=[DataRequired(), EqualTo("Palavra-passe", message="A palavra-passe digitada não confere")])
    botao_submit_criarconta = SubmitField("Criar Conta")
    
    
class FormLogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    palavra_passe = PasswordField("Palavra-passe", validators=[DataRequired(), Length(6, 20)])
    lembrar_dados = BooleanField("Lembrar dados de acesso")
    botao_submit_login = SubmitField("Fazer Login")
    