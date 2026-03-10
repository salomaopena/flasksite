from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Olá meu site flask está no ar...</p>"

@app.route("/contato")
def contato():
    return "<h1>Qualquer dúvida ligue para a equipe de suporte da nossa central</h1>"


if __name__ == "__main__":
    app.run(debug=True)