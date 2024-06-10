from dotenv import load_dotenv
import os
import pymysql

load_dotenv()

host_name = os.environ.get("mysql_host")
user_name = os.environ.get("mysql_user")
user_password = os.environ.get("mysql_pass")
database_name = os.environ.get("mysql_db")


with pymysql.connect(
    host = host_name,
    user = user_name,
    password = user_password,
    database = database_name,
) as connection:
    with connection.cursor() as cursor:
        insert_sql = """
        INSERT INTO person (first_name, last_name)
        VALUES (%s, %s)
        """
        values = ("Sam", "Bbb")
        cursor.execute(insert_sql, values)
        connection.commit()