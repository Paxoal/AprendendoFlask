from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#contém todo flash
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////storage.db'
db = SQLAlchemy(app)


from app.controllers import default

