from flask import Blueprint

bpTest = Blueprint('testing', __name__)
bpAccount = Blueprint('account', __name__)

from helios_app.routes import testing
from helios_app.routes import account