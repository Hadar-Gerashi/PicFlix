from db import create_connection


def create_video(user_id, video_url):
    with create_connection() as conn:
        with conn.cursor() as cursor:
            query = "INSERT INTO videos(users_id, video_url) VALUES (%s, %s)"
            cursor.execute(query, (user_id, video_url))
        conn.commit()
