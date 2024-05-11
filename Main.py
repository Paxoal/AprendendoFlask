from flask import Flask

#contém todo flash
app = Flask(__name__)

#faz a rota da pagina
@app.route("/")
def index():
    return "Hello world!"

if __name__ == "__main__":
    app.run()