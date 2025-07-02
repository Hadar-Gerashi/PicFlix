from db import create_connection


def read_user_videos(user_id):
    with create_connection() as conn:
        with conn.cursor() as cursor:
            query = "SELECT video_id, video_url FROM videos WHERE users_id = %s"
            cursor.execute(query, (user_id,))
            rows = cursor.fetchall()  # [{'video_id': 1, 'video_url': '...'}, ...]
            data = [(row['video_id'], row['video_url']) for row in rows]
            print(data)
            return data
