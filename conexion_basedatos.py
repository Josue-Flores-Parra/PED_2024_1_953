import constantes
from mysql.connector import connect, Error
def conectar_bd():
    try:
        dbConexion = connect(host=constantes.SERVER,
                             user=constantes.USER,
                             password=constantes.PASSWORD,
                             database=constantes.DATABASE)
        return dbConexion
    except Error as e:
        print(constantes.MSG_ERROR)


def insertar_datos():
    pass


def consultar_datos():
    pass