import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
db_passowrd = os.getenv('DB_PASSWORD') if os.getenv('DB_PASSWORD') else "1234"

with mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = db_passowrd,
    database = "python_test"
) as connection:
    
    with connection.cursor(dictionary=True) as cursor:
        cursor.execute("select * from users")
        rows = cursor.fetchall()
        print(rows)
        for row in rows:
            print(row['id'], row['name'], row['email'])
        
        print(f"{cursor.rowcount}개의 행이 조회 되었습니다.")
        