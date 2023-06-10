from flask import render_template, request, redirect, url_for, flash, session
from .forms import Categories
from . import models
from werkzeug.security import generate_password_hash, check_password_hash
from . import categoria


#Ruta muestra la tabla de categorias
@categoria.route('/', methods=["GET", "POST"])
def list_categories():
    if 'documento' in session:
        row = models.datos_categoria()
        return render_template('listCategories.html', Datostabla=row)
    else:
        return redirect(url_for('inicio.login'))

#Ruta para crear registros
@categoria.route('/crear', methods=["GET", "POST"])
def createCategories():
    if 'documento' in session:
        if session['privilegio'] != 'C':
            form = Categories()
            
            if request.method == 'POST':
                if form.validate_on_submit():
                    IdCategoria = form.IdCategoria.data
                    NombreCategoria = form.NombreCategoria.data
                    # Validar que no exista el registro categoria
                    row = models.validar_categoria(IdCategoria)

                    if row == None:
                        # Se crea un nuevo registro en categoria
                        models.crear_categoria(NombreCategoria ,)
                        flash('Registro Creado Exitosamente', 'success')
                    else:
                        flash('El Registro ya existe', 'success')

                return redirect(url_for('categoria.list_categories'))
            else:
                return render_template('createCategories.html', form=form)
        else:
            flash('No dispone de privilegios para crear registros', 'success')
            return redirect(url_for('inicio.home'))
    else:
        return redirect(url_for('inicio.login'))
    
#Ruta para consultar registros
@categoria.route('/see/<int:codigo>', methods=["GET", "POST"])
def see_categories(codigo):
    if 'documento' in session:
            form = Categories()
            row = models.datos_categoria()
            return render_template('seeCategories.html', form=form, Datoregistro=row)
    else:
        return redirect(url_for('inicio.login'))

#Ruta para editar registros
@categoria.route('/edit/<int:codigo>', methods=["GET", "POST"])
def editcategories(codigo):
    if 'documento' in session:
            if session['privilegio'] != 'C':
                form = Categories()
                datos=models.datos_categoria1(codigo)
                if request.method == 'POST':
                    if form.validate_on_submit():
                        IdCategoria = form.IdCategoria.data
                        NombreCategoria = form. NombreCategoria.data
                        # Validar que no exista el registro categoria
                        models.actualizar_categoria(NombreCategoria , IdCategoria)
                        flash('Registro Actualizado Exitosamente', 'success')
                        return redirect(url_for('categoria.list_categories'))
                    else:
                        return render_template('editCategories.html', form=form, Datoregistro=datos)
                else:
                    return render_template('editCategories.html', form=form, Datoregistro=datos)
            else:
                flash('No dispone de privilegios para editar registros', 'success')
                return render_template('seeStudent.html', form=form, Datoregistro=datos)
    else:
        return redirect(url_for('inicio.login'))

#Ruta para eliminar registros
@categoria.route('/delete/<int:codigo>', methods=["GET", "POST"])
def deletecategories(codigo):
    if 'documento' in session:
            if session['privilegio'] != 'C':
                try:
                    models.eliminar_categoria(codigo)
                    flash('Registro Eliminado Exitosamente', 'success')
                except:
                    flash('El Registro no puede ser eliminado', 'success')
            else:
                flash('No dispone de privilegios para eliminar registros', 'success')
            return redirect(url_for('categoria.list_categories'))  
    else:
        return redirect(url_for('inicio.login'))

