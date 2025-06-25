import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server (adjust credentials if needed)
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""  # Replace with your actual password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        # Create database (if not exists)
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error: Failed to connect or create database.\n{e}")

finally:
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
