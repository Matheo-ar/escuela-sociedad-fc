from flask import render_template, request, redirect, url_for, flash, session
from .forms import Employee
from . import models
from werkzeug.security import generate_password_hash, check_password_hash
from . import empleado

#Ruta muestra la tabla de empleados
@empleado.route('/', methods=["GET", "POST"])
def list_empleado():
    if 'documento' in session:
        row = models.datos_empleado()
        return render_template('listEmployee.html', Datostabla=row)
    else:
        return redirect(url_for('inicio.login'))

#Ruta para crear registros
@empleado.route('/crear', methods=["GET", "POST"])
def createEmployee():
    if 'documento' in session:
        if session['privilegio'] != 'C':
            form = Employee()
            sedes = models.validar_sede()
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
                    TypeEmployee = form.TypeEmployee.data
                    FieldEmployee = form.FieldEmployee.data
                    ActiveEmployee = form.ActiveEmployee.data
                    # Validar que no exista el registro persona
                    row = models.validar_persona(Documento)

                    if row == None:
                        # Se crea un nuevo registro en persona
                        Nacimiento = str(Nacimiento).replace('-', '')
                        # Validamos el rol del registro
                        es_alumno = 0
                        es_acudiente = 0
                        es_colaborador = 1

                        models.crear_persona(Tipodoc, Documento, Nombres, Apellidos, Nacimiento, Genero, Email,
                                             Telefono, Direccion, es_alumno, es_acudiente, es_colaborador)
                        # Se crea un nuevo registro en usuario
                        Nom_usuario = Nombres+' '+Apellidos
                        models.crear_usuario(Documento, Nom_usuario, Email, Telefono, Rol, Contrasena)
                        models.crear_empleado(Documento, TypeEmployee, FieldEmployee,
                                                 ActiveEmployee)
                        flash('Registro Creado Exitosamente', 'success')
                    else:
                        flash('El usuario '+Documento+' ya existe', 'success')

                sedes = models.validar_sede()
                return redirect(url_for('empleado.list_empleado'))
            else:
                return render_template('createEmployee.html', form=form, sedes=sedes)
        else:
            flash('No dispone de privilegios para crear registros', 'success')
            return redirect(url_for('inicio.home'))
    else:
        return redirect(url_for('inicio.login'))
    
#Ruta para consultar registros
@empleado.route('/see/<int:codigo>', methods=["GET", "POST"])
def see_employee(codigo):
    if 'documento' in session:
            form = Employee()
            row = models.ver_empleado(codigo)
            return render_template('seeEmployee.html', form=form, Datoregistro=row)
    else:
        return redirect(url_for('inicio.login'))

#Ruta para editar registros
@empleado.route('/edit/<int:codigo>', methods=["GET", "POST"])
def editemployee(codigo):
    if 'documento' in session:
            if session['privilegio'] != 'C':
                form = Employee()
                datos=models.ver_empleado(codigo)
                datoscombo1 = models.validar_sede()
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
                        FieldEmployee = form.FieldEmployee.data
                        ActiveEmployee = form.ActiveEmployee.data
                        TypeEmployee = form.TypeEmployee.data
                        # Validar que no exista el registro persona
                        models.actualizar_persona(Tipodoc, Documento, Nombres, Apellidos, Nacimiento, Genero, Email,
                                             Telefono, Direccion)
                        models.actualizar_empleado(Documento, FieldEmployee, ActiveEmployee,TypeEmployee)
                        flash('Registro Actualizado Exitosamente', 'success')
                        return redirect(url_for('empleado.list_empleado'))
                    else:
                        return render_template('editEmployee.html', form=form, Datoregistro=datos, datoscombo1=datoscombo1)
                else:
                    return render_template('editEmployee.html', form=form, Datoregistro=datos, datoscombo1=datoscombo1)
            else:
                flash('No dispone de privilegios para editar registros', 'success')
                return render_template('seeEmployee.html', form=form, Datoregistro=datos)
    else:
        return redirect(url_for('inicio.login'))
    
#Ruta para eliminar registros
@empleado.route('/delete/<int:codigo>', methods=["GET", "POST"])
def deleteemployee(codigo):
    if 'documento' in session:
            if session['privilegio'] != 'C':
                models.eliminar_empleado(codigo)
                models.eliminar_usuario(codigo)
                models.eliminar_persona(codigo)
                flash('Registro Eliminado Exitosamente', 'success')
            else:
                flash('No dispone de privilegios para eliminar registros', 'success')
            return redirect(url_for('empleado.list_empleado'))  
    else:
        return redirect(url_for('inicio.login'))
