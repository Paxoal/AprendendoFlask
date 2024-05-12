from flask import render_template
from app import app

from app.models.forms import LoginForm

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
    return render_template('login.html', form=form)
'''
@app.route("/teste")
@app.route("/teste/<nome>")
def teste(nome=None):
    if nome:
        return "Olá, %s!" % nome
        else:
            return "Olá, usuário!"
    
@app.route("/inteiro")
@app.route("/inteiro/<int:inteiro>")
def inteiro(inteiro=None):
    if inteiro:
        return "Olá, o usuário tem id igual a %i" %inteiro
    else:
        return "Olá, o usuário não tem id"
    
@app.route("/met", methods=['GET'])
def met():
    return "Olá!"
'''