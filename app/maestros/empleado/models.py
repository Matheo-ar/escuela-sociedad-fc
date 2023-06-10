from app.database import mysql

#CREATE
def crear_usuario(Documento, Nom_usuario, Email, Telefono, Rol,Contraseña):
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

def crear_empleado(Documento, TypeEmployee, FieldEmployee, ActiveEmployee):
    # Cursor para la ejecución
    cur = mysql.connection.cursor()  # Siempre va este
    # QUERY de Insert
    sQuery = '''INSERT INTO empleado (idEmpleado, TipoEmpleado, Sede, Activo) 
      VALUES(%s, %s, %s, %s)'''
    #print(sQuery)
    # Ejecucion de la Sentencia
    cur.execute(sQuery, (Documento,TypeEmployee, FieldEmployee, ActiveEmployee))
    
    mysql.connection.commit()

    # Cerramos el cursor
    cur.close() 
    
#READ
def datos_empleado():
    cur = mysql.connection.cursor()
    sQuery = '''SELECT * FROM bd_escuela.v_datos_empleado '''.format()
    #print(sQuery)
    cur.execute(sQuery)
    row = cur.fetchall()

    # Ejecucion de la Sentencia
    cur.execute(sQuery)
    mysql.connection.commit()

    # Cerramos el cursor
    cur.close()

    return row

def ver_empleado(codigo):
    cur = mysql.connection.cursor()
    sQuery = '''SELECT * FROM bd_escuela.v_datos_empleado Where identificacion='{}' '''.format(codigo)
    #print(sQuery)
    cur.execute(sQuery)
    row = cur.fetchone()

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

def actualizar_empleado(Documento, FieldEmployee, ActiveEmployee,TypeEmployee):
    # Cursor para la ejecución
    cur = mysql.connection.cursor()
    # QUERY de UPDATE
    # Ejecucion de la Sentencia
    cur.execute('''UPDATE bd_escuela.empleado SET Sede=%s, Activo=%s, TipoEmpleado=%s
     WHERE IdEmpleado=%s ''', (FieldEmployee, ActiveEmployee,TypeEmployee,Documento))
    mysql.connection.commit()

    # Cerramos el cursor
    cur.close()

#DELETE
def eliminar_empleado(Documento):
    # Cursor para la ejecución
    cur = mysql.connection.cursor()
    # QUERY de UPDATE
    # Ejecucion de la Sentencia
    cur.execute('''DELETE from bd_escuela.empleado WHERE IdEmpleado=%s ''', (Documento,))
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
