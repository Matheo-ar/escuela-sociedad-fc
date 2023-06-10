from flask import Blueprint

categoria = Blueprint('categoria',__name__, template_folder='templates',url_prefix='/categoria')

from . import routes