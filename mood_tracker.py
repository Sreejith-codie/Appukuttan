from database import cursor, conn

def update_mood(user_id, mood):
    cursor.execute("DELETE FROM mood WHERE user_id=?", (user_id,))
    cursor.execute("INSERT INTO mood VALUES (?, ?)", (user_id, mood))
    conn.commit()