from db import create_connection
import pymysql.cursors


def read_liked_video_ids_by_user(user_id):
    try:
        with create_connection() as conn:
            with conn.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute("SELECT video_id FROM likes WHERE users_id = %s", (user_id,))
                results = cursor.fetchall()
                liked_videos = [row['video_id'] for row in results]
                return liked_videos
    except Exception as e:
        print("Error reading liked videos:", e)
        return []
