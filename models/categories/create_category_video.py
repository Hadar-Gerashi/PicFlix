from db import create_connection


def create_category_video(video_id, category_id):
    with create_connection() as conn:
        with conn.cursor() as cursor:
            query = "INSERT IGNORE INTO category_video (video_id, category_id) VALUES (%s, %s)"
            cursor.execute(query, (video_id, category_id))
        conn.commit()
