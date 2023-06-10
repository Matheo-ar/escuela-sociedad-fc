from app.database import mysql
    
#CREATE
def crear_categoria(NombreCategoria):
    # Cursor para la ejecución
    cur = mysql.connection.cursor()  # Siempre va este
    # QUERY de Insert
    sQuery = '''INSERT INTO bd_escuela.categoria (Nom_Categoria) 
      VALUES(%s)'''
    # Ejecucion de la Sentencia
    cur.execute(sQuery, (NombreCategoria,))
    
    mysql.connection.commit()

#READ
#model para llenar la tabla de categorias
def datos_categoria():
    cur = mysql.connection.cursor()
    sQuery = '''SELECT * FROM bd_escuela.categoria '''.format()
    #print(sQuery)
    cur.execute(sQuery)
    row = cur.fetchall()

    # Ejecucion de la Sentencia
    cur.execute(sQuery)
    mysql.connection.commit()

    # Cerramos el cursor
    cur.close()

    return row

#model para traer los datos de un categoria en particular
def datos_categoria1(id):
    cur = mysql.connection.cursor()
    sQuery = '''SELECT * FROM bd_escuela.categoria where idCategoria like '%{}%' '''.format(id)
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
def validar_categoria(IdCategoria):
    cur = mysql.connection.cursor()
    sQuery = "SELECT * FROM bd_escuela.categoria where idCategoria='{}' ".format(IdCategoria)
    #print(sQuery)
    cur.execute(sQuery)
    row = cur.fetchone()

    # Ejecucion de la Sentencia
    cur.execute(sQuery)
    mysql.connection.commit()

    # Cerramos el cursor
    cur.close()

    return row

#UPDATE
def actualizar_categoria(NombreCategoria, IdCategoria):
    # Cursor para la ejecución
    cur = mysql.connection.cursor()
    # QUERY de UPDATE
    # Ejecucion de la Sentencia
    cur.execute('''UPDATE bd_escuela.categoria SET Nom_Categoria=%s  WHERE Idcategoria=%s ''', (NombreCategoria, IdCategoria))
    mysql.connection.commit()

    # Cerramos el cursor
    cur.close()

#DELETE
def eliminar_categoria(IdCategoria):
    # Cursor para la ejecución
    cur = mysql.connection.cursor()
    # QUERY de UPDATE
    # Ejecucion de la Sentencia

    cur.execute('''DELETE from bd_escuela.categoria WHERE Idcategoria=%s ''', (IdCategoria,))
    mysql.connection.commit()

    # Cerramos el cursor
    cur.close()