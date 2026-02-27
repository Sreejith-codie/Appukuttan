from database import cursor, conn

def set_goal(user_id, goal):
    cursor.execute("DELETE FROM income WHERE user_id=?", (user_id,))
    cursor.execute("INSERT INTO income VALUES (?, ?, ?)", (user_id, goal, 0))
    conn.commit()

def update_income(user_id, amount):
    cursor.execute("UPDATE income SET current=? WHERE user_id=?", (amount, user_id))
    conn.commit()