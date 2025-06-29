from db import create_connection


def update_categories_user(user_id, category_ids):
    with create_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM user_categories WHERE users_id = %s", (user_id,))
            data = [(user_id, cat_id) for cat_id in category_ids]
            cursor.executemany(
                "INSERT INTO user_categories (users_id, category_id) VALUES (%s, %s)", data
            )
        conn.commit()
