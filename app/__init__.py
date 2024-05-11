from flask import Flask

#contém todo flash
app = Flask(__name__)

from app.controllers import default

