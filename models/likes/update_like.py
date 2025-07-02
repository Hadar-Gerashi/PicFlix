from db import create_connection


def update_like(user_id, video_id):
    try:
        with create_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    SELECT 1 FROM likes WHERE users_id = %s AND video_id = %s
                """, (user_id, video_id))
                already_liked = cursor.fetchone()

                if already_liked:
                    cursor.execute("""
                        DELETE FROM likes WHERE users_id = %s AND video_id = %s
                    """, (user_id, video_id))
                    action = "unliked"
                else:
                    cursor.execute("""
                        INSERT INTO likes (users_id, video_id) VALUES (%s, %s)
                    """, (user_id, video_id))
                    action = "liked"

                cursor.execute("""
                    SELECT COUNT(*) AS cnt FROM likes WHERE video_id = %s
                """, (video_id,))
                new_count = cursor.fetchone()['cnt']

        return {"status": "success", "action": action, "likes_count": new_count}

    except Exception as e:
        print("Error updating like:", repr(e))
        import traceback
        traceback.print_exc()
        return {"status": "error", "message": str(e)}
