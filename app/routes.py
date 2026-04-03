
from flask import render_template, url_for, request, flash, redirect
from App import app, database, bcrypt
from App.forms import FormLogin, FormCriarConta, FormEditarPerfil, FormCriarPost
from App.models import Usuario, Post
from flask_login import login_user, logout_user, current_user, login_required
import secrets
import os
from PIL import Image



@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")



@app.route("/usuarios")
@login_required
def usuarios():
    lista_usuarios = Usuario.query.all()
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
            param_next = request.args.get('next')
            if param_next:
                return redirect(param_next)
            else:
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
@login_required
def sair():
    logout_user()
    flash(f"Logout feito com sucesso","alert-success")
    return redirect(url_for("home"))


@app.route('/perfil')
@login_required
def perfil():
    foto_perfil = url_for("static", filename="images/profile/{}".format(current_user.foto_perfil))
    return render_template("perfil.html", foto_perfil=foto_perfil)


def salvar_imagem(imagem):
    # adicionar o código no nome da imagem
    token = secrets.token_hex(8)
    nome, extensao = os.path.splitext(imagem.filename)
    #nome_completo = os.path.join(nome, token, extensao)
    nome_completo = nome + token + extensao
    caminho_completo = os.path.join(app.root_path, 'static/images/profile',nome_completo)
    # reduzir a imagem
    tamanho = (400,400)
    imagem_reduzida = Image.open(imagem)
    imagem_reduzida.thumbnail(tamanho)
    # salavar 
    imagem_reduzida.save(caminho_completo)
    return nome_completo

def atualizar_cursos(form):
    lista_cursos = []
    for campo in form:
        if 'curso_' in campo.name:
            if campo.data:
                lista_cursos.append(campo.label.text)
    return ';'.join(lista_cursos)


# editar o perfil do usuário
@app.route('/perfil/editar', methods=["GET", "POST"])
@login_required
def perfil_editar():
    form = FormEditarPerfil()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        
        if form.foto_perfil.data:
            nom_imagem = salvar_imagem(form.foto_perfil.data)
            current_user.foto_perfil = nom_imagem
            
        current_user.cursos = atualizar_cursos(form)
        
        database.session.commit()
        flash('Perfil atualizado com sucesso', "alert-success")
        return redirect(url_for('perfil'))
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email
    foto_perfil = url_for("static", filename="images/profile/{}".format(current_user.foto_perfil))
    return render_template('editar_perfil.html', foto_perfil=foto_perfil, form=form)


@app.route('/post/criar',methods=["GET", "POST"])
@login_required
def post_criar():
    form = FormCriarPost()
    if form.validate_on_submit():
        post = Post(titulo=form.titulo.data, texto=form.texto.data, id_usuario=current_user.id)
        database.session.add(post)
        database.session.commit()
        flash('Post criado com sucesso', 'alert-success')
        return redirect(url_for('home'))
    return render_template("criar_post.html", form=form)
