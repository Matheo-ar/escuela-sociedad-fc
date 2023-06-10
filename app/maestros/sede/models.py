from app.database import mysql

#CREATE
def crear_sede(NombreSede, Direccion, Telefono, Director, ActiveCampus):
    # Cursor para la ejecución
    cur = mysql.connection.cursor()  # Siempre va este
    # QUERY de Insert
    sQuery = '''INSERT INTO sede (Nombre_sede, Direccion, Telefono, Director, Activo) 
      VALUES(%s, %s, %s, %s, %s, %s)'''
    #print(sQuery)
    # Ejecucion de la Sentencia
    cur.execute(sQuery, (NombreSede, Direccion, Telefono, Director, ActiveCampus))
    
    mysql.connection.commit()

    # Cerramos el cursor
    cur.close() 
    
#READ
def datos_sede():
    cur = mysql.connection.cursor()
    sQuery = '''SELECT * FROM bd_escuela.sede '''.format()
    #print(sQuery)
    cur.execute(sQuery)
    row = cur.fetchall()

    # Ejecucion de la Sentencia
    cur.execute(sQuery)
    mysql.connection.commit()

    # Cerramos el cursor
    cur.close()

    return row

def ver_sede(codigo):
    cur = mysql.connection.cursor()
    sQuery = '''SELECT * FROM bd_escuela.sede Where IdSede like '%{}%' '''.format(codigo)
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
def validar_sede(idsede):
    cur = mysql.connection.cursor()
    sQuery = "SELECT * FROM bd_escuela.sede where idSede='{}' ".format(idsede,)
    #print(sQuery)
    cur.execute(sQuery)
    row = cur.fetchall()

    # Ejecucion de la Sentencia
    cur.execute(sQuery)
    mysql.connection.commit()

    # Cerramos el cursor
    cur.close()

    return row

def actualizar_sede(NombreSede, Direccion, Telefono, Director, ActiveCampus, IdSede):
    # Cursor para la ejecución
    cur = mysql.connection.cursor()
    # QUERY de UPDATE
    # Ejecucion de la Sentencia
    cur.execute('''UPDATE bd_escuela.sede SET Sede=%s, Activo=%s, Tiposede=%s
     WHERE Idsede=%s ''', (NombreSede, Direccion, Telefono, Director, ActiveCampus, IdSede))
    mysql.connection.commit()

    # Cerramos el cursor
    cur.close()

#DELETE
def eliminar_sede(Documento):
    # Cursor para la ejecución
    cur = mysql.connection.cursor()
    # QUERY de UPDATE
    # Ejecucion de la Sentencia
    cur.execute('''DELETE from bd_escuela.sede WHERE Idsede=%s ''', (Documento,))
    mysql.connection.commit()

    # Cerramos el cursor
    cur.close()