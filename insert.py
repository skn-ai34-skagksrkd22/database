import mysql.connector

with mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "2401",
    database = "python_test"
) as connection:

    with connection.cursor() as cursor:
        sql = "insert into users (name, email) values (%s, %s)"
        values = ["Encore", "encore@example.com"]

        cursor.execute(sql, values)
        connection.commit()

        print(f"{cursor.rowcount}개의 행이 삽입되었습니다.")
