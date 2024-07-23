import mysql.connector
from mysql.connector import Error

def connect_database():
    db_name = "fitnesscenter"
    user = 'root'
    password = 'Tuckerstriker12'
    host = '127.0.0.1'

    try:
        conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host
        )

        if conn.is_connected():
            print('Connected to MySQL database successfully')

    except Error as e:
        print(f'Error: {e}')
