from flask import Blueprint

bp = Blueprint('routes', __name__)

from helios_app.routes import testing