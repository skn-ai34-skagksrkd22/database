import streamlit as st
import mysql.connector
import os
from dotenv import load_dotenv

"""
menudb 스키마 내 tbl_menu 테이블 안의 정보를 가져와 Streamlit 조회 테이블로 만들어보기

- 만약 READ 구현이 다 되었다면 추가로 CRUD도 구현해보기
"""


load_dotenv()
db_passowrd = os.getenv('DB_PASSWORD') if os.getenv('DB_PASSWORD') else "1234"
lst = {}

with mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = db_passowrd,
    database = "menudb"
) as connection:
    
    with connection.cursor(dictionary=True) as cursor:
        cursor.execute("select * from tbl_menu")
        rows = cursor.fetchall()
        
        # for i, row in enumerate(rows):
            # st.write(row['menu_code'], row['menu_name'], row['menu_price'], row['category_code'], row['orderable_status'])

st.dataframe(rows)

