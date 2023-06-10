from app.database import mysql
    
#READ
def validar_usuario(Documento):
    # Cursor para la ejecución
    cur = mysql.connection.cursor()
    sQuery = "SELECT Usuario,Contraseña,Privilegio,Nom_usuario FROM bd_escuela.usuario WHERE Usuario like '%{}%'".format(
        Documento)
    # print(sQuery)
    cur.execute(sQuery)
    row = cur.fetchone()
    # Cerramos el cursor
    cur.close()

    return row

