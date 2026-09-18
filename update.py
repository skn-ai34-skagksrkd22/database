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

    with connection.cursor() as cursor:
        sql = "update users set email = %s where name = %s"
        values = ("new_encore@example.com", "Encore")

        cursor.execute(sql, values)
        connection.commit()

        print(f"{cursor.rowcount}개의 행이 수정 되었습니다.")