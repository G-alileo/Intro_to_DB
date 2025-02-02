import mysql.connector
from mysql.connector import Error


def create_database():
    connection = None
    
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="28387327" 
        )

        if connection.is_connected():
           
            cursor = connection.cursor()
            
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


if __name__ == "__main__":
    create_database()