from db import create_connection


def delete_category_by_id(video_id):
    with create_connection() as conn:
        with conn.cursor() as cursor:
            query = "DELETE FROM category_video WHERE video_id = %s"
            cursor.execute(query, (video_id,))
        conn.commit()
