from flask import Blueprint

empleado = Blueprint('empleado',__name__, template_folder='templates',url_prefix='/empleado')

from . import routes