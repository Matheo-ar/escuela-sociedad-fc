from app.database import mysql

#CREATE
def crear_usuario(Documento, Nom_usuario, Email, Telefono, Rol, Contraseña):
    # Cursor para la ejecución
    cur = mysql.connection.cursor()
    # QUERY de Insert
    sQuery = '''INSERT INTO usuario (Usuario, Nom_usuario, Email, Telefono, Privilegio, Contraseña) 
      VALUES(%s, %s, %s, %s, %s, %s)'''
    # print(sQuery)

    # Ejecucion de la Sentencia
    cur.execute(sQuery, (Documento, Nom_usuario,
                Email, Telefono, Rol, Contraseña))
    mysql.connection.commit()

    # Cerramos el cursor
    cur.close()

def crear_alumno(Documento, CategorieStudent, FieldStudent, AttendantStudent, ActiveStudent, 
                 DateRegistration, LastPayment):
    # Cursor para la ejecución
    cur = mysql.connection.cursor()  # Siempre va este
    # QUERY de Insert
    sQuery = '''INSERT INTO alumno (idAlumno, Categoria, Sede, Acudiente, Activo, Fecha_Matricula, Ult_pago) 
      VALUES(%s, %s, %s, %s, %s, %s, %s)'''
    # Ejecucion de la Sentencia
    cur.execute(sQuery, (Documento, CategorieStudent, FieldStudent, AttendantStudent, ActiveStudent, 
                         DateRegistration, LastPayment))
    
    mysql.connection.commit()

