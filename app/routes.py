
from flask import render_template, url_for, request, flash, redirect
from App import app, database, bcrypt
from App.forms import FormLogin, FormCriarConta
from App.models import Usuario, Post
from flask_login import login_user, logout_user, current_user

lista_usuarios = ['Pena','Salomão','Nilo','Bento']


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/usuarios")
def usuarios():
    return render_template("usuarios.html", lista_usuarios=lista_usuarios)


@app.route("/login", methods=["GET", "POST"])
def login():
    form_login = FormLogin()
    form_criaconta = FormCriarConta()
    
    if form_login.validate_on_submit() and "botao_submit_login" in request.form:
        
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
    
        if usuario and bcrypt.check_password_hash(usuario.palavra_passe, form_login.palavra_passe.data):
            login_user(usuario, remember=form_login.lembrar_dados.data)
            # exibir mensagem de logim bem sucedido
            flash(f"Login efetuado com sucesso no email: {form_login.email.data}", "alert-success")
            return redirect(url_for('home'))
        else:
            flash(f"Falha ao fazer login. E-mail e/ou Senha incorretos", "alert-danger")
        
    
    
    if form_criaconta.validate_on_submit() and "botao_submit_criarconta" in request.form:
        # exibir mensagem de criação de conta bem sucedida
        # criar um usuário
        palavra_passe_crypt = bcrypt.generate_password_hash(form_criaconta.palavra_passe.data)
        usuario = Usuario(
            username=form_criaconta.username.data,
            email=form_criaconta.email.data, 
            palavra_passe=palavra_passe_crypt,
            )
        database.session.add(usuario)
        database.session.commit()
        
        flash(f"Conta criada para o form criar conta para o email: {form_criaconta.email.data}","alert-success")
        return redirect(url_for("home"))
    return render_template('login.html', form_login=form_login, form_criaconta=form_criaconta)


@app.route('/sair')
def sair():
    logout_user()
    flash(f"Logout feito com sucesso","alert-success")
    return redirect(url_for("home"))

@app.route('/perfil')
def perfil():
    return render_template("perfil.html")

@app.route('/post/criar')
def post_criar():
    return render_template("criar_post.html")