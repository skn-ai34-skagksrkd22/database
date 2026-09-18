import mysql.connector
import os
from dotenv import load_dotenv

"""
menudb 스키마 내 tbl_menu 테이블 안의 정보를 가져와 Streamlit 조회 테이블로 만들어보기

- 만약 READ 구현이 다 되었다면 추가로 CRUD도 구현해보기
"""



load_dotenv()
db_password = os.getenv("DB_PASSWORD")

with mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = db_password,
    database = "python_test"
) as connection:
    
    with connection.cursor() as cursor:
        sql = "delete from users where name = %s"
        values = ["Encore"]
        
        cursor.execute(sql, values)
        connection.commit()
        
        print(f"{cursor.rowcount}개의 행이 삭제 되었습니다.")