from flask import Blueprint

alumno = Blueprint('alumno',__name__, template_folder='templates',static_url_path='app.static', 
                   url_prefix='/alumno')

from . import routes