from flask import Flask, render_template, session
from flask_login import LoginManager, user_accessed
from .database import mysql
import bcrypt
from .inicio import inicio
from .maestros.alumno import alumno
from .maestros.acudiente import acudiente
from .maestros.empleado import empleado
from .maestros.categoria import categoria
from .maestros.sede import sede

app = Flask(__name__)

try:
    # CONEXION A LA BD MYSQL
    app.config['MYSQL_HOST'] = 'localhost'  # 190.158.204.52
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'admin'
    app.config['MYSQL_DB'] = 'bd_escuela'
    mysql.init_app(app)

    resultado = 'Conectado'
except:
    resultado = 'No Conectado'

login_manager = LoginManager(app)
login_manager.login_view = "inicio"

# SEMILLA PARA EL ENCRIPTAMIENTO
semilla = bcrypt.gensalt()
# Settings
app.secret_key = semilla

#Rutas de maestros
app.register_blueprint(inicio)
app.register_blueprint(alumno)
app.register_blueprint(acudiente)
app.register_blueprint(empleado)
app.register_blueprint(categoria)
app.register_blueprint(sede)

# Manejo de errores
@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def error_interno(error):
    return render_template('500.html'), 500

@login_manager.user_loader
def load_user(user_id):
    return user_accessed.get(user_id)