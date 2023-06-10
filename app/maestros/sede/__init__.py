from flask import Blueprint

sede = Blueprint('sede',__name__, template_folder='templates',url_prefix='/sede')

from . import routes