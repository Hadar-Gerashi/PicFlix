from db import create_connection


def read_categories():
    try:
        with create_connection() as conn:
            with conn.cursor() as cursor:
                query = "SELECT category_id, category_name FROM categories"
                cursor.execute(query)
                results = cursor.fetchall()
                return [(row['category_id'], row['category_name']) for row in results]
    except Exception as e:
        print("Error reading categories:", e)
        return []
