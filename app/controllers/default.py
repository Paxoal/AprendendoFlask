from flask import redirect, render_template, flash, url_for
from flask_login import login_user, logout_user
from app import app, db
from app.models.tables import User
from app.models.forms import LoginForm

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash("Logged in")
            return redirect(url_for("index"))
        else:
            flash("Invalid login")
    return render_template('login.html', form=form)

@app.route("/logout")
def logout():
    logout_user()
    flash("Logged out")
    return redirect(url_for("login"))

'''
@app.route("/teste/<info>")
@app.route("/teste", defaults={"info": None})
def teste(info):
    user = User("Paschoal","1234", "Arthur Paschoal", "arthurpaschoal500@gmail.com")
    print(user)
    db.session.add(user)
    db.session.commit()
    return "ok"

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