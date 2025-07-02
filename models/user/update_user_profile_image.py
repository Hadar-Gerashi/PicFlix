import os
from db import create_connection


def update_user_profile_image(user_id, filename_or_url):
    try:
        with create_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "UPDATE users SET profile_image = %s WHERE users_id = %s",
                    (filename_or_url, user_id)
                )
            conn.commit()
        return True
    except Exception as e:
        print(f"Error updating profile image for user {user_id}: {e}")
        return False
