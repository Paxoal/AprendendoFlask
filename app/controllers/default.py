from app import app

#faz a rota da pagina
@app.route("/")
def index():
    return "Hello world!"