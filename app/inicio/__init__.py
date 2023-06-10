from flask import Blueprint

inicio = Blueprint('inicio',__name__, template_folder='templates',url_prefix='/')

from . import routes