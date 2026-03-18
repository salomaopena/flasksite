from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from App.models import Usuario

class FormCriarConta(FlaskForm):
    username = StringField("Nome do usuário", validators=[DataRequired(), Length(min=3, max=100)])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    palavra_passe = PasswordField("Palavra-passe", validators=[DataRequired(), Length(6, 20)])
    conf_palavra_passe= PasswordField("Confirmar Palavra-passe", validators=[DataRequired(), EqualTo("palavra_passe", message="A palavra-passe digitada não confere")])
    botao_submit_criarconta = SubmitField("Criar Conta")
    
    def validate_email(self, email, extra_validators = None):
        usuario = Usuario.query.filter_by(email=email.data).first_or_404()
        if usuario:
            raise ValidationError("E-mail já cadastrado. Cadastre-se com outro e-mail ou faça login para continuar")
    
    
class FormLogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    palavra_passe = PasswordField("Palavra-passe", validators=[DataRequired(), Length(6, 20)])
    lembrar_dados = BooleanField("Lembrar dados de acesso")
    botao_submit_login = SubmitField("Fazer Login")
    