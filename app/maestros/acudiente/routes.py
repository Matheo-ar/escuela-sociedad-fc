from flask import render_template, request, redirect, url_for, flash, session
from .forms import Attendant
from . import models
from werkzeug.security import generate_password_hash, check_password_hash
from . import acudiente

#Ruta muestra la tabla de acudientes
@acudiente.route('/', methods=["GET", "POST"])
def list_attendant():
    if 'documento' in session:
        row = models.datos_persona()
        return render_template('listAttendant.html', Datostabla=row)
    else:
        return redirect(url_for('inicio.login'))

@acudiente.route('/crear', methods=["GET", "POST"])
def createattendant():
    if 'documento' in session:
        if session['privilegio'] != 'C':
            form = Attendant()
            if request.method == 'POST':
                if form.validate_on_submit():
                    Tipodoc = form.Tipodoc.data
                    Documento = form.Documento.data
                    Nombres = form.Nombres.data
                    Apellidos = form.Apellidos.data
                    Nacimiento = form.Nacimiento.data
                    Genero = form.Genero.data
                    Email = form.Email.data
                    Telefono = form.Telefono.data
                    Direccion = form.Direccion.data
                    Rol = 'C'
                    Contrasena = generate_password_hash(form.Contrasena.data)
                    # Validar que no exista el registro persona
                    row = models.validar_persona(Documento)

                    if row == None:
                        # Se crea un nuevo registro en persona
                        Nacimiento = str(Nacimiento).replace('-', '')

                        # Validamos el rol del registro
                        es_alumno = 0
                        es_acudiente = 1
                        es_colaborador = 0

                        models.crear_persona(Tipodoc, Documento, Nombres, Apellidos, Nacimiento, Genero, Email,
                                             Telefono, Direccion, es_alumno, es_acudiente, es_colaborador)
                        # Se crea un nuevo registro en usuario
                        Nom_usuario = Nombres+' '+Apellidos
                        models.crear_usuario(Documento, Nom_usuario, Email, Telefono, Rol, Contrasena)
                        flash('Registro Creado Exitosamente', 'success')
                    else:
                        flash('El usuario '+Documento+' ya existe', 'success')

                return redirect(url_for('acudiente.list_attendant'))
            else:
                return render_template('createAttendant.html', form=form)
        else:
            return redirect(url_for('inicio.home'))
    else:
        return redirect(url_for('inicio.login'))

#Ruta para consultar registros
@acudiente.route('/see/<int:codigo>', methods=["GET", "POST"])
def see_attendant(codigo):
    if 'documento' in session:
            form = Attendant()
            row = models.see_persona(codigo)
            return render_template('seeAttendant.html', form=form, Datoregistro=row)
    else:
        return redirect(url_for('inicio.login'))

#Ruta para editar registros
@acudiente.route('/edit/<int:codigo>', methods=["GET", "POST"])
def editattendant(codigo):
    if 'documento' in session:
            if session['privilegio'] != 'C':
                form = Attendant()
                datos=models.see_persona(codigo)
                if request.method == 'POST':
                    if form.validate_on_submit():
                        Tipodoc = form.Tipodoc.data
                        Nombres = form.Nombres.data
                        Apellidos = form.Apellidos.data
                        Nacimiento = form.Nacimiento.data
                        Genero = form.Genero.data
                        Email = form.Email.data
                        Telefono = form.Telefono.data
                        Direccion = form.Direccion.data
                        # Validar que no exista el registro persona
                        models.actualizar_persona(Tipodoc, codigo, Nombres, Apellidos, Nacimiento, Genero, Email,
                                             Telefono, Direccion)
                        flash('Registro Actualizado Exitosamente', 'success')
                        return redirect(url_for('acudiente.list_attendant'))
                    else:
                        return render_template('editAttendent.html', form=form, Datoregistro=datos)
                else:
                    return render_template('editAttendant.html', form=form, Datoregistro=datos)
            else:
                flash('No dispone de privilegios para editar registros', 'success')
                return render_template('seeAttendant.html', form=form, Datoregistro=datos)
    else:
        return redirect(url_for('inicio.login'))

#Ruta para eliminar registros
@acudiente.route('/delete/<int:codigo>', methods=["GET", "POST"])
def deleteattendant(codigo):
    if 'documento' in session:
            if session['privilegio'] != 'C':
                try:
                    models.eliminar_persona(codigo)
                    flash('Registro Eliminado Exitosamente', 'success')
                except:
                    flash('Registro no se puede eliminar', 'success')
            else:
                flash('No dispone de privilegios para eliminar registros', 'success')
            return redirect(url_for('acudiente.list_attendant'))  
    else:
        return redirect(url_for('inicio.login'))