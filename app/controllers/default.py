from flask import render_template
from app import app

#faz a rota da pagina 


@app.route("/index/<user>")
@app.route("/", defaults={"user":None})
def index(user):
    return render_template('index.html', user=user)


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