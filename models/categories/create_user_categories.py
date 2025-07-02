from db import create_connection


def create_user_categories(user_id, category_ids):
    with create_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM user_categories WHERE users_id = %s", (user_id,))
            for cat_id in category_ids:
                cursor.execute(
                    "INSERT INTO user_categories (users_id, category_id) VALUES (%s, %s)",
                    (user_id, cat_id)
                )
        conn.commit()
