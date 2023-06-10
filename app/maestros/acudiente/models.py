from app.database import mysql

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
      Correo, Telefono, Direccion, Es_Alumno, Es_Acudiente, Es_empleado) 
      VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
    # print(sQuery)

    # Ejecucion de la Sentencia
    cur.execute(sQuery, (Tipodoc, Documento, Nombres, Apellidos, Nacimiento, Genero, Email,
                         Telefono, Direccion, es_alumno, es_acudiente, es_empleado))
    mysql.connection.commit()

    # Cerramos el cursor
    cur.close()

#READ
#model para llenar la tabla de acudientes
def datos_persona():
    cur = mysql.connection.cursor()
    sQuery = '''SELECT * FROM bd_escuela.persona Where es_acudiente='1' '''.format()
    #print(sQuery)
    cur.execute(sQuery)
    row = cur.fetchall()

    # Ejecucion de la Sentencia
    cur.execute(sQuery)
    mysql.connection.commit()

    # Cerramos el cursor
    cur.close()

    return row

def see_persona(id):
    cur = mysql.connection.cursor()
    sQuery = '''SELECT * from bd_escuela.v_datos_acudiente Where identificacion='{}' '''.format(id)
    #print(sQuery)
    cur.execute(sQuery)
    row = cur.fetchone()

    # Ejecucion de la Sentencia
    cur.execute(sQuery)
    mysql.connection.commit()

    # Cerramos el cursor
    cur.close()

    return row

#READ
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
def actualizar_persona(TipoId, Documento, Nombres, Apellidos, Nacimiento, Genero, Email,Telefono, Direccion):
    # Cursor para la ejecución
    cur = mysql.connection.cursor()
    # QUERY de UPDATE
    # Ejecucion de la Sentencia
    cur.execute('''UPDATE bd_escuela.persona SET TipoId=%s, Nombres=%s, Apellidos=%s, Direccion=%s,
    Telefono=%s, FechaNacimiento=%s, Genero=%s, Correo=%s WHERE Identificacion=%s ''', (TipoId,Nombres,
    Apellidos, Direccion,Telefono,Nacimiento, Genero, Email,Documento))
    mysql.connection.commit()

    # Cerramos el cursor
    cur.close()

#Delete
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
