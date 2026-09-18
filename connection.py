import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "2401",
    database = "python_test"
)

if connection.is_connected():
    print("Mysql 접속 성공!")

connection.close()