from db import create_connection

import pymysql.cursors
from db import create_connection


def read_videos_guest():
    try:
        with create_connection() as conn:
            with conn.cursor(pymysql.cursors.DictCursor) as cursor:
                query = """
                    SELECT
                        v.video_id,
                        v.users_id,
                        u.users_name,
                        v.video_url,
                        u.profile_image,
                        IFNULL(like_counts.like_count, 0) AS likes_count
                    FROM videos v
                    JOIN users u ON v.users_id = u.users_id
                    LEFT JOIN (
                        SELECT video_id, COUNT(*) AS like_count
                        FROM likes
                        GROUP BY video_id
                    ) AS like_counts ON v.video_id = like_counts.video_id
                    ORDER BY v.created_at DESC
                """
                cursor.execute(query)
                results = cursor.fetchall()

                return [
                    (
                        row['video_id'],
                        row['users_id'],
                        row['users_name'],
                        row['video_url'],
                        row['profile_image'],
                        row['likes_count']
                    )
                    for row in results
                ]
    except Exception as e:
        print("Error reading guest videos:", e)
        return []
