from db import create_connection
import pymysql.cursors


def read_user_by_id(user_id):
    with create_connection() as conn:
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            query = "SELECT * FROM users WHERE users_id = %s"
            cursor.execute(query, (user_id,))
            data = cursor.fetchone()
            print(data)
            return data
