from database import cursor, conn

def save_memory(user_id, key, value):
    cursor.execute("INSERT INTO memory VALUES (?, ?, ?)", (user_id, key, value))
    conn.commit()

def get_memory(user_id):
    cursor.execute("SELECT key, value FROM memory WHERE user_id=?", (user_id,))
    return cursor.fetchall()