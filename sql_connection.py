import mysql.connector
from mysql.connector import Error


config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'concessionaria',
}


def server_connection():
    connection = None
    try:
        connection = mysql.connector.connect(**config)

        if connection.is_connected():
            print('Connection established!')
            cursor = connection.cursor()

    except Error as err:
        print('Error:', err)

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


def view_query(connection, query):
    cursor = connection.cursor(buffered=True)
    try:
        cursor.execute(query)
        connection.commit()
        return cursor.fetchall()
    except Error as err:
        print(f"Error: '{err}'")


def close_connection(connection):
    if connection.is_connected():
        connection.close()
        print('Connection closed.')
