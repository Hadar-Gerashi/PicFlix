import pymysql.cursors
from db import create_connection


def read_video_id(users_id, video_url):
    with create_connection() as conn:
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            query = "SELECT video_id FROM videos WHERE users_id = %s AND video_url = %s"
            cursor.execute(query, (users_id, video_url))
            data = cursor.fetchone()
            if data:

                return data['video_id']
            return None
