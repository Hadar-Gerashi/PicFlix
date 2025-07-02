import pymysql.cursors
from db import create_connection


def read_videos(user_id):
    try:
        with create_connection() as conn:
            with conn.cursor(pymysql.cursors.DictCursor) as cursor:
                query = """
                           SELECT 
                               sub.video_id, 
                               sub.users_id,
                               u.users_name,
                               sub.video_url, 
                               u.profile_image,
                               IFNULL(like_counts.like_count, 0) AS likes_count
                           FROM (
                               SELECT 
                                   v.video_id, 
                                   v.video_url, 
                                   v.users_id,
                                   CASE 
                                       WHEN EXISTS (
                                           SELECT 1 
                                           FROM category_video cv2
                                           JOIN user_categories uc2 ON cv2.category_id = uc2.category_id
                                           WHERE cv2.video_id = v.video_id AND uc2.users_id = %s
                                       ) THEN 0
                                       ELSE 1
                                   END AS preference_order,
                                   RAND() AS random_order
                               FROM videos v
                           ) AS sub
                           JOIN users u ON sub.users_id = u.users_id
                           LEFT JOIN (
                               SELECT video_id, COUNT(*) AS like_count
                               FROM likes
                               GROUP BY video_id
                           ) AS like_counts ON sub.video_id = like_counts.video_id
                           ORDER BY 
                               sub.preference_order, 
                               sub.random_order
                           """
                cursor.execute(query, (user_id,))
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
        print("Error reading videos:", e)
        return []
