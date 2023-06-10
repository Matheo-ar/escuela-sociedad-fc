from flask import Blueprint

acudiente = Blueprint('acudiente',__name__, template_folder='templates',url_prefix='/acudiente')

from . import routes