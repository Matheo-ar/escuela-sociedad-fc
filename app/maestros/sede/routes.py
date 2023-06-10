from flask import render_template, request, redirect, url_for, flash, session
from .forms import Campus
from . import models
from werkzeug.security import generate_password_hash, check_password_hash
from . import sede

#Ruta muestra la tabla de sedes
@sede.route('/', methods=["GET", "POST"])
def list_sede():
    if 'documento' in session:
        row = models.datos_sede()
        return render_template('listCampus.html', Datostabla=row)
    else:
        return redirect(url_for('inicio.login'))

#Ruta para crear registros
@sede.route('/crear', methods=["GET", "POST"])
def createCampus():
    if 'documento' in session:
        if session['privilegio'] != 'C':
            form = Campus()
            sedes = models.datos_sede()
            if request.method == 'POST':
                if form.validate_on_submit():
                    IdSede = form.IdSede.data
                    NombreSede = form.NombreSede.data
                    Direccion = form.Direccion.data
                    Telefono = form.Telefono.data
                    Director = form.Genero.data
                    Rol = 'C'
                    ActiveCampus = form.ActiveCampus.data
                    # Validar que no exista el registro persona
                    row = models.validar_sede(IdSede)

                    if row == None:
                        # Se crea un nuevo registro en persona
                        models.crear_sede(NombreSede, Direccion, Telefono, Director,  ActiveCampus)
                        flash('Registro Creado Exitosamente', 'success')
                    else:
                        flash('El Registro ya existe', 'success')

                return redirect(url_for('sede.list_sede'))
            else:
                return render_template('createCampus.html', form=form, sedes=sedes)
        else:
            flash('No dispone de privilegios para crear registros', 'success')
            return redirect(url_for('inicio.home'))
    else:
        return redirect(url_for('inicio.login'))
    
#Ruta para consultar registros
@sede.route('/see/<int:codigo>', methods=["GET", "POST"])
def see_Campus(codigo):
    if 'documento' in session:
            form = Campus()
            row = models.ver_sede(codigo)
            return render_template('seeCampus.html', form=form, Datoregistro=row)
    else:
        return redirect(url_for('inicio.login'))

#Ruta para editar registros
@sede.route('/edit/<int:codigo>', methods=["GET", "POST"])
def editCampus(codigo):
    if 'documento' in session:
            if session['privilegio'] != 'C':
                form = Campus()
                datos=models.ver_sede(codigo)
                datoscombo1 = models.validar_sede()
                if request.method == 'POST':
                    if form.validate_on_submit():
                        IdSede = form.IdSede.data
                        NombreSede = form.NombreSede.data
                        Direccion = form.Direccion.data
                        Telefono = form.Telefono.data
                        Director = form.Genero.data
                        ActiveCampus = form.ActiveCampus.data
                        # Validar que no exista el registro persona
                        models.actualizar_sede(NombreSede, Direccion, Telefono, Director, ActiveCampus)
                        flash('Registro Actualizado Exitosamente', 'success')
                        return redirect(url_for('sede.list_sede'))
                    else:
                        return render_template('editCampus.html', form=form, Datoregistro=datos)
                else:
                    return render_template('editCampus.html', form=form, Datoregistro=datos)
            else:
                flash('No dispone de privilegios para editar registros', 'success')
                return render_template('seeCampus.html', form=form, Datoregistro=datos)
    else:
        return redirect(url_for('inicio.login'))
    
#Ruta para eliminar registros
@sede.route('/delete/<int:codigo>', methods=["GET", "POST"])
def deleteCampus(codigo):
    if 'documento' in session:
            if session['privilegio'] != 'C':
                models.eliminar_sede(codigo)
                flash('Registro Eliminado Exitosamente', 'success')
            else:
                flash('No dispone de privilegios para eliminar registros', 'success')
            return redirect(url_for('sede.list_sede'))  
    else:
        return redirect(url_for('inicio.login'))
