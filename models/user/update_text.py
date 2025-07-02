from db import create_connection


def update_text(user_id, new_text):
    with create_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT users_id FROM users WHERE users_id = %s", (user_id,))
            if cursor.fetchone() is None:
                return False

            cursor.execute("UPDATE users SET profile_text = %s WHERE users_id = %s", (new_text, user_id))
        conn.commit()
        return True
