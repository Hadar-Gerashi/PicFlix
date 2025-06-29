from flask import jsonify
from db import create_connection


def read_users_by_name(query):
    conn = create_connection()
    try:
        cursor = conn.cursor()
        sql = "SELECT users_id, users_name FROM users WHERE users_name LIKE %s"
        cursor.execute(sql, (f'{query}%',))
        results = cursor.fetchall()
        users = [{"id": row["users_id"], "name": row["users_name"]} for row in results]
        return jsonify({"users": users})
    finally:
        cursor.close()
        conn.close()
