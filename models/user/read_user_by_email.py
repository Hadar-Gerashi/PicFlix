from db import create_connection
import pymysql.cursors


def read_user_by_email(email):
    with create_connection() as conn:
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            query = "SELECT * FROM users WHERE email = %s"
            cursor.execute(query, (email,))
            row = cursor.fetchone()
            if row:
                return {
                    'id': row['users_id'],
                    'users_name': row['users_name'],
                    'email': row['email'],
                    'password_user': row['password_user']
                }
            return None