def crear_persona(Tipodoc, Documento, Nombres, Apellidos, Nacimiento, Genero, Email,  # Siempre va mysql
                  Telefono, Direccion, es_alumno, es_acudiente, es_empleado):
    # Cursor para la ejecución
    cur = mysql.connection.cursor()  # Siempre va este
    # QUERY de Insert
    sQuery = '''INSERT INTO persona (TipoId, Identificacion, Nombres, Apellidos, FechaNacimiento, Genero,
      Correo, Telefono, Direccion, Es_Alumno, Es_Acudiente, Es_Empleado) 
      VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
    # print(sQuery)

    # Ejecucion de la Sentencia
    cur.execute(sQuery, (Tipodoc, Documento, Nombres, Apellidos, Nacimiento, Genero, Email,
                         Telefono, Direccion, es_alumno, es_acudiente, es_empleado))
    mysql.connection.commit()

    # Cerramos el cursor
    cur.close()


#READ
#model para llenar la tabla de alumnos
def datos_persona():
    cur = mysql.connection.cursor()
    sQuery = '''SELECT * FROM bd_escuela.v_datos_alumno '''.format()
    #print(sQuery)
    cur.execute(sQuery)
    row = cur.fetchall()

    # Ejecucion de la Sentencia
    cur.execute(sQuery)
    mysql.connection.commit()

    # Cerramos el cursor
    cur.close()

    return row

#model para traer los datos de un alumno en particular
def datos_alumno(id):
    cur = mysql.connection.cursor()
    sQuery = '''SELECT * FROM bd_escuela.v_datos_alumno where identificacion like '%{}%' '''.format(id)
    #print(sQuery)
    cur.execute(sQuery)
    row = cur.fetchone()

    # Ejecucion de la Sentencia
    cur.execute(sQuery)
    mysql.connection.commit()

    # Cerramos el cursor
    cur.close()

    return row

#model para traer los datos de las categorias para seleccionar
def validar_categoria():
    cur = mysql.connection.cursor()
    sQuery = "SELECT idCategoria, Nom_Categoria FROM bd_escuela.categoria ".format()
    #print(sQuery)
    cur.execute(sQuery)
    row = cur.fetchall()

    # Ejecucion de la Sentencia
    cur.execute(sQuery)
    mysql.connection.commit()

    # Cerramos el cursor
    cur.close()

    return row

#model para traer los datos de las sedes para seleccionar
def validar_sede():
    cur = mysql.connection.cursor()
    sQuery = "SELECT * FROM bd_escuela.sede ".format()
    #print(sQuery)
    cur.execute(sQuery)
    row = cur.fetchall()

    # Ejecucion de la Sentencia
    cur.execute(sQuery)
    mysql.connection.commit()

    # Cerramos el cursor
    cur.close()

    return row

#model para traer los datos de las acudientes para seleccionar
def datos_Acudientes():
     #print(nit)
     #Cursor para la ejecución
     cur= mysql.connection.cursor()            
     sQuery="SELECT Identificacion,concat(Nombres,' ',Apellidos) as Nombre FROM bd_escuela.persona where Es_Acudiente=1".format(
        )
     cur.execute(sQuery)
     Listacudientes=cur.fetchall()
     #Cerramos el cursor
     cur.close()

     return Listacudientes

#model para vaidar que el registro no exista
def validar_persona(Documento):
    # Cursor para la ejecución
    cur = mysql.connection.cursor()
    sQuery = "SELECT Identificacion FROM persona WHERE Identificacion='{}'".format(
        Documento)
    cur.execute(sQuery)
    row = cur.fetchone()
    # Cerramos el cursor
    cur.close()

    return row

#UPDATE
def actualizar_persona(Tipodoc, Documento, Nombres, Apellidos, Nacimiento, Genero, Email,Telefono, Direccion):
    # Cursor para la ejecución
    cur = mysql.connection.cursor()
    # QUERY de UPDATE
    # Ejecucion de la Sentencia
    cur.execute('''UPDATE bd_escuela.persona SET TipoId=%s, Nombres=%s, Apellidos=%s, Direccion=%s,
    Telefono=%s, FechaNacimiento=%s, Genero=%s, Correo=%s WHERE Identificacion=%s ''', (Tipodoc,Nombres,
    Apellidos, Direccion,Telefono,Nacimiento, Genero, Email,Documento))
    mysql.connection.commit()

    # Cerramos el cursor
    cur.close()

def actualizar_alumno(Documento, CategorieStudent, FieldStudent, AttendantStudent, ActiveStudent,
    DateRegistration, LastPayment):
    # Cursor para la ejecución
    cur = mysql.connection.cursor()
    # QUERY de UPDATE
    # Ejecucion de la Sentencia
    cur.execute('''UPDATE bd_escuela.alumno SET Categoria=%s, Sede=%s, Acudiente=%s, Activo=%s,
    Fecha_Matricula=%s, Ult_pago=%s WHERE IdAlumno=%s ''', (CategorieStudent, FieldStudent, AttendantStudent,
    ActiveStudent,DateRegistration, LastPayment,Documento))
    mysql.connection.commit()

    # Cerramos el cursor
    cur.close()

#DELETE
def eliminar_alumno(Documento):
    # Cursor para la ejecución
    cur = mysql.connection.cursor()
    # QUERY de UPDATE
    # Ejecucion de la Sentencia
    cur.execute('''DELETE from bd_escuela.alumno WHERE IdAlumno=%s ''', (Documento,))
    mysql.connection.commit()

    # Cerramos el cursor
    cur.close()

def eliminar_usuario(Documento):
    # Cursor para la ejecución
    cur = mysql.connection.cursor()
    # QUERY de UPDATE
    # Ejecucion de la Sentencia
    cur.execute('''DELETE from bd_escuela.usuario WHERE Usuario=%s ''', (Documento,))
    mysql.connection.commit()

    # Cerramos el cursor
    cur.close()

def eliminar_persona(Documento):
    # Cursor para la ejecución
    cur = mysql.connection.cursor()
    # QUERY de UPDATE
    # Ejecucion de la Sentencia
    cur.execute('''DELETE from bd_escuela.persona WHERE Identificacion=%s ''', (Documento,))
    mysql.connection.commit()

    # Cerramos el cursor
    cur.close()