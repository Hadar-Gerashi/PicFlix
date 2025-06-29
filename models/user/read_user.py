from db import create_connection


def read_user(password, name):
    with create_connection() as conn:
        with conn.cursor() as cursor:
            query = "SELECT * FROM users WHERE password_user = %s AND users_name = %s"
            cursor.execute(query, (password, name))
            data = cursor.fetchone()
            print(data)
            return data
