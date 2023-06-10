from flask import render_template, request, redirect, url_for, flash, session
from .forms import Student
from . import models
from werkzeug.security import generate_password_hash, check_password_hash
from . import alumno

#Ruta muestra la tabla de alumnos
@alumno.route('/', methods=["GET", "POST"])
def list_student():
    if 'documento' in session:
        row = models.datos_persona()
        return render_template('listStudent.html', Datostabla=row)
    else:
        return redirect(url_for('inicio.login'))

#Ruta para crear registros
@alumno.route('/crear', methods=["GET", "POST"])
def createstudent():
    if 'documento' in session:
        if session['privilegio'] != 'C':
            form = Student()
            datoscombo = models.datos_Acudientes()
            datoscombo1 = models.validar_sede()
            datoscombo2 = models.validar_categoria()
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
                    CategorieStudent = form.CategorieStudent.data
                    FieldStudent = form.FieldStudent.data
                    AttendantStudent = form.AttendantStudent.data
                    DateRegistration = form.DateRegistration.data
                    LastPayment = form.LastPayment.data
                    ActiveStudent = form.ActiveStudent.data
                    # Validar que no exista el registro persona
                    row = models.validar_persona(Documento)

                    if row == None:
                        # Se crea un nuevo registro en persona
                        Nacimiento = str(Nacimiento).replace('-', '')
                        DateRegistration = str(
                            DateRegistration).replace('-', '')
                        LastPayment = str(LastPayment).replace('-', '')
                        LastPayment = LastPayment[0:6]

                        # Validamos el rol del registro
                        es_alumno = 1
                        es_acudiente = 0
                        es_colaborador = 0

                        models.crear_persona(Tipodoc, Documento, Nombres, Apellidos, Nacimiento, Genero, Email,
                                             Telefono, Direccion, es_alumno, es_acudiente, es_colaborador)
                        # Se crea un nuevo registro en usuario
                        Nom_usuario = Nombres+' '+Apellidos
                        models.crear_usuario(Documento, Nom_usuario, Email, Telefono, Rol, Contrasena)
                        models.crear_alumno(Documento, CategorieStudent, FieldStudent, AttendantStudent, ActiveStudent,
                                            DateRegistration, LastPayment)
                        flash('Registro Creado Exitosamente', 'success')
                    else:
                        flash('El usuario '+Documento+' ya existe', 'success')

                datoscombo = models.datos_Acudientes()
                datoscombo1 = models.validar_sede()
                datoscombo2 = models.validar_categoria()
                return redirect(url_for('alumno.list_student'))
            else:
                return render_template('createStudent.html', form=form, datoscombo=datoscombo, datoscombo1=datoscombo1, datoscombo2=datoscombo2)
        else:
            flash('No dispone de privilegios para crear registros', 'success')
            return redirect(url_for('inicio.home'))
    else:
        return redirect(url_for('inicio.login'))
    
#Ruta para consultar registros
@alumno.route('/see/<int:codigo>', methods=["GET", "POST"])
def see_student(codigo):
    if 'documento' in session:
            form = Student()
            row = models.datos_alumno(codigo)
            return render_template('seeStudent.html', form=form, Datoregistro=row)
    else:
        return redirect(url_for('inicio.login'))

#Ruta para editar registros
@alumno.route('/edit/<int:codigo>', methods=["GET", "POST"])
def editstudent(codigo):
    if 'documento' in session:
            if session['privilegio'] != 'C':
                form = Student()
                datos=models.datos_alumno(codigo)
                datoscombo = models.datos_Acudientes()
                datoscombo1 = models.validar_sede()
                datoscombo2 = models.validar_categoria()
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
                        CategorieStudent = form.CategorieStudent.data
                        FieldStudent = form.FieldStudent.data
                        AttendantStudent = form.AttendantStudent.data
                        DateRegistration = form.DateRegistration.data
                        LastPayment = form.LastPayment.data
                        ActiveStudent = form.ActiveStudent.data
                        # Validar que no exista el registro persona
                        models.actualizar_persona(Tipodoc, Documento, Nombres, Apellidos, Nacimiento, Genero, Email,
                                             Telefono, Direccion)
                        models.actualizar_alumno(Documento, CategorieStudent, FieldStudent, AttendantStudent, ActiveStudent,
                                            DateRegistration, LastPayment)
                        flash('Registro Actualizado Exitosamente', 'success')
                        return redirect(url_for('alumno.list_student'))
                    else:
                        return render_template('editStudent.html', form=form, Datoregistro=datos, datoscombo=datoscombo, datoscombo1=datoscombo1, datoscombo2=datoscombo2)
                else:
                    return render_template('editStudent.html', form=form, Datoregistro=datos, datoscombo=datoscombo, datoscombo1=datoscombo1, datoscombo2=datoscombo2)
            else:
                flash('No dispone de privilegios para editar registros', 'success')
                return render_template('seeStudent.html', form=form, Datoregistro=datos)
    else:
        return redirect(url_for('inicio.login'))

#Ruta para eliminar registros
@alumno.route('/delete/<int:codigo>', methods=["GET", "POST"])
def deletestudent(codigo):
    if 'documento' in session:
            if session['privilegio'] != 'C':
                models.eliminar_alumno(codigo)
                models.eliminar_usuario(codigo)
                models.eliminar_persona(codigo)
                flash('Registro Eliminado Exitosamente', 'success')
            else:
                flash('No dispone de privilegios para eliminar registros', 'success')
            return redirect(url_for('alumno.list_student'))  
    else:
        return redirect(url_for('inicio.login'))

