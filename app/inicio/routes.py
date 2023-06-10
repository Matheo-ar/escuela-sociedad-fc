from flask import render_template, request, redirect, url_for, flash, session
from .forms import Login
from . import models
from werkzeug.security import generate_password_hash, check_password_hash
from . import inicio

@inicio.route('/')
def index():
    return render_template('inicio.html')

@inicio.route('/login', methods=["GET", "POST"])
def login():
    form = Login()
    if request.method == 'POST':
        if form.validate_on_submit():
            Documento = form.Documento.data
            # Validamos si el usuario existe
            row = models.validar_usuario( Documento)
            if len(row) > 0 and check_password_hash(row[1], form.Contrasena.data):
                # Registra la session
                session['documento'] = request.form['Documento']
                session['privilegio'] = row[2]
                session['usuario'] = row[3]
                return redirect(url_for('inicio.home'))

            else:
                flash('El usuario o la contraseña no son validos', 'alert')
                return render_template('login.html', form=form)
        return render_template('login.html', form=form)
    return render_template('login.html', form=form)


@inicio.route('/home')
def home():
    if 'documento' in session:
        usuario=session['usuario']
        return render_template('home.html',usuario=usuario)
    else:
        return redirect('/login')


