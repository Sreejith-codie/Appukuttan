from database import cursor, conn

def update_health(user_id, sleep, water, workout):
    cursor.execute("DELETE FROM health WHERE user_id=?", (user_id,))
    cursor.execute(
        "INSERT INTO health VALUES (?, ?, ?, ?)",
        (user_id, sleep, water, workout)
    )
    conn.commit()