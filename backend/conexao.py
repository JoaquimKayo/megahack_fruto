import mysql.connector
from mysql.connector import Error

def criar_conexao():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='user',
            passwd='123456',
            database='teste'
        )
        print("Conexao realizada")
    except Error as e:
        print("Deu erro")

    return connection
