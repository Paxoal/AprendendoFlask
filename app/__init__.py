from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#contém todo flash
app = Flask(__name__)
app.config.from_object("config")


db = SQLAlchemy(app)

migrate = Migrate(app, db)

from app.controllers import default

