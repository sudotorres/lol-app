from flask import Blueprint

bp = Blueprint('champions', __name__)

from app.champions import routes