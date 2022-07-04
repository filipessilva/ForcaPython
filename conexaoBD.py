import mysql.connector  # acessa o SQL
from mysql.connector import errorcode  # trata as "exceções" (erros)


def conectar():
    try:
        db_connection = mysql.connector.connect(host='localhost', user='root', password='', database='bdti13n')

        print('Conectado!')
        return db_connection
    except mysql.connector.Error as erro:  # Guardando as possiveis exceções na variavel
        if erro.errno == errorcode.ER_BAD_DB_ERROR:  # caso o banco de dados não exista
            print('Banco de dados não existe!, {}'.format(erro))
        elif erro.errno == errorcode.ER_ACCESS_DENIED_ERROR:  # Caso usuario ou senha estejam errados
            print('Usuario ou senha incorreto, {}'.format(erro))
        else:
            print(erro)
    else:
        db_connection.close()
