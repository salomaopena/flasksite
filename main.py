from flask import Flask, render_template, url_for, request, flash, redirect
from dotenv import load_dotenv
from forms import FormLogin, FormCriarConta


app = Flask(__name__)

lista_usuarios = ["Salomão", "Pena", "Bento", "Nilo"]

app.config["SECRET_KEY"] = "8ca9a711780a25374702f2dbc78cb29c900365efeaa4545d41cc0592d62ec45b"#load_dotenv(".env.TOKEN")

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
        # exibir mensagem de logim bem sucedido
        flash(f"Login efetuado com sucesso no email: {form_login.email.data}", "alert-success")
        return redirect(url_for('home'))
    if form_criaconta.validate_on_submit() and "botao_submit_criarconta" in request.form:
        # exibir mensagem de criação de conta bem sucedida
        flash(f"Conta criada para o form criar conta para o email: {form_criaconta.email.data}")
        return redirect(url_for("home"))
    return render_template('login.html', form_login=form_login, form_criaconta=form_criaconta)


if __name__ == "__main__":
    app.run(debug=True)